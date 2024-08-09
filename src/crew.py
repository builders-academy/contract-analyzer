__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')



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

def create_smart_contract_analysis_crew(contract_code):
    agents = SmartContractAnalysisAgents()
    tasks = SmartContractAnalysisTasks()

    contract_summarizer = agents.contract_summarizer_agent()
    function_analyzer = agents.function_analyzer_agent()
    diagram_creator = agents.diagram_creator_agent()
    updateability_analyzer = agents.update_analyzer_agent()
    security_analyzer = agents.security_analyzer_agent()
    report_compiler = agents.report_compiler_agent()

    task1 = tasks.summarize_task(contract_summarizer, contract_code)
    task2 = tasks.analyze_task(function_analyzer, contract_code)
    task3 = tasks.diagram_task(diagram_creator, contract_code)
    task4 = tasks.updateable_task(updateability_analyzer)
    task5 = tasks.security_task(security_analyzer)
    task6 = tasks.compiler_task(report_compiler, contract_code )

    crew = Crew(
        agents=[contract_summarizer, function_analyzer, updateability_analyzer, report_compiler],
        tasks=[task1, task2, task4, task3, task5, task6],
        process=Process.sequential,
        memory=True
    )

    return crew



def main():
    st.title("Smart Contract Analysis")

    contract_id = st.text_input("Enter Contract ID")
    contract_name = st.text_input("Enter Contract Name")

    if st.button("Analyze"):
        if contract_id and contract_name:
            with st.spinner("Fetching contract code..."):
                contract_code = fetch_contract_source(contract_id, contract_name)
        
            if contract_code.startswith("Error"):
                st.error(f"Failed to fetch contract code: {contract_code}")
            else:
                st.success("Contract code retrived successfully!")
                st.code(contract_code[:100] + "..." if len(contract_code) > 100 else contract_code)
                crew = create_smart_contract_analysis_crew(contract_code)
                with st.spinner("Analyzing..."):
                    result = crew.kickoff()
                    st.success("Analysis complete!")
                    st.markdown(result)
        else:
            st.error("Please enter both Contract ID and Contract Name.")

if __name__ == "__main__":
    main()