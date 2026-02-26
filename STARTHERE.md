# Congreso Monitor

## Project Goal

Monitor the Chilean Congress to track executive influence over legislation and detect potential authoritarian drift. The long-term goal is a public website where citizens can see what's happening in Congress.

## Current Phase: GitHub Pages Site Built

All research phases (1-9) are complete plus the Democratic Clock (Phase 10). The project now has a Chile-specific early warning scale modeled on the Doomsday Clock, with 5 dimensions, 15+ quantitative indicators, and an initial assessment of **4:30 to midnight (Early Erosion)**.

A GitHub Pages site has been built in `docs/` with three pages:
- **index.html** — Homepage with SVG semicircular gauge, 5 dimension bars (expand/collapse), key facts strip, and navigation cards
- **investigacion.html** — All 10 research phases with links to the markdown files and PDF download
- **metodologia.html** — Full methodology: zones, dimensions, indicators table, scoring, point of no return

The site is plain HTML/CSS/JS with no dependencies or build step. To update the clock reading, edit `docs/js/clock.js` (the `CLOCK_DATA` object) and commit.

**Next step:** Create a GitHub remote, push, and enable GitHub Pages (deploy from `/docs` on `main` branch).

## Research Plan

Research documents in `docs/research/`:

| Phase | Topic | File | Status |
|-------|-------|------|--------|
| 1 | Institutional Structure | `01-institutional-structure.md` | Done |
| 2 | Executive Power Over Legislation | `02-executive-power.md` | Done |
| 3 | Legal Framework | `03-legal-framework.md` | Done |
| 4 | Historical Patterns & Comparative Context | `04-historical-patterns.md` | Done |
| 5 | Chile Today: Political Landscape 2019-2026 | `05-chile-today.md` | Done |
| 6 | Security Narrative & Migration | `06-security-migration.md` | Done |
| 7 | Economic Pressures & Democratic Erosion | `07-economic-pressures.md` | Done |
| 8 | Civil Society & Democratic Resilience | `08-civil-society.md` | Done |
| 9 | **Erosion Scenarios — Synthesis** | `09-erosion-scenarios.md` | Done |
| 10 | **El Reloj Democratico de Chile** | `10-democratic-clock.md` | Done |

## Key Context

- Chilean Congress is bicameral: Cámara de Diputados (155) + Senado (50)
- The President has significant legislative power: exclusive initiative, urgencies, vetos, extraordinary sessions
- Data sources exist: opendata.congreso.cl, Cámara API, Senado API, BCN linked data
- Existing civic tech: Ciudadanía Inteligente, Congreso Abierto, Congreso Virtual

## Bibliography

See `docs/research/bibliography.md` for all sources.

## Compiled Report

`docs/Congreso_Monitor_Informe_Investigacion.pdf` — Full research report (1.8 MB, ~7,000 lines across all phases)

## Directory Structure

```
docs/
  research/                                    # Research documents (one per phase)
    01-institutional-structure.md               # Phase 1: Bicameral structure, legislative process, committees
    02-executive-power.md                       # Phase 2: Presidential powers, urgencies, veto, states of exception
    03-legal-framework.md                       # Phase 3: Constitution, LOC 18.918, TC, Contraloría, transparency
    04-historical-patterns.md                   # Phase 4: Chilean history, Latin American comparisons, erosion indicators
    05-chile-today.md                          # Phase 5: Political fragmentation, post-estallido, trust crisis, 2025 elections
    06-security-migration.md                   # Phase 6: Crime, migration, states of exception, militarization
    07-economic-pressures.md                   # Phase 7: Pensions, inequality, copper dependency, employment
    08-civil-society.md                        # Phase 8: Media, watchdogs, judiciary, movements, resilience
    09-erosion-scenarios.md                    # Phase 9: SYNTHESIS — Chile-specific erosion scenarios, risk profile, early warnings
    10-democratic-clock.md                     # Phase 10: El Reloj Democrático — early warning scale (4:30 to midnight)
    bibliography.md                            # All sources, kept up to date
  Congreso_Monitor_Informe_Investigacion.pdf   # Compiled PDF report
  css/
    style.css                                  # Single stylesheet (layout, typography, colors, responsive)
  js/
    clock.js                                   # SVG gauge rendering, dimension bars, clock data object
  index.html                                   # Homepage: the clock
  investigacion.html                           # Research phases listing
  metodologia.html                             # How the clock works
  plans/                                       # Design and implementation plans (future)
generate_report.py                             # Script to regenerate the PDF report
.gitignore                                     # .DS_Store, .venv, __pycache__, *.pyc
```
