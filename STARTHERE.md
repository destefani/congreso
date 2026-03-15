# Congreso Monitor

## Project Goal

Monitor the Chilean Congress to track executive influence over legislation and detect potential authoritarian drift. The long-term goal is a public website where citizens can see what's happening in Congress.

## Current Phase: First Update — March 2026

All research phases (1-10) are complete. The first periodic update (March 2026) has been completed, adding three new research documents covering the Kast inauguration (March 11, 2026), democracy indices, and security/migration developments.

**Key developments since last assessment (Feb 2026):**
- Jose Antonio Kast (Partido Republicano) won with 58.16% in runoff (Dec 14, 2025) — most-voted candidate in Chilean history
- Inaugurated March 11, 2026 as "gobierno de emergencia"
- Plan Escudo Fronterizo: 3,000+ troops, walls, trenches, detention centers at northern border
- Announced presidential pardons for 102 police/military convicted of estallido social human rights violations
- Four Supreme Court vacancies for Kast to fill
- Total State Audit of Boric government
- Congress split: Senate tied 25-25; Chamber without government majority
- Only 49% of citizens prefer democracy (CEP)

**Clock reading:** Proposed adjustment from 4:30 to **4:00 a medianoche** (still Erosion Temprana, but closer to lower bound). See `docs/research/CHANGELOG.md` for full justification.

**Next update:** June 2026 (or sooner if critical events occur)

## GitHub Pages Site

Built in `docs/` with three pages:
- **index.html** — Homepage with SVG semicircular gauge, 5 dimension bars (expand/collapse), key facts strip, and navigation cards
- **investigacion.html** — All 10 research phases with links to the markdown files and PDF download
- **metodologia.html** — Full methodology: zones, dimensions, indicators table, scoring, point of no return

The site is plain HTML/CSS/JS with no dependencies or build step. To update the clock reading, edit `docs/js/clock.js` (the `CLOCK_DATA` object) and commit.

**Next step:** Update clock.js with new reading, update site pages with new research links, push to GitHub Pages.

## Research Plan

Research documents in `docs/research/`:

### Baseline Research (Feb 2026)

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
| 9 | Erosion Scenarios — Synthesis | `09-erosion-scenarios.md` | Done |
| 10 | El Reloj Democratico de Chile | `10-democratic-clock.md` | Done |

### Periodic Updates

| Phase | Topic | File | Date | Status |
|-------|-------|------|------|--------|
| 11 | Democracy Indices 2025-2026 | `11-democracy-indices-2025-2026.md` | Mar 2026 | Done |
| 12 | Situation Report Feb-Mar 2026 | `12-situation-report-2026-03.md` | Mar 2026 | Done |
| 13 | Security & Migration Update 2025-2026 | `13-security-migration-update-2025-2026.md` | Mar 2026 | Done |

### Update Tracking

| File | Purpose |
|------|---------|
| `CHANGELOG.md` | All clock reading changes with justification, history, and next monitoring indicators |
| `bibliography.md` | All sources across all phases, kept up to date |

## Key Context

- Chilean Congress is bicameral: Camara de Diputados (155) + Senado (50)
- The President has significant legislative power: exclusive initiative, urgencies, vetos, extraordinary sessions
- Data sources exist: opendata.congreso.cl, Camara API, Senado API, BCN linked data
- Existing civic tech: Ciudadania Inteligente, Congreso Abierto, Congreso Virtual
- **New government (Mar 2026):** Jose Antonio Kast (Republicano), coalition with Chile Vamos, Democrats, Amarillos
- **Senate tied 25-25** — mandatory negotiation for all legislation
- **Four Supreme Court vacancies** — critical appointment power

## Bibliography

See `docs/research/bibliography.md` for all sources.

## Compiled Report

`docs/Congreso_Monitor_Informe_Investigacion.pdf` — Full research report (1.8 MB, ~7,000 lines across all phases). Needs regeneration to include phases 11-13.

## Directory Structure

```
docs/
  research/
    01-institutional-structure.md               # Phase 1: Bicameral structure, legislative process, committees
    02-executive-power.md                       # Phase 2: Presidential powers, urgencies, veto, states of exception
    03-legal-framework.md                       # Phase 3: Constitution, LOC 18.918, TC, Contraloria, transparency
    04-historical-patterns.md                   # Phase 4: Chilean history, Latin American comparisons, erosion indicators
    05-chile-today.md                          # Phase 5: Political fragmentation, post-estallido, trust crisis, 2025 elections
    06-security-migration.md                   # Phase 6: Crime, migration, states of exception, militarization
    07-economic-pressures.md                   # Phase 7: Pensions, inequality, copper dependency, employment
    08-civil-society.md                        # Phase 8: Media, watchdogs, judiciary, movements, resilience
    09-erosion-scenarios.md                    # Phase 9: SYNTHESIS — Chile-specific erosion scenarios, risk profile
    10-democratic-clock.md                     # Phase 10: El Reloj Democratico — early warning scale
    11-democracy-indices-2025-2026.md          # Phase 11: V-Dem, Freedom House, EIU, TI, WJP, RSF, Latinobarometro
    12-situation-report-2026-03.md             # Phase 12: Kast inauguration, first week, elections, full situation
    13-security-migration-update-2025-2026.md  # Phase 13: Security/migration deep update (mid-2025 to Mar 2026)
    CHANGELOG.md                               # Clock reading history, dimensional changes, justifications
    bibliography.md                            # All sources, kept up to date
  Congreso_Monitor_Informe_Investigacion.pdf   # Compiled PDF report
  css/
    style.css                                  # Single stylesheet
  js/
    clock.js                                   # SVG gauge rendering, dimension bars, clock data object
  index.html                                   # Homepage: the clock
  investigacion.html                           # Research phases listing
  metodologia.html                             # How the clock works
  plans/                                       # Design and implementation plans
generate_report.py                             # Script to regenerate the PDF report
.gitignore                                     # .DS_Store, .venv, __pycache__, *.pyc
```
