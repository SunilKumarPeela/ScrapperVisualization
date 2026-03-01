JOBRIGHT - FINAL INTEGRATED (ONLY)

Files:
- pipelinescrapper_mod.py
- pipelinescrapper_mod_with_branch_canonical.py
- canonical_majors_custom_full.xlsx
- setup_and_run.py
- jobright_jobs.xlsx
- gui_runner_with_branch_canonical_INTEGRATED.py   (GUI)
- dashboard_app_with_branch_canonical_INTEGRATED.py (Streamlit: Main + Branch Summary)

How to run (recommended):
1) Setup env + install deps + playwright browser:
   python setup_and_run.py

2) Start GUI (scrape + open dashboard):
   python gui_runner_with_branch_canonical_INTEGRATED.py

Inside the dashboard:
- Tab 1: Main Dashboard (filters + branch metrics + multi-X chart)
- Tab 2: Branch Salary Summary (Generate summary excel + charts)

If you want to run dashboard directly:
   streamlit run dashboard_app_with_branch_canonical_INTEGRATED.py
