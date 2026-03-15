/* ============================================
   El Reloj Democratico de Chile
   Clock SVG + Dimension Bars
   ============================================ */

const CLOCK_DATA = {
  reading: "4:00",
  hoursToMidnight: 4.0,
  zone: "Erosion Temprana",
  zoneColor: "#e67e22",
  date: "Marzo 2026",
  previousReading: "4:30",
  previousDate: "Febrero 2026",
  dimensions: [
    {
      name: "Estado de Excepcion",
      reading: "3:30",
      hours: 3.5,
      zone: "orange",
      zoneName: "Erosion Temprana",
      description: "Chile supero 1.000 dias continuos de estado de excepcion en la macrozona sur (feb 2025). Solo 51 dias sin estado de excepcion desde octubre 2021, con 61 prorrogas. El Plan Escudo Fronterizo (mar 2026) despliega 3.000+ militares permanentes en la frontera norte, con muros de 5m, zanjas de 3m, centros de detencion y vigilancia biometrica. La militarizacion de la seguridad se profundiza sin precedentes en el Chile post-Pinochet."
    },
    {
      name: "Legitimidad Democratica",
      reading: "5:00",
      hours: 5.0,
      zone: "orange",
      zoneName: "Erosion Temprana",
      description: "Solo 49% de los chilenos prefiere la democracia (CEP). Solo 12% cree que funciona bien. 19% prefiere un gobierno autoritario. Chile tiene el optimismo economico mas bajo de America Latina (30%, Latinobarometro) y el 77% teme al crimen. El EIU califica la cultura politica en 5,63/10 — el factor que impide la clasificacion como democracia plena."
    },
    {
      name: "Equilibrio de Poderes",
      reading: "5:30",
      hours: 5.5,
      zone: "orange",
      zoneName: "Erosion Temprana",
      description: "Kast declaro que 'el Congreso no es tan relevante como la gente podria imaginar' y marco su administracion como 'gobierno de emergencia'. Seis decretos firmados el dia de asuncion. El oficialismo controla las presidencias de ambas camaras. Auditoria total al gobierno anterior como posible herramienta de persecucion politica. Mitigante: el Senado esta empatado 25-25 y la Camara requiere alianzas cruzadas."
    },
    {
      name: "Independencia Institucional",
      reading: "5:30",
      hours: 5.5,
      zone: "orange",
      zoneName: "Erosion Temprana",
      description: "Cuatro vacantes en la Corte Suprema que Kast llenara — poder transformativo sobre el Poder Judicial. Ex-ministra Vivanco en prision preventiva por cohecho; caso Hermosilla con peticion de 14 anos. Anuncio de indultos presidenciales para 102 uniformados condenados por violaciones de DDHH en el estallido social. Ministros de Defensa y Justicia con historial de defensa de Pinochet. Mitigante: Contraloria y tribunales siguen operando con independencia."
    },
    {
      name: "Resiliencia Civil",
      reading: "7:00",
      hours: 7.0,
      zone: "yellow",
      zoneName: "Tensiones Democraticas",
      description: "Chile cayo 17 posiciones en libertad de prensa (RSF: 69°, era 52°). Indicador economico de prensa el peor (88°) por concentracion mediatica. CIPER, El Mostrador y The Clinic siguen operando. 115 organizaciones de DDHH protestaron nombramientos ministeriales. La sociedad civil esta activa pero la fatiga civica post-estallido y post-constituyente es real."
    }
  ],
  keyFacts: [
    { number: "3.000+", label: "militares desplegados en frontera norte" },
    { number: "49%", label: "de los chilenos prefiere la democracia" },
    { number: "102", label: "uniformados que Kast planea indultar" }
  ]
};

/* --- Zone Colors --- */
const ZONE_COLORS = {
  green:   "#27ae60",
  yellow:  "#f1c40f",
  orange:  "#e67e22",
  red:     "#e74c3c",
  darkred: "#922b21"
};

/* --- SVG Gauge --- */
function renderGauge(containerId) {
  var container = document.getElementById(containerId);
  if (!container) return;

  var NS = "http://www.w3.org/2000/svg";
  var w = 560, h = 330;
  var cx = 280, cy = 275;
  var r = 190;
  var arcStroke = 42;
  var trackStroke = 50;
  var font = "-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif";

  function el(tag, attrs) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) {
      if (attrs.hasOwnProperty(k)) e.setAttribute(k, String(attrs[k]));
    }
    return e;
  }

  // Hours (0-12) to angle in radians. 0:00=180deg (left), 12:00=0deg (right)
  function hToRad(hours) {
    return (180 - hours * 15) * Math.PI / 180;
  }

  // Point on circle at given hour and radius
  function pt(hours, radius) {
    var a = hToRad(hours);
    return [cx + radius * Math.cos(a), cy - radius * Math.sin(a)];
  }

  // SVG arc path from hourA to hourB at given radius
  function arc(hFrom, hTo, radius) {
    var p1 = pt(hFrom, radius);
    var p2 = pt(hTo, radius);
    var span = (hTo - hFrom) * 15;
    var large = span > 180 ? 1 : 0;
    return "M " + p1[0] + " " + p1[1] + " A " + radius + " " + radius + " 0 " + large + " 1 " + p2[0] + " " + p2[1];
  }

  var svg = el("svg", { viewBox: "0 0 " + w + " " + h, xmlns: NS, role: "img" });

  // Accessible title
  var titleEl = el("title", {});
  titleEl.textContent = "El Reloj Democratico de Chile: " + CLOCK_DATA.reading + " a medianoche - " + CLOCK_DATA.zone;
  svg.appendChild(titleEl);

  // --- Defs ---
  var defs = el("defs", {});

  // Needle shadow filter
  var nf = el("filter", { id: "nshadow", x: "-50%", y: "-50%", width: "200%", height: "200%" });
  nf.appendChild(el("feGaussianBlur", { "in": "SourceAlpha", stdDeviation: "2.5" }));
  nf.appendChild(el("feOffset", { dx: "1", dy: "2", result: "s" }));
  var nm = el("feMerge", {});
  nm.appendChild(el("feMergeNode", { "in": "s" }));
  nm.appendChild(el("feMergeNode", { "in": "SourceGraphic" }));
  nf.appendChild(nm);
  defs.appendChild(nf);

  // Zone glow filter
  var gf = el("filter", { id: "zglow", x: "-30%", y: "-30%", width: "160%", height: "160%" });
  gf.appendChild(el("feGaussianBlur", { "in": "SourceGraphic", stdDeviation: "6", result: "g" }));
  var gm = el("feMerge", {});
  gm.appendChild(el("feMergeNode", { "in": "g" }));
  gm.appendChild(el("feMergeNode", { "in": "SourceGraphic" }));
  gf.appendChild(gm);
  defs.appendChild(gf);

  // Text path for zone labels (midline arc)
  var textArcPath = arc(0, 12, r);
  var tp = el("path", { id: "zone-arc-text", d: textArcPath });
  defs.appendChild(tp);

  svg.appendChild(defs);

  // === Layer 1: Dark background track ===
  svg.appendChild(el("path", {
    d: arc(0, 12, r), fill: "none", stroke: "#1e2d3d",
    "stroke-width": trackStroke, "stroke-linecap": "round"
  }));

  // === Layer 2: Zone arcs ===
  var zones = [
    { from: 0,  to: 1,  color: ZONE_COLORS.darkred, label: "CRISIS" },
    { from: 1,  to: 3,  color: ZONE_COLORS.red,     label: "ACTIVA" },
    { from: 3,  to: 6,  color: ZONE_COLORS.orange,  label: "EROSION" },
    { from: 6,  to: 10, color: ZONE_COLORS.yellow,  label: "TENSIONES" },
    { from: 10, to: 12, color: ZONE_COLORS.green,    label: "PLENA" }
  ];

  var currentH = CLOCK_DATA.hoursToMidnight;

  zones.forEach(function(z) {
    var d = arc(z.from, z.to, r);
    var isCurrent = currentH >= z.from && currentH < z.to;

    // Glow under current zone
    if (isCurrent) {
      svg.appendChild(el("path", {
        d: d, fill: "none", stroke: z.color, "stroke-width": arcStroke + 10,
        "stroke-linecap": "butt", opacity: "0.35", filter: "url(#zglow)"
      }));
    }

    svg.appendChild(el("path", {
      d: d, fill: "none", stroke: z.color, "stroke-width": arcStroke,
      "stroke-linecap": "butt"
    }));
  });

  // === Layer 3: Tick marks ===
  var tickOuter = r + trackStroke / 2 - 3;
  for (var hr = 0; hr <= 12; hr++) {
    var major = (hr % 3 === 0);
    var tickInner = major ? (r - trackStroke / 2 + 3) : (r - arcStroke / 4);
    var p1 = pt(hr, tickOuter);
    var p2 = pt(hr, tickInner);
    svg.appendChild(el("line", {
      x1: p1[0], y1: p1[1], x2: p2[0], y2: p2[1],
      stroke: "#fff", "stroke-width": major ? "2.5" : "1.2",
      opacity: major ? "0.9" : "0.4"
    }));
  }

  // === Layer 4: Scale labels outside arc ===
  var labelR = r + trackStroke / 2 + 16;
  [0, 3, 6, 9, 12].forEach(function(h) {
    var p = pt(h, labelR);
    var t = el("text", {
      x: p[0], y: p[1], "text-anchor": "middle", "dominant-baseline": "middle",
      "font-size": "13", "font-weight": "700", "font-family": font, fill: "#444"
    });
    t.textContent = h + ":00";
    svg.appendChild(t);
  });

  // Endpoint labels: MEDIANOCHE / MEDIODIA (positioned below the hour numbers)
  var pLeft = pt(0, labelR);
  var tMn = el("text", {
    x: pLeft[0], y: pLeft[1] + 15, "text-anchor": "middle", "dominant-baseline": "middle",
    "font-size": "8", "font-weight": "700", "letter-spacing": "0.1em",
    "font-family": font, fill: "#922b21"
  });
  tMn.textContent = "MEDIANOCHE";
  svg.appendChild(tMn);

  var pRight = pt(12, labelR);
  var tMd = el("text", {
    x: pRight[0], y: pRight[1] + 15, "text-anchor": "middle", "dominant-baseline": "middle",
    "font-size": "8", "font-weight": "700", "letter-spacing": "0.1em",
    "font-family": font, fill: "#27ae60"
  });
  tMd.textContent = "MEDIODIA";
  svg.appendChild(tMd);

  // === Layer 5: Zone name labels along the arc ===
  // Use textPath on the midline arc for clean curved text
  var arcLen = Math.PI * r; // total semicircle length
  zones.forEach(function(z) {
    var startPct = (z.from / 12) * 100;
    var endPct = (z.to / 12) * 100;
    var midPct = (startPct + endPct) / 2;

    var txt = el("text", {
      "font-size": "10", "font-weight": "700", "letter-spacing": "0.18em",
      "font-family": font, fill: "rgba(255,255,255,0.85)", "text-anchor": "middle"
    });
    var tpath = el("textPath", { href: "#zone-arc-text", startOffset: midPct + "%" });
    tpath.textContent = z.label;
    txt.appendChild(tpath);
    svg.appendChild(txt);
  });

  // === Layer 6: Needle ===
  var needleLen = r - arcStroke / 2 - 15;
  var targetRot = currentH * 15 - 90;
  var startRot = 90; // starts at 12:00 (right side)

  var ng = el("g", { id: "clock-needle", filter: "url(#nshadow)" });
  ng.setAttribute("transform", "rotate(" + startRot + "," + cx + "," + cy + ")");

  // Needle body: tapered triangle pointing up from center
  ng.appendChild(el("polygon", {
    points: cx + "," + (cy - needleLen) + " " + (cx - 7) + "," + (cy - 12) + " " + (cx + 7) + "," + (cy - 12),
    fill: "#c0392b"
  }));

  // Needle shaft: thin rect connecting triangle to center
  ng.appendChild(el("rect", {
    x: cx - 2.5, y: cy - 12, width: 5, height: 12, rx: 1, fill: "#a93226"
  }));

  // Small counterweight tail
  ng.appendChild(el("polygon", {
    points: cx + "," + (cy + 22) + " " + (cx - 5) + "," + (cy + 2) + " " + (cx + 5) + "," + (cy + 2),
    fill: "#7b241c"
  }));

  svg.appendChild(ng);

  // === Layer 7: Center hub ===
  svg.appendChild(el("circle", { cx: cx, cy: cy, r: 14, fill: "#1a3a5c" }));
  svg.appendChild(el("circle", { cx: cx, cy: cy, r: 9, fill: "#c0392b" }));
  svg.appendChild(el("circle", { cx: cx, cy: cy, r: 4, fill: "#fff" }));

  // === Layer 8: Reading text inside the gauge ===
  var tReading = el("text", {
    x: cx, y: cy - 105, "text-anchor": "middle", "dominant-baseline": "middle",
    "font-size": "60", "font-weight": "800", "font-family": font, fill: "#1a3a5c"
  });
  tReading.textContent = CLOCK_DATA.reading;
  svg.appendChild(tReading);

  var tSub = el("text", {
    x: cx, y: cy - 65, "text-anchor": "middle", "dominant-baseline": "middle",
    "font-size": "15", "font-weight": "400", "letter-spacing": "0.05em",
    "font-family": font, fill: "#666"
  });
  tSub.textContent = "a medianoche";
  svg.appendChild(tSub);

  // Add SVG to container
  container.appendChild(svg);

  // === Needle animation ===
  // Animate from 12:00 position to target after a brief delay
  requestAnimationFrame(function() {
    setTimeout(function() {
      var needle = document.getElementById("clock-needle");
      if (!needle) return;
      var anim = document.createElementNS(NS, "animateTransform");
      anim.setAttribute("attributeName", "transform");
      anim.setAttribute("type", "rotate");
      anim.setAttribute("from", startRot + " " + cx + " " + cy);
      anim.setAttribute("to", targetRot + " " + cx + " " + cy);
      anim.setAttribute("dur", "1.5s");
      anim.setAttribute("fill", "freeze");
      anim.setAttribute("calcMode", "spline");
      anim.setAttribute("keySplines", "0.25 0.1 0.25 1");
      anim.setAttribute("keyTimes", "0;1");
      needle.appendChild(anim);
      anim.beginElement();
    }, 400);
  });
}

/* --- Dimension Bars (built with DOM API) --- */
function renderDimensions(containerId) {
  var container = document.getElementById(containerId);
  if (!container) return;

  CLOCK_DATA.dimensions.forEach(function(dim, i) {
    var color = ZONE_COLORS[dim.zone];
    var pct = (dim.hours / 12) * 100;

    var bar = document.createElement("div");
    bar.className = "dimension-bar";
    bar.id = "dim-" + i;

    // Header
    var header = document.createElement("div");
    header.className = "dimension-header";
    header.addEventListener("click", function() { toggleDimension(i); });

    var indicator = document.createElement("span");
    indicator.className = "dimension-indicator";
    indicator.style.background = color;

    var name = document.createElement("span");
    name.className = "dimension-name";
    name.textContent = dim.name;

    var reading = document.createElement("span");
    reading.className = "dimension-reading";
    reading.textContent = dim.reading;

    var zoneTag = document.createElement("span");
    zoneTag.className = "dimension-zone-tag";
    zoneTag.style.background = color;
    if (dim.zone === "yellow") zoneTag.style.color = "#333";
    zoneTag.textContent = dim.zoneName;

    var toggle = document.createElement("span");
    toggle.className = "dimension-toggle";
    toggle.textContent = "\u25BC";

    header.appendChild(indicator);
    header.appendChild(name);
    header.appendChild(reading);
    header.appendChild(zoneTag);
    header.appendChild(toggle);

    // Progress bar
    var progress = document.createElement("div");
    progress.className = "dimension-progress";
    var fill = document.createElement("div");
    fill.className = "dimension-progress-fill";
    fill.style.width = pct + "%";
    fill.style.background = color;
    progress.appendChild(fill);

    // Detail
    var detail = document.createElement("div");
    detail.className = "dimension-detail";
    var detailInner = document.createElement("div");
    detailInner.className = "dimension-detail-inner";
    detailInner.textContent = dim.description;
    detail.appendChild(detailInner);

    bar.appendChild(header);
    bar.appendChild(progress);
    bar.appendChild(detail);
    container.appendChild(bar);
  });
}

function toggleDimension(index) {
  var el = document.getElementById("dim-" + index);
  if (el) el.classList.toggle("open");
}

/* --- Key Facts (built with DOM API) --- */
function renderKeyFacts(containerId) {
  var container = document.getElementById(containerId);
  if (!container) return;

  CLOCK_DATA.keyFacts.forEach(function(fact) {
    var div = document.createElement("div");
    div.className = "fact";

    var num = document.createElement("div");
    num.className = "fact-number";
    num.textContent = fact.number;

    var label = document.createElement("div");
    label.className = "fact-label";
    label.textContent = fact.label;

    div.appendChild(num);
    div.appendChild(label);
    container.appendChild(div);
  });
}

/* --- Initialize --- */
document.addEventListener("DOMContentLoaded", function() {
  renderGauge("clock-gauge");
  renderDimensions("dimensions-list");
  renderKeyFacts("facts-content");
});
