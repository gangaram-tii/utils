import argparse
import os
from config_utils import config_file_as_dict, linux_config_description

def generate_md_table(base, target):
    markdown_table = f"| Config Name | Description | {os.path.basename(base)}  | {os.path.basename(target)} |\n|---|---|---|---|\n"
    baseconf = config_file_as_dict(base)
    targetconf = config_file_as_dict(target)

    for conf, setting in baseconf.items():
        desc = linux_config_description(conf, True)
        if conf in targetconf:
            targetsetting = targetconf[conf]
        else:
            targetsetting = "NOT AVAILABLE!"
        markdown_table = markdown_table + f"| {conf} | {desc} | {setting}  | {targetsetting} |\n"
    return markdown_table

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Compare two kernel config files.")
    parser.add_argument('basefile', help="Path to the first kernel config file")
    parser.add_argument('targetfile', help="Path to the second kernel config file")

    # Parse the arguments
    args = parser.parse_args()

    # Run the comparison
    mdt = generate_md_table(args.basefile, args.targetfile)
    with open("configs.md", "w") as file:
        file.write(mdt)

if __name__ == "__main__":
    main()
