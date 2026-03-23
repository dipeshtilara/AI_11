"""
Class 11 AI — One Shot Revision | CBSE 2025-26
Streamlit app.py  ·  Subject Code 843

Run:
    pip install streamlit
    streamlit run app.py
"""

import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Class 11 AI — One Shot | CBSE 2025-26",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── FONTS + GLOBAL CSS ───────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@300;400;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ── Root palette ─────────────────────────────── */
:root {
    --ink:     #0f1014;
    --paper:   #f5f3ee;
    --paper2:  #ede9e1;
    --r:  #c84b2f;
    --b:  #2563ae;
    --g:  #1a7a4a;
    --p:  #8b3fb5;
    --a:  #c9720e;
    --line: rgba(15,16,20,0.12);
}

/* ── Override Streamlit chrome ────────────────── */
html, body, [data-testid="stApp"] {
    background: var(--paper) !important;
    font-family: 'Outfit', sans-serif !important;
}

/* Main content area */
[data-testid="stAppViewContainer"] > .main,
section.main > div.block-container {
    background: var(--paper) !important;
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 960px !important;
}

/* ── Sidebar ──────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #0f1014 !important;
    min-width: 260px !important;
}
[data-testid="stSidebar"] * { color: rgba(245,243,238,0.75) !important; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.08) !important; }
[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #f5f3ee !important;
    font-family: 'DM Serif Display', serif !important;
}
[data-testid="stSidebar"] .stMarkdown code {
    background: rgba(255,255,255,0.07) !important;
    color: rgba(245,243,238,0.6) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMarkdown p {
    color: rgba(245,243,238,0.55) !important;
    font-size: 0.82rem !important;
}

/* ── Typography helpers ───────────────────────── */
.unit-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    display: block;
}
.unit-h {
    font-family: 'DM Serif Display', serif;
    font-size: 1.9rem;
    line-height: 1.15;
    color: var(--ink);
    margin: 0.1rem 0 0.6rem;
}
.unit-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: rgba(15,16,20,0.38);
    letter-spacing: 0.04em;
    margin-bottom: 1rem;
}

/* ── Key-term pills ───────────────────────────── */
.pills { display:flex; flex-wrap:wrap; gap:6px; margin-bottom:1.2rem; }
.pill {
    padding: 3px 10px;
    border-radius: 5px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.67rem;
    border: 1px solid;
    display: inline-block;
}
.pill-r { background:rgba(200,75,47,.08); color:#a83320; border-color:rgba(200,75,47,.25); }
.pill-b { background:rgba(37,99,174,.08); color:#1a4e8a; border-color:rgba(37,99,174,.25); }
.pill-g { background:rgba(26,122,74,.08); color:#145e38; border-color:rgba(26,122,74,.25); }
.pill-p { background:rgba(139,63,181,.08); color:#6b2e96; border-color:rgba(139,63,181,.25); }
.pill-a { background:rgba(201,114,14,.08); color:#8c510a; border-color:rgba(201,114,14,.25); }

/* ── Topic grid ───────────────────────────────── */
.tgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:1px; background:var(--line); border:1px solid var(--line); border-radius:10px; overflow:hidden; margin-bottom:1.2rem; }
.tcell { background:var(--paper); padding:1.1rem 1.2rem; transition:background .18s; }
.tcell:hover { background:var(--paper2); }
.tcell-title { font-weight:700; font-size:0.88rem; margin-bottom:0.4rem; }
.tcell-list { list-style:none; padding:0; margin:0; }
.tcell-list li { font-size:0.78rem; color:rgba(15,16,20,0.58); padding-left:12px; position:relative; line-height:1.5; margin-bottom:2px; }
.tcell-list li::before { content:''; position:absolute; left:0; top:8px; width:4px; height:4px; border-radius:50%; background:currentColor; opacity:.4; }

/* ── Callout boxes ────────────────────────────── */
.callout { border-left:3px solid; padding:.9rem 1.1rem; border-radius:0 8px 8px 0; margin-bottom:1.2rem; }
.callout-title { font-family:'JetBrains Mono',monospace; font-size:0.62rem; letter-spacing:.12em; text-transform:uppercase; margin-bottom:.45rem; font-weight:600; }
.callout-list { list-style:none; padding:0; margin:0; }
.callout-list li { font-size:0.81rem; padding-left:14px; position:relative; line-height:1.6; margin-bottom:3px; }
.callout-list li::before { content:'→'; position:absolute; left:0; opacity:.45; font-size:.7rem; top:2px; }
.callout.rem { background:rgba(200,75,47,.05); border-color:#c84b2f; }
.callout.rem .callout-title { color:#c84b2f; }
.callout.tip { background:rgba(37,99,174,.05); border-color:#2563ae; }
.callout.tip .callout-title { color:#2563ae; }

/* ── Code blocks ──────────────────────────────── */
.cblock { background:#0f1014; border-radius:10px; overflow:hidden; margin-bottom:1.2rem; }
.cblock-header { display:flex; align-items:center; gap:6px; padding:.55rem 1.1rem; border-bottom:1px solid rgba(255,255,255,.06); }
.cdot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.cdot-r { background:#ff5f57; }
.cdot-y { background:#febc2e; }
.cdot-g { background:#28c840; }
.cfn  { font-family:'JetBrains Mono',monospace; font-size:0.63rem; color:rgba(245,243,238,.3); margin-left:5px; }
.cblock pre { font-family:'JetBrains Mono',monospace; font-size:0.78rem; line-height:1.75; padding:1.1rem 1.3rem; margin:0; overflow-x:auto; color:rgba(245,243,238,.85); white-space:pre; }
.kw{color:#c792ea} .fn{color:#82aaff} .st{color:#c3e88d} .cm{color:#546e7a} .nm{color:#f78c6c} .cl{color:#ffcb6b}

/* ── Comparison table ─────────────────────────── */
.ctable-wrap { overflow-x:auto; border-radius:10px; border:1px solid var(--line); margin-bottom:1.2rem; }
.ctable { width:100%; border-collapse:collapse; font-size:0.81rem; }
.ctable th { background:#0f1014; color:rgba(245,243,238,.55); font-family:'JetBrains Mono',monospace; font-size:0.6rem; letter-spacing:.1em; text-transform:uppercase; padding:9px 13px; text-align:left; font-weight:400; }
.ctable td { padding:9px 13px; border-bottom:1px solid rgba(15,16,20,.07); vertical-align:top; line-height:1.5; color:rgba(15,16,20,.65); }
.ctable tr:last-child td { border-bottom:none; }
.ctable tr:hover td { background:var(--paper2); }
.ctable td.em { color:var(--ink); font-weight:600; }

/* ── Section rule ─────────────────────────────── */
.srule { display:flex; align-items:center; gap:.8rem; margin:2rem 0 1.6rem; }
.srule-line { flex:1; height:1px; background:var(--line); }
.srule-txt { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:.14em; text-transform:uppercase; color:rgba(15,16,20,.28); white-space:nowrap; }

/* ── Data type grid ───────────────────────────── */
.dtgrid { display:grid; grid-template-columns:repeat(3,1fr); gap:1px; background:var(--line); border-radius:10px; overflow:hidden; border:1px solid var(--line); margin-bottom:1.2rem; }
.dtcell { background:var(--paper); padding:1rem .9rem; }
.dtcell:hover { background:var(--paper2); }
.dtlabel { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:.1em; text-transform:uppercase; margin-bottom:.4rem; font-weight:700; }
.dtex { font-family:'JetBrains Mono',monospace; font-size:0.7rem; color:rgba(15,16,20,.5); line-height:1.6; }

/* ── Hero ─────────────────────────────────────── */
.hero { background:#1c1e27; border-radius:12px; padding:2.5rem 2.8rem 2rem; margin-bottom:2rem; position:relative; overflow:hidden; }
.hero-eye { font-family:'JetBrains Mono',monospace; font-size:.62rem; letter-spacing:.18em; text-transform:uppercase; color:#c84b2f; margin-bottom:.8rem; }
.hero-title { font-family:'DM Serif Display',serif; font-size:2.8rem; line-height:1.1; color:#f5f3ee; margin-bottom:.7rem; }
.hero-title em { font-style:italic; color:rgba(245,243,238,.4); }
.hero-desc { font-family:'JetBrains Mono',monospace; font-size:.72rem; color:rgba(245,243,238,.45); max-width:520px; line-height:1.7; margin-bottom:1.3rem; }
.hero-pills { display:flex; gap:8px; flex-wrap:wrap; }
.hero-pill { padding:4px 12px; border:1px solid rgba(255,255,255,.15); border-radius:100px; font-family:'JetBrains Mono',monospace; font-size:.62rem; color:rgba(255,255,255,.45); }

/* Streamlit widget tweaks */
div[data-testid="stSelectbox"] > div { background: #1c1e27 !important; border-color: rgba(255,255,255,0.15) !important; }
.stSlider > div > div > div { background: rgba(200,75,47,0.3) !important; }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# DATA
# ════════════════════════════════════════════════════════════════════════════

UNITS = [
    {"id": "unit1", "num": "01", "tag_cls": "r", "color": "#c84b2f",
     "title": "Introduction: AI for Everyone",
     "meta": "4 hrs theory · 10 hrs practical",
     "marks": 14,
     "pills": [("r","Artificial Intelligence"),("r","Machine Learning"),("r","Deep Learning"),
               ("r","Turing Test"),("b","Narrow AI"),("b","General AI"),("b","Super AI"),("g","Domains of AI")]},
    {"id": "unit2", "num": "02", "tag_cls": "b", "color": "#2563ae",
     "title": "Unlocking Your Future in AI",
     "meta": "4 hrs theory",
     "marks": 9,
     "pills": [("b","AI Project Cycle"),("b","Problem Scoping"),("b","Data Acquisition"),
               ("b","Modelling"),("b","Evaluation"),("r","5W1H Framework")]},
    {"id": "unit3", "num": "03", "tag_cls": "g", "color": "#1a7a4a",
     "title": "Python Programming for AI",
     "meta": "10 hrs theory · 20 hrs practical",
     "marks": 25,
     "pills": [("g","Variables & Types"),("g","Control Flow"),("g","Functions"),("g","Lists/Tuples/Dicts"),
               ("a","NumPy"),("a","Pandas"),("a","Matplotlib"),("r","Scikit-learn")]},
    {"id": "unit4", "num": "04", "tag_cls": "p", "color": "#8b3fb5",
     "title": "Introduction to Capstone Project",
     "meta": "6 hrs theory · 15 hrs practical",
     "marks": 20,
     "pills": [("p","Problem Statement"),("p","SDGs"),("p","Dataset"),("p","Prototype"),
               ("b","5W1H"),("b","Kaggle"),("b","UCI")]},
    {"id": "unit5", "num": "05", "tag_cls": "a", "color": "#c9720e",
     "title": "Data Literacy — Collection to Analysis",
     "meta": "6 hrs theory · 15 hrs practical",
     "marks": 21,
     "pills": [("a","Structured Data"),("a","Unstructured Data"),("a","EDA"),("a","Missing Values"),
               ("r","Outliers"),("r","Mean/Median/Mode"),("b","Std Deviation"),("b","Correlation")]},
    {"id": "unit6", "num": "06", "tag_cls": "r", "color": "#c84b2f",
     "title": "Machine Learning Algorithms",
     "meta": "9 hrs theory · 15 hrs practical",
     "marks": 21,
     "pills": [("r","Supervised"),("b","Unsupervised"),("g","Reinforcement"),("r","Regression"),
               ("r","Classification"),("b","Clustering"),("a","K-Means"),("a","KNN"),
               ("a","Decision Tree"),("p","Overfitting"),("p","Confusion Matrix")]},
    {"id": "unit7", "num": "07", "tag_cls": "b", "color": "#2563ae",
     "title": "Leveraging Linguistics — NLP",
     "meta": "5 hrs theory · 10 hrs practical",
     "marks": 15,
     "pills": [("b","NLP"),("b","Tokenization"),("b","Stop Words"),("b","Stemming"),
               ("b","Lemmatization"),("r","Bag of Words"),("r","TF-IDF"),("g","Sentiment Analysis")]},
    {"id": "unit8", "num": "08", "tag_cls": "g", "color": "#1a7a4a",
     "title": "AI Ethics and Values",
     "meta": "4 hrs theory",
     "marks": 9,
     "pills": [("g","AI Bias"),("g","Fairness"),("g","Transparency"),("g","Accountability"),
               ("g","Privacy"),("r","Deepfake"),("r","Surveillance"),("b","Explainable AI"),("b","GDPR")]},
]

MARKS_COLORS = {
    "Intro AI":"#c84b2f","AI Future":"#2563ae","Python":"#1a7a4a",
    "Capstone":"#8b3fb5","Data":"#c9720e","ML Algo":"#c84b2f","NLP":"#2563ae","Ethics":"#1a7a4a"
}

# ════════════════════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════════════════════

def pills(items):
    html = '<div class="pills">'
    for cls, label in items:
        html += f'<span class="pill pill-{cls}">{label}</span>'
    html += '</div>'
    return html

def unit_header(u):
    tag_colors = {"r":"#c84b2f","b":"#2563ae","g":"#1a7a4a","p":"#8b3fb5","a":"#c9720e"}
    c = tag_colors[u["tag_cls"]]
    return f"""
<span class="unit-eyebrow" style="color:{c}">Unit {u['num']}</span>
<h2 class="unit-h">{u['title']}</h2>
<div class="unit-meta">{u['meta']} &nbsp;·&nbsp; <strong style="color:{c}">{u['marks']} marks</strong></div>
"""

def section_rule(label):
    return f'<div class="srule"><div class="srule-line"></div><div class="srule-txt">{label}</div><div class="srule-line"></div></div>'

def callout(kind, title, items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="callout {kind}"><div class="callout-title">{title}</div><ul class="callout-list">{li}</ul></div>'

def topic_grid(cells):
    """cells = list of (title, icon, list_of_strings)"""
    html = '<div class="tgrid">'
    for title, icon, items in cells:
        lis = "".join(f"<li>{i}</li>" for i in items)
        html += f'<div class="tcell"><div class="tcell-title">{icon} {title}</div><ul class="tcell-list">{lis}</ul></div>'
    html += '</div>'
    return html

def cmp_table(headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f'<td class="em">{row[0]}</td>' + "".join(f"<td>{c}</td>" for c in row[1:]))
        trs += f"<tr>{tds}</tr>"
    return f'<div class="ctable-wrap"><table class="ctable"><tr>{ths}</tr>{trs}</table></div>'

def code_block(filename, code_html):
    return f"""<div class="cblock">
<div class="cblock-header">
  <span class="cdot cdot-r"></span><span class="cdot cdot-y"></span><span class="cdot cdot-g"></span>
  <span class="cfn">{filename}</span>
</div>
<pre>{code_html}</pre>
</div>"""


# ════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
<div style="padding:0.2rem 0 0.8rem">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.55rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,243,238,.28);margin-bottom:.5rem">CBSE · Code 843 · 2025-26</div>
  <div style="font-family:'DM Serif Display',serif;font-size:1.5rem;color:#f5f3ee;line-height:1.2">Class 11<br>Artificial<br>Intelligence</div>
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:rgba(245,243,238,.35);margin-top:.3rem">One Shot Revision</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # Marks mini chart
    st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.55rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,243,238,.28);margin-bottom:.6rem">MARKS AT A GLANCE</div>', unsafe_allow_html=True)

    marks_data = [
        ("Intro AI", 14, 25, "#c84b2f"),
        ("AI Future", 9, 25, "#2563ae"),
        ("Python", 25, 25, "#1a7a4a"),
        ("Capstone", 20, 25, "#8b3fb5"),
        ("Data", 21, 25, "#c9720e"),
        ("ML Algo", 21, 25, "#c84b2f"),
        ("NLP", 15, 25, "#2563ae"),
        ("Ethics", 9, 25, "#1a7a4a"),
    ]
    for label, val, mx, color in marks_data:
        pct = int(val / mx * 100)
        st.markdown(f"""
<div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
  <span style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:rgba(245,243,238,.45);width:56px;flex-shrink:0">{label}</span>
  <div style="flex:1;height:3px;background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden">
    <div style="height:3px;width:{pct}%;background:{color};border-radius:2px;transition:width 1s ease"></div>
  </div>
  <span style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;color:rgba(245,243,238,.3);width:20px;text-align:right">{val}</span>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Unit navigator
    st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.55rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,243,238,.28);margin-bottom:.5rem">NAVIGATE</div>', unsafe_allow_html=True)

    unit_options = [f"{'—' if i==0 else ''}  U{u['num']} · {u['title']}" for i, u in enumerate(UNITS)]
    unit_options[0] = f"  U{UNITS[0]['num']} · {UNITS[0]['title']}"
    selected_unit = st.selectbox("Jump to unit", unit_options, label_visibility="collapsed")

    st.markdown("---")

    # Stats
    st.markdown("""
<div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:rgba(245,243,238,.28);line-height:2">
  Theory: 50 marks<br>
  Practical: 50 marks<br>
  Total: 100 marks<br>
  8 units · 50+ concepts
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
  <div class="hero-eye">⬤ CBSE 2025-26 · Class XI · Subject Code 843</div>
  <div class="hero-title">One Shot<br><em>Revision</em></div>
  <div class="hero-desc">Complete syllabus. All 8 units. Key concepts, interactive demos, Python code &amp; exam tips — on one page.</div>
  <div class="hero-pills">
    <span class="hero-pill">8 Units</span>
    <span class="hero-pill">100 Marks</span>
    <span class="hero-pill">Theory + Practical</span>
    <span class="hero-pill">Interactive Demos</span>
    <span class="hero-pill">Python Snippets</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 1 — Intro to AI
# ════════════════════════════════════════════════════════════════════════════

st.markdown(unit_header(UNITS[0]), unsafe_allow_html=True)
st.markdown(pills(UNITS[0]["pills"]), unsafe_allow_html=True)

# AI Hierarchy interactive
st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ AI Hierarchy — select a layer</div>', unsafe_allow_html=True)

hier_choice = st.radio(
    "hierarchy", ["AI (Artificial Intelligence)", "Machine Learning", "Deep Learning", "Neural Networks"],
    label_visibility="collapsed", horizontal=True, key="hier"
)

hier_info = {
    "AI (Artificial Intelligence)": "**AI (1956)** — Umbrella term for machines imitating human intelligence. Coined by John McCarthy at the Dartmouth Conference. Includes ML, robotics, NLP, expert systems, computer vision.",
    "Machine Learning": "**ML** — Algorithms that learn patterns from data **without being explicitly programmed**. Subset of AI. Key paradigm shift: instead of hand-coding rules, the machine learns them from examples.",
    "Deep Learning": "**Deep Learning** — Neural networks with **many hidden layers** (hence 'deep'). Powers image recognition, speech, and large language models. Needs large data + GPU compute.",
    "Neural Networks": "**Neural Networks** — Layers of weighted connections inspired by biological neurons. Input layer → Hidden layer(s) → Output layer. Learns via backpropagation (adjusting weights to reduce error).",
}
st.info(hier_info[hier_choice])

# Hierarchy visual
hier_html = """
<div style="display:flex;flex-direction:column;align-items:center;margin-bottom:1rem">
  <div style="width:100%;background:#f0ece3;border-radius:8px 8px 0 0;padding:.8rem 1rem;text-align:center">
    <strong>Artificial Intelligence (AI)</strong>
    <span style="display:block;font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(15,16,20,.45);margin-top:2px">simulation of human intelligence · 1956</span>
  </div>
  <div style="width:82%;background:#e8e1d6;border-top:1px solid #d5cec4;padding:.75rem 1rem;text-align:center">
    <strong>Machine Learning</strong>
    <span style="display:block;font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(15,16,20,.4);margin-top:2px">learns from data without explicit programming</span>
  </div>
  <div style="width:60%;background:#ddd6c8;border-top:1px solid #d5cec4;padding:.75rem 1rem;text-align:center">
    <strong>Deep Learning</strong>
    <span style="display:block;font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(15,16,20,.4);margin-top:2px">many-layered neural networks</span>
  </div>
  <div style="width:40%;background:#c84b2f;border-top:1px solid rgba(0,0,0,.1);border-radius:0 0 8px 8px;padding:.75rem 1rem;text-align:center">
    <strong style="color:#f5f3ee">Neural Networks</strong>
    <span style="display:block;font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(245,243,238,.55);margin-top:2px">inspired by the brain</span>
  </div>
</div>
"""
st.markdown(hier_html, unsafe_allow_html=True)

st.markdown(topic_grid([
    ("What is AI?", "🤖", [
        "Simulation of human intelligence in machines",
        "Can: learn, reason, solve problems, understand language",
        "Coined by <strong>John McCarthy</strong> at Dartmouth, 1956",
        "AI ≠ human intelligence — it is narrow/task-specific",
    ]),
    ("Types of AI (by Capability)", "🔭", [
        "<strong style='color:#c84b2f'>Narrow AI</strong> — specific tasks (Siri, spam filter, Chess engine)",
        "<strong style='color:#2563ae'>General AI</strong> — human-level intelligence (hypothetical)",
        "<strong style='color:#1a7a4a'>Super AI</strong> — surpasses humans (theoretical future)",
    ]),
    ("Domains of AI", "🧩", [
        "Computer Vision — face recognition, object detection",
        "Natural Language Processing — chatbots, translation",
        "Robotics — industrial robots, autonomous machines",
        "Expert Systems — rule-based decision making",
        "Machine Learning — patterns from data",
    ]),
    ("AI vs Human Intelligence", "⚖️", [
        "AI: fast, tireless, no emotions, data-driven",
        "Human: creative, emotional, generalises easily",
        "AI lacks common sense &amp; self-awareness",
        "<strong>Turing Test</strong> (Alan Turing, 1950) — can a machine fool a human?",
    ]),
    ("Evolution of AI", "📅", [
        "1956 — Dartmouth Conference, AI born",
        "1960–80s — Expert Systems (MYCIN, DENDRAL)",
        "1997 — Deep Blue beats chess world champion",
        "2012 — Deep Learning revolution (AlexNet)",
        "2022–24 — LLMs: ChatGPT, Gemini, Claude",
    ]),
    ("Applications", "🌐", [
        "Healthcare — disease diagnosis, drug discovery",
        "Agriculture — crop monitoring, pest detection",
        "Finance — fraud detection, algorithmic trading",
        "Transport — self-driving cars",
        "Education — personalised tutoring",
    ]),
]), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "Hierarchy: <strong>AI ⊃ ML ⊃ Deep Learning ⊃ Neural Networks</strong>",
    "Turing Test = machine imitating a human in text conversation",
    "Current AI is Narrow AI — no machine has achieved General AI yet",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 2 — AI Future
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 2"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[1]), unsafe_allow_html=True)
st.markdown(pills(UNITS[1]["pills"]), unsafe_allow_html=True)

# Interactive AI Project Cycle
st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ AI Project Cycle — click each step</div>', unsafe_allow_html=True)

CYCLE_STEPS = [
    ("Problem Scoping", "Define the problem with 5W1H. Ask: **What** is the problem? **Why** does it matter? **Who** are the stakeholders? **Where** will the solution be used? **When**? **How** will AI solve it?"),
    ("Data Acquisition", "Collect relevant, high-quality data. Sources: Kaggle, UCI, government portals, APIs, surveys. **Primary** = collected by you; **Secondary** = existing datasets. Quality > Quantity always."),
    ("Data Exploration", "Explore the data: `df.describe()`, `df.info()`, handle missing values, visualise distributions, find patterns and correlations. This is **EDA** (Exploratory Data Analysis)."),
    ("Modelling", "Choose an algorithm, split data (80/20), train the model with `fit()`, tune hyperparameters (K in KNN, depth in Decision Tree). Compare multiple models on validation data."),
    ("Evaluation", "Measure performance: accuracy, confusion matrix, precision, recall. If unsatisfactory, go back to any earlier step. AI Project Cycle is **iterative**, not linear."),
]

cols = st.columns(5)
step_labels = ["01 Problem\nScoping", "02 Data\nAcquisition", "03 Data\nExploration", "04 Modelling", "05 Evaluation"]

step_idx = st.session_state.get("cycle_step", 0)

for i, (col, label) in enumerate(zip(cols, step_labels)):
    with col:
        if st.button(label, key=f"cycle_{i}", use_container_width=True):
            st.session_state["cycle_step"] = i
            step_idx = i

name, detail = CYCLE_STEPS[step_idx]
st.markdown(f"""
<div style="padding:.85rem 1.1rem;background:rgba(37,99,174,.07);border-left:3px solid #2563ae;border-radius:0 8px 8px 0;font-size:0.82rem;line-height:1.6;color:rgba(15,16,20,.7);margin-bottom:1.2rem">
<strong style="color:#2563ae">{name}</strong> — {detail}
</div>
""", unsafe_allow_html=True)

st.markdown(topic_grid([
    ("AI Career Paths", "🎯", [
        "AI/ML Engineer — build &amp; deploy models",
        "Data Scientist — analyze &amp; extract insights",
        "NLP Engineer — language AI systems",
        "Computer Vision Engineer — image/video AI",
        "AI Researcher — advance AI theory",
        "Prompt Engineer — design AI prompts",
    ]),
    ("Skills for AI", "🛠️", [
        "Programming — Python, R",
        "Maths — Linear Algebra, Statistics, Calculus",
        "Domain knowledge (healthcare, finance…)",
        "Data handling &amp; visualisation",
        "Critical thinking &amp; problem-solving",
    ]),
]), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "AI Project Cycle is <strong>iterative</strong> — you can go back to earlier steps",
    "GIGO — Garbage In, Garbage Out: data quality > model complexity",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 3 — Python
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 3"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[2]), unsafe_allow_html=True)
st.markdown(pills(UNITS[2]["pills"]), unsafe_allow_html=True)

# Data structures visual
st.markdown("""
<div class="dtgrid">
  <div class="dtcell"><div class="dtlabel" style="color:#c84b2f">List [ ]</div><div class="dtex">[1, "hello", 3.14]<br>ordered · mutable<br>allows duplicates</div></div>
  <div class="dtcell"><div class="dtlabel" style="color:#2563ae">Tuple ( )</div><div class="dtex">(1, "hello", 3.14)<br>ordered · immutable<br>allows duplicates</div></div>
  <div class="dtcell"><div class="dtlabel" style="color:#1a7a4a">Dict { }</div><div class="dtex">{'name': 'Riya'}<br>key-value pairs<br>mutable · unique keys</div></div>
  <div class="dtcell"><div class="dtlabel" style="color:#8b3fb5">Set { }</div><div class="dtex">{1, 2, 3}<br>unordered · mutable<br>no duplicates</div></div>
  <div class="dtcell"><div class="dtlabel" style="color:#c9720e">NumPy Array</div><div class="dtex">np.array([1,2,3])<br>N-dimensional · typed<br>fast vectorised ops</div></div>
  <div class="dtcell"><div class="dtlabel" style="color:#c84b2f">DataFrame</div><div class="dtex">pd.DataFrame()<br>2D table with labels<br>rows × columns</div></div>
</div>
""", unsafe_allow_html=True)

# Python tab explorer
py_tab1, py_tab2, py_tab3, py_tab4, py_tab5 = st.tabs(["🐍 Basics", "📦 NumPy", "🐼 Pandas", "📊 Matplotlib", "🤖 Sklearn"])

with py_tab1:
    st.markdown(code_block("python_basics.py", """<span class="cm"># ── Data Types ──────────────────────────────────</span>
x = <span class="nm">10</span>          <span class="cm"># int</span>
pi = <span class="nm">3.14</span>      <span class="cm"># float</span>
name = <span class="st">"Riya"</span>  <span class="cm"># str</span>
flag = <span class="kw">True</span>    <span class="cm"># bool</span>

<span class="cm"># ── Control Flow ────────────────────────────────</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="nm">5</span>):
    <span class="kw">if</span> i % <span class="nm">2</span> == <span class="nm">0</span>:
        <span class="fn">print</span>(i, <span class="st">"is even"</span>)

<span class="cm"># ── Functions ───────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">square</span>(x):
    <span class="kw">return</span> x ** <span class="nm">2</span>

double = <span class="kw">lambda</span> x: x * <span class="nm">2</span>  <span class="cm"># lambda function</span>

<span class="cm"># ── List Comprehension ──────────────────────────</span>
evens = [x <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="nm">20</span>) <span class="kw">if</span> x % <span class="nm">2</span> == <span class="nm">0</span>]"""), unsafe_allow_html=True)

with py_tab2:
    st.markdown(code_block("numpy_basics.py", """<span class="kw">import</span> numpy <span class="kw">as</span> np

arr = np.<span class="fn">array</span>([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])
<span class="fn">print</span>(arr.mean(), arr.std(), arr.shape)
<span class="cm"># → 3.0  1.414  (5,)</span>

arr_2d = arr.<span class="fn">reshape</span>(<span class="nm">5</span>, <span class="nm">1</span>)    <span class="cm"># column vector</span>
zeros = np.<span class="fn">zeros</span>((<span class="nm">3</span>, <span class="nm">3</span>))       <span class="cm"># 3×3 zeros</span>
ones  = np.<span class="fn">ones</span>((<span class="nm">2</span>, <span class="nm">4</span>))        <span class="cm"># 2×4 ones</span>
r     = np.<span class="fn">arange</span>(<span class="nm">0</span>, <span class="nm">10</span>, <span class="nm">2</span>)   <span class="cm"># [0,2,4,6,8]</span>
lin   = np.<span class="fn">linspace</span>(<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">5</span>)  <span class="cm"># 5 evenly spaced</span>

<span class="cm"># Element-wise operations</span>
a = np.<span class="fn">array</span>([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])
b = np.<span class="fn">array</span>([<span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>])
<span class="fn">print</span>(a + b)   <span class="cm"># [5 7 9]</span>
<span class="fn">print</span>(a * b)   <span class="cm"># [4 10 18]  element-wise!</span>
<span class="fn">print</span>(np.<span class="fn">dot</span>(a, b))  <span class="cm"># 32  (dot product)</span>"""), unsafe_allow_html=True)

with py_tab3:
    st.markdown(code_block("pandas_basics.py", """<span class="kw">import</span> pandas <span class="kw">as</span> pd

df = pd.<span class="fn">read_csv</span>(<span class="st">'students.csv'</span>)

<span class="cm"># Explore</span>
<span class="fn">print</span>(df.shape)          <span class="cm"># (200, 5)</span>
<span class="fn">print</span>(df.<span class="fn">head</span>())         <span class="cm"># first 5 rows</span>
<span class="fn">print</span>(df.<span class="fn">info</span>())         <span class="cm"># dtypes + nulls</span>
<span class="fn">print</span>(df.<span class="fn">describe</span>())    <span class="cm"># stats</span>
<span class="fn">print</span>(df.<span class="fn">isnull</span>().<span class="fn">sum</span>())<span class="cm"># count nulls</span>

<span class="cm"># Select</span>
df[<span class="st">'marks'</span>]                    <span class="cm"># single column</span>
df[[<span class="st">'name'</span>, <span class="st">'marks'</span>]]          <span class="cm"># multiple cols</span>
df[df[<span class="st">'marks'</span>] > <span class="nm">80</span>]           <span class="cm"># filter rows</span>

<span class="cm"># Clean</span>
df[<span class="st">'marks'</span>].<span class="fn">fillna</span>(df[<span class="st">'marks'</span>].mean(), inplace=<span class="kw">True</span>)
df.<span class="fn">drop_duplicates</span>(inplace=<span class="kw">True</span>)
df[<span class="st">'marks'</span>] = df[<span class="st">'marks'</span>].<span class="fn">astype</span>(<span class="fn">int</span>)

<span class="cm"># Group & aggregate</span>
df.<span class="fn">groupby</span>(<span class="st">'section'</span>)[<span class="st">'marks'</span>].<span class="fn">mean</span>()"""), unsafe_allow_html=True)

with py_tab4:
    st.markdown(code_block("matplotlib_basics.py", """<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">import</span> numpy <span class="kw">as</span> np

x = np.<span class="fn">arange</span>(<span class="nm">10</span>)

<span class="cm"># Line chart</span>
plt.<span class="fn">plot</span>(x, x**<span class="nm">2</span>, color=<span class="st">'steelblue'</span>, label=<span class="st">'y=x²'</span>)

<span class="cm"># Bar chart</span>
plt.<span class="fn">bar</span>([<span class="st">'A'</span>,<span class="st">'B'</span>,<span class="st">'C'</span>], [<span class="nm">45</span>,<span class="nm">82</span>,<span class="nm">67</span>], color=<span class="st">'coral'</span>)

<span class="cm"># Histogram</span>
plt.<span class="fn">hist</span>(data, bins=<span class="nm">15</span>, color=<span class="st">'skyblue'</span>, edgecolor=<span class="st">'white'</span>)

<span class="cm"># Scatter plot</span>
plt.<span class="fn">scatter</span>(x, y, c=<span class="st">'tomato'</span>, alpha=<span class="nm">0.7</span>)

<span class="cm"># Always add labels!</span>
plt.<span class="fn">xlabel</span>(<span class="st">'X axis'</span>)
plt.<span class="fn">ylabel</span>(<span class="st">'Y axis'</span>)
plt.<span class="fn">title</span>(<span class="st">'My Chart'</span>)
plt.<span class="fn">legend</span>()
plt.<span class="fn">tight_layout</span>()
plt.<span class="fn">show</span>()"""), unsafe_allow_html=True)

with py_tab5:
    st.markdown(code_block("sklearn_quickstart.py", """<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.neighbors <span class="kw">import</span> KNeighborsClassifier
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score

<span class="cm"># 1. Split</span>
X_train, X_test, y_train, y_test = <span class="fn">train_test_split</span>(
    X, y, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>
)

<span class="cm"># 2. Scale (optional but good practice)</span>
sc = <span class="cl">StandardScaler</span>()
X_train = sc.<span class="fn">fit_transform</span>(X_train)
X_test  = sc.<span class="fn">transform</span>(X_test)

<span class="cm"># 3. Train</span>
clf = <span class="cl">KNeighborsClassifier</span>(n_neighbors=<span class="nm">3</span>)
clf.<span class="fn">fit</span>(X_train, y_train)

<span class="cm"># 4. Evaluate</span>
acc = <span class="fn">accuracy_score</span>(y_test, clf.<span class="fn">predict</span>(X_test))
<span class="fn">print</span>(<span class="st">f"Accuracy: {acc*100:.1f}%"</span>)"""), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "Python is <strong>case-sensitive</strong> and <strong>dynamically typed</strong>",
    "List → mutable; Tuple → immutable; Dict keys → unique &amp; immutable",
    "NumPy arrays are <strong>faster</strong> than Python lists for numerical operations",
    "<code>df.isnull().sum()</code> finds missing values; <code>df.describe()</code> gives stats",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 4 — Capstone
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 4"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[3]), unsafe_allow_html=True)
st.markdown(pills(UNITS[3]["pills"]), unsafe_allow_html=True)

st.markdown(topic_grid([
    ("What is a Capstone Project?", "🚀", [
        "Culminating project applying all AI skills",
        "Follows the AI Project Cycle end-to-end",
        "Solves a real-world problem using AI/ML",
        "Must link to UN SDGs (Sustainable Development Goals)",
    ]),
    ("Problem Statement — 5W1H", "📋", [
        "<strong style='color:#c84b2f'>What?</strong> — Define the problem clearly",
        "<strong style='color:#2563ae'>Why?</strong> — Importance / impact",
        "<strong style='color:#1a7a4a'>Who?</strong> — Stakeholders / beneficiaries",
        "Where? — Context / geography",
        "When? — Timeframe",
        "How? — AI approach",
    ]),
    ("SDG Examples", "🌍", [
        "Crop disease AI → <strong>SDG 2</strong> (Zero Hunger)",
        "Mental health chatbot → <strong>SDG 3</strong> (Good Health)",
        "Smart tutoring → <strong>SDG 4</strong> (Quality Education)",
        "Air quality model → <strong>SDG 13</strong> (Climate Action)",
    ]),
    ("Dataset Sources", "🗄️", [
        "<strong>Kaggle.com</strong> — 50,000+ community datasets",
        "<strong>UCI ML Repository</strong> — classic benchmark datasets",
        "<strong>data.gov.in</strong> — Indian government open data",
        "<strong>Google Dataset Search</strong> — dataset search engine",
        "<strong>WHO / World Bank</strong> — health &amp; economic data",
    ]),
]), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "Capstone = entire AI Project Cycle applied to a real problem",
    "Always link your project to at least one SDG with justification",
    "Document every stage: proposal → EDA report → model results → presentation",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 5 — Data Literacy
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 5"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[4]), unsafe_allow_html=True)
st.markdown(pills(UNITS[4]["pills"]), unsafe_allow_html=True)

# Interactive statistics demo using Streamlit + matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ Statistics Explorer — drag the sliders</div>', unsafe_allow_html=True)

col_sl1, col_sl2 = st.columns(2)
with col_sl1:
    mu = st.slider("Mean (μ)", min_value=10, max_value=90, value=50, key="stat_mu")
with col_sl2:
    sigma = st.slider("Std Deviation (σ)", min_value=2, max_value=30, value=12, key="stat_sigma")

x_vals = np.linspace(0, 100, 500)
y_vals = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - mu) / sigma) ** 2)

fig, ax = plt.subplots(figsize=(8, 2.8))
fig.patch.set_facecolor("#ede9e1")
ax.set_facecolor("#ede9e1")

# ±1σ fill
mask = (x_vals >= mu - sigma) & (x_vals <= mu + sigma)
ax.fill_between(x_vals[mask], y_vals[mask], alpha=0.25, color="#c84b2f", label=f"±1σ (68%)")

# Curve
ax.plot(x_vals, y_vals, color="#c84b2f", linewidth=2)

# Mean line
ax.axvline(mu, color="#2563ae", linewidth=1.5, linestyle="--", label=f"μ = {mu}")

ax.set_xlim(0, 100)
ax.set_ylim(0, None)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(colors="rgba(15,16,20,0.4)", labelsize=8)
ax.set_xlabel("Value", fontsize=9, color="rgba(15,16,20,0.4)")
ax.legend(fontsize=8, framealpha=0)
ax.set_title(f"Normal Distribution  μ={mu}  σ={sigma}  |  68% range: {mu-sigma}–{mu+sigma}", fontsize=9, color="#0f1014")

plt.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close()

st.markdown(f"""
<div style="display:flex;gap:2rem;flex-wrap:wrap;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:rgba(15,16,20,.45);margin-bottom:1.2rem">
  <span>Mean: <strong style="color:#c84b2f">{mu}</strong></span>
  <span>Std Dev: <strong style="color:#2563ae">{sigma}</strong></span>
  <span>68% of data within: <strong style="color:#1a7a4a">{mu-sigma} – {mu+sigma}</strong></span>
  <span>95% within: <strong style="color:#8b3fb5">{mu-2*sigma} – {mu+2*sigma}</strong></span>
</div>
""", unsafe_allow_html=True)

st.markdown(topic_grid([
    ("Types of Data", "📊", [
        "<strong>Structured</strong> — rows/columns (CSV, DB)",
        "<strong>Unstructured</strong> — images, audio, text, video",
        "<strong>Semi-structured</strong> — JSON, XML, HTML",
        "Quantitative — numerical (height, marks)",
        "Qualitative — categorical (colour, gender)",
    ]),
    ("Data Cleaning", "🧹", [
        "Handle missing: fillna() / dropna()",
        "Remove duplicates: drop_duplicates()",
        "Fix data types: astype(int)",
        "Detect outliers: IQR or Z-score method",
        "Normalise or standardise values",
    ]),
    ("EDA Commands", "🔍", [
        "df.shape — (rows, columns)",
        "df.describe() — stats summary",
        "df.info() — dtypes &amp; null count",
        "df.value_counts() — frequency",
        "df.corr() — correlation matrix",
    ]),
    ("Key Statistics", "📐", [
        "<strong style='color:#c84b2f'>Mean</strong> — Σx / n (average)",
        "<strong style='color:#2563ae'>Median</strong> — middle value when sorted",
        "<strong style='color:#1a7a4a'>Mode</strong> — most frequent value",
        "Variance = Σ(x−μ)² / n",
        "Std Dev = √Variance; spread of data",
        "Correlation: −1 to +1",
    ]),
]), unsafe_allow_html=True)

st.markdown(code_block("eda.py", """<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt

df = pd.<span class="fn">read_csv</span>(<span class="st">'students.csv'</span>)

<span class="cm"># ── Basic EDA ──────────────────────────────────</span>
<span class="fn">print</span>(df.<span class="fn">isnull</span>().<span class="fn">sum</span>())       <span class="cm"># count nulls per col</span>
<span class="fn">print</span>(df.<span class="fn">describe</span>())           <span class="cm"># min, max, mean, std…</span>

<span class="cm"># ── Handle Missing Values ──────────────────────</span>
df[<span class="st">'marks'</span>].<span class="fn">fillna</span>(df[<span class="st">'marks'</span>].mean(), inplace=<span class="kw">True</span>)

<span class="cm"># ── Outlier Detection (IQR) ────────────────────</span>
Q1  = df[<span class="st">'marks'</span>].quantile(<span class="nm">0.25</span>)
Q3  = df[<span class="st">'marks'</span>].quantile(<span class="nm">0.75</span>)
IQR = Q3 - Q1
df_clean = df[~((df[<span class="st">'marks'</span>] < Q1 - <span class="nm">1.5</span>*IQR) | (df[<span class="st">'marks'</span>] > Q3 + <span class="nm">1.5</span>*IQR))]

<span class="cm"># ── Visualise ──────────────────────────────────</span>
fig, axes = plt.<span class="fn">subplots</span>(<span class="nm">1</span>, <span class="nm">2</span>, figsize=(<span class="nm">10</span>, <span class="nm">4</span>))
axes[<span class="nm">0</span>].<span class="fn">hist</span>(df[<span class="st">'marks'</span>], bins=<span class="nm">15</span>)
axes[<span class="nm">1</span>].<span class="fn">boxplot</span>(df[<span class="st">'marks'</span>])   <span class="cm"># shows outliers</span>
plt.<span class="fn">show</span>()"""), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "GIGO — Garbage In, Garbage Out",
    "Normalisation: scale to [0,1]; Standardisation: mean=0, std=1",
    "<strong>Correlation ≠ Causation</strong>",
    "Box plot shows: Q1, Q3, Median, Whiskers &amp; Outliers visually",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 6 — ML Algorithms
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 6"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[5]), unsafe_allow_html=True)
st.markdown(pills(UNITS[5]["pills"]), unsafe_allow_html=True)

# Interactive ML scatter demo
st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ ML Demo — generate synthetic data &amp; visualise</div>', unsafe_allow_html=True)

from sklearn.datasets import make_classification, make_regression, make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ml_col1, ml_col2 = st.columns([1, 2])
with ml_col1:
    ml_algo = st.radio("Algorithm", ["KNN Classification", "Linear Regression", "K-Means Clustering"], key="ml_algo")
    n_pts = st.slider("Data points", 30, 200, 80, key="ml_n")
    if ml_algo == "KNN Classification":
        k_val = st.slider("K (neighbours)", 1, 15, 3, key="ml_k")
    elif ml_algo == "K-Means Clustering":
        k_clusters = st.slider("K (clusters)", 2, 5, 3, key="ml_kc")
    noise_val = st.slider("Noise", 0.0, 1.0, 0.3, 0.05, key="ml_noise")

rng = np.random.default_rng(42)

with ml_col2:
    fig2, ax2 = plt.subplots(figsize=(5.5, 3.5))
    fig2.patch.set_facecolor("#ede9e1")
    ax2.set_facecolor("#f5f3ee")
    ax2.spines[["top","right"]].set_visible(False)
    ax2.tick_params(colors="rgba(15,16,20,0.35)", labelsize=7)

    if ml_algo == "KNN Classification":
        X, y = make_classification(n_samples=n_pts, n_features=2, n_redundant=0,
                                    n_clusters_per_class=1, flip_y=noise_val, random_state=42)
        clf = KNeighborsClassifier(n_neighbors=k_val)
        clf.fit(X, y)
        xx, yy = np.meshgrid(np.linspace(X[:,0].min()-0.5, X[:,0].max()+0.5, 120),
                             np.linspace(X[:,1].min()-0.5, X[:,1].max()+0.5, 120))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax2.contourf(xx, yy, Z, alpha=0.12, colors=["#c84b2f","#2563ae"])
        ax2.scatter(X[y==0,0], X[y==0,1], c="#c84b2f", s=22, alpha=0.8, label="Class A")
        ax2.scatter(X[y==1,0], X[y==1,1], c="#2563ae", s=22, alpha=0.8, label="Class B")
        ax2.set_title(f"KNN  K={k_val}  acc={clf.score(X,y)*100:.0f}%", fontsize=9, color="#0f1014")
        ax2.legend(fontsize=8, framealpha=0)

    elif ml_algo == "Linear Regression":
        x_r = rng.uniform(0, 10, n_pts)
        y_r = 2.5 * x_r + 4 + rng.normal(0, noise_val * 8, n_pts)
        reg = LinearRegression().fit(x_r.reshape(-1,1), y_r)
        xline = np.linspace(0, 10, 100)
        ax2.scatter(x_r, y_r, c="#1a7a4a", s=22, alpha=0.7)
        ax2.plot(xline, reg.predict(xline.reshape(-1,1)), c="#c84b2f", linewidth=2,
                 label=f"y = {reg.coef_[0]:.2f}x + {reg.intercept_:.2f}")
        ax2.set_title(f"Linear Regression  R²={reg.score(x_r.reshape(-1,1),y_r):.3f}", fontsize=9, color="#0f1014")
        ax2.legend(fontsize=8, framealpha=0)

    else:
        X_c, _ = make_blobs(n_samples=n_pts, centers=k_clusters, cluster_std=noise_val+0.3, random_state=42)
        km = KMeans(n_clusters=k_clusters, random_state=42, n_init=10)
        labels = km.fit_predict(X_c)
        colors_km = ["#c84b2f","#2563ae","#1a7a4a","#8b3fb5","#c9720e"]
        for ki in range(k_clusters):
            ax2.scatter(X_c[labels==ki,0], X_c[labels==ki,1],
                       c=colors_km[ki], s=22, alpha=0.8, label=f"Cluster {ki+1}")
        ax2.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1],
                   c="black", s=90, marker="X", zorder=5, label="Centroid")
        ax2.set_title(f"K-Means  K={k_clusters}  inertia={km.inertia_:.0f}", fontsize=9, color="#0f1014")
        ax2.legend(fontsize=8, framealpha=0, ncol=2)

    plt.tight_layout()
    st.pyplot(fig2, use_container_width=True)
    plt.close()

st.markdown(cmp_table(
    ["Type", "Definition", "Input", "Output", "Examples"],
    [
        ["Supervised", "Learns from labeled data (input+output pairs)", "Labeled dataset", "Class or value", "Spam detection, price prediction"],
        ["Unsupervised", "Finds patterns in unlabeled data", "Unlabeled dataset", "Clusters / patterns", "Customer segmentation"],
        ["Reinforcement", "Agent learns by reward/punishment", "Environment + reward", "Policy / actions", "Game playing (AlphaGo)"],
    ]
), unsafe_allow_html=True)

st.markdown(code_block("ml_models.py", """<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.neighbors <span class="kw">import</span> KNeighborsClassifier
<span class="kw">from</span> sklearn.cluster <span class="kw">import</span> KMeans
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score, confusion_matrix

<span class="cm"># ── Split ──────────────────────────────────────</span>
X_train, X_test, y_train, y_test = <span class="fn">train_test_split</span>(
    X, y, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>)   <span class="cm"># 80/20</span>

<span class="cm"># ── KNN Classification ─────────────────────────</span>
clf = <span class="cl">KNeighborsClassifier</span>(n_neighbors=<span class="nm">3</span>)
clf.<span class="fn">fit</span>(X_train, y_train)
acc = <span class="fn">accuracy_score</span>(y_test, clf.<span class="fn">predict</span>(X_test))
<span class="fn">print</span>(<span class="st">f"Accuracy: {acc*100:.1f}%"</span>)

<span class="cm"># ── Confusion Matrix ───────────────────────────</span>
cm = <span class="fn">confusion_matrix</span>(y_test, clf.<span class="fn">predict</span>(X_test))
<span class="cm"># [[TP  FP]</span>
<span class="cm">#  [FN  TN]]</span>

<span class="cm"># ── K-Means Clustering ─────────────────────────</span>
km = <span class="cl">KMeans</span>(n_clusters=<span class="nm">3</span>, random_state=<span class="nm">42</span>)
km.<span class="fn">fit</span>(X)
<span class="fn">print</span>(km.labels_)    <span class="cm"># cluster id per sample</span>
<span class="fn">print</span>(km.cluster_centers_)  <span class="cm"># centroid coords</span>"""), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "Regression → continuous output; Classification → categorical output",
    "K in KNN = nearest neighbours; K in K-Means = cluster count",
    "Always split: <strong>80% train / 20% test</strong>",
    "Overfitting = high train accuracy, low test accuracy",
    "Confusion Matrix: TP, TN, FP, FN",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 7 — NLP
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 7"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[6]), unsafe_allow_html=True)
st.markdown(pills(UNITS[6]["pills"]), unsafe_allow_html=True)

# Interactive NLP Pipeline
st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ Live NLP Pipeline — type any sentence</div>', unsafe_allow_html=True)

nlp_input = st.text_input("Input sentence", value="Artificial Intelligence is transforming the world rapidly!", key="nlp_in")

STOP_WORDS = {"is","the","a","an","are","was","were","be","been","being","have","has","had",
              "do","does","did","will","would","shall","should","may","might","must","can",
              "could","i","you","he","she","it","we","they","them","their","this","that",
              "these","those","and","but","or","so","at","by","for","in","of","on","to",
              "up","as","into","through","about","with","not","no","nor","very","just","also"}

def simple_stem(w):
    rules = [("ing",""),("tion","t"),("ness",""),("ment",""),("ious",""),("ly",""),
             ("ies","y"),("es",""),("ed",""),("er",""),("est","")]
    for suf, rep in rules:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[:len(w)-len(suf)] + rep
    return w

if nlp_input:
    lowered  = nlp_input.lower()
    tokens   = [w for w in lowered.replace(",","").replace("!","").replace(".","").split() if w]
    filtered = [t for t in tokens if t not in STOP_WORDS]
    stemmed  = [simple_stem(t) for t in filtered]

    nlp_cols = st.columns(5)
    nlp_stages = [
        ("Original", nlp_input[:50] + ("…" if len(nlp_input) > 50 else ""), "#c84b2f"),
        ("Lowercased", lowered[:50] + ("…" if len(lowered) > 50 else ""), "#2563ae"),
        ("Tokens", " | ".join(tokens[:6]) + (" …" if len(tokens) > 6 else ""), "#1a7a4a"),
        ("Stop removed", " | ".join(filtered[:5]) + (" …" if len(filtered) > 5 else ""), "#8b3fb5"),
        ("Stemmed", " | ".join(stemmed[:5]) + (" …" if len(stemmed) > 5 else ""), "#c9720e"),
    ]
    for col, (name, val, color) in zip(nlp_cols, nlp_stages):
        col.markdown(f"""
<div style="background:var(--paper2);border:1px solid var(--line);border-radius:8px;padding:.7rem .8rem;min-height:80px">
  <div style="font-family:'JetBrains Mono',monospace;font-size:.57rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.3rem">{name}</div>
  <div style="font-size:.75rem;color:{color};font-weight:500;line-height:1.4;word-break:break-word">{val}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(topic_grid([
    ("What is NLP?", "💬", [
        "AI for human language understanding",
        "Bridge between human text and computers",
        "Tools: NLTK, spaCy, HuggingFace Transformers",
        "Applications: chatbots, translation, search engines",
    ]),
    ("Stemming vs Lemmatization", "🔄", [
        "<strong style='color:#c84b2f'>Stemming</strong> — chop suffix: 'running' → 'run'",
        "Fast but can give invalid words: 'studies' → 'studi'",
        "<strong style='color:#2563ae'>Lemmatization</strong> — dictionary: 'better' → 'good'",
        "Slower but always produces valid words",
    ]),
    ("Text Representation", "🗃️", [
        "<strong style='color:#c84b2f'>Bag of Words</strong> — word frequency vector; ignores order",
        "<strong style='color:#2563ae'>TF-IDF</strong> — penalises common words; importance weight",
        "<strong style='color:#1a7a4a'>Word2Vec</strong> — dense embeddings; captures meaning",
    ]),
    ("NLP Applications", "🤖", [
        "Sentiment Analysis — positive/negative/neutral",
        "Machine Translation — Google Translate",
        "Text Summarisation — auto-summary",
        "NER — identify names, places, dates",
        "Voice Assistants — Siri, Alexa, Google",
    ]),
]), unsafe_allow_html=True)

st.markdown(code_block("nlp_basics.py", """<span class="kw">import</span> nltk
<span class="kw">from</span> nltk.tokenize <span class="kw">import</span> word_tokenize
<span class="kw">from</span> nltk.corpus <span class="kw">import</span> stopwords
<span class="kw">from</span> nltk.stem <span class="kw">import</span> PorterStemmer, WordNetLemmatizer

text = <span class="st">"Artificial Intelligence is transforming the world."</span>

<span class="cm"># Step 1: Tokenise</span>
tokens = <span class="fn">word_tokenize</span>(text.lower())

<span class="cm"># Step 2: Remove stop words</span>
stop = <span class="fn">set</span>(stopwords.<span class="fn">words</span>(<span class="st">'english'</span>))
filtered = [w <span class="kw">for</span> w <span class="kw">in</span> tokens <span class="kw">if</span> w.isalpha() <span class="kw">and</span> w <span class="kw">not in</span> stop]

<span class="cm"># Step 3: Stem  (fast, imprecise)</span>
ps = <span class="cl">PorterStemmer</span>()
stems = [ps.<span class="fn">stem</span>(w) <span class="kw">for</span> w <span class="kw">in</span> filtered]

<span class="cm"># Step 4: Lemmatize  (slow, accurate)</span>
lem = <span class="cl">WordNetLemmatizer</span>()
lemmas = [lem.<span class="fn">lemmatize</span>(w) <span class="kw">for</span> w <span class="kw">in</span> filtered]

<span class="cm"># Step 5: Bag of Words</span>
<span class="kw">from</span> sklearn.feature_extraction.text <span class="kw">import</span> CountVectorizer, TfidfVectorizer
bow   = <span class="cl">CountVectorizer</span>().<span class="fn">fit_transform</span>([text])
tfidf = <span class="cl">TfidfVectorizer</span>().<span class="fn">fit_transform</span>([text])"""), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "Stop words = common words with little meaning (the, is, at)",
    "Stemming: fast but inaccurate; Lemmatization: slow but accurate",
    "BoW ignores word order; TF-IDF adds importance weighting",
    "Rule-based chatbot uses pattern matching; AI chatbot uses ML",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# UNIT 8 — Ethics
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Unit 8"), unsafe_allow_html=True)
st.markdown(unit_header(UNITS[7]), unsafe_allow_html=True)
st.markdown(pills(UNITS[7]["pills"]), unsafe_allow_html=True)

# Ethics radar using matplotlib
st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(15,16,20,.35);margin-bottom:.6rem">⬡ Responsible AI Pillars — adjust sliders</div>', unsafe_allow_html=True)

ethics_labels = ["Fairness","Transparency","Accountability","Privacy","Safety","Inclusivity"]
ethics_colors = ["#c84b2f","#2563ae","#1a7a4a","#8b3fb5","#c9720e","#555555"]
ethics_defaults = [85, 78, 90, 82, 88, 75]

eth_col1, eth_col2 = st.columns([1, 2])
ethics_vals = []

with eth_col1:
    for label, default, color in zip(ethics_labels, ethics_defaults, ethics_colors):
        v = st.slider(label, 0, 100, default, key=f"eth_{label}")
        ethics_vals.append(v / 100)
        st.markdown(f'<div style="height:3px;background:{color};width:{v}%;border-radius:2px;margin-top:-12px;margin-bottom:4px"></div>', unsafe_allow_html=True)

with eth_col2:
    N = len(ethics_labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    vals_plot = ethics_vals + ethics_vals[:1]

    fig3, ax3 = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    fig3.patch.set_facecolor("#ede9e1")
    ax3.set_facecolor("#f5f3ee")

    # Grid
    for r in [0.25, 0.5, 0.75, 1.0]:
        ax3.plot(angles, [r] * (N + 1), color="rgba(15,16,20,0.08)", linewidth=0.5, linestyle="-")

    # Filled polygon
    ax3.fill(angles, vals_plot, alpha=0.15, color="#c84b2f")
    ax3.plot(angles, vals_plot, color="#c84b2f", linewidth=1.5)

    # Dots per pillar
    for i, (angle, val, color) in enumerate(zip(angles[:-1], ethics_vals, ethics_colors)):
        ax3.plot(angle, val, "o", color=color, markersize=7, zorder=5)

    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(ethics_labels, size=8, color="#0f1014")
    ax3.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax3.set_yticklabels(["25","50","75","100"], size=6, color="rgba(15,16,20,0.3)")
    ax3.spines["polar"].set_visible(False)
    ax3.set_title("Responsible AI Score", fontsize=9, color="#0f1014", pad=12)

    plt.tight_layout()
    st.pyplot(fig3, use_container_width=True)
    plt.close()

st.markdown(topic_grid([
    ("AI Bias", "⚖️", [
        "Unfair results due to biased training data",
        "Types: gender, racial, confirmation bias",
        "Example: facial recognition fails for dark skin tones",
        "Fix: diverse datasets, bias auditing, fairness metrics",
    ]),
    ("Privacy & Data Ethics", "🔒", [
        "Collect personal data only with <strong>consent</strong>",
        "<strong>GDPR</strong> (Europe), <strong>PDPB</strong> (India) — data protection laws",
        "Data minimisation — collect only what's needed",
        "Right to be forgotten — user can delete their data",
    ]),
    ("AI Misuse & Threats", "⚠️", [
        "<strong style='color:#c84b2f'>Deepfakes</strong> — AI-generated fake videos/images",
        "Surveillance capitalism — tracking for profit",
        "Autonomous weapons — AI-powered warfare",
        "Job displacement — automation replacing humans",
    ]),
    ("AI for Social Good", "🌱", [
        "Healthcare: early disease detection",
        "Education: personalised tutoring, accessibility",
        "Climate: deforestation detection, weather modelling",
        "Disaster management: early warning systems",
    ]),
]), unsafe_allow_html=True)

st.markdown(callout("rem", "⚡ Must Remember", [
    "<strong>Bias in → Bias out</strong>: biased data produces biased models",
    "XAI = Explainable AI — ability to explain why the model decided",
    "India: NITI Aayog's National Strategy for AI (2018) — inclusive &amp; responsible",
    "Deepfake detection is an active research area",
]), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE TABLE
# ════════════════════════════════════════════════════════════════════════════

st.markdown(section_rule("Quick Reference"), unsafe_allow_html=True)
st.markdown('<h2 class="unit-h" style="font-size:1.5rem;margin-bottom:1rem">ML Algorithm Cheat Sheet</h2>', unsafe_allow_html=True)

st.markdown(cmp_table(
    ["Algorithm", "Type", "Output", "Key Param", "sklearn Class", "Use Case"],
    [
        ["Linear Regression", "Supervised", "Continuous", "coefficients", "LinearRegression()", "Predict prices, marks"],
        ["KNN", "Supervised", "Class/Value", "n_neighbors=K", "KNeighborsClassifier()", "Species, disease diagnosis"],
        ["Decision Tree", "Supervised", "Class", "max_depth", "DecisionTreeClassifier()", "Spam, medical diagnosis"],
        ["Naive Bayes", "Supervised", "Class", "prior probs", "GaussianNB()", "Text classification"],
        ["K-Means", "Unsupervised", "Clusters", "n_clusters=K", "KMeans()", "Customer segmentation"],
    ]
), unsafe_allow_html=True)

st.markdown('<h2 class="unit-h" style="font-size:1.5rem;margin-bottom:1rem;margin-top:1rem">Python Libraries</h2>', unsafe_allow_html=True)

st.markdown(cmp_table(
    ["Library", "Purpose", "Key Functions"],
    [
        ["NumPy", "Numerical computing, N-D arrays", "array(), mean(), std(), reshape(), linspace()"],
        ["Pandas", "Data manipulation, DataFrames", "read_csv(), describe(), fillna(), groupby(), merge()"],
        ["Matplotlib", "Visualisation", "plot(), bar(), scatter(), hist(), subplots(), show()"],
        ["Scikit-learn", "ML algorithms", "fit(), predict(), train_test_split(), accuracy_score()"],
        ["NLTK", "Natural Language Processing", "word_tokenize(), stopwords, PorterStemmer()"],
    ]
), unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center;padding:2rem 1rem 1rem;font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:rgba(15,16,20,.3);line-height:2;margin-top:2rem;border-top:1px solid rgba(15,16,20,.1)">
  <strong style="color:rgba(15,16,20,.55)">Class 11 AI — One Shot Revision</strong><br>
  CBSE · Subject Code 843 · Session 2025-26<br>
  Theory 50 marks &nbsp;|&nbsp; Practical 50 marks &nbsp;|&nbsp; Total 100 marks<br><br>
  Best of luck for your exams! 🚀
</div>
""", unsafe_allow_html=True)
