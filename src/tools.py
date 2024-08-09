from crewai_tools import CodeDocsSearchTool
import requests

codeSearchTool = CodeDocsSearchTool(
    docs_url="https://book.clarity-lang.org/ch04-00-storing-data.html" + 
             "https://book.clarity-lang.org/ch05-00-functions.html" + 
             "https://book.clarity-lang.org/ch03-00-keywords.html" + 
             "https://book.clarity-lang.org/ch02-00-types.html",
)

functionSearchTool = CodeDocsSearchTool(
    docs_url="https://book.clarity-lang.org/ch05-00-functions.html" +
             "https://book.clarity-lang.org/ch05-01-public-functions.html" +
             "https://book.clarity-lang.org/ch05-02-private-functions.html",
)

# updateableTool = CodeDocsSearchTool(
#     docs_url="https://book.clarity-lang.org/ch05-00-functions.html" +
#              "https://book.clarity-lang.org/ch05-01-public-functions.html" +
#              "https://book.clarity-lang.org/ch05-02-private-functions.html",
#             chunk_size=1000,
#             min_chunk_size=100,  
#             chunk_overlap=50
# )

def fetch_contract_source(contract_id, contract_name):
    base_url = "https://api.hiro.so/v2/contracts/source"
    url = f"{base_url}/{contract_id}/{contract_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("source")
    else:
        return f"Error: {response.status_code} - {response.text}"
