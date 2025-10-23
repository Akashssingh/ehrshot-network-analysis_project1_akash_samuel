import os

# Automatically detect the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The default EHRShot folder (if user downloaded it into ./data/)
DEFAULT_EHRSHOT_DIR = os.path.join(BASE_DIR, "data", "EHRShot_sampled_2000patients")

# User may override the EHRShot directory via an environment variable
# Run export EHRSHOT_DATA_DIR=/path/to/EHRShot_sampled_2000patients to override
# User must have downloaded EHRShot_sampled_2000patients
EHRSHOT_DIR = os.getenv("EHRSHOT_DATA_DIR", DEFAULT_EHRSHOT_DIR)

# Expected required files inside EHRShot directory
DIAG_FILE = "sampled_condition_occurrence.csv"
CONCEPT_FILE = "concept.csv"

# Full absolute paths
DIAG_PATH = os.path.join(EHRSHOT_DIR, DIAG_FILE)
CONCEPT_PATH = os.path.join(EHRSHOT_DIR, CONCEPT_FILE)

# Output directory for figures
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# Analysis parameters
MIN_DIAG_COUNT = 20
TOP_N_DIAG = 2000
EDGE_MIN_WEIGHT = 3


def verify_data_files():
    """Ensure both required data files exist inside the EHRShot folder."""
    missing = []
    for f in [DIAG_PATH, CONCEPT_PATH]:
        if not os.path.exists(f):
            missing.append(f)

    if missing:
        print("\nERROR: Required EHRShot data files not found!\n")
        print("Expected the following files inside your EHRShot dataset folder:")
        print(f"  • {DIAG_FILE}")
        print(f"  • {CONCEPT_FILE}\n")
        print("The program looked for them here:")
        print(f"  {EHRSHOT_DIR}\n")
        print("To fix this:")
        print("Download or locate your 'EHRShot_sampled_2000patients' directory.")
        print("Place it under:")
        print(f"  {os.path.join(BASE_DIR, 'data')}")
        print("   — OR —")
        print("Set an environment variable to point to it:")
        print("   Linux/macOS:")
        print("       export EHRSHOT_DATA_DIR=/path/to/EHRShot_sampled_2000patients")
        print("   Windows PowerShell:")
        print('       setx EHRSHOT_DATA_DIR "D:\\Path\\EHRShot_sampled_2000patients"')
        print("\nThen re-run:")
        print("   python run.py\n")
        raise FileNotFoundError("Missing required data files in EHRShot directory.")

    print(f"Found EHRShot dataset: {EHRSHOT_DIR}")
    print(f"Using:\n     - {DIAG_FILE}\n     - {CONCEPT_FILE}\n")