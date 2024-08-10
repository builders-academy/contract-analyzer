import sys
import time
sys.modules['sqlite3'] = __import__('pysqlite3')

import streamlit as st
from crewai import Crew, Process
from agents import SmartContractAnalysisAgents
from tasks import SmartContractAnalysisTasks
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import requests

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

def fetch_contract_source(contract_id, contract_name):
    url = f"https://api.hiro.so/v2/contracts/source/{contract_id}/{contract_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("source")
    else:
        return f"Error: {response.status_code} - {response.text}"

def fetch_function(contract_id, contract_name):
    url = f"https://api.hiro.so/v2/contracts/interface/{contract_id}/{contract_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  
        return data.get("functions")
    else:
        return f"Error: {response.status_code} - {response.text}"

def create_smart_contract_analysis_crew(contract_code, contract_functions):
    agents = SmartContractAnalysisAgents()
    tasks = SmartContractAnalysisTasks()

    contract_summarizer = agents.contract_summarizer_agent()
    function_analyzer = agents.function_analyzer_agent()
    diagram_creator = agents.diagram_creator_agent()
    updateability_analyzer = agents.update_analyzer_agent()
    security_analyzer = agents.security_analyzer_agent()
    report_compiler = agents.report_compiler_agent()

    task1 = tasks.summarize_task(contract_summarizer, contract_code)
    task2 = tasks.analyze_task(function_analyzer,  contract_functions)
    task3 = tasks.diagram_task(diagram_creator,  contract_functions)
    task4 = tasks.updateable_task(updateability_analyzer,  contract_functions)
    task5 = tasks.security_task(security_analyzer,  contract_functions)
    task6 = tasks.compiler_task(report_compiler)

    crew = Crew(
        agents=[contract_summarizer, function_analyzer, updateability_analyzer, report_compiler],
        tasks=[task1, task2, task4, task3, task5, task6],
        process=Process.sequential,
        memory=True
    )

    return crew

def main():
    st.set_page_config(page_title="Smart Contract Analyzer", page_icon="🔍", layout="wide")
    
    st.title("Smart Contract Analyzer 🧠")
    st.markdown("Analyze Stacks smart contracts with ease using AI-powered insights.")

    with st.form("analysis_form"):
        contract_id = st.text_input("Contract ID", help="Enter the unique identifier for the contract", placeholder="e.g. SP000000000000000000002Q6VF78.pox")
        contract_name = st.text_input("Contract Name", help="Enter the name of the contract")
        submitted = st.form_submit_button("Analyze Contract")

    if submitted and contract_id and contract_name:
        with st.spinner("Fetching contract data..."):
            contract_code = fetch_contract_source(contract_id, contract_name)
            contract_functions = fetch_function(contract_id, contract_name)
        
        if isinstance(contract_code, str) and contract_code.startswith("Error"):
            st.error(f"Failed to fetch contract code: {contract_code}")
        elif isinstance(contract_functions, str) and contract_functions.startswith("Error"):
            st.error(f"Failed to fetch contract functions: {contract_functions}")
        else:
            with st.expander("View Contract Code"):
                st.code(contract_code)
                st.subheader("Contract Functions")
                st.code(str(contract_functions))

            st.header("Analysis Results")
            try:
                crew = create_smart_contract_analysis_crew(contract_code, contract_functions)
                
                progress_bar = st.progress(0)
                
                with st.spinner("Analyzing..."):
                    result = crew.kickoff()
                    for i in range(100):
                        time.sleep(0.05)  
                        progress_bar.progress(i + 1)
                
                st.success("Analysis complete!")

                result_str = str(result)
                st.markdown(result_str)

                st.download_button(
                    label="Download Analysis Report (Text)",
                    data=result_str,
                    file_name="smart_contract_analysis.txt",
                    mime="text/plain",
                )

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please check your inputs and try again.")
    else:
        st.info("Enter Contract ID and Contract Name, then click 'Analyze Contract' to see results.")

if __name__ == "__main__":
    main()