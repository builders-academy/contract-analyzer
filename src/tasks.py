from crewai import Task
from textwrap import dedent

class SmartContractAnalysisTasks:

    def contract_task(self, agent):
        return Task(
            description=dedent("""
                Retrieve and save the available functions of the smart contract.
            """),
            expected_output=dedent("""
                A ContractInfo object containing the available functions.
            """),
            agent=agent,
            async_execution=True
        )

    def summarize_task(self, agent, contract_info):
        return Task(
            description=dedent(f"""
                Provide a comprehensive summary of the given smart contract's purpose.
                Contract Info: {contract_info}
            """),
            expected_output=dedent("""
                A detailed paragraph explaining the main purpose and functionality of the contract.
            """),
            agent=agent,
            async_execution=False
        )

    def analyze_task(self, agent, contract_info):
        return Task(
            description=dedent(f"""
                Identify all public, private, and read-only functions, summarize them, and indicate if they move funds.
                Contract Info: {contract_info}
            """),
            expected_output=dedent("""
                A list of FunctionInfo objects, each containing the function name, visibility, description, and whether it moves funds.
            """),
            agent=agent,
            async_execution=True
        )

    def diagram_task(self, agent, contract_info):
        return Task(
            description=dedent(f"""
                Create mermaidjs diagrams showing control flow within the contract and between contracts.
                Contract Info: {contract_info}
            """),
            expected_output=dedent("""
                A string containing mermaidjs code for two diagrams: one showing internal control flow and another showing inter-contract interactions.
            """),
            agent=agent,
            async_execution=True
        )

    def updateable_task(self, agent, contract_info):
        return Task(
            description=dedent(f"""
                Assess if any parts of the contract can be updated and by whom.
                Contract Info: {contract_info}
            """),
            expected_output=dedent("""
                A detailed explanation of which parts of the contract are upgradeable, if any, and who has the authority to make updates.
            """),
            agent=agent,
            async_execution=True
        )

    def security_task(self, agent, contract_info):
        return Task(
            description=dedent(f"""
                Identify and explain any potential security vulnerabilities in the contract.
                Contract Info: {contract_info}
            """),
            expected_output=dedent("""
                A list of SecurityVulnerability objects, each containing a description of the vulnerability, potential exploit, and potential issues.
            """),
            agent=agent,
            async_execution=True
        )

    def compiler_task(self, agent, contract_info, summary, functions, diagrams, updateability, vulnerabilities):
        return Task(
            description=dedent(f"""
                Compile all analyses into a comprehensive final report.
                Contract Info: {contract_info}
                Summary: {summary}
                Functions: {functions}
                Diagrams: {diagrams}
                Updateability: {updateability}
                Vulnerabilities: {vulnerabilities}
            """),
            expected_output=dedent("""
                An AnalysisReport object containing all the information gathered from previous tasks, formatted in a clear and organized manner.
            """),
            agent=agent,
            async_execution=False
        )
