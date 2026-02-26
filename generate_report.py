#!/usr/bin/env python3
"""Generate a PDF report from all research documents."""

import markdown
from weasyprint import HTML
from pathlib import Path

RESEARCH_DIR = Path("docs/research")
OUTPUT_FILE = Path("docs/Congreso_Monitor_Informe_Investigacion.pdf")

# Order of documents to include
DOCUMENTS = [
    "01-institutional-structure.md",
    "02-executive-power.md",
    "03-legal-framework.md",
    "04-historical-patterns.md",
    "05-chile-today.md",
    "06-security-migration.md",
    "07-economic-pressures.md",
    "08-civil-society.md",
    "09-erosion-scenarios.md",
    "bibliography.md",
]

CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm;
    @bottom-center {
        content: "Congreso Monitor — Informe de Investigación | Página " counter(page);
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
    padding-top: 8cm;
}
.cover h1 {
    font-size: 32pt;
    font-weight: 700;
    color: #1a3a5c;
    margin-bottom: 0.3em;
    letter-spacing: -0.5px;
}
.cover .subtitle {
    font-size: 16pt;
    color: #4a4a4a;
    margin-bottom: 2em;
}
.cover .meta {
    font-size: 11pt;
    color: #666;
    margin-top: 4cm;
}
.cover .meta p {
    margin: 0.3em 0;
}

/* TOC page */
.toc {
    page-break-after: always;
}
.toc h2 {
    color: #1a3a5c;
    border-bottom: 2px solid #1a3a5c;
}
.toc ul {
    list-style: none;
    padding: 0;
}
.toc li {
    padding: 0.4em 0;
    border-bottom: 1px dotted #ccc;
}
.toc li.phase {
    font-weight: 600;
    font-size: 12pt;
    padding-top: 1em;
    border-bottom: none;
    color: #1a3a5c;
}

/* Section separator */
.section-separator {
    page-break-before: always;
}

/* Headings */
h1 {
    font-size: 22pt;
    color: #1a3a5c;
    border-bottom: 3px solid #1a3a5c;
    padding-bottom: 0.3em;
    margin-top: 1.5em;
    page-break-after: avoid;
}
h2 {
    font-size: 16pt;
    color: #2a5a8c;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
    margin-top: 1.2em;
    page-break-after: avoid;
}
h3 {
    font-size: 13pt;
    color: #3a6a9c;
    margin-top: 1em;
    page-break-after: avoid;
}
h4 {
    font-size: 11.5pt;
    color: #4a7aac;
    margin-top: 0.8em;
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

/* Blockquotes - used for relevance notes */
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

/* Code blocks */
pre {
    background-color: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1em;
    font-size: 9pt;
    line-height: 1.4;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
}
code {
    font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
    font-size: 9.5pt;
    background-color: #f0f0f0;
    padding: 0.1em 0.3em;
    border-radius: 3px;
}
pre code {
    background-color: transparent;
    padding: 0;
}

/* Lists */
ul, ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
li {
    margin-bottom: 0.3em;
}

/* Horizontal rules as section breaks */
hr {
    border: none;
    border-top: 2px solid #1a3a5c;
    margin: 2em 0;
}

/* Strong emphasis for monitoring indicators */
strong {
    color: #1a1a1a;
}

/* Links */
a {
    color: #2a5a8c;
    text-decoration: none;
}
"""


def build_cover_html():
    return """
    <div class="cover">
        <h1>Congreso Monitor</h1>
        <p class="subtitle">Informe de Investigación:<br>
        Estructura Institucional, Marco Legal, Contexto Actual<br>
        y Escenarios de Erosión Democrática en Chile</p>
        <div class="meta">
            <p>Proyecto de monitoreo legislativo para la detección de deriva autoritaria</p>
            <p>Febrero 2026</p>
        </div>
    </div>
    """


def build_toc_html():
    return """
    <div class="toc">
        <h2>Tabla de Contenidos</h2>
        <ul>
            <li class="phase">Fase 1: Estructura Institucional</li>
            <li>1. Estructura Bicameral (Cámara de Diputados y Senado)</li>
            <li>2. El Proceso de Formación de la Ley</li>
            <li>3. Sistema de Comisiones</li>
            <li>4. Actores Institucionales Clave</li>
            <li>5. Mecánica de las Sesiones</li>
            <li>6. Consideraciones para el Monitoreo</li>

            <li class="phase">Fase 2: Poder Ejecutivo sobre la Legislación</li>
            <li>1. Iniciativa Legislativa Presidencial</li>
            <li>2. El Sistema de Urgencias</li>
            <li>3. Veto Presidencial</li>
            <li>4. Legislatura Extraordinaria</li>
            <li>5. Legislación Delegada (DFL, Decretos Supremos)</li>
            <li>6. Estados de Excepción Constitucional</li>
            <li>7. Otros Mecanismos de Influencia Ejecutiva</li>
            <li>8. Mapa de Herramientas Ejecutivas</li>
            <li>9. Indicadores de Alerta</li>

            <li class="phase">Fase 3: Marco Jurídico</li>
            <li>1. Constitución Política de la República</li>
            <li>2. LOC del Congreso Nacional — Ley 18.918</li>
            <li>3. Reglamentos Internos</li>
            <li>4. Ley 21.535 — Reforma de Quórum (2023)</li>
            <li>5. Tribunal Constitucional</li>
            <li>6. Contraloría General de la República</li>
            <li>7. Transparencia y Acceso a la Información</li>
            <li>8. Implicancias para el Monitoreo</li>

            <li class="phase">Fase 4: Patrones Históricos y Contexto Comparado</li>
            <li>1. Precedente Histórico Chileno</li>
            <li>2. Patrones de Abuso de Urgencias</li>
            <li>3. Casos Comparados en América Latina</li>
            <li>4. Indicadores desde la Ciencia Política</li>
            <li>5. Marco de Monitoreo para Chile</li>

            <li class="phase">Fase 5: Chile Hoy — Panorama Político 2019-2026</li>
            <li>1. Fragmentación Política y Crisis del Sistema de Partidos</li>
            <li>2. Post-Estallido Social y Procesos Constituyentes</li>
            <li>3. Confianza Pública y Legitimidad Institucional</li>
            <li>4. Dinámicas del Gobierno Boric</li>
            <li>5. Paisaje Electoral 2025-2026</li>

            <li class="phase">Fase 6: Narrativa de Seguridad y Migración</li>
            <li>1. Evolución del Crimen y Crimen Organizado</li>
            <li>2. La Ola Migratoria</li>
            <li>3. Estados de Excepción como Herramienta de Gobernanza</li>
            <li>4. Militarización de la Seguridad Pública</li>
            <li>5. Tradeoffs de Libertades Civiles</li>
            <li>6. La Narrativa de Seguridad en el Discurso Político</li>

            <li class="phase">Fase 7: Presiones Económicas</li>
            <li>1. La Crisis de Pensiones (AFP)</li>
            <li>2. Desigualdad y Costo de Vida</li>
            <li>3. Dependencia del Cobre y Vulnerabilidad Fiscal</li>
            <li>4. Empleo, Informalidad y Trabajo Migrante</li>
            <li>5. Crisis Económica como Precondición Autoritaria</li>

            <li class="phase">Fase 8: Sociedad Civil y Resiliencia Democrática</li>
            <li>1. Paisaje Mediático</li>
            <li>2. Organizaciones de Vigilancia</li>
            <li>3. Independencia Judicial</li>
            <li>4. Universidades y Think Tanks</li>
            <li>5. Movimientos Sociales Post-Estallido</li>
            <li>6. Prevención y Resiliencia</li>

            <li class="phase">Fase 9: Escenarios de Erosión — Síntesis</li>
            <li>1. Perfil de Riesgo de Chile</li>
            <li>2. Escenarios Chile-Específicos</li>
            <li>3. Vulnerabilidad Institucional</li>
            <li>4. Señales de Alerta Temprana</li>
            <li>5. Análisis de Temporalidad</li>
            <li>6. Vías de Salida</li>

            <li class="phase">Bibliografía</li>
            <li>Fuentes oficiales, portales de datos, ciencia política, índices democráticos</li>
        </ul>
    </div>
    """


def md_to_html(md_text):
    extensions = ["tables", "fenced_code", "toc", "smarty"]
    return markdown.markdown(md_text, extensions=extensions)


def main():
    html_parts = [build_cover_html(), build_toc_html()]

    for i, doc_name in enumerate(DOCUMENTS):
        doc_path = RESEARCH_DIR / doc_name
        if not doc_path.exists():
            print(f"Warning: {doc_path} not found, skipping.")
            continue

        md_content = doc_path.read_text(encoding="utf-8")
        doc_html = md_to_html(md_content)

        # Add section separator
        html_parts.append(f'<div class="section-separator">{doc_html}</div>')
        print(f"Included: {doc_name}")

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>{CSS}</style>
</head>
<body>
{''.join(html_parts)}
</body>
</html>"""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=full_html).write_pdf(str(OUTPUT_FILE))
    print(f"\nPDF generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
