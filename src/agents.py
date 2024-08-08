from textwrap import dedent
from crewai import Agent
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

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
        return Agent(
            role='contract summarizer',
            goal='Provide a comprehensive summary of the smart contract\'s purpose.',
            tools=[],
            backstory=dedent("""
                You are a blockchain analyst with expertise in understanding smart contract code in the Clarity language."""),
            verbose=True,

            
        )

    def function_analyzer_agent(self):
        return Agent(
            role='function analyzer',
            goal='Identify and summarize all functions in the smart contract.',
            tools=[],
            backstory=dedent("""
               You are a smart contract developer with deep knowledge of function analysis in the Clarity language on the Stacks blockchain."""),
            verbose=True,
        )

    def diagram_creator_agent(self):
        return Agent(
            role='diagram creator',
            goal=' Create mermaidjs diagrams for contract control flow.',
            tools=[],
            backstory=dedent("""
                You are a visualization expert specializing in creating clear and informative diagrams of smart contract structures in the Clarity language on the Stacks blockchain."""),
            verbose=True,
        )
    
    def update_analyzer_agent(self):
        return Agent(
            role='updateability analyzer',
            goal=' Assess if any parts of the contract can be updated and by whom.',
            tools=[],
            backstory=dedent("""
               You are a smart contract auditor with expertise in contract governance and upgrade mechanisms in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )
    
    def security_analyzer_agent(self):
        return Agent(
            role='security analyzer',
            goal='Identify and explain potential security vulnerabilities in the contract',
            tools=[],
            backstory=dedent("""
               You are a blockchain security expert with a keen eye for detecting potential vulnerabilities in smart contracts in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )
    
    def report_compiler_agent(self):
        return Agent(
            role='report compiler',
            goal='Compile all analyses into a comprehensive final report.',
            tools=[],
            backstory=dedent("""
               You are a technical writer with expertise in creating clear and concise reports on complex blockchain topics in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )