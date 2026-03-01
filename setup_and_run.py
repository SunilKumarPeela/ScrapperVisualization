import os
import sys
import subprocess
from pathlib import Path

VENV_DIR = Path(".venv")

REQUIRED_PACKAGES = [
    "playwright",
    "beautifulsoup4",
    "openpyxl",
    "pandas",
    "streamlit",
    "plotly",
]


def is_windows() -> bool:
    return os.name == "nt"


def venv_python_path() -> Path:
    if is_windows():
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def run(cmd, *, check=True):
    """Run a command and stream output live."""
    print(f"\n➡️  Running: {' '.join(map(str, cmd))}\n")
    subprocess.run(list(map(str, cmd)), check=check)


def ensure_venv():
    if VENV_DIR.exists() and venv_python_path().exists():
        print("✅ Virtual environment already exists.")
        return

    print("🛠 Creating virtual environment: .venv")
    run([sys.executable, "-m", "venv", str(VENV_DIR)])


def pip_install():
    py = venv_python_path()
    if not py.exists():
        raise FileNotFoundError("Venv python not found. .venv creation failed.")

    # Upgrade pip inside venv
    run([py, "-m", "pip", "install", "--upgrade", "pip"])

    # Install packages inside venv
    run([py, "-m", "pip", "install", *REQUIRED_PACKAGES])


def install_playwright_browsers():
    py = venv_python_path()
    # Install browsers (chromium is usually enough; change to `install` for all)
    run([py, "-m", "playwright", "install", "chromium"])


def run_gui():
    py = venv_python_path()
    script = Path("gui_runner_with_branch_canonical.py")
    if not script.exists():
        raise FileNotFoundError(f"Missing file: {script}")
    run([py, str(script)])


def run_dashboard():
    py = venv_python_path()
    app = Path("dashboard_app_with_branch_canonical.py")
    if not app.exists():
        raise FileNotFoundError(f"Missing file: {app}")

    # Run Streamlit using venv python -m streamlit (works without activation)
    run([py, "-m", "streamlit", "run", str(app)])


def main():
    # Detect environment info (helpful for debugging)
    print("🧭 Environment detection")
    print(f"   OS: {sys.platform}")
    print(f"   Python: {sys.executable}")
    print(f"   Working dir: {Path.cwd()}")

    ensure_venv()
    pip_install()
    install_playwright_browsers()

    # Optional: run something after setup
    choice = (sys.argv[1].lower().strip() if len(sys.argv) > 1 else "")
    if choice in ("gui", "g"):
        run_gui()
    elif choice in ("dash", "dashboard", "d"):
        run_dashboard()
    else:
        print("\n✅ Setup complete.")
        print("Next steps (choose one):")
        print("  - Run GUI:       python setup_and_run.py gui")
        print("  - Run Dashboard: python setup_and_run.py dash")
        print("\nOr manually run:")
        if is_windows():
            print(r"  .venv\Scripts\python.exe gui_runner_with_branch_canonical.py")
            print(r"  .venv\Scripts\python.exe -m streamlit run dashboard_app_with_branch_canonical.py")
        else:
            print(r"  .venv/bin/python gui_runner_with_branch_canonical.py")
            print(r"  .venv/bin/python -m streamlit run dashboard_app_with_branch_canonical.py")


if __name__ == "__main__":
    main()
