# Git Guide

> *A practical Git reference for the IAssistant project.*

---

# Philosophy

Git is the memory of the project.

Every commit tells a part of IAssistant's story.

A commit should explain **why** something was done, not simply **what** changed.

---

# Our Workflow

At the end of every development session:

1. Check the project status.
2. Stage the modifications.
3. Verify the staged files.
4. Create a meaningful commit.
5. Push the changes to GitHub.

---

# Commands

## Check project status

```bash
git status
```

Displays modified, deleted and new files.

Always start here.

---

## Stage every modification

```bash
git add .
```

Stages every modified file.

The dot (`.`) means "everything in the current project".

---

## Stage a single file

```bash
git add README.md
```

Useful when only one file should be committed.

---

## Verify staged files

```bash
git status
```

Files displayed in green are ready to be committed.

---

## Create a commit

```bash
git commit -m "Meaningful commit message"
```

Examples:

```bash
git commit -m "Establish the architectural foundations of IAssistant"

git commit -m "Add project development conventions"

git commit -m "Implement User domain model"
```

Avoid messages like:

```
Update
Fix
Test
...
```

A commit should describe the intention.

---

## Send changes to GitHub

```bash
git push
```

Uploads local commits to GitHub.

---

## Retrieve changes

```bash
git pull
```

Downloads the latest changes from GitHub.

Useful when working on multiple computers.

---

## Clone the project

```bash
git clone https://github.com/rolandsebastien-blip/IAssistant.git
```

Downloads the complete project.

Only used once on a new computer.

---

# Typical Session

```bash
git status

git add .

git status

git commit -m "Implement Need domain model"

git push
```

---

# Good Practices

✔ Commit often.

✔ One commit = one logical idea.

✔ Write commit messages in English.

✔ Push your work at the end of every session.

✔ Never modify history unless absolutely necessary.

---

# Golden Rule

Git is not a backup tool.

Git tells the story of the project.

Every commit should make that story easier to understand.