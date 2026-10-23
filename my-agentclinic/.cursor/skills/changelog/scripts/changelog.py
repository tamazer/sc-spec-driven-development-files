#!/usr/bin/env python3
"""Maintain CHANGELOG.md from git commit history."""

import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def git_root():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip()).resolve()


def pathspec():
    """Limit history to this project when the git root is a parent directory."""
    cwd = Path.cwd().resolve()
    root = git_root()
    if cwd == root:
        return None
    try:
        cwd.relative_to(root)
    except ValueError:
        return None
    return "."


def git_log(since_date=None):
    """Return commits as {date: [subject, ...]}."""
    cmd = ["git", "log", "--format=%ad|%s", "--date=short"]
    if since_date:
        cmd.append(f"--after={since_date}")
    spec = pathspec()
    if spec:
        cmd.extend(["--", spec])
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    by_date = defaultdict(list)
    for line in result.stdout.strip().splitlines():
        if "|" not in line:
            continue
        date, subject = line.split("|", 1)
        by_date[date.strip()].append(subject.strip())
    return by_date


def last_date_in_changelog(path):
    """Return the first ## YYYY-MM-DD heading, or None."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("## "):
            continue
        candidate = line[3:].strip()
        try:
            datetime.strptime(candidate, "%Y-%m-%d")
        except ValueError:
            continue
        return candidate
    return None


def render_sections(by_date):
    lines = []
    for date in sorted(by_date, reverse=True):
        lines.append(f"\n## {date}\n\n")
        for subject in by_date[date]:
            lines.append(f"- {subject}\n")
    return lines


def main():
    changelog = Path("CHANGELOG.md")

    if not changelog.exists():
        by_date = git_log()
        if not by_date:
            print("No commits found — nothing to write.")
            return
        content = ["# Changelog\n"] + render_sections(by_date)
        changelog.write_text("".join(content), encoding="utf-8")
        total = sum(len(subjects) for subjects in by_date.values())
        print(f"Created CHANGELOG.md with {total} entries across {len(by_date)} date(s).")
        return

    last = last_date_in_changelog(changelog)
    by_date = git_log(since_date=last)
    if last:
        by_date.pop(last, None)
    if not by_date:
        print("No new commits since last entry — CHANGELOG.md is up to date.")
        return

    existing = changelog.read_text(encoding="utf-8")
    lines = existing.splitlines(keepends=True)
    insert_at = 1 if lines and lines[0].startswith("# ") else 0
    updated = "".join(lines[:insert_at] + render_sections(by_date) + lines[insert_at:])
    changelog.write_text(updated, encoding="utf-8")
    total = sum(len(subjects) for subjects in by_date.values())
    print(f"Added {total} new entries to CHANGELOG.md.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        message = error.stderr.strip() if error.stderr else "git command failed"
        print(message, file=sys.stderr)
        sys.exit(error.returncode or 1)
