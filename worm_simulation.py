import os
import shutil

def replicate():
    # Path to the current script
    script_path = os.path.abspath(__file__)

    # Directory for the "infection"
    target_dir = os.path.expanduser("~/worm_simulation")

    # Create the directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create multiple copies of the script
    for i in range(5):  # Adjust the number of copies
        copy_path = os.path.join(target_dir, f"worm_copy_{i}.py")
        shutil.copyfile(script_path, copy_path)

    print(f"Simulated worm created copies in {target_dir}")

if __name__ == "__main__":
    print("Running a harmless worm simulation...")
    replicate()
