import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.tools import Tool
from langchain.schema import Document


def fetch_and_parse_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the main content section
    article = soup.select_one('section#article article')
    if not article:
        return ""

    # Extract the title
    title = article.find('h2')
    title_text = title.text if title else ""

    # Remove code blocks and buttons
    for element in article.select('.code, .buttons'):
        element.decompose()

    # Extract the main text content
    content = article.get_text(separator='\n', strip=True)

    # Combine title and content
    full_content = f"{title_text}\n\n{content}"

    return full_content

def create_vector_store(urls, chunk_size=1000, chunk_overlap=200):
    documents = []
    for url in urls:
        content = fetch_and_parse_content(url)
        documents.append(Document(page_content=content, metadata={"source": url}))
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    splits = text_splitter.split_documents(documents)
    
    return Chroma.from_documents(splits, OpenAIEmbeddings())


# Create vector stores for different types of documentation
code_vector_store = create_vector_store([
    "https://book.clarity-lang.org/ch04-00-storing-data.html",
    "https://book.clarity-lang.org/ch05-00-functions.html",
    "https://book.clarity-lang.org/ch03-00-keywords.html",
    "https://book.clarity-lang.org/ch02-00-types.html"
])

function_vector_store = create_vector_store([
    "https://book.clarity-lang.org/ch05-00-functions.html",
    "https://book.clarity-lang.org/ch05-01-public-functions.html",
    "https://book.clarity-lang.org/ch05-02-private-functions.html"
    "https://book.clarity-lang.org/ch05-03-read-only-functions.html"
])



# Create tools using the vector stores
def create_search_tool(vector_store, name, description):
    def search_func(query: str):
        results = vector_store.similarity_search(query, k=3)
        return "\n\n".join(f"From {doc.metadata['source']}:\n{doc.page_content}" for doc in results)

    return Tool(
        name=name,
        func=search_func,
        description=description
    )

code_search_tool = create_search_tool(
    code_vector_store,
    "Code Search",
    "Search for information about Clarity language syntax, types, and general concepts."
)

function_search_tool = create_search_tool(
    function_vector_store,
    "Function Search",
    "Search for specific information about functions in Clarity language."
)