from crewai_tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def get_contract(url: str) -> str:
    """
    Retrieve the source code and available functions of a smart contract from the provided URL.
    
    Args:
        url (str): The URL of the smart contract page.
    
    Returns:
        str: The source code and available functions of the smart contract.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example of scraping logic (update selectors based on actual HTML structure)
    source_code = soup.find('pre', {'class': 'contract-source'}).text
    functions = soup.find_all('div', {'class': 'function-name'})
    function_names = [function.text for function in functions]

    return {
        'source_code': source_code,
        'functions': function_names
    }
