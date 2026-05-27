"""
The Four Mes - v2 (category edition) - Streamlit wrapper.

Streamlit's role here is hosting only. The real dashboard is `bump_3d.html`,
a self-contained file we serve as a static asset.

Static-file serving requires `.streamlit/config.toml` to have
`enableStaticServing = true`. The dashboard ends up at /app/static/bump_3d.html.
"""

import shutil
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Places - Bump 3D",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- keep the canonical files at repo root, mirror into static/ ----------
# This lets you edit bump_3d.html at the repo root and Streamlit picks up changes
# on next reload, while the iframe URL stays at /app/static/bump_3d.html.
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)
for fname in ("bump_3d.html", "report.pdf"):
    src = Path(__file__).parent / fname
    dst = static_dir / fname
    if src.exists() and (not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime):
        shutil.copy(src, dst)

# ---------- hide Streamlit's default chrome so the embed feels native ----------
st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; height: 0; }
      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      .stApp { background: #0a0a0d; }
      iframe { border: 0; display: block; }
      [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- backup download button (Streamlit-native, always works) ----------
pdf_path = Path(__file__).parent / "report.pdf"
if pdf_path.exists():
    cols = st.columns([10, 1])
    with cols[1]:
        st.download_button(
            label="📄 Report",
            data=pdf_path.read_bytes(),
            file_name="May-Bump-Report.pdf",
            mime="application/pdf",
        )

# ---------- embed the dashboard via a real-URL iframe ----------
# components.iframe(src) uses a real iframe with src= (not srcdoc), so the
# embedded page has a normal browsing context and MapLibre's WebGL workers
# can spawn correctly.
components.iframe("./app/static/bump_3d.html", height=920, scrolling=False)
