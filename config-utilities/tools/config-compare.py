import argparse
import os
from config_utils import config_file_as_dict

def compare_configs(file1, file2):
    """Compares two kernel config files and prints differences, considering commented lines."""
    # Read the configuration from both files

    file1conf = config_file_as_dict(file1)
    file2conf = config_file_as_dict(file2)

    if len(file1conf) > len(file2conf):
        config1 = file2conf
        config2 = file1conf
        fname1=os.path.basename(file2)
        fname2=os.path.basename(file1)
    else:
        config1 = file1conf
        config2 = file2conf
        fname1=os.path.basename(file1)
        fname2=os.path.basename(file2)

    index = 0
    # Iterate through each configuration in the first file
    for config_name, line1 in config1.items():
        index = index + 1
        print(f"{index}. [{fname1}]: {line1}")  # Print the line from file1

        # Check if the same configuration is present in file2 (either active or commented)
        if config_name in config2:
            print(f"  [{fname2}]: {config2[config_name]}\n")  # Print the line from file2
        else:
            print(f"  [{fname2}]: {config_name}: NOT SET\n")  # If not found in file2
def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Compare two kernel config files.")
    parser.add_argument('file1', help="Path to the first kernel config file")
    parser.add_argument('file2', help="Path to the second kernel config file")

    # Parse the arguments
    args = parser.parse_args()

    # Run the comparison
    compare_configs(args.file1, args.file2)

if __name__ == "__main__":
    main()
