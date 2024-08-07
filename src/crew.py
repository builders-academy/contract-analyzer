import streamlit as st
from crewai import Crew, Process
from agents import SmartContractAnalysisAgents
from tasks import SmartContractAnalysisTasks

def create_smart_contract_analysis_crew():
    agents = SmartContractAnalysisAgents()
    tasks = SmartContractAnalysisTasks()

    contract_retriever = agents.contract_retriver_agent()
    contract_summarizer = agents.contract_summarizer_agent()
    function_analyzer = agents.function_analyzer_agent()
    diagram_creator = agents.diagram_creator_agent()
    updateability_analyzer = agents.update_analyzer_agent()
    security_analyzer = agents.security_analyzer_agent()
    report_compiler = agents.report_compiler_agent()

    task1 = tasks.contract_task(contract_retriever)
    task2 = tasks.summarize_task(contract_summarizer, task1.expected_output)
    task3 = tasks.analyze_task(function_analyzer, task1.expected_output)
    task4 = tasks.diagram_task(diagram_creator, task3.expected_output)
    task5 = tasks.updateable_task(updateability_analyzer, task1.expected_output)
    task6 = tasks.security_task(security_analyzer, task3.expected_output)
    task7 = tasks.compiler_task(
        report_compiler,
        contract_info=task1.expected_output,
        summary=task2.expected_output,
        functions=task3.expected_output,
        diagrams=task4.expected_output,
        updateability=task5.expected_output,
        vulnerabilities=task6.expected_output
    )

    crew = Crew(
        agents=[contract_retriever, contract_summarizer, function_analyzer, diagram_creator, updateability_analyzer, security_analyzer, report_compiler],
        tasks=[task1, task2, task3, task4, task5, task6, task7],
        process=Process.sequential
    )

    return crew

# Define the Streamlit app
def main():
    st.title("Smart Contract Analysis")

    url = st.text_input("Enter Smart Contract URL:")

    if st.button("Analyze"):
        if url:
            crew = create_smart_contract_analysis_crew()
            with st.spinner("Analyzing..."):
                result = crew.kickoff(inputs={'url': url})
                st.success("Analysis complete!")
                st.write(result)
        else:
            st.error("Please enter a URL.")

if __name__ == "__main__":
    main()
