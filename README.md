**CAI5155.001F25 - Network Analysis and ML**

**Project 1**

**Authors - Akash Singh & Samuel Infante Trillos**

**Requirement - Must have latest python installed in your device! 3.12.12 is latest from the date of latest update on this repo**

Since the data may contain sensitive patient information, it is not shared on github repository. It is taken as granted that the user has downloaded the EHRShot_sampled_2000patients data.

It is highly recommended to not change the names of the files unziped from downloaded EHRShot data

In the root directory, you should have src folder and a data folder containing EHRShot_sampled_2000patients repository. Cloned repo do not come with data folder.

The congif.py script figures out the directory path issues but the names of the files must be as expected. 

Data stored in -> data/EHRShot_sampled_2000patients/
EHRShot_sampled_2000patients directory must have 
     - sampled_condition_occurrence.csv
     - concept.csv

If you do not want to download or relocate data then you may manually direct the path to your root directory containing the csv files by below command. 

```bash
export EHRSHOT_DATA_DIR=/path/to/your/EHRShot_sampled_2000patients 
```

However, it is highly recommended to align your data to the cloned repo. Downloaded repo is the root directory, make relocate data as data/EHRShot_sampled_2000patients in it.
Clone the repository and run the pipeline with a **single command**:

```bash
cd ehrshot-network-analysis_project1_akash_samuel
python3 run.py
```

The run.py takes care of installing any necessary dependencies required to run this project. It will create a temprorary python venv and run it automatically for you, it will also delete is once the process is finished executing. After runnign the command, you will see making and processing of graph and other data processing. Figures will be saved in figures directory (do not need to create) and tables will be displayed in the integrated terminal where the script is ran.