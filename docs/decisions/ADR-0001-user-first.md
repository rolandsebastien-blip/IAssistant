# ADR-0001 — User First

**Status**  
Accepted

**Date**  
2026-07-21

---

## Context

IAssistant was born from a simple observation: although modern home automation platforms are extremely powerful, they are primarily designed around technology.

Users are expected to understand concepts such as entities, automations, integrations, protocols, and services. While these concepts are essential for the system itself, they do not reflect how people naturally think about their homes.

A home is not experienced as a collection of connected devices. It is experienced through habits, routines, needs, preferences and emotions.

During the project's founding interview, it became clear that IAssistant was never intended to become a better automation engine, nor a replacement for Home Assistant.

Its purpose is to understand the people living in a home in order to help the home adapt naturally to them.

This observation leads to a fundamental architectural decision:

**The center of the project is the user, not the technology.**

---

## Decision

IAssistant adopts a **User First** architecture.

Every architectural, functional and technical decision must ultimately serve the user.

Devices, integrations, protocols and automations are considered implementation tools rather than objectives.

The success of a feature is measured by the value it brings to the inhabitants, not by its technical sophistication.

---

## Consequences

This decision establishes several guiding principles.

- Understanding users always comes before automating their environment.
- Connected devices are resources, not goals.
- Every suggestion produced by IAssistant should be explainable through knowledge acquired about the user.
- Future developments should prioritize improving the assistant's understanding before increasing its technical capabilities.
- Home Assistant is viewed as an integration, not as the center of the system.

---

## Alternatives Considered

### Technology First

Building IAssistant around Home Assistant entities and integrations.

This approach was rejected because it naturally leads to designing an assistant focused on devices instead of people.

### Automation First

Building an engine primarily dedicated to generating automations.

This approach was also rejected.

Automation is considered the consequence of understanding the user, not the purpose of the assistant.

---

## Derived Principles

This decision serves as the foundation for several future architectural decisions, including:

- Knowledge-driven reasoning.
- Progressive learning of habits and preferences.
- Human validation for important decisions.
- Continuous learning from user feedback.

Each of these topics will be formalized in future ADRs.

---

## Founding Principle

> **IAssistant is not designed to understand a house.**
>
> **It is designed to understand the people living in it so that the house can naturally adapt to them.**