import streamlit as st
import tempfile
import os

from main import analyze_resume


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResumeIQ — AI Candidate Matching",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

if "job_description" not in st.session_state:
    st.session_state.job_description = ""


# ============================================================
# CSS / DESIGN SYSTEM
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       VARIABLES
       ======================================================== */

    :root {
        --bg: #f7f8fc;
        --surface: #ffffff;
        --surface-soft: #fafbff;

        --text: #11162a;
        --text-2: #30374a;
        --muted: #667085;
        --subtle: #98a2b3;

        --primary: #6657e8;
        --primary-2: #5678ee;
        --primary-soft: #efedff;

        --green: #16b98a;
        --green-soft: #eafaf5;

        --red: #e85d6a;
        --red-soft: #fff0f2;

        --yellow: #d99a22;
        --yellow-soft: #fff7e4;

        --border: #e5e8f0;

        --shadow:
            0 12px 35px rgba(35, 39, 70, 0.065);
    }


    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 80% 0%,
                rgba(111, 92, 255, 0.07),
                transparent 25%
            ),
            var(--bg);

        color: var(--text);
    }

    .block-container {
        max-width: 1450px;
        padding: 1rem 3.5rem 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }


    /* ========================================================
       NAVBAR
       ======================================================== */

    .navbar {
        height: 60px;

        display: flex;
        align-items: center;
        justify-content: space-between;

        margin-bottom: 1.25rem;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 0.7rem;
    }

    .brand-logo {
        width: 38px;
        height: 38px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 11px;

        background:
            linear-gradient(
                135deg,
                #735df3,
                #5a79ee
            );

        color: white;

        font-size: 1rem;
        font-weight: 850;

        box-shadow:
            0 8px 22px rgba(102, 87, 232, 0.23);
    }

    .brand-name {
        color: #11162a;

        font-size: 0.96rem;
        font-weight: 800;
    }

    .brand-subtitle {
        color: var(--muted);

        font-size: 0.64rem;

        margin-top: 1px;
    }

    .nav-links {
        display: flex;
        align-items: center;

        gap: 1.6rem;

        color: #697286;

        font-size: 0.73rem;
        font-weight: 650;
    }

    .nav-active {
        color: var(--primary);

        background: var(--primary-soft);

        padding: 0.52rem 0.82rem;

        border-radius: 8px;
    }

    .engine-status {
        display: flex;
        align-items: center;

        gap: 0.45rem;

        padding: 0.52rem 0.82rem;

        background: white;

        border: 1px solid var(--border);

        border-radius: 999px;

        color: #687185;

        font-size: 0.66rem;
        font-weight: 650;

        box-shadow:
            0 4px 14px rgba(35, 39, 70, 0.04);
    }

    .green-dot {
        width: 7px;
        height: 7px;

        border-radius: 50%;

        background: #19c58e;

        box-shadow:
            0 0 8px rgba(25, 197, 142, 0.55);
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;

        min-height: 285px;

        padding: 2.6rem 3rem;

        border-radius: 24px;

        border: 1px solid #dfe2f5;

        background:
            linear-gradient(
                115deg,
                #ffffff 0%,
                #f7f6ff 48%,
                #e9edff 100%
            );

        overflow: hidden;

        box-shadow:
            0 18px 55px rgba(63, 68, 120, 0.08);
    }

    .hero::after {
        content: "";

        position: absolute;

        width: 450px;
        height: 450px;

        right: -160px;
        top: -190px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(112, 92, 255, 0.15),
                transparent 68%
            );
    }

    .hero-eyebrow {
        position: relative;
        z-index: 2;

        color: #6657e8;

        font-size: 0.67rem;

        font-weight: 800;

        letter-spacing: 0.16em;

        text-transform: uppercase;

        margin-bottom: 0.75rem;
    }

    .hero-title {
        position: relative;
        z-index: 2;

        font-size: 3rem;

        line-height: 1.04;

        font-weight: 850;

        letter-spacing: -0.055em;

        max-width: 720px;

        color: #11162a;
    }

    .hero-title span {
        background:
            linear-gradient(
                90deg,
                #6657e8,
                #566fec
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        position: relative;
        z-index: 2;

        max-width: 710px;

        margin-top: 0.9rem;

        color: #667085;

        font-size: 0.9rem;

        line-height: 1.65;
    }

    .hero-pills {
        position: relative;
        z-index: 3;

        display: flex;

        gap: 0.55rem;

        margin-top: 1.35rem;
    }

    .hero-pill {
        padding: 0.43rem 0.68rem;

        background: rgba(255, 255, 255, 0.82);

        border: 1px solid #e0e2ef;

        border-radius: 8px;

        color: #4d556a;

        font-size: 0.65rem;

        font-weight: 600;

        box-shadow:
            0 4px 12px rgba(50, 55, 100, 0.04);
    }


    /* ========================================================
       HERO AI VISUAL
       ======================================================== */

    .ai-visual {
        position: absolute;

        z-index: 4;

        right: 5%;

        top: 48%;

        transform: translateY(-50%);

        width: 355px;
        height: 190px;
    }

    .mini-document {
        position: absolute;

        width: 135px;
        height: 108px;

        padding: 0.9rem;

        border-radius: 13px;

        background: white;

        border: 1px solid #e0e4f2;

        box-shadow:
            0 15px 30px rgba(48, 54, 110, 0.10);
    }

    .resume-doc {
        left: 0;
        top: 18px;

        transform: rotate(-6deg);
    }

    .jd-doc {
        right: 0;
        top: 18px;

        transform: rotate(6deg);
    }

    .doc-title {
        font-size: 0.61rem;

        font-weight: 800;

        color: #4f46c6;

        margin-bottom: 0.6rem;
    }

    .doc-line {
        height: 5px;

        border-radius: 5px;

        background: #e8eaf4;

        margin-bottom: 6px;
    }

    .doc-line.short {
        width: 65%;
    }

    .ai-core {
        position: absolute;

        left: 50%;
        top: 50%;

        transform: translate(-50%, -50%);

        width: 72px;
        height: 72px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 19px;

        background:
            linear-gradient(
                135deg,
                #6958ed,
                #5275ed
            );

        color: white;

        font-size: 1.35rem;

        font-weight: 850;

        box-shadow:
            0 16px 35px rgba(91, 87, 220, 0.28);
    }

    .connection {
        position: absolute;

        height: 2px;

        background:
            linear-gradient(
                90deg,
                #aaa3f5,
                #7597ef
            );

        width: 75px;

        top: 50%;
    }

    .connection.left {
        left: 105px;
    }

    .connection.right {
        right: 105px;
    }


    /* ========================================================
       WORKFLOW
       ======================================================== */

    .workflow {
        display: flex;

        align-items: center;

        margin: 2rem 0 1.7rem;
    }

    .workflow-step {
        display: flex;

        align-items: center;

        gap: 0.65rem;

        min-width: 190px;
    }

    .step-number {
        width: 31px;
        height: 31px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 10px;

        background: white;

        border: 1px solid #dce0f2;

        color: #5263d8;

        font-size: 0.65rem;

        font-weight: 800;

        box-shadow:
            0 4px 12px rgba(50, 55, 100, 0.04);
    }

    .step-number.active {
        background:
            linear-gradient(
                135deg,
                #6d5cf1,
                #5877ed
            );

        color: white;

        border: none;
    }

    .step-title {
        color: #333b50;

        font-size: 0.72rem;

        font-weight: 700;
    }

    .step-subtitle {
        color: #9aa2b3;

        font-size: 0.61rem;

        margin-top: 2px;
    }

    .workflow-line {
        flex: 1;

        max-width: 130px;

        height: 1px;

        background: #dfe2eb;

        margin: 0 0.7rem;
    }


    /* ========================================================
       SECTION
       ======================================================== */

    .section-eyebrow {
        color: #8a91a2;

        font-size: 0.61rem;

        font-weight: 800;

        letter-spacing: 0.13em;

        text-transform: uppercase;
    }

    .section-title {
        margin-top: 0.25rem;

        font-size: 1.28rem;

        font-weight: 800;

        color: #151a2c;
    }

    .section-description {
        margin-top: 0.2rem;

        color: #8991a3;

        font-size: 0.69rem;
    }


    /* ========================================================
       INPUT CARDS
       ======================================================== */

    .input-card {
        min-height: 90px;

        padding: 1.35rem;

        border-radius: 17px;

        border: 1px solid var(--border);

        background: white;

        box-shadow: var(--shadow);
    }

    .input-card-head {
        display: flex;

        align-items: center;

        gap: 0.7rem;
    }

    .input-icon {
        width: 38px;
        height: 38px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 11px;

        font-size: 1rem;
    }

    .resume-icon {
        background: #eeecff;

        color: #6454e7;
    }

    .job-icon {
        background: #fff0f1;

        color: #d95766;
    }

    .input-title {
        color: #171c2d;

        font-size: 0.88rem;

        font-weight: 800;
    }

    .input-subtitle {
        color: #8c94a5;

        font-size: 0.65rem;

        margin-top: 2px;
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        margin-top: 1rem;
    }

    [data-testid="stFileUploaderDropzone"] {
        min-height: 165px !important;

        border-radius: 14px !important;

        border: 1.5px dashed #cbd0ef !important;

        background:
            linear-gradient(
                180deg,
                #fafaff,
                #f8f9ff
            ) !important;
    }

    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: #7969ee !important;

        background: #f8f7ff !important;
    }


    /* ========================================================
       UPLOAD BUTTON
       ======================================================== */

    [data-testid="stFileUploaderDropzone"] button {
        background: #ffffff !important;

        color: #30374a !important;

        border: 1px solid #d8dce8 !important;

        border-radius: 9px !important;

        font-weight: 700 !important;

        box-shadow:
            0 3px 10px rgba(35, 39, 70, 0.05) !important;
    }

    [data-testid="stFileUploaderDropzone"] button:hover {
        background: #f5f3ff !important;

        color: #5b4bd7 !important;

        border-color: #aaa1f0 !important;
    }

    [data-testid="stFileUploaderDropzone"] button span {
        color: #30374a !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] {
        color: #697286 !important;
    }

    [data-testid="stFileUploaderFileName"] {
        color: #30374a !important;
    }


    /* ========================================================
       TEXT AREA
       ======================================================== */

    [data-testid="stTextArea"] {
        margin-top: 1rem;
    }

    [data-testid="stTextArea"] textarea {
        min-height: 165px !important;

        border-radius: 14px !important;

        border: 1px solid #e0e3eb !important;

        background: #fbfcfe !important;

        color: #242a3d !important;

        font-size: 0.77rem !important;

        line-height: 1.55 !important;
    }

    [data-testid="stTextArea"] textarea:focus {
        border-color: #8174e9 !important;

        box-shadow:
            0 0 0 3px rgba(102, 87, 232, 0.08) !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    div.stButton > button {
        border-radius: 10px;

        min-height: 2.55rem;

        font-size: 0.72rem;

        font-weight: 700;

        border: 1px solid #e0e3eb;

        background: white;

        color: #596176;

        transition: 0.18s ease;
    }

    div.stButton > button:hover {
        border-color: #b8b0f4;

        color: #5546d1;

        box-shadow:
            0 6px 16px rgba(65, 60, 140, 0.07);
    }

    div.stButton > button[kind="primary"] {
        color: white;

        border: none;

        background:
            linear-gradient(
                90deg,
                #6e5df1,
                #5577ee
            );

        box-shadow:
            0 10px 25px rgba(96, 83, 225, 0.20);
    }

    div.stButton > button[kind="primary"]:hover {
        color: white;

        transform: translateY(-1px);

        box-shadow:
            0 14px 30px rgba(96, 83, 225, 0.27);
    }


    /* ========================================================
       SCORE CARDS
       ======================================================== */

    .score-card {
        padding: 1.15rem;

        border-radius: 15px;

        border: 1px solid var(--border);

        background: white;

        box-shadow:
            0 7px 24px rgba(35, 39, 70, 0.045);
    }

    .score-label {
        color: #8b93a4;

        font-size: 0.59rem;

        font-weight: 800;

        letter-spacing: 0.11em;

        text-transform: uppercase;
    }

    .score-value {
        color: #151a2c;

        margin-top: 0.45rem;

        font-size: 1.75rem;

        font-weight: 850;
    }

    .score-description {
        color: #9aa1b0;

        font-size: 0.61rem;

        margin-top: 0.25rem;
    }


    /* ========================================================
       RESULT PANELS
       ======================================================== */

    .result-panel {
        padding: 1.1rem;

        border-radius: 14px;

        border: 1px solid var(--border);

        background: white;

        box-shadow:
            0 7px 24px rgba(35, 39, 70, 0.045);
    }

    .result-title {
        color: #20263a;

        font-size: 0.82rem;

        font-weight: 800;
    }

    .result-description {
        color: #929aaa;

        font-size: 0.64rem;

        margin-top: 0.25rem;
    }


    /* ========================================================
       STATUS
       ======================================================== */

    .status {
        display: inline-flex;

        align-items: center;

        padding: 0.35rem 0.65rem;

        border-radius: 999px;

        font-size: 0.64rem;

        font-weight: 750;
    }

    .status-success {
        color: #10956e;

        background: #e8faf4;
    }

    .status-warning {
        color: #b57912;

        background: #fff6df;
    }

    .status-danger {
        color: #d04d5a;

        background: #ffedef;
    }

    .status-neutral {
        color: #697285;

        background: #f0f2f6;
    }


    /* ========================================================
       SKILLS
       ======================================================== */

    .skill-chip {
        display: inline-block;

        padding: 0.38rem 0.62rem;

        margin: 0.16rem;

        border-radius: 7px;

        font-size: 0.64rem;

        border: 1px solid #e2e5ed;

        background: #fafbfc;

        color: #60697b;
    }

    .matched-chip {
        color: #118965;

        border-color: #c9eee2;

        background: #effbf7;
    }

    .missing-chip {
        color: #d04e5c;

        border-color: #f5d0d5;

        background: #fff5f6;
    }


    /* ========================================================
       INSIGHTS
       ======================================================== */

    .insight {
        padding: 0.75rem 0.9rem;

        margin-bottom: 0.45rem;

        border-radius: 9px;

        background: #fafbfe;

        border: 1px solid #edf0f5;

        color: #626b7e;

        font-size: 0.7rem;

        line-height: 1.5;
    }


    /* ========================================================
       TABS
       ======================================================== */

    [data-baseweb="tab-list"] {
        gap: 1.5rem !important;

        border-bottom: 1px solid #e5e8f0 !important;
    }

    [data-baseweb="tab"] {
        color: #667085 !important;

        font-size: 0.72rem !important;

        font-weight: 700 !important;

        padding: 0.7rem 0.1rem !important;
    }

    [data-baseweb="tab"]:hover {
        color: #6657e8 !important;
    }

    [aria-selected="true"] {
        color: #6657e8 !important;
    }

    [data-baseweb="tab-highlight"] {
        background-color: #6657e8 !important;
    }


    /* ========================================================
       STREAMLIT METRIC
       ======================================================== */

    [data-testid="stMetricLabel"] {
        color: #7f8798 !important;

        font-size: 0.68rem !important;
    }

    [data-testid="stMetricValue"] {
        color: #171c2d !important;
    }


    /* ========================================================
       INFO / SUCCESS / ERROR
       ======================================================== */

    [data-testid="stAlert"] {
        border-radius: 11px !important;
    }


    /* ========================================================
       PROGRESS
       ======================================================== */

    [data-testid="stProgress"] {
        margin-top: 0.5rem;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;

        color: #a1a7b4;

        font-size: 0.62rem;

        padding: 3rem 0 0.5rem;
    }


    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 1000px) {

        .block-container {
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }

        .hero-title {
            font-size: 2.3rem;
        }

        .ai-visual {
            display: none;
        }

        .nav-links {
            display: none;
        }

        .workflow-line {
            max-width: 50px;
        }

    }

    </style>
    """
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def status_badge(status):

    status = str(status).lower()

    if status in ["matched", "met", "available"]:
        css = "status-success"
        icon = "✓"

    elif status in ["partially met", "unknown"]:
        css = "status-warning"
        icon = "⚠"

    elif status in ["not matched", "not met"]:
        css = "status-danger"
        icon = "✕"

    else:
        css = "status-neutral"
        icon = "●"

    return f"""
        <span class="status {css}">
            {icon} {status.title()}
        </span>
    """


def show_status(status):
    st.html(status_badge(status))


def score_card(
    label,
    value,
    description
):

    st.html(
        f"""
        <div class="score-card">

            <div class="score-label">
                {label}
            </div>

            <div class="score-value">
                {value}
            </div>

            <div class="score-description">
                {description}
            </div>

        </div>
        """
    )


def skill_chips(
    skills,
    prefix="",
    chip_type=""
):

    if not skills:
        st.caption("None detected")
        return

    html = ""

    for skill in skills:

        html += f"""
            <span class="skill-chip {chip_type}">
                {prefix}{skill}
            </span>
        """

    st.html(html)


def safe_progress_value(value):

    """
    Convert NumPy float32 / float64 / Python numeric
    into a safe Python float for Streamlit.
    """

    return float(
        min(
            max(
                float(value),
                0.0
            ),
            1.0
        )
    )


def coverage_percent(value):

    """
    Backend may return coverage as:

        0.0 - 1.0

    OR:

        0 - 100

    Normalize both formats to percentage.
    """

    value = float(value)

    if value <= 1.0:
        return value * 100.0

    return value


# ============================================================
# NAVBAR
# ============================================================

st.html(
    """
    <div class="navbar">

        <div class="brand">

            <div class="brand-logo">
                ✦
            </div>

            <div>

                <div class="brand-name">
                    ResumeIQ
                </div>

                <div class="brand-subtitle">
                    Candidate intelligence
                </div>

            </div>

        </div>


        <div class="nav-links">

            <span class="nav-active">
                Home
            </span>

            <span>
                Analyze
            </span>

            <span>
                Results
            </span>

            <span>
                About
            </span>

        </div>


        <div class="engine-status">

            <span class="green-dot"></span>

            AI engine ready

        </div>

    </div>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-eyebrow">
            Intelligent Resume Matching
        </div>

        <div class="hero-title">
            Find the right
            <span>candidate fit.</span>
        </div>

        <div class="hero-description">
            Analyze skills, role alignment, experience requirements,
            project evidence and semantic similarity from a single
            resume and job description.
        </div>


        <div class="hero-pills">

            <div class="hero-pill">
                ✓ Skill extraction
            </div>

            <div class="hero-pill">
                ✓ Experience analysis
            </div>

            <div class="hero-pill">
                ✓ Evidence detection
            </div>

            <div class="hero-pill">
                ✓ Semantic matching
            </div>

        </div>


        <div class="ai-visual">

            <div class="mini-document resume-doc">

                <div class="doc-title">
                    👤 RESUME
                </div>

                <div class="doc-line"></div>
                <div class="doc-line"></div>
                <div class="doc-line short"></div>

            </div>


            <div class="connection left"></div>


            <div class="ai-core">
                AI
            </div>


            <div class="connection right"></div>


            <div class="mini-document jd-doc">

                <div class="doc-title">
                    💼 JOB
                </div>

                <div class="doc-line"></div>
                <div class="doc-line"></div>
                <div class="doc-line short"></div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# WORKFLOW
