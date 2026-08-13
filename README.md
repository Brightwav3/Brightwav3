<h1 align="center">Brightwave</h1>

<p align="center">
Building modular AI systems, developer infrastructure, and local-first software designed to outlive any single model or interface.
</p>

<p align="center">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/WebGL-990000?style=flat-square&logo=webgl&logoColor=white" />
<img src="https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white" />
<img src="https://img.shields.io/badge/Local--First-181717?style=flat-square" />
<img src="https://img.shields.io/badge/Agent--First-181717?style=flat-square" />
<img src="https://img.shields.io/badge/Headless-181717?style=flat-square" />
</p>

---

## About

I'm interested in building software where the intelligence, interface, and underlying system are separate things.

My main project is **Jarvis** — a long-term experiment in building a modular personal AI system around replaceable models, persistent memory, voice interaction, device control, and independent system components.

Rather than building an assistant around one model or API, I'm interested in building the infrastructure that different generations of models can inhabit.

The same principle carries into my other work: reusable engines, stable contracts, headless operation, automation, and interfaces that remain replaceable.

> **Models change. Interfaces change. The system should survive both.**

---

## Jarvis

**Jarvis** is an experimental modular architecture for a persistent personal AI system.

Instead of treating an assistant as a single application, Jarvis separates capabilities into independent components with explicit contracts between them.

```text
                         ┌────────────────────┐
                         │       Jarvis       │
                         │      Runtime       │
                         └─────────┬──────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
   Intelligence Core         Memory / State           Speech System
          │                                                │
          │                                      ┌─────────┼─────────┐
          │                                      │         │         │
          ▼                                      ▼         ▼         ▼
   Local / Cloud Models                          STT    Realtime     TTS
          │
          │
          ├──────────────► Device Network
          │
          ├──────────────► Tools / Agents
          │
          └──────────────► External Systems
```

### Design principles

* **Model-independent** — intelligence providers should be replaceable.
* **Headless-first** — the system should exist independently of any GUI.
* **Agent-first** — capabilities should be usable programmatically, not only through human interfaces.
* **Local-first** — local execution and ownership are preferred where practical.
* **Event-driven** — components communicate through explicit events and contracts.
* **Persistent** — memory and state belong to the assistant, not to the model currently running it.
* **Composable** — speech, activation, memory, intelligence, devices, and interfaces remain independent components.

The goal is not to recreate a particular chatbot interface.

The goal is to build an environment capable of surviving many generations of models.

---

## Jarvis Ecosystem

| Component             | Purpose                                                               |
| --------------------- | --------------------------------------------------------------------- |
| **Assistant Runtime** | Composition layer coordinating the rest of the system.                |
| **Intelligence Core** | Model-independent interface for reasoning and intelligence providers. |
| **Memory Core**       | Persistent long-term information and retrieval infrastructure.        |
| **State Core**        | Current interaction and system state.                                 |
| **Activation Core**   | Wake words, gestures, claps, snaps, and other activation mechanisms.  |
| **Speech System**     | Provider-independent speech infrastructure.                           |
| **Realtime Core**     | Low-latency conversational audio sessions and interruption handling.  |
| **Voice Core**        | Speech synthesis and voice-provider abstraction.                      |
| **Scribe Core**       | Speech recognition and transcription.                                 |
| **Device Network**    | Communication between Jarvis and physical machines/devices.           |
| **Brain Core**        | Shared infrastructure for higher-level cognitive components.          |

Individual components are designed to remain useful even when the models behind them change.

---

## Other Projects

Jarvis is the main architectural experiment, but I build other software around many of the same ideas.

| Project                                                                                    | Description                                                                                                                   |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **[FreeDF](https://github.com/Brightwav3/custom-pdf-engine)** *(in development)*           | Local-first PDF engine built around immutable operations, stable contracts, and equivalent Python, HTTP, and JSON interfaces. |
| **[One Tool](https://github.com/Brightwav3/One-tool-to-rule-them-all)** *(in development)* | Desktop workspace for file conversion and editing backed by reusable services designed for both humans and agents.            |
| **[semantic-backlinks](https://github.com/Brightwav3/semantic-backlinks)**                 | Obsidian plugin for semantic note linking using local embeddings or external model APIs.                                      |
| **[liquid-metal-effect](https://github.com/Brightwav3/liquid-metal-effect)**               | WebGL liquid-metal rendering experiment with a complete implementation and technical documentation.                           |
| **[Invoicee](https://github.com/Brightwav3/invoicee)**                                     | Prototype Czech invoicing application featuring a browser-based invoice editor.                                               |
| **[personal-portfolio](https://github.com/Brightwav3/personal-portfolio)**                 | Literary-inspired portfolio focused on interaction, animation, and visual storytelling.                                       |
| **[Coding-Agent-Theme](https://github.com/Brightwav3/Coding-Agent-Theme)**                 | Custom theme for coding-agent interfaces.                                                                                     |

---

## What I'm Interested In

**AI systems**

* Persistent assistants
* Model-independent architecture
* Memory and state
* Realtime voice interaction
* Local inference
* Agent infrastructure

**Software architecture**

* Headless systems
* Stable interfaces and contracts
* Event-driven architecture
* API design
* Automation
* Long-lived software

**Developer tools**

* Document processing
* Desktop applications
* Rendering and graphics
* Agent-accessible tooling
* Local-first software

---

## Current Focus

### Jarvis

Building the foundations for a personal AI system whose identity and capabilities are not tied to one model provider.

Current work includes:

* realtime conversational voice
* activation and presence
* memory and state
* intelligence-provider abstraction
* device communication
* agent/tool interfaces
* long-running headless runtimes

### FreeDF

Developing a reusable document engine with the same principle of separating the underlying capability from its interfaces.

### One Tool

Building a human-facing desktop workspace on top of reusable document and conversion infrastructure.

---

## Architecture Philosophy

I prefer systems where:

```text
                Core Capability
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
         GUI           API         Agent
          │            │            │
          └────────────┼────────────┘
                       │
                  Automation
```

The graphical interface should be **a client of the system**, not the system itself.

AI models should follow the same rule.

```text
Jarvis ≠ Model

Jarvis = architecture + memory + state + capabilities + interfaces

Model = replaceable intelligence provider
```

This allows the software around a model to continue evolving even when the model itself is replaced.

---

## At a Glance

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Brightwav3&theme=github-dark&hide_border=true" height="170" alt="GitHub Streak"/>
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Brightwav3&theme=github_dark" height="170" alt="Languages by Repository"/>
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Brightwav3&theme=github_dark" width="100%" alt="Contribution Graph"/>
</p>

<p align="center">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://raw.githubusercontent.com/Brightwav3/Brightwav3/output/github-contribution-grid-snake-dark.svg"
    />
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://raw.githubusercontent.com/Brightwav3/Brightwav3/output/github-contribution-grid-snake.svg"
    />
    <img
      alt="GitHub contribution snake"
      src="https://raw.githubusercontent.com/Brightwav3/Brightwav3/output/github-contribution-grid-snake.svg"
    />
  </picture>
</p>

---

## Philosophy

> **Build the infrastructure once. Let everything else be replaceable.**

Models will improve. APIs will disappear. Interfaces will be redesigned.

The architecture underneath them should not need to start over.

---

<p align="center">
  <a href="mailto:simon.zelenkovi@gmail.com">
    <img src="https://img.shields.io/badge/Email-181717?style=flat-square&logo=gmail&logoColor=white" />
  </a>
  <a href="https://simzel.eu/">
    <img src="https://img.shields.io/badge/Portfolio-181717?style=flat-square&logo=vercel&logoColor=white" />
  </a>
</p>
