import requests
from bs4 import BeautifulSoup
import sys

def get_kernel_config_description(config_name):
    """
    Fetches the description of a given kernel config from cateee.net.
    """
    conf=config_name.strip("CONFIG_")
    # URL for cateee.net that holds the kernel config descriptions
    cateee_url = f"https://cateee.net/lkddb/web-lkddb/{conf}.html"

    try:
        # Sending the HTTP request to cateee.net for the kernel config description
        response = requests.get(cateee_url)
        response.raise_for_status()  # Check if the request was successful
        print(response)
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the description in the page content
        description_div = soup.find('div', {'class': 'Help text'})

        if description_div:
            print(f"Description for {config_name}:")
            print(description_div.text.strip())  # Print the description of the config
        else:
            print(f"No description found for {config_name}. It might not be available on cateee.net.")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching kernel config description: {e}")
        return


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 get_config_description.py <CONFIG_NAME>")
        sys.exit(1)
    
    config_name = sys.argv[1]
    get_kernel_config_description(config_name)


if __name__ == "__main__":
    main()

