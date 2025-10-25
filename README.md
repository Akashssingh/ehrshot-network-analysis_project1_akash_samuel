**CAI5155.001F25 - Network Analysis and ML**

**Project 1**

**Authors - Akash Singh & Samuel Infante Trillos**

**Requirement - Must have the latest Python installed on your device! 3.12.12 is the latest from the date of the latest update on this repo**

Since the data may contain sensitive patient information, it is not shared on the GitHub repository. It is assumed that the user has downloaded the EHRShot_sampled_2000patients data.

It is highly recommended not to change the names of the files unzipped from the downloaded EHRShot data.

In the root directory, you should have a src folder and a data folder containing the EHRShot_sampled_2000patients repository. The cloned repo does not come with a data folder.

The config.py script figures out the directory path issues, but the names of the files must be as expected. 

Data stored in -> data/EHRShot_sampled_2000patients/

EHRShot_sampled_2000patients directory must have 
     - sampled_condition_occurrence.csv
     - concept.csv

If you do not want to download or relocate data, then you may manually direct the path to your data directory containing the CSV files (respective CSV file names must be the same as required by the program) by using the commands below. 

Unix-based systems, Linux, or macOS
```bash
export EHRSHOT_DATA_DIR=/path/to/your/EHRShot_sampled_2000patients 
```

Windows
```powershell
$env:EHRSHOT_DATA_DIR = "C:\path\to\EHRShot_sampled_2000patients"

To confirm the path was set
echo $env:EHRSHOT_DATA_DIR
```

However, it is highly recommended to align your data to the cloned repo. Downloaded repo is the root directory, relocate your data folder as data/EHRShot_sampled_2000patients in it. If after setting environment variable using above command, the program runs and gives an error, then you must set a data folder in the cloned repo, and in that data folder, copy and paste the EHRShot_sampled_2000patients folder.

Clone the repository and run the pipeline with a **single command**:

The commands below are for Unix-based systems and should work on Linux/MacOS. Windows users should run the run.py using the IDE run functionality or use the respective Windows CLI commands for running this script in your IDE terminal. Use a bash or a zsh terminal in an IDE (recommended). 

```bash
git clone https://github.com/Akashssingh/ehrshot-network-analysis_project1_akash_samuel.git
cd ehrshot-network-analysis_project1_akash_samuel
python3 run.py
```

The run.py takes care of installing any necessary dependencies required to run this project. It will create a temporary Python venv and run it automatically for you; it will also delete it once the process is finished executing. After running the command, you will see the making and processing of the graph and other data processing. Figures will be saved in the figures directory (do not need to create), and tables will be displayed in the integrated terminal where the script is run.
