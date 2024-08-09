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
                Store your summary in the crew's shared memory with the key 'summary'.
            """),
            expected_output="A detailed paragraph summarizing the smart contract's purpose and main functions.",
            agent=agent
        )

    def analyze_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Identify all public, private, and read-only functions, and indicate if they move funds.
                Contract Code:
                {contract_code}
                Your response should be a detailed paragraph listing and describing each function, its visibility, and whether it moves funds.
                Store your analysis in the crew's shared memory with the key 'function_analysis'.
            """),
            expected_output="A detailed paragraph listing and describing each function, its visibility, and whether it moves funds.",
            agent=agent
        )


    def updateable_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Assess if any parts of the contract can be updated and by whom.      
                Contract Code:
                {contract_code}
                Your response should be a detailed paragraph explaining which parts of the contract are upgradeable, if any, 
                and who has the authority to make updates. Consider the functions analysis to identify any specific functions 
                that might affect the updatability of the contract.
                Store your assessment in the crew's shared memory with the key 'updateability'.
            """),
            expected_output="A detailed paragraph explaining which parts of the contract are upgradeable and who can update them.",
            agent=agent,
            async_execution=False
        )
    
    def security_task(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Identify and explain any potential security vulnerabilities in the contract.
                Contract Code:
                {contract_code}
                Store your analysis in the crew's shared memory with the key 'security_analysis'.
            """),
            expected_output="A list of SecurityVulnerability objects, each containing a description of the vulnerability, potential exploit, and potential issues.",
            agent=agent,
            async_execution=False
        )

    def compiler_task(self, agent):
        return Task(
            description=dedent("""
                Compile all the output into a comprehensive final report.
                Use the following information from the crew's shared memory to create a detailed report:

                1. Summary (Access this from the shared memory with the key 'summary')
                2. Functions Analysis (Access this from the shared memory with the key 'function_analysis')
                3. Updateability (Access this from the shared memory with the key 'updateability')
                4. Security (Acess this from the shared memory with the key 'security_analysis')
                Ensure you integrate all this information into a cohesive report.
            """),
            expected_output="A comprehensive final report integrating the summary, function analysis, and updateability assessment of the smart contract.",
            agent=agent,
            async_execution=False
        )