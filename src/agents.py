from textwrap import dedent
from crewai import Agent


from tools import codeSearchTool, functionSearchTool


class SmartContractAnalysisAgents:
    # contract_retriver
    # def contract_retriver_agent(self):
    #     return Agent(
    #         role='Contract Retriever and Analyzer',
    #         goal='Retrieve and analyze the content of smart contract web pages, extracting relevant information from various HTML elements.',
    #         tools=[get_contract],
    #         backstory=dedent("""
    #             You are an expert in blockchain technology, smart contract analysis, and web scraping.
    #             You know how to extract and interpret information from web pages, focusing on content
    #             within div, span, and p tags. Your expertise allows you to identify key aspects of
    #             smart contracts from this extracted information."""),
    #         verbose=True,
    # )

    def contract_summarizer_agent(self):
        print("-----------------RUNNING-SUMMARIZER-------------------")
        return Agent(
            role='contract summarizer',
            goal='Provide a comprehensive summary of the smart contract\'s purpose.',
            tools=[codeSearchTool],
            backstory=dedent("""
                You are a blockchain analyst with expertise in understanding smart contract code in the Clarity language."""),
            verbose=True,
            
        )

    def function_analyzer_agent(self):
        print("-----------------RUNNING-ANALYZER-------------------")
        return Agent(
            role='function analyzer',
            goal='Identify all functions in the smart contract.',
            tools=[functionSearchTool],
            backstory=dedent("""
               You are a smart contract developer with deep knowledge of function analysis in the Clarity language on the Stacks blockchain."""),
            verbose=True,
        )

    # def diagram_creator_agent(self):
    #     print("-----------------CREATING-DIAGRAM-------------------")
    #     return Agent(
    #         role='diagram creator',
    #         goal=' Create mermaidjs diagrams for contract control flow.',
    #         tools=[],
    #         backstory=dedent("""
    #             You are a visualization expert specializing in creating clear and informative diagrams of smart contract structures in the Clarity language on the Stacks blockchain."""),
    #         verbose=True,
    #     )
    
    def update_analyzer_agent(self):
        print("-----------------CHECKING-UPDATABILITY-------------------")
        return Agent(
            role='updateability analyzer',
            goal=' Assess if any parts of the contract can be updated and by whom.',
            tools=[],
            backstory=dedent("""
               You are a smart contract auditor with expertise in contract governance and upgrade mechanisms in the Clarity language on the Stacks blockchain.
                To determine contract upgradeability, several key functions and principles can be implemented in smart contracts. These functions help ensure that a contract can be modified or extended without losing existing state or functionality. Here are some essential functions and concepts that contribute to contract upgradeability:
                Key Functions for Contract Upgradeability
                Ownership Management Functions:
                set-contract-owner(new-owner: principal): This function allows the current contract owner to transfer ownership to a new principal, ensuring that upgrades can be managed by a designated authority.
                get-contract-owner(): A read-only function that retrieves the current owner of the contract.
                Proposal and Voting Management:
                insert-proposal(title: string, end-height: uint, proposer: principal): This function adds a new proposal to the contract, allowing it to manage proposals dynamically.
                set-vote(for: bool, voter: principal, proposal-id: uint): This function registers a vote for a specific proposal, enabling the contract to handle voting logic flexibly.
                Dynamic Dispatch Functions:
                is-member(who: principal): This function checks if a principal is a member, allowing the contract to interact with a separate member management contract.
                contract-call?(member-storage-ref, is-member, tx-sender): This function demonstrates how to call functions dynamically from other contracts, facilitating modular design.
                State Management Functions:
                get-proposal(proposal-id: uint): A read-only function that retrieves proposal details, allowing for querying without modifying state.
                get-vote(member: principal, proposal-id: uint): This function checks the voting status of a member for a specific proposal.
                Error Handling and Assertions:
                asserts!(condition, error-code): Used throughout the contract to enforce rules and conditions, ensuring that only valid actions are taken, which is crucial for maintaining contract integrity during upgrades.
                Multi-Principal Ownership:
                Implementing functions that manage multiple owners or stakeholders, such as set-whitelisted(is-whitelisted: bool, who: principal), allows for a more robust governance model that can adapt to changes in ownership or authority.
"""),
            verbose=True,
            allow_delegation=False
        )
    
    def security_analyzer_agent(self):
        print("-----------------RUNNING-SECURITY-ANALYSIS-------------------")
        return Agent(
            role='security analyzer',
            goal='Identify and explain potential security vulnerabilities in the contract',
            tools=[codeSearchTool, functionSearchTool],
            backstory=dedent("""
               You are a blockchain security expert with a keen eye for detecting potential vulnerabilities in smart contracts in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )
    
    def report_compiler_agent(self):
        print("-----------------COMPILING-------------------")
        return Agent(
            role='report compiler',
            goal='Compile all output into a final report.',
            tools=[],
            backstory=dedent("""
               You are a technical writer with expertise in creating clear and concise reports on complex blockchain topics in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
            allow_delegation=False
        )