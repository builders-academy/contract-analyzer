from crewai import Task
from textwrap import dedent

class SmartContractAnalysisTasks:

    def summarize_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Provide a comprehensive summary of the given smart contract's purpose.
                Contract Code:
                {contract_code}
                
                Your response should be a detailed paragraph providing what the codes and the functions are in the contract.
            """),
            expected_output="A detailed paragraph explaining the main purpose and functionality of the contract.",
            agent=agent,
            async_execution=False
        )

    def analyze_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Identify all public, private, and read-only functions, summarize them, and indicate if they move funds.
                Contract Code:
                {contract_code}
                
                Your response should be a detailed paragraph listing and describing each function, its visibility, and whether it moves funds.
            """),
            expected_output="A detailed paragraph listing and describing each function, its visibility, and whether it moves funds.",
            agent=agent,
            async_execution=True
        )

    def diagram_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Create mermaidjs diagrams showing control flow within the contract and between contracts.
                Contract Code:
                {contract_code}
                
                Your response should be a paragraph describing the control flow, followed by the mermaidjs code for two diagrams: 
                one showing internal control flow and another showing inter-contract interactions.
            """),
            expected_output="A paragraph describing the control flow and mermaidjs code for two diagrams.",
            agent=agent,
            async_execution=True
        )

    def updateable_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Assess if any parts of the contract can be updated and by whom.
                Contract Code:
                {contract_code}
                
                Your response should be a detailed paragraph explaining which parts of the contract are upgradeable, if any, 
                and who has the authority to make updates.
            """),
            expected_output="A detailed paragraph explaining which parts of the contract are upgradeable and who can update them.",
            agent=agent,
            async_execution=True
        )

    def security_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Identify and explain any potential security vulnerabilities in the contract.
                Contract Code:
                {contract_code}
                
                Your response should be a detailed paragraph listing and describing each potential vulnerability, 
                including possible exploits and issues.
            """),
            expected_output="A detailed paragraph listing and describing each potential vulnerability, including possible exploits and issues.",
            agent=agent,
            async_execution=True
        )

    def compiler_task(self, agent, contract_code, summary, functions, diagrams, updateability, vulnerabilities):
        return Task(
            description=dedent(f"""
                Compile all analysis into a comprehensive final report.
                Use the following information to create a well-structured, detailed report:

                Contract Address: {contract_code}

                ## Summary
                {summary}

                ## Functions Analysis
                {functions}

                ## Diagrams
                {diagrams}

                ## Updateability Analysis
                {updateability}

                ## Security Vulnerabilities
                {vulnerabilities}

                Your report should include the following sections:
                1. Executive Summary
                2. Contract Overview
                3. Functional Analysis
                4. Control Flow Diagrams
                5. Updateability Assessment
                6. Security Analysis
                7. Recommendations

                Format the report in a clear, professional manner. Use markdown for headings and formatting.
                Ensure that each section provides valuable insights and is easy to understand.
            """),
            expected_output="A comprehensive, well-structured report covering all aspects of the smart contract analysis.",
            agent=agent,
            async_execution=False
    )