# ============================================================

st.html(
    """
    <div class="workflow">

        <div class="workflow-step">

            <div class="step-number active">
                01
            </div>

            <div>

                <div class="step-title">
                    Upload resume
                </div>

                <div class="step-subtitle">
                    Provide candidate's PDF
                </div>

            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="step-number">
                02
            </div>

            <div>

                <div class="step-title">
                    Add job description
                </div>

                <div class="step-subtitle">
                    Paste the complete JD
                </div>

            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="step-number">
                03
            </div>

            <div>

                <div class="step-title">
                    Analyze fit
                </div>

                <div class="step-subtitle">
                    Get detailed match analysis
                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# INPUT HEADER
# ============================================================

st.html(
    """
    <div style="margin-bottom: 1rem;">

        <div class="section-eyebrow">
            START HERE
        </div>

        <div class="section-title">
            Analyze a candidate
        </div>

        <div class="section-description">
            Provide the resume and the target role you want to evaluate.
        </div>

    </div>
    """
)


# ============================================================
# INPUT COLUMNS
# ============================================================

left, right = st.columns(
    [0.95, 1.05],
    gap="large"
)


# ============================================================
# RESUME INPUT
# ============================================================

with left:

    st.html(
        """
        <div class="input-card">

            <div class="input-card-head">

                <div class="input-icon resume-icon">
                    📄
                </div>

                <div>

                    <div class="input-title">
                        Candidate resume
                    </div>

                    <div class="input-subtitle">
                        Upload a PDF resume · text-based resumes work best
                    </div>

                </div>

            </div>

        </div>
        """
    )


    resume_file = st.file_uploader(
        "Resume PDF",
        type=["pdf"],
        label_visibility="collapsed",
        help="Upload a candidate resume."
    )


    if resume_file:

        st.success(
            f"✓ {resume_file.name}"
        )

        st.caption(
            f"{resume_file.size / 1024:.1f} KB · Ready for analysis"
        )

    else:

        st.caption(
            "Drag & drop your resume above or browse files."
        )


# ============================================================
# JOB DESCRIPTION
# ============================================================

with right:

    st.html(
        """
        <div class="input-card">

            <div class="input-card-head">

                <div class="input-icon job-icon">
                    💼
                </div>

                <div>

                    <div class="input-title">
                        Target job description
                    </div>

                    <div class="input-subtitle">
                        Include responsibilities, skills and experience requirements.
                    </div>

                </div>

            </div>

        </div>
        """
    )


    job_description = st.text_area(
        "Job Description",
        value=st.session_state.job_description,
        height=165,
        label_visibility="collapsed",
        placeholder=(
            "Paste the complete job description here...\n\n"
            "Example:\n"
            "We are looking for a Backend Developer.\n"
            "Python is required.\n"
            "The candidate must have 2 years of experience "
            "with FastAPI.\n"
            "Experience with Django is preferred."
        )
    )


    st.session_state.job_description = job_description


    char_count = len(
        job_description
    )


    st.caption(
        f"{char_count:,} / 5,000 characters"
    )


# ============================================================
# JD ACTION BUTTONS
# ============================================================

action_left, action_right, _ = st.columns(
    [1, 1, 4]
)


with action_left:

    if st.button(
        "📄 Load sample JD",
        use_container_width=True
    ):

        st.session_state.job_description = (
            "We are looking for a Backend Developer.\n\n"
            "Python is required.\n\n"
            "The candidate must have 2 years of "
            "experience with FastAPI.\n\n"
            "Experience with Django is preferred.\n\n"
            "At least 1 year of experience with SQL is required.\n\n"
            "Knowledge of Docker is a plus."
        )

        st.rerun()


with action_right:

    if st.button(
        "Clear",
        use_container_width=True
    ):

        st.session_state.job_description = ""

        st.rerun()


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.write("")


analyze_button = st.button(
    "✦  Analyze candidate  →",
    type="primary",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze_button:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if resume_file is None:

        st.error(
            "Please upload a resume PDF."
        )

        st.stop()


    if not job_description.strip():

        st.error(
            "Please enter a job description."
        )

        st.stop()


    # --------------------------------------------------------
    # TEMPORARY PDF
    # --------------------------------------------------------

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            resume_file.getbuffer()
        )

        temp_resume_path = temp_file.name


    # --------------------------------------------------------
    # RUN ENGINE
    # --------------------------------------------------------

    try:

        with st.status(
            "Analyzing candidate...",
            expanded=True
        ) as analysis_status:

            st.write(
                "Extracting resume content..."
            )

            results = analyze_resume(
                temp_resume_path,
                job_description=job_description,
                mode="1"
            )

            st.write(
                "Matching skills and role..."
            )

            st.write(
                "Analyzing experience and evidence..."
            )

            st.write(
                "Calculating semantic similarity..."
            )

            analysis_status.update(
                label="Analysis complete",
                state="complete",
                expanded=False
            )


    except Exception as error:

        st.error(
            f"Analysis failed: {error}"
        )

        st.stop()


    finally:

        if os.path.exists(
            temp_resume_path
        ):

            os.remove(
                temp_resume_path
            )


    # ========================================================
    # FINAL ASSESSMENT
    # ========================================================

    final_assessment = results.get(
        "final_assessment",
        {}
    )


    role_assessment = final_assessment.get(
        "role",
        {}
    )


    required = final_assessment.get(
        "required_skills",
        {}
    )


    preferred = final_assessment.get(
        "preferred_skills",
        {}
    )


    experience = final_assessment.get(
        "experience_requirements",
        []
    )


    evidence = final_assessment.get(
        "evidence",
        {}
    )


    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.divider()


    st.html(
        """
        <div style="margin-bottom:1rem;">

            <div class="section-eyebrow">
                MATCH ANALYSIS
            </div>

            <div class="section-title">
                Candidate fit signals
            </div>

            <div class="section-description">
                Analysis generated by the ResumeIQ matching engine.
            </div>

        </div>
        """
    )


    # ========================================================
    # SCORE CARDS
    # ========================================================

    c1, c2, c3, c4 = st.columns(
        4,
        gap="medium"
    )


    with c1:

        score_card(
            "SKILL COVERAGE",
            f"{float(results['skill_score']) * 100:.1f}%",
            "Resume skills found in JD"
        )


    with c2:

        score_card(
            "REQUIRED COVERAGE",
            f"{coverage_percent(required.get('coverage', 0.0)):.1f}%",
            "Required skills matched"
        )


    with c3:

        score_card(
            "SEMANTIC MATCH",
            f"{float(results['semantic_similarity']) * 100:.1f}%",
            "Meaning-level similarity"
        )


    with c4:

        score_card(
            "TF-IDF MATCH",
            f"{float(results['tfidf_similarity']) * 100:.1f}%",
            "Lexical similarity"
        )


    st.write("")


    # ========================================================
    # ROLE ANALYSIS
    # ========================================================

    role_cols = st.columns(
        [1, 1, 0.75],
        gap="medium"
    )


    with role_cols[0]:

        st.html(
            f"""
            <div class="result-panel">

                <div class="result-title">
                    Target role
                </div>

                <div class="result-description">
                    Detected from the job description
                </div>

                <div style="
                    margin-top:0.65rem;
                    font-weight:800;
                    color:#171c2d;
                ">
                    {results.get("job_role", "Unknown")}
                </div>

            </div>
            """
        )


    with role_cols[1]:

        st.html(
            f"""
            <div class="result-panel">

                <div class="result-title">
                    Normalized role
                </div>

                <div class="result-description">
                    Canonical role representation
                </div>

                <div style="
                    margin-top:0.65rem;
                    font-weight:800;
                    color:#171c2d;
                ">
                    {results.get("normalized_role", "Unknown")}
                </div>

            </div>
            """
        )


    with role_cols[2]:

        st.html(
            """
            <div class="result-panel">

                <div class="result-title">
                    Role status
                </div>

            </div>
            """
        )

        show_status(
            role_assessment.get(
                "status",
                "unknown"
            )
        )


    st.write("")


    # ========================================================
    # RESULT TABS
    # ========================================================

    (
        overview,
        skills,
        experience_tab,
        evidence_tab,
        nlp
    ) = st.tabs(
        [
            "Overview",
            "Skills",
            "Experience",
            "Evidence",
            "NLP Analysis"
        ]
    )


    # ========================================================
    # OVERVIEW TAB
    # ========================================================

    with overview:

        st.write("")


        a, b = st.columns(
            2,
            gap="large"
        )


        # ----------------------------------------------------
        # REQUIRED
        # ----------------------------------------------------

        with a:

            st.subheader(
                "🔒 Required skills"
            )

            show_status(
                required.get(
                    "status",
                    "unknown"
                )
            )

            st.metric(
                "Coverage",
                f"{coverage_percent(required.get('coverage', 0.0)):.1f}%"
            )

            st.caption(
                "Matched"
            )

            skill_chips(
                required.get(
                    "matched",
                    []
                ),
                "✓ ",
                "matched-chip"
            )

            st.caption(
                "Missing"
            )

            skill_chips(
                required.get(
                    "missing",
                    []
                ),
                "✕ ",
                "missing-chip"
            )


        # ----------------------------------------------------
        # PREFERRED
        # ----------------------------------------------------

        with b:

            st.subheader(
                "✨ Preferred skills"
            )

            show_status(
                preferred.get(
                    "status",
                    "unknown"
                )
            )

            st.metric(
                "Coverage",
                f"{coverage_percent(preferred.get('coverage', 0.0)):.1f}%"
            )

            st.caption(
                "Matched"
            )

            skill_chips(
                preferred.get(
                    "matched",
                    []
                ),
                "✓ ",
                "matched-chip"
            )

            st.caption(
                "Missing"
            )

            skill_chips(
                preferred.get(
                    "missing",
                    []
                ),
                "✕ ",
                "missing-chip"
            )


        st.divider()


        st.subheader(
            "Key insights"
        )


        insights = results.get(
            "final_insights",
            []
        )


        if insights:

            for insight in insights:

                st.html(
                    f"""
                    <div class="insight">
                        {insight}
                    </div>
                    """
                )

        else:

            st.info(
                "No additional insights available."
            )


    # ========================================================
    # SKILLS TAB
    # ========================================================

    with skills:

        st.write("")


        a, b = st.columns(
            2,
            gap="large"
        )


        with a:

            st.subheader(
                "✓ Matched skills"
            )

            skill_chips(
                results.get(
                    "matched_skills",
                    []
                ),
                "✓ ",
                "matched-chip"
            )


        with b:

            st.subheader(
                "✕ Missing skills"
            )

            skill_chips(
                results.get(
                    "missing_skills",
                    []
                ),
                "✕ ",
                "missing-chip"
            )


        st.divider()


        st.subheader(
            "Category analysis"
        )


        category_data = results.get(
            "category_comparison",
            {}
        )


        if category_data:

            category_count = min(
                len(category_data),
                3
            )


            if category_count > 0:

                cols = st.columns(
                    category_count
                )


                for index, (
                    category,
                    data
                ) in enumerate(
                    category_data.items()
                ):

                    with cols[
                        index % category_count
                    ]:

                        st.html(
                            f"""
                            <div class="result-panel">

                                <div class="result-title">
                                    {category.replace("_", " ").title()}
                                </div>

                            </div>
                            """
                        )


                        matched = data.get(
                            "matched",
                            []
                        )


                        missing = data.get(
                            "missing",
                            []
                        )


                        if matched:

                            st.caption(
                                "Matched"
                            )

                            skill_chips(
                                matched,
                                "✓ ",
                                "matched-chip"
                            )


                        if missing:

                            st.caption(
                                "Missing"
                            )

                            skill_chips(
                                missing,
                                "✕ ",
                                "missing-chip"
                            )

        else:

            st.info(
                "No category analysis available."
            )


    # ========================================================
    # EXPERIENCE TAB
    # ========================================================

    with experience_tab:

        st.write("")


        if experience:

            for item in experience:

                skill = item.get(
                    "skill",
                    "Unknown"
                )

                required_years = item.get(
                    "required_years",
                    0
                )

                resume_months = item.get(
                    "resume_months",
                    0
                )

                status = item.get(
                    "status",
                    "unknown"
                )


                st.html(
                    f"""
                    <div class="result-panel">

                        <div class="result-title">
                            💼 {skill}
                        </div>

                    </div>
                    """
                )


                a, b, c = st.columns(
                    3
                )


                with a:

                    score_card(
                        "REQUIRED",
                        f"{required_years} years",
                        "Job requirement"
                    )


                with b:

                    score_card(
                        "RESUME",
                        f"{resume_months} months",
                        "Detected experience"
                    )


                with c:

                    st.caption(
                        "STATUS"
                    )

                    show_status(
                        status
                    )


                st.write("")


        else:

            st.info(
                "No explicit experience requirements detected."
            )


    # ========================================================
    # EVIDENCE TAB
    # ========================================================

    with evidence_tab:

        st.write("")


        a, b, c = st.columns(
            3
        )


        with a:

            score_card(
                "SKILL EVIDENCE",
                "Available"
                if evidence.get("skill")
                else "Unavailable",
                "Direct resume evidence"
            )


        with b:

            score_card(
                "PROJECT EVIDENCE",
                "Available"
                if evidence.get("project")
                else "Unavailable",
                "Project-based support"
            )


        with c:

            score_card(
                "EXPERIENCE EVIDENCE",
                "Available"
                if evidence.get("experience")
                else "Unavailable",
                "Experience-based support"
            )


        st.divider()


        # ----------------------------------------------------
        # PROJECT EVIDENCE
        # ----------------------------------------------------

        st.subheader(
            "Project evidence"
        )


        project_evidence = results.get(
            "project_evidence",
            {}
        )


        project_found = False


        for skill, projects in project_evidence.items():

            if projects:

                project_found = True

                st.markdown(
                    f"**{skill}**"
                )


                for project in projects:

                    st.write(
                        f"→ {project}"
                    )


        if not project_found:

            st.info(
                "No project evidence found."
            )


        # ----------------------------------------------------
        # EXPERIENCE EVIDENCE
        # ----------------------------------------------------

        st.subheader(
            "Experience evidence"
        )


        experience_evidence = results.get(
            "experience_evidence",
            {}
        )


        experience_found = False


        for skill, experiences in experience_evidence.items():

            if experiences:

                experience_found = True

                st.markdown(
                    f"**{skill}**"
                )


                for item in experiences:

                    st.write(
                        f"→ {item}"
                    )


        if not experience_found:

            st.info(
                "No experience evidence found."
            )


    # ========================================================
    # NLP ANALYSIS TAB
    # ========================================================

    with nlp:

        st.write("")


        a, b = st.columns(
            2,
            gap="large"
        )


        # ----------------------------------------------------
        # TF-IDF
        # ----------------------------------------------------

        with a:

            st.subheader(
                "TF-IDF similarity"
            )


            score = results[
                "tfidf_similarity"
            ]


            score_float = float(
                score
            )


            st.metric(
                "Similarity",
                f"{score_float * 100:.2f}%"
            )


            st.progress(
                safe_progress_value(
                    score
                )
            )


            st.caption(
                "Lexical similarity between resume and job description."
            )


        # ----------------------------------------------------
        # SEMANTIC
        # ----------------------------------------------------

        with b:

            st.subheader(
                "Semantic similarity"
            )


            score = results[
                "semantic_similarity"
            ]


            score_float = float(
                score
            )


            st.metric(
                "Similarity",
                f"{score_float * 100:.2f}%"
            )


            st.progress(
                safe_progress_value(
                    score
                )
            )


            st.caption(
                "Meaning-level similarity using sentence embeddings."
            )


        st.divider()


        st.subheader(
            "How to read these signals"
        )


        st.info(
            "TF-IDF captures lexical overlap between the resume "
            "and job description, while semantic similarity "
            "captures meaning-level similarity. These are separate "
            "signals and should be interpreted alongside skill, "
            "role, experience and evidence analysis."
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">

        ResumeIQ · AI-powered candidate matching
        · Python · NLP · Machine Learning · Streamlit

    </div>
    """
)