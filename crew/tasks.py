from crewai import Task

class SmartContractAnalysisTasks:
    def summarize_contract(self, agent, contract_info):
        print("Contract Source Code:")
        print(contract_info["source_code"])
        print("Running task: summarizer...")
        return Task(
            description="Provide a comprehensive summary of the smart contract's purpose.",
            agent=agent,
            context=[
                {
                    "source_code": contract_info['source_code'],
                    "description": "Contract source code provided for analysis.",
                    "expected_output": "Summary of the contract's purpose"
                }
            ],
            expected_output="Summary of the contract's purpose"
        )

    def analyze_functions(self, agent, contract_info, summary):
        print("Running task: analyzer...")
        return Task(
            description="Identify the functions and summarize them.",
            agent=agent,
            context=[
                {
                    "source_code": contract_info['source_code'],
                    "contract_summary": summary,
                    "description": "Contract source code and summary provided for function analysis.",
                    "expected_output": "Analysis of the functions and their characteristics"
                }
            ],
            expected_output="Analysis of all functions."
        )

    # def create_diagrams(self, agent, contract_info, functions):
    #     return Task(
    #         description="Create mermaidjs diagrams showing control flow within the contract and between contracts.",
    #         agent=agent,
    #         context=[
    #             {
    #                 "source_code": contract_info['source_code'],
    #                 "function_analysis": functions,
    #                 "description": "Contract source code and function analysis provided for diagram creation.",
    #                 "expected_output": "MermaidJS diagrams of the contract's control flow"
    #             }
    #         ],
    #         expected_output="MermaidJS diagrams of the contract's control flow"
    #     )

    def analyze_updateability(self, agent, contract_info, summary):
        print("Running task: updateability...")
        return Task(
            description="Assess if any parts of the contract can be updated and by whom if do not find any leave it.",
            agent=agent,
            context=[
                {
                    "source_code": contract_info['source_code'],
                    "contract_summary": summary,
                    "description": "Contract source code and summary provided for updateability assessment.",
                    "expected_output": "Updateability analysis of the contract"
                }
            ],
            expected_output="Updateability analysis of the contract"
        )

    def analyze_security(self, agent, contract_info, functions, updateability):
        print("Running task: security...")
        return Task(
            description="Identify and explain any potential security vulnerabilities in the contract.",
            agent=agent,
            context=[
                {
                    "source_code": contract_info['source_code'],
                    "function_analysis": functions,
                    "updateability_analysis": updateability,
                    "description": "Check how secure is the contract.",
                    "expected_output": "Security analysis of the contract"
                }
            ],
            expected_output="Security analysis of the contract"
        )

    def compile_report(self, agent, contract_info, summary, functions, updateability, vulnerabilities):
        print("Running task: report...")
        return Task(
            description="Compile all analyses into a comprehensive final report.",
            agent=agent,
            context=[
                {
                    "contract_address": contract_info['address'],
                    "contract_name": contract_info['name'],
                    "summary": summary,
                    "function_analysis": functions,
                    # "diagrams": diagrams,
                    "updateability_analysis": updateability,
                    "security_vulnerabilities": vulnerabilities,
                    "description": "All analyses provided for final report compilation.",
                    "expected_output": "Final comprehensive report"
                }
            ],
            expected_output="Final comprehensive report"
        )
