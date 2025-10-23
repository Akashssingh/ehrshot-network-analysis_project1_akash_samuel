import os
import sys
import subprocess
import venv
import tempfile
import shutil
import ensurepip

def create_temp_venv():
    """Create a temporary isolated virtual environment."""
    print("Creating temporary Python virtual environment...")
    temp_dir = tempfile.mkdtemp(prefix="ehrshot_env_")
    venv_dir = os.path.join(temp_dir, "venv")
    venv.create(venv_dir, with_pip=True)
    print(f"Virtual environment created at: {venv_dir}")
    return venv_dir, temp_dir

def install_dependencies(python_exec, req_path):
    """Install all dependencies in the temp environment."""
    print("Installing dependencies...")
    # Ensure pip exists and is upgraded
    subprocess.run([python_exec, "-m", "ensurepip"], check=True)
    subprocess.run([python_exec, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([python_exec, "-m", "pip", "install", "-r", req_path], check=True)
    print("Dependencies installed successfully.")

def run_main_script(python_exec):
    """Run the main analysis program."""
    print("\nRunning EHRShot Network Analysis (main.py)...\n")
    src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "main.py")
    subprocess.run([python_exec, src_path], check=True)
    print("\nAnalysis completed successfully! Figures saved under ./figures\n")

def cleanup(temp_dir):
    """Remove the temporary environment."""
    try:
        shutil.rmtree(temp_dir)
        print(f"Cleaned up temporary environment: {temp_dir}")
    except Exception as e:
        print(f"Could not delete temp directory ({e})")

def main():
    print("\nStarting setup and execution...\n")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    req_path = os.path.join(root_dir, "requirements.txt")

    # Verify requirements file exists
    if not os.path.exists(req_path):
        print(f"ERROR: Missing requirements.txt in {root_dir}")
        sys.exit(1)

    # Create temporary virtual environment
    venv_dir, temp_dir = create_temp_venv()

    # Find Python executable inside the new venv
    python_exec = os.path.join(
        venv_dir,
        "Scripts" if os.name == "nt" else "bin",
        "python.exe" if os.name == "nt" else "python"
    )

    try:
        install_dependencies(python_exec, req_path)
        run_main_script(python_exec)
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Subprocess failed (exit code {e.returncode})")
    except Exception as e:
        print(f"\nERROR: Unexpected error: {e}")
    finally:
        cleanup(temp_dir)

if __name__ == "__main__":
    main()