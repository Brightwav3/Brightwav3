<h1 align="center">Brightwave</h1>

<p align="center">
Building modular AI systems, developer infrastructure, and local-first software designed to outlive any single model or interface.
</p>

<p align="center">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white" />
<img src="https://img.shields.io/badge/Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Anthropic-D97757?style=flat-square&logo=anthropic&logoColor=white" />
<img src="https://img.shields.io/badge/Mistral_AI-FA520F?style=flat-square&logo=mistralai&logoColor=white" />
</p>

---

<h2 align="center">About</h2>

<p align="center">
I'm interested in building AI systems as infrastructure rather than standalone applications.
<br><br>
Most of my work explores modular agentic architectures, local-first software, developer tooling, and the boundaries between AI models and the systems around them. I particularly enjoy designing software where models, interfaces, and providers can be replaced without rebuilding the underlying architecture.
<br><br>
Outside of AI infrastructure, I experiment with document engines, desktop applications, rendering, automation, and developer tools.
</p>

---

<h2 align="center">
  <a href="https://github.com/Brightwav3/Assistant-mark-II">Assistant M.A.R.K. II</a>
</h2>

<p align="center">
I'm building a headless, agent-first runtime for a persistent personal AI system.
<br><br>
Assistant Mark II is the active successor to the frozen Mark I baseline. It composes independent cores for intelligence, memory, state, speech, activation, tools, devices, and echo cancellation through explicit contracts.
<br><br>
The runtime is designed to keep memory, orchestration, tools, and device access under the assistant's control instead of coupling them to a single model, speech provider, or user interface.
<br><br>
Realtime voice is an active area of development, with deterministic runtime verification kept separate from hardware-dependent microphone, speaker, and acoustic-echo qualification.
</p>

<p align="center">
  <strong>The model may change. The runtime, boundaries, and ownership should endure.</strong>
</p>

---

```text
                         ┌────────────────────────┐
                         │  Assistant M.A.R.K. II │
                         │    Composed Runtime    │
                         └────────────┬───────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
 Intelligence Core             Memory Core                    Speech System
        │                       persistent memory              realtime sessions
        │                             │                       STT / TTS / VAD
        ▼                             ▼                             │
 Local or Cloud Models       State Core / Events                    ▼
                                      │                        AEC System
                                      │                    echo cancellation
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
  Tool System                 Device Network                 Activation Core
  agents and actions          hardware boundaries             wake / trigger paths
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      ▼
                              External Systems
```

---

## Design Principles

- **Model-independent** — providers and models should be replaceable without rewriting the runtime.
- **Headless-first** — the assistant exists independently of a graphical interface.
- **Agent-first** — capabilities are exposed through explicit tools and programmable contracts.
- **Local-first** — local execution, ownership, and inspectability are preferred where practical.
- **Persistent by design** — memory belongs to the assistant and survives model or session changes.
- **Explicit state** — runtime state, persistent memory, and external side effects have separate ownership.
- **Composable** — speech, activation, memory, intelligence, tools, devices, and interfaces remain independently testable.
- **Provider-neutral** — external AI services are adapters, not the architecture.
- **Hardware-aware** — microphone, speaker, realtime, and echo-cancellation behavior is qualified separately from deterministic software tests.
- **Contract-driven** — components communicate through small, explicit interfaces instead of hidden coupling.

## Hlavní změny oproti původní verzi:

- odkazuje na aktivní `Assistant Mark II`, ne na zmrazený Mark I;
- popisuje skutečný `assistant-runtime` a modulární core repozitáře;
- přidává persistent memory, explicit state, tools, device network a AEC;
- nepředstírá, že realtime voice nebo full-duplex audio jsou hotové bez hardwarové kvalifikace;
- zachovává provider/model independence, ale popisuje ji praktičtěji;
- rozlišuje deterministic CI od mikrofonu, reproduktoru a echo-cancellation testů.

---

<h2 align="center">
  <a href="https://github.com/Brightwav3/full-duplex-attempts">Full-Duplex Attempts</a>
</h2>

<p align="center">
An atlas of my attempts at building a full-duplex voice system — one where the user and the assistant can both speak at once, and each keeps hearing the other.
<br><br>
It contains no code. Every attempt lives in its own repository. What lives here is the part that never survives inside a single project: what each attempt was trying, which half of the problem it solved, where it hit a wall, and what the wall was made of.
</p>

<p align="center">
The central finding is that "full-duplex" describes three architectures, not two — and that conflating the middle one with the last makes an unreachable ceiling look like an unfinished integration.
</p>

<div align="center">

| Generation | Shape | Turn detection |
| --- | --- | --- |
| 1 — Cascade | STT → chat → TTS | a silence timer in your code |
| 2 — Turn-based native | one model, audio in and out | provider-side, still on silence |
| 3 — Full-duplex | one model, continuous both ways | none — the model decides |

</div>

<p align="center">
Two attempts are documented against five criteria: <a href="https://github.com/Brightwav3/Assistant-mark-I">Assistant Mark I</a>, which solved the media half and cannot act, and <a href="https://github.com/Brightwav3/voxtral-live">voxtral-live</a>, which solved the application half and cannot stop taking turns. They are complementary halves of one architecture rather than two failed systems.
</p>

<p align="center">
Written under three rules: every architectural claim cites the file and construct it came from, every page names the date and commit it was read against, and nothing is vendored — links only.
</p>

<p align="center">
  <strong>Some ceilings are in the model, not in the architecture.</strong>
</p>

---

<h1 align="center">Other Featured Projects</h1>

| Project                                                                                    | Description                                                                                                                      |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **[FreeDF](https://github.com/Brightwav3/custom-pdf-engine)** *(in development)*           | A local-first PDF engine built around immutable operations, stable contracts, and equivalent Python, HTTP, and JSON interfaces.  |
| **[One Tool](https://github.com/Brightwav3/One-tool-to-rule-them-all)** *(in development)* | A desktop workspace for document conversion and editing designed around reusable backend services and agent-friendly automation. |
| **[semantic-backlinks](https://github.com/Brightwav3/semantic-backlinks)**                 | An Obsidian plugin for semantic note linking using local embeddings through Ollama / LM Studio or the OpenAI API.                |
| **[liquid-metal-effect](https://github.com/Brightwav3/liquid-metal-effect)**               | A WebGL liquid-metal rendering experiment with a complete implementation and technical documentation.                            |
| **[Invoicee](https://github.com/Brightwav3/invoicee)**                                     | A prototype Czech invoicing application featuring a browser-based invoice editor.                                                |
| **[personal-portfolio](https://github.com/Brightwav3/personal-portfolio)**                 | A literary-inspired portfolio focused on interaction, animation, and visual storytelling.                                        |
| **[Coding-Agent-Theme](https://github.com/Brightwav3/Coding-Agent-Theme)**                 | A custom theme for coding-agent interfaces.                                                                                      |

---

<h1 align="center">At a Glance</h1>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Brightwav3&theme=github-dark&hide_border=true" height="170" alt="GitHub Streak" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Brightwav3&theme=github_dark" height="170" alt="Languages by Repository" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Brightwav3&theme=github_dark" width="100%" alt="Contribution Graph" />
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

## Interests

* AI infrastructure
* Agentic systems
* Developer tools
* Local-first software
* Software architecture
* API design
* Automation & MCP
* Document processing
* Rendering & graphics
* Desktop applications

<p align="center">
  <a href="mailto:simon.zelenkovi@gmail.com">
    <img src="https://img.shields.io/badge/Email-181717?style=flat-square&logo=gmail&logoColor=white" />
  </a>
  <a href="https://simzel.eu/">
    <img src="https://img.shields.io/badge/Portfolio-181717?style=flat-square&logo=vercel&logoColor=white" />
  </a>
</p>
