# Congreso Monitor

## Project Goal

Monitor the Chilean Congress to track executive influence over legislation and detect potential authoritarian drift. The long-term goal is a public website where citizens can see what's happening in Congress.

## Current Phase: Research Complete — Ready for Design

All four research phases are complete. A compiled PDF report is available at `docs/Congreso_Monitor_Informe_Investigacion.pdf`. Next step: design the monitoring tool.

## Research Plan

Four phases of research, each producing a document in `docs/research/`:

| Phase | Topic | File | Status |
|-------|-------|------|--------|
| 1 | Institutional Structure | `01-institutional-structure.md` | Done |
| 2 | Executive Power Over Legislation | `02-executive-power.md` | Done |
| 3 | Legal Framework | `03-legal-framework.md` | Done |
| 4 | Historical Patterns & Comparative Context | `04-historical-patterns.md` | Done |

## Key Context

- Chilean Congress is bicameral: Cámara de Diputados (155) + Senado (50)
- The President has significant legislative power: exclusive initiative, urgencies, vetos, extraordinary sessions
- Data sources exist: opendata.congreso.cl, Cámara API, Senado API, BCN linked data
- Existing civic tech: Ciudadanía Inteligente, Congreso Abierto, Congreso Virtual

## Bibliography

See `docs/research/bibliography.md` for all sources.

## Compiled Report

`docs/Congreso_Monitor_Informe_Investigacion.pdf` — Full research report (820 KB, ~2,500 lines across all phases)

## Directory Structure

```
docs/
  research/                                    # Research documents (one per phase)
    01-institutional-structure.md               # Phase 1: Bicameral structure, legislative process, committees
    02-executive-power.md                       # Phase 2: Presidential powers, urgencies, veto, states of exception
    03-legal-framework.md                       # Phase 3: Constitution, LOC 18.918, TC, Contraloría, transparency
    04-historical-patterns.md                   # Phase 4: Chilean history, Latin American comparisons, erosion indicators
    bibliography.md                             # All sources, kept up to date
  Congreso_Monitor_Informe_Investigacion.pdf    # Compiled PDF report
  plans/                                        # Design and implementation plans (future)
generate_report.py                              # Script to regenerate the PDF report
```
