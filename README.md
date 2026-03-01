# 🔍 Jobright Pipeline — Scraper + Dashboard

A fully automated job scraping, enrichment, and analytics pipeline built for [Jobright.ai](https://jobright.ai). Scrape hundreds of job listings, canonicalize fields (branch/major, role, seniority), and explore results through an interactive Streamlit dashboard.

---

## 📁 Project Structure

```
jobright-pipeline/
│
├── pipelinescrapper_mod.py                        # Core scraper (Playwright-based)
├── pipelinescrapper_mod_with_branch_canonical.py  # Enrichment wrapper (canonical mapping)
├── gui_runner_with_branch_canonical_INTEGRATED.py # Tkinter GUI launcher
├── dashboard_app_with_branch_canonical_INTEGRATED.py # Streamlit dashboard (2 tabs)
├── setup_and_run.py                               # One-click env setup script
│
├── canonical_majors_custom_full.xlsx              # Canonical majors reference list
├── jobright_jobs.xlsx                             # Output: scraped + enriched jobs
├── branch_salary_dashboard_ready.xlsx             # Output: branch salary summary
├── branch_salary_dashboard_ready__seniority.xlsx  # Output: seniority salary summary
│
├── state.json                                     # Scraper resume state
├── jobs_raw.jsonl                                 # Raw scraped job data
├── container_dom_MERGED.html                      # DOM snapshot (debug)
│
└── README.md
```

---

## ⚙️ Requirements

- Python 3.9+
- Google Chrome (for Playwright)
- Internet connection (to access Jobright.ai)

Dependencies installed automatically by `setup_and_run.py`:
```
playwright, beautifulsoup4, openpyxl, pandas, streamlit, plotly
```

---

## 🚀 Quick Start

### Step 1 — Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/jobright-pipeline.git
cd jobright-pipeline
```

### Step 2 — Run setup (creates virtualenv + installs all dependencies)
```bash
python setup_and_run.py
```

### Step 3 — Launch the GUI
```bash
# Windows
.venv\Scripts\python.exe gui_runner_with_branch_canonical_INTEGRATED.py

# macOS / Linux
.venv/bin/python gui_runner_with_branch_canonical_INTEGRATED.py
```

Or use the shortcut:
```bash
python setup_and_run.py gui
```

### Step 4 — Scrape Jobs
1. Select how many jobs to scrape (50–300 or Manual).
2. Click **Start Scraping** — a browser window opens.
3. **Log in** to Jobright.ai in that browser.
4. Return to the GUI and click **Continue after login**.
5. The scraper runs and saves results to `jobright_jobs.xlsx`.

### Step 5 — Open the Dashboard
Click **Open Integrated Dashboard** in the GUI, or run directly:
```bash
.venv/bin/python -m streamlit run dashboard_app_with_branch_canonical_INTEGRATED.py
```

---

## 📊 Dashboard Overview

### Tab 1 — Main Dashboard
- Filter by role, work model, degree level, seniority, branch/major
- View job counts, salary ranges, and a configurable multi-axis chart

### Tab 2 — Branch Salary Summary
- Generate a summary Excel with salary breakdowns by branch/major
- Interactive charts for comparing compensation across fields

---

## 🧠 Canonical Mapping System

The enrichment pipeline maps free-text job fields into standardized buckets:

| Field | Example Raw Value | Canonical Output |
|---|---|---|
| `branch` | "info sys", "MIS", "CIS" | `information systems` |
| `role_name` | "Sr. Security Analyst" | `security analyst` |
| `seniority` | "Senior", "Sr." | `senior` |

Canonical majors are loaded from `canonical_majors_custom_full.xlsx` (sheet: `canonical_list_only`). You can edit this file to add or modify mappings without changing any code.

Mapping strategy (in order):
1. Custom alias rules (hardcoded common variants)
2. Exact match against canonical list
3. Fuzzy match via `difflib`

---

## 📂 Output Files

| File | Description |
|---|---|
| `jobright_jobs.xlsx` | All scraped jobs with canonical columns added |
| `branch_salary_dashboard_ready.xlsx` | Salary summary grouped by branch/major |
| `branch_salary_dashboard_ready__seniority.xlsx` | Salary summary grouped by seniority level |
| `jobs_raw.jsonl` | Raw JSON lines from scraper (before enrichment) |
| `state.json` | Scraper resume checkpoint (target, saved count, scroll position) |

---

## 🔧 Customization

### Change canonical majors
Edit `canonical_majors_custom_full.xlsx` → sheet `canonical_list_only` → column `canonical`.

### Add role patterns
Open `pipelinescrapper_mod_with_branch_canonical.py` and edit the `ROLE_PATTERNS` dictionary.

### Add seniority patterns
Edit the `SENIORITY_PATTERNS` dictionary in the same file.

---

## ⚠️ Notes & Limitations

- Jobright.ai requires a **free account** to access job listings.
- Scraping speed depends on network and Jobright's rate limits.
- `state.json` acts as a **resume checkpoint** — if the scraper is interrupted, it can pick up where it left off.
- The `container_dom_MERGED.html` file is a debug snapshot and is not required for normal operation.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙋 Author

Built by **Sunil Kumar Peela**  
📧 sunilkumarryo@gmail.com | [LinkedIn](https://linkedin.com/in/sunilkumarpeela) | [GitHub](https://github.com/SunilKumarPeela)
