# Project Conventions

## Purpose

This document defines the development conventions followed throughout the IAssistant project.

These conventions ensure that every contribution remains coherent with the project's philosophy and long-term vision.

---

# Language

- Source code is written in English.
- Architecture Decision Records (ADR) are written in English.
- The development book is currently written in French.
- Comments should be written in English whenever possible.

---

# Documentation

Every development session should produce:

- meaningful code;
- updated documentation when necessary;
- an ADR whenever an architectural decision is made;
- a Git commit describing the accomplished work.

---

# Architecture

No implementation should contradict an accepted ADR.

If an ADR must evolve, a new ADR is created.

Existing ADRs are never modified to rewrite history.

---

# Git

Commits should describe the intention rather than the technical change.

Example:

✓ Establish the architectural foundations of IAssistant

instead of

✗ Update files

---

# Development Philosophy

Understand before designing.

Design before coding.

Code before optimizing.

Optimize before extending.

---

# Golden Rule

Every line of code should answer one simple question:

"How does this improve the user's daily life?"