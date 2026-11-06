"""
CSIT 349 · Applied AI — Autobiography and Portfolio App
Fill in everything marked TODO with your OWN words, numbers and projects.
Run with:  streamlit run app.py
"""
import os
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

# ─────────────────────────────────────────────────────────────
# 1. YOUR CONTENT  (edit this block — everything else reads from it)
# ─────────────────────────────────────────────────────────────
NAME = "Raphael Jude Alvarado"
SECTION = "CSIT 349 – G01"
PROGRAM = "BS Information Technology, 4th Year"
SCHOOL = "Cebu Institute of Technology – University (CIT-U)"
EMAIL = ""  # optional: add an email to show it in the sidebar
GITHUB = "https://github.com/doydoyi"
TAGLINE = "Hakuna Matata."
PHOTO = "photo.jpg"  # put your photo next to app.py with this name

SHORT_BIO = """4th-year BSIT student at CIT-U, focused on cybersecurity and programming."""

AUTOBIOGRAPHY = {
    "Background": "A simple life.",
    "Education": "I'm a 4th-year BS Information Technology student at Cebu Institute of Technology – University (CIT-U).",
    "Interests": "Cybersecurity.",
    "Goals": "To work in cybersecurity, and one day build my own cybersecurity company.",
}

# (year, event) — confirm the years
MILESTONES = [
    ("2023", "Started BSIT at CIT-U"),            # TODO: confirm year
    ("2026", "Building a Linux learning site, a homelab and an anti-phishing site"),
    ("Next", "Work in cybersecurity"),
    ("Someday", "Found my own cybersecurity company"),
]

# skill: (self-rating 0–100, category)
SKILLS = {
    "Cybersecurity fundamentals": (50, "Security"),
    "Programming": (50, "Development"),
    "Linux": (50, "Systems"),
}

# At least three projects are required
IN_DEV = "In development"

PROJECTS = [
    {
        "title": "Linux Learning Site",
        "year": 2026,
        "role": "Solo developer",
        "tools": ["Linux"],
        "description": "A Linux learning site for 3rd-year students, so they are ready for industry after graduating.",
        "outcome": IN_DEV,
        "link": "https://github.com/doydoyi",
    },
    {
        "title": "Homelab",
        "year": 2026,
        "role": "Solo",
        "tools": ["Docker"],
        "description": "A personal homelab running self-hosted services in Docker containers.",
        "outcome": IN_DEV,
        "link": "https://github.com/doydoyi",
    },
    {
        "title": "Anti-Phishing Site",
        "year": 2026,
        "role": "Solo",
        "tools": [],  # optional: add the language/framework you use
        "description": "A site that checks links and flags likely phishing URLs.",
        "outcome": IN_DEV,
        "link": "https://github.com/doydoyi",
    },
]

# ─────────────────────────────────────────────────────────────
# 2. PAGE SETUP + STYLE
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="🛡️", layout="wide")

st.markdown(
    """
    <style>
    .card {padding:1.1rem 1.3rem; border-radius:14px;
           background:rgba(0,230,138,0.05); border:1px solid rgba(0,230,138,0.30);
           margin-bottom:0.8rem;}
    .tag {display:inline-block; padding:2px 10px; margin:2px; border-radius:999px;
          background:rgba(0,230,138,0.18); font-size:0.8rem;}
    .term {background:#050806; border:1px solid rgba(0,230,138,0.35); border-radius:10px;
           padding:0.9rem 1.1rem; font-family:monospace; color:#00E68A; line-height:1.6;}
    .term .p {color:#6FA88A;}
    .term .o {color:#D7F5E3;}
    .cursor {animation:blink 1s step-end infinite;}
    @keyframes blink {50% {opacity:0;}}
    .milestone {border-left:3px solid #00E68A; padding-left:12px; margin-bottom:10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1
st.session_state.setdefault("likes", 0)
st.session_state.setdefault("messages", [])


def show_photo(width="stretch"):
    if os.path.exists(PHOTO):
        st.image(PHOTO, width=width, caption=NAME)
    else:
        # Clearly labeled stand-in until you add photo.jpg
        grad = np.linspace(0, 1, 200)
        img = np.dstack([np.outer(grad, np.ones(200)) * 0.1 + 0.05,
                         np.full((200, 200), 0.75),
                         np.outer(np.ones(200), grad) * 0.3 + 0.3])
        st.image(img, width=width, caption="Photo placeholder — add photo.jpg", clamp=True)


# ─────────────────────────────────────────────────────────────
# 3. SIDEBAR
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    show_photo()
    st.subheader(NAME)
    st.caption(f"{PROGRAM} · {SCHOOL}")
    st.caption(f"📘 {SECTION}")
    st.divider()

    st.markdown("**Customize the view**")
    show_bio = st.checkbox("Show short bio", value=True)
    accent = st.color_picker("Accent color", "#00E68A")
    st.divider()

    st.link_button("GitHub", GITHUB, width="stretch")
    if EMAIL:
        st.markdown(f"✉️ {EMAIL}")
    st.caption(f"Page views this session: {st.session_state.visits}")

# ─────────────────────────────────────────────────────────────
# 4. HERO
# ─────────────────────────────────────────────────────────────
left, right = st.columns([3, 1])
with left:
    st.markdown(f"<h1 style='color:{accent};margin-bottom:0'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"#### _{TAGLINE}_")
    user = GITHUB.rstrip("/").split("/")[-1]
    bio_line = f"<span class='o'>{SHORT_BIO}</span><br>" if show_bio else ""
    st.markdown(
        f"""<div class='term'>
        <span class='p'>{user}@cit-u:~$</span> whoami<br>
        <span class='o'>{NAME}</span><br>
        <span class='p'>{user}@cit-u:~$</span> cat about.txt<br>
        <span class='o'>{PROGRAM} · {SECTION}</span><br>{bio_line}
        <span class='p'>{user}@cit-u:~$</span> <span class='cursor'>█</span>
        </div>""",
        unsafe_allow_html=True,
    )
with right:
    if st.button("👍 Like this page", width="stretch"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!")
    st.metric("Likes", st.session_state.likes)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Skills tracked", len(SKILLS))
m3.metric("In development", sum(p["outcome"] == IN_DEV for p in PROJECTS))
m4.metric("Top skill", max(SKILLS, key=lambda k: SKILLS[k][0]))

st.divider()

# ─────────────────────────────────────────────────────────────
# 5. TABS
# ─────────────────────────────────────────────────────────────
tab_about, tab_skills, tab_projects, tab_contact = st.tabs(
    ["📖 Autobiography", "🛠️ Skills", "💼 Projects", "📬 Contact"]
)

# ---- Autobiography
with tab_about:
    st.header("My Story")
    c1, c2 = st.columns([2, 1])
    with c1:
        section = st.radio("Jump to", list(AUTOBIOGRAPHY), horizontal=True)
        st.markdown(f"<div class='card'><h4>{section}</h4>{AUTOBIOGRAPHY[section]}</div>",
                    unsafe_allow_html=True)
        with st.expander("Read the full autobiography"):
            for title, text in AUTOBIOGRAPHY.items():
                st.markdown(f"**{title}.** {text}")
    with c2:
        st.subheader("Milestones")
        for year, event in MILESTONES:
            st.markdown(f"<div class='milestone'><b>{year}</b><br>{event}</div>",
                        unsafe_allow_html=True)

# ---- Skills
with tab_skills:
    st.header("Skills")
    df_skills = pd.DataFrame(
        [(k, v[0], v[1]) for k, v in SKILLS.items()],
        columns=["Skill", "Level", "Category"],
    )
    categories = st.multiselect("Filter by category", sorted(df_skills.Category.unique()),
                                default=sorted(df_skills.Category.unique()))
    min_level = st.slider("Minimum level", 0, 100, 0, step=5)
    shown = df_skills[df_skills.Category.isin(categories) & (df_skills.Level >= min_level)]

    c1, c2 = st.columns([1, 1])
    with c1:
        st.dataframe(
            shown, hide_index=True, width="stretch",
            column_config={"Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100)},
        )
    with c2:
        st.bar_chart(shown.set_index("Skill")["Level"], color=accent)

    st.subheader("Skill focus")
    pick = st.selectbox("Choose a skill", df_skills.Skill)
    lvl = SKILLS[pick][0]
    st.progress(lvl / 100, text=f"{pick}: {lvl}/100")

# ---- Projects
with tab_projects:
    st.header("Portfolio")
    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    tool_filter = st.multiselect("Show projects using", all_tools)
    sort_by = st.selectbox("Sort by", ["Newest first", "Oldest first", "Title"])

    projects = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if sort_by == "Newest first":
        projects.sort(key=lambda p: -p["year"])
    elif sort_by == "Oldest first":
        projects.sort(key=lambda p: p["year"])
    else:
        projects.sort(key=lambda p: p["title"])

    if not projects:
        st.warning("No projects match that filter.")
    cols = st.columns(3)
    for i, p in enumerate(projects):
        with cols[i % 3]:
            with st.container(border=True):
                st.subheader(p["title"])
                st.caption(f"{p['year']} · {p['role']}")
                if p["tools"]:
                    st.markdown("".join(f"<span class='tag'>{t}</span>" for t in p["tools"]),
                                unsafe_allow_html=True)
                st.write(p["description"])
                if p["outcome"] == IN_DEV:
                    st.info("🚧 **Status:** In development")
                else:
                    st.success(f"**Outcome:** {p['outcome']}")
                st.link_button("View project", p["link"])

    st.download_button(
        "⬇️ Download project list (CSV)",
        pd.DataFrame(PROJECTS).assign(tools=lambda d: d.tools.str.join(", ")).to_csv(index=False),
        file_name="projects.csv",
        mime="text/csv",
    )

# ---- Contact
with tab_contact:
    st.header("Get in touch")
    c1, c2 = st.columns([3, 2])
    with c1:
        with st.form("contact", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            reason = st.radio("Reason", ["Feedback", "Collaboration", "Just saying hi"], horizontal=True)
            rating = st.slider("Rate this site", 1, 5, 5)
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send")
        if submitted:
            if not name or not message:
                st.error("Please add your name and a message.")
            else:
                st.session_state.messages.append(
                    {"time": datetime.now().strftime("%H:%M"), "name": name,
                     "reason": reason, "rating": rating, "message": message}
                )
                st.success(f"Thanks, {name}! Your message was received.")
                st.balloons()
    with c2:
        st.subheader("Messages this session")
        if st.session_state.messages:
            st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)
        else:
            st.info("No messages yet — be the first!")

st.divider()
st.caption(f"© {datetime.now().year} {NAME} · {SECTION} · Built with Streamlit")
