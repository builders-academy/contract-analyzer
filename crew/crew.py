from crew.agents import SmartContractAnalysisAgents
from crew.tasks import SmartContractAnalysisTasks
from crewai import Crew

class SmartContractAnalysisCrew:
    def __init__(self, contract_address: str, contract_name: str, contract_source: str):
        self.contract_info = {
            "address": contract_address,
            "name": contract_name,
            "source_code": contract_source
        }
        self.agents = SmartContractAnalysisAgents()
        self.tasks = SmartContractAnalysisTasks()

    def run_analysis(self):
        print("Contract Source Code:")
        print(self.contract_info["source_code"])

        # Create tasks with placeholders
        summarize_task = self.tasks.summarize_contract(self.agents.contract_summarizer(), self.contract_info)
        analyze_functions_task = self.tasks.analyze_functions(self.agents.function_analyzer(), self.contract_info, "{{summarize_task.result}}")
        analyze_updateability_task = self.tasks.analyze_updateability(self.agents.updateability_analyzer(), self.contract_info, "{{summarize_task.result}}")
        analyze_security_task = self.tasks.analyze_security(self.agents.security_analyzer(), self.contract_info, "{{analyze_functions_task.result}}", "{{analyze_updateability_task.result}}")
        compile_report_task = self.tasks.compile_report(self.agents.report_compiler(), self.contract_info, "{{summarize_task.result}}", "{{analyze_functions_task.result}}", "{{analyze_updateability_task.result}}", "{{analyze_security_task.result}}")

        crew = Crew(
            agents=[
                self.agents.contract_summarizer(),
                self.agents.function_analyzer(),
                # self.agents.diagram_creator(),
                self.agents.updateability_analyzer(),
                self.agents.security_analyzer(),
                self.agents.report_compiler()
            ],
            tasks=[
                summarize_task,
                analyze_functions_task,
                # self.tasks.create_diagrams(self.agents.diagram_creator(), self.contract_info, "{{analyze_functions_task.result}}"),
                analyze_updateability_task,
                analyze_security_task,
                compile_report_task
            ],
            verbose=2
        )
        result = crew.kickoff()

        # Save the result to a file
        with open('smart_contract_analysis_report.md', 'w') as f:
            f.write(result)

        return crew.kickoff()
