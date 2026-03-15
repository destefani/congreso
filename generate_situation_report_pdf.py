#!/usr/bin/env python3
"""Generate a PDF of the situation report in Spanish."""

import markdown
from weasyprint import HTML
from pathlib import Path

INPUT_FILE = Path("docs/research/12-situation-report-2026-03.md")
OUTPUT_FILE = Path("docs/Informe_Situacion_Chile_Marzo_2026.pdf")

CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm;
    @bottom-center {
        content: "Congreso Monitor — Informe de Situacion Marzo 2026 | Pagina " counter(page);
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
}

/* Cover page */
.cover {
    page-break-after: always;
    text-align: center;
    padding-top: 6cm;
}
.cover h1 {
    font-size: 28pt;
    font-weight: 700;
    color: #1a3a5c;
    margin-bottom: 0.3em;
}
.cover .subtitle {
    font-size: 16pt;
    color: #4a4a4a;
    margin-bottom: 0.5em;
}
.cover .clock-reading {
    font-size: 20pt;
    font-weight: 700;
    color: #e67e22;
    margin: 1em 0;
}
.cover .meta {
    font-size: 11pt;
    color: #666;
    margin-top: 3cm;
}
.cover .meta p {
    margin: 0.3em 0;
}

/* Headings */
h1 {
    font-size: 20pt;
    color: #1a3a5c;
    border-bottom: 3px solid #1a3a5c;
    padding-bottom: 0.3em;
    margin-top: 1.5em;
    page-break-after: avoid;
}
h2 {
    font-size: 15pt;
    color: #2a5a8c;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
    margin-top: 1.2em;
    page-break-after: avoid;
}
h3 {
    font-size: 12pt;
    color: #3a6a9c;
    margin-top: 1em;
    page-break-after: avoid;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}
th {
    background-color: #1a3a5c;
    color: white;
    padding: 0.5em 0.8em;
    text-align: left;
    font-weight: 600;
}
td {
    padding: 0.4em 0.8em;
    border-bottom: 1px solid #ddd;
}
tr:nth-child(even) td {
    background-color: #f5f7fa;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #c0392b;
    background-color: #fef5f4;
    padding: 0.8em 1em;
    margin: 1em 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
}
blockquote strong {
    color: #c0392b;
}

/* Lists */
ul, ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
li {
    margin-bottom: 0.3em;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 2px solid #1a3a5c;
    margin: 2em 0;
}

strong {
    color: #1a1a1a;
}

a {
    color: #2a5a8c;
    text-decoration: none;
}

/* Erosion assessment boxes - paragraphs starting with EROSION ASSESSMENT */
p strong:first-child {
    color: #c0392b;
}
"""


# Translation map for section headers and key terms
TRANSLATIONS = {
    "# Chile Situation Report: February - March 2026": "# Informe de Situacion: Chile, Febrero - Marzo 2026",
    "## Democratic Erosion Monitoring Update": "## Actualizacion del Monitoreo de Erosion Democratica",
    "**Period covered:**": "**Periodo cubierto:**",
    "**Report date:**": "**Fecha del informe:**",
    "**Purpose:**": "**Proposito:**",
    "Comprehensive political situation assessment for the El Reloj Democratico de Chile project": "Evaluacion integral de la situacion politica para el proyecto El Reloj Democratico de Chile",
    "## 1. 2025 Presidential and Parliamentary Elections Results": "## 1. Resultados de las elecciones presidenciales y parlamentarias 2025",
    "### Presidential Election": "### Eleccion presidencial",
    "### Parliamentary Elections (November 16, 2025)": "### Elecciones parlamentarias (16 de noviembre de 2025)",
    "## 2. New President and Government": "## 2. Nuevo presidente y gobierno",
    "### Inauguration (March 11, 2026)": "### Inauguracion (11 de marzo de 2026)",
    '### Inaugural Speech - "Government of Emergency"': '### Discurso inaugural — "Gobierno de emergencia"',
    "### First Six Decrees (signed March 11, 2026)": "### Seis primeros decretos (firmados el 11 de marzo de 2026)",
    "### Cabinet (24 Ministers, appointed January 20, 2026)": "### Gabinete (24 ministros, nombrados el 20 de enero de 2026)",
    "### Coalition Dynamics": "### Dinamica de la coalicion",
    "## 3. States of Exception": "## 3. Estados de excepcion",
    "### Macrozona Sur (Araucania / Biobio)": "### Macrozona sur (Araucania / Biobio)",
    "### Northern Border (Macrozona Norte)": "### Frontera norte (macrozona norte)",
    "## 4. Security and Migration Policy": "## 4. Politica de seguridad y migracion",
    "### Plan Escudo Fronterizo (Frontier Shield Plan)": "### Plan Escudo Fronterizo",
    "### Mass Deportation Plan": "### Plan de deportacion masiva",
    "### Human Rights Concerns": "### Preocupaciones de derechos humanos",
    "## 5. Constitutional and Institutional Changes": "## 5. Cambios constitucionales e institucionales",
    "### Supreme Court Crisis - Four Vacancies": "### Crisis en la Corte Suprema — cuatro vacantes",
    "### Contraloria General de la Republica": "### Contraloria General de la Republica",
    "### Tribunal Constitucional": "### Tribunal Constitucional",
    "### INDH (National Institute of Human Rights)": "### INDH (Instituto Nacional de Derechos Humanos)",
    "### State Audit as Institutional Tool": "### Auditoria del Estado como herramienta institucional",
    "## 6. Civil Liberties and Human Rights": "## 6. Libertades civiles y derechos humanos",
    "### Pardons for Police/Military Convicted of Estallido Social Abuses": "### Indultos a uniformados condenados por abusos del estallido social",
    "### Civil Society Organizations' Concerns": "### Preocupaciones de la sociedad civil",
    "### UN Human Rights Examination": "### Examen de derechos humanos de la ONU",
    "## 7. Public Opinion": "## 7. Opinion publica",
    "### CADEM Polls (February-March 2026)": "### Encuestas CADEM (febrero-marzo 2026)",
    "### Criteria Poll (March 2026)": "### Encuesta Criteria (marzo 2026)",
    "### CEP - Democratic Satisfaction Data": "### CEP — Satisfaccion democratica",
    "### Institutional Trust (CEP)": "### Confianza institucional (CEP)",
    "## 8. Congress Dynamics": "## 8. Dinamica congresional",
    "### Leadership of Both Chambers": "### Direccion de ambas camaras",
    '### Legislative Agenda - "Plan Desafio 90"': '### Agenda legislativa — "Plan Desafio 90"',
    '### "National Reconstruction" Bill (announced March 14, 2026)': '### Proyecto de "Reconstruccion Nacional" (anunciado el 14 de marzo de 2026)',
    "### Political Dynamics": "### Dinamica politica",
    "## 9. Judiciary": "## 9. Poder Judicial",
    "### Caso Hermosilla (Caso Audios) - Status": "### Caso Hermosilla (Caso Audios) — Estado",
    "### Caso Muneca Bielorrusa (Belarusian Doll Case) - Angela Vivanco": "### Caso Muneca Bielorrusa — Angela Vivanco",
    "### Broader Judicial Crisis": "### Crisis judicial mas amplia",
    "### Former Fiscal Manuel Guerra": "### Ex-fiscal Manuel Guerra",
    "## 10. Economic Situation": "## 10. Situacion economica",
    "### GDP Growth": "### Crecimiento del PIB",
    "### Inflation": "### Inflacion",
    "### Monetary Policy": "### Politica monetaria",
    "### Employment": "### Empleo",
    "### Pension Reform (Ley 21.735)": "### Reforma de pensiones (Ley 21.735)",
    "### Kast's Economic Agenda": "### Agenda economica de Kast",
    "### Wildfires Emergency (January 2026)": "### Emergencia por incendios forestales (enero 2026)",
    "## 11. International Relations and Geopolitical Context": "## 11. Relaciones internacionales y contexto geopolitico",
    "### China-Chile Submarine Cable Controversy": "### Controversia del cable submarino Chile-China",
    "### Inauguration Diplomacy": "### Diplomacia de inauguracion",
    "## Summary: Democratic Erosion Risk Assessment (as of March 15, 2026)": "## Resumen: Evaluacion de riesgo de erosion democratica (al 15 de marzo de 2026)",
    "### High-Risk Indicators": "### Indicadores de alto riesgo",
    "### Mitigating Factors": "### Factores mitigantes",
    "### Key Indicators to Monitor Next 90 Days": "### Indicadores clave a monitorear en los proximos 90 dias",
    "**EROSION ASSESSMENT:**": "**EVALUACION DE EROSION:**",
    "**This is the single most alarming development for democratic erosion monitoring.**": "**Este es el desarrollo mas alarmante para el monitoreo de erosion democratica.**",
    "Sources:": "Fuentes:",
    "Key observation:": "Observacion clave:",
    "Key facts:": "Datos clave:",
    "Key quotes:": "Citas clave:",
    "**Criminal proceedings:**": "**Proceso penal:**",
    "**Hermosilla's counter-accusations:**": "**Contra-acusaciones de Hermosilla:**",
    "**Opposition reaction was fierce:**": "**La reaccion opositora fue intensa:**",
    "**Notable attendees:**": "**Asistentes notables:**",
    "**Notable absence:**": "**Ausencia notable:**",
    "**Party composition:**": "**Composicion partidaria:**",
    "**Key appointments:**": "**Nombramientos clave:**",
    "**First Round (November 16, 2025):**": "**Primera vuelta (16 de noviembre de 2025):**",
    "**Second Round / Runoff (December 14, 2025):**": "**Segunda vuelta (14 de diciembre de 2025):**",
    "**Chamber of Deputies (155 seats, all renewed):**": "**Camara de Diputados (155 escanos, todos renovados):**",
    "**Senate (23 of 50 seats renewed; total composition for 2026-2030):**": "**Senado (23 de 50 escanos renovados; composicion total 2026-2030):**",
    "**Boric's final approval (March 8, 2026):**": "**Aprobacion final de Boric (8 de marzo de 2026):**",
    "**Expectations for Kast (March 1-9, 2026):**": "**Expectativas para Kast (1-9 de marzo de 2026):**",
    "**Kast's initial image (March 13, CADEM):**": "**Imagen inicial de Kast (13 de marzo, CADEM):**",
    "Candidate": "Candidato",
    "Party/Coalition": "Partido/Coalicion",
    "% of Vote": "% Votos",
    "Votes": "Votos",
    "Coalition": "Coalicion",
    "Seats": "Escanos",
    "Bloc": "Bloque",
    "Position": "Cartera",
    "Name": "Nombre",
    "Institution": "Institucion",
    "Trust %": "% Confianza",
}


def translate_headers(text):
    """Apply header and key term translations."""
    for eng, esp in TRANSLATIONS.items():
        text = text.replace(eng, esp)
    return text


def md_to_html(md_text):
    extensions = ["tables", "fenced_code", "toc", "smarty"]
    return markdown.markdown(md_text, extensions=extensions)


def build_cover():
    return """
    <div class="cover">
        <h1 style="border:none">Informe de Situacion</h1>
        <p class="subtitle">Chile: Febrero — Marzo 2026</p>
        <p class="clock-reading">Reloj Democratico: 4:30 &rarr; 4:00 a medianoche</p>
        <p class="subtitle" style="font-size:12pt">Erosion Temprana</p>
        <div class="meta">
            <p>Congreso Monitor</p>
            <p>Proyecto de monitoreo de erosion democratica en Chile</p>
            <p>15 de marzo de 2026</p>
        </div>
    </div>
    """


def main():
    if not INPUT_FILE.exists():
        print(f"Error: {INPUT_FILE} not found")
        return

    md_content = INPUT_FILE.read_text(encoding="utf-8")

    # Translate headers and key terms
    md_content = translate_headers(md_content)

    # Convert to HTML
    doc_html = md_to_html(md_content)

    # Build full HTML
    cover = build_cover()
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>{CSS}</style>
</head>
<body>
{cover}
<div class="section-separator">
{doc_html}
</div>
</body>
</html>"""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=full_html).write_pdf(str(OUTPUT_FILE))
    print(f"PDF generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
