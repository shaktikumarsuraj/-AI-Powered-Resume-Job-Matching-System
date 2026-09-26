<div align="center">

# 🚀 ResumeIQ

### AI-Powered Resume – Job Matching System

<p>
  <b>Turn resumes into actionable hiring insights using NLP, semantic similarity, skill analysis & evidence-based matching.</b>
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Sentence%20Transformers-6A5ACD?style=for-the-badge"/>
<img src="https://img.shields.io/badge/NLP-00A67E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/AI%20Matching-8A2BE2?style=for-the-badge"/>

<br><br>

<img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
<img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square"/>
<img src="https://img.shields.io/badge/Architecture-Modular-blue?style=flat-square"/>

</div>

---

# 🌟 What is ResumeIQ?

**ResumeIQ** is an AI-powered resume–job matching system designed to analyze how well a candidate's resume aligns with a given job description.

Instead of relying on a single keyword match, ResumeIQ combines multiple layers of analysis:

> 📄 Resume Parsing → 🧠 NLP → 🛠️ Skill Matching → 🎯 Role Matching → 💼 Experience Analysis → 🔎 Evidence Detection → 📊 Similarity Analysis → 📋 Final Assessment

The system produces a structured analysis of the candidate's profile against the requirements of a job.

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 📄 **PDF Resume Extraction** | Extracts text directly from PDF resumes |
| 🧹 **Text Preprocessing** | Cleans and normalizes extracted resume text |
| 🧩 **Resume Section Parsing** | Identifies skills, experience, projects and other sections |
| 🛠️ **Skill Extraction** | Detects technical skills from resumes and job descriptions |
| 🎯 **Role Detection** | Identifies the target job role |
| 🔄 **Role Normalization** | Maps related role names into normalized roles |
| ⭐ **Priority Detection** | Identifies required and preferred skills |
| 💼 **Experience Matching** | Compares required experience against resume evidence |
| 📅 **Experience Duration Analysis** | Estimates relevant experience duration |
| 🔎 **Skill Evidence** | Finds evidence supporting claimed skills |
| 🚀 **Project Evidence** | Connects projects with required skills |
| 👨‍💻 **Experience Evidence** | Connects professional experience with skills |
| 📐 **TF-IDF Similarity** | Calculates lexical similarity |
| 🧠 **Semantic Similarity** | Uses Sentence Transformers for semantic matching |
| 📊 **Category Analysis** | Performs category-wise skill matching |
| 🧾 **Final Assessment** | Generates structured candidate assessment |
| 💡 **Matching Insights** | Produces human-readable insights |
| 🎨 **Interactive Dashboard** | Streamlit-based visual interface |

---

# 🧠 How ResumeIQ Works

```text
                    ┌──────────────────────┐
                    │     JOB INPUT        │
                    │  Natural Language JD │
                    │  / Structured Input  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  JD PROCESSING       │
                    │                      │
                    │ Role Detection       │
                    │ Skill Extraction     │
                    │ Priority Detection  │
                    │ Experience Parsing   │
                    └──────────┬───────────┘
                               │
                               │
┌──────────────────┐           │
│   RESUME PDF     │           │
└────────┬─────────┘           │
         │                     │
         ▼                     │
┌──────────────────┐           │
│ PDF TEXT         │           │
│ EXTRACTION       │           │
└────────┬─────────┘           │
         ▼                     │
┌──────────────────┐           │
│ PREPROCESSING    │           │
└────────┬─────────┘           │
         ▼                     │
┌──────────────────┐           │
│ SECTION PARSER   │           │
└────────┬─────────┘           │
         ▼                     │
┌──────────────────┐           │
│ SKILL EXTRACTION │◄──────────┘
└────────┬─────────┘
         │
         ▼
┌────────────────────────────────┐
│       MATCHING ENGINE          │
│                                │
│  🎯 Role Matching              │
│  🛠️ Skill Matching             │
│  ⭐ Priority Analysis          │
│  💼 Experience Analysis        │
│  📊 Category Analysis          │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│        EVIDENCE ENGINE         │
│                                │
│  🔎 Skill Evidence             │
│  🚀 Project Evidence           │
│  👨‍💻 Experience Evidence       │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│       SIMILARITY ENGINE        │
│                                │
│  📐 TF-IDF                     │
│  🧠 Sentence Transformers      │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│      FINAL ASSESSMENT           │
│                                │
│  Role Status                   │
│  Required Skills               │
│  Preferred Skills              │
│  Experience Status             │
│  Evidence Availability         │
│  Similarity Scores             │
└───────────────┬────────────────┘
                │
                ▼
        ┌─────────────────┐
        │ 🎨 STREAMLIT UI │
        │                 │
        │ Dashboard       │
        │ Insights        │
        │ Skill Analysis  │
        │ Evidence        │
        └─────────────────┘
