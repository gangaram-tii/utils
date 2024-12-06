import sys
from config_utils import linux_config_description


def CreateMDTable(configs):
    markdown_table = "| Config Name | Description |  |  |\n|-------------|-------------|--|--|\n"
    for conf in configs:
        desc = linux_config_description(conf)
        markdown_table = markdown_table + f"| {conf} | {desc} |  |  |\n"
    return markdown_table

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 get_config_description.py <CONFIG_NAME>")
        sys.exit(1)

    config_name = sys.argv[1]
    description = linux_config_description(config_name)
    print(description)
    '''
    configs = ["CONFIG_MEMTEST", "CONFIG_BUG" ]
    mdt = CreateMDTable(configs)
    with open("example.md", "w") as file:
        file.write(mdt)
    '''
if __name__ == "__main__":
    main()
