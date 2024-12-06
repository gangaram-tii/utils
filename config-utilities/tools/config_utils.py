import os
import requests
from bs4 import BeautifulSoup

def config_setting(line):
    if line.strip()[0] == '#':
        return "NOT_SET"
    else:
        return [1]

def config_file_as_dict(file_path):
    """Reads a config file and returns a dictionary of CONFIG_ entries, including comments."""
    config_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines
            if not line:
                continue

            # Check if the line contains CONFIG_ (whether commented or not)
            if 'CONFIG_' in line:
                if line.startswith('#'):
                    # It's a commented CONFIG_ line, so we remove the # and save it
                    config_name = line.lstrip('#').strip().split(' ')[0]
                    config_name = config_name.split('=')[0].strip()
                    config_dict[config_name] = f"DEFAULT"
                else:
                    # It's an active CONFIG_ line
                    sline = line.strip().split('=')
                    config_name = sline[0].strip()
                    config_dict[config_name] = sline[1]

    return config_dict

def linux_config_description(config_name, mdformat=False):
    """
    Fetches the description of a given kernel config from cateee.net.
    """
    conf=config_name.replace("CONFIG_", "")
    # URL for cateee.net that holds the kernel config descriptions
    cateee_url = f"https://cateee.net/lkddb/web-lkddb/{conf}.html"
    #cateee_url = f"https://www.kernelconfig.io/{config_name}"

    try:
        # Sending the HTTP request to cateee.net for the kernel config description
        response = requests.get(cateee_url)
        response.raise_for_status()  # Check if the request was successful
        #print(response.text)
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(response.text)
        # Search for the description in the page content
        headings = ['h1', 'h2', 'h3', 'h4']
        for heading in headings:
            help_text = soup.find(heading, string="Help text")
            if help_text != None:
                break
        if help_text:
            p_tag = help_text.find_next('p')
            if p_tag:
                description = p_tag.get_text()
                if mdformat:
                  description = description.replace('\n', " <br /> ")
                return description
            else:
                return "Not Available"
        else:
            return "No 'Help text' found"

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching kernel config description: {e}")
        return ""
