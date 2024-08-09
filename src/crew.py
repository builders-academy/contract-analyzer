import streamlit as st
from crewai import Crew, Process
from agents import SmartContractAnalysisAgents
from tasks import SmartContractAnalysisTasks
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

def create_smart_contract_analysis_crew(contract_code):
    agents = SmartContractAnalysisAgents()
    tasks = SmartContractAnalysisTasks()

    contract_summarizer = agents.contract_summarizer_agent()
    function_analyzer = agents.function_analyzer_agent()
    updateability_analyzer = agents.update_analyzer_agent()
    security_analyzer = agents.security_analyzer_agent()
    report_compiler = agents.report_compiler_agent()

    task1 = tasks.summarize_task(contract_summarizer, contract_code)
    task2 = tasks.analyze_task(function_analyzer, contract_code)
    task4 = tasks.updateable_task(updateability_analyzer, contract_code)
    task5 = tasks.security_task(security_analyzer, contract_code)
    task6 = tasks.compiler_task(report_compiler)

    crew = Crew(
        agents=[contract_summarizer, function_analyzer, updateability_analyzer, report_compiler],
        tasks=[task1, task2, task4, task5, task6],
        process=Process.sequential,
        memory=True
    )

    return crew

def main():
    st.title("Smart Contract Analysis")

    contract_code = st.text_area("Enter Smart Contract Code:", height=300)

    if st.button("Analyze"):
        if contract_code:
            crew = create_smart_contract_analysis_crew(contract_code)
            with st.spinner("Analyzing..."):
                result = crew.kickoff()
                st.success("Analysis complete!")
                st.markdown(result)
        else:
            st.error("Please enter the contract code.")

if __name__ == "__main__":
    main()