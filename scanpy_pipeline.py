# RUN SCRNASEQ PREPROCESSING PIPELINE
# Need to run different parts in different conda environments

# import packages
import subprocess
import sys

def run_in_env(env_name, script_name):
    print(f"\n--- Attempting to run {script_name} in Conda environment '{env_name}' ---")
    
    # Use conda run -n <env_name> python <script_name>.py to execute
    command = ['conda', 'run', '-n', env_name, 'python', script_name]
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running in {env_name}:")
        print(e.stderr)
    except FileNotFoundError:
        print("Error: `conda` command not found. Ensure Conda is in your system's PATH.")


if __name__ == "__main__":
    # Check if the environments "env1" and "env2" exist first (optional)
    # You need to create these environments beforehand using `conda create -n env1 python=x.x pandas` etc.

    # first, generate initial QC plots, set manual filters for low quality cells
    run_in_env("scanpy", "QC_and_filtering.py")

    # Run SoupX to get rid of ambient RNA
    run_in_env("R-SoupX", "exclude_ambient_RNA.py")

    # Get rid of doublets using DoubletFinder
    run_in_env("RDoubletFinder", "exclude_dublets.py")

    # Feature (gene) selection
    run_in_env("r-scry", "select_genes.py")

    # Visualize and Cluster
    run_in_env("scanpy", "viz_and_cluster.py")

