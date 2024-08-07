from textwrap import dedent
from crewai import Agent
from crewtools import get_contract
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

class SmartContractAnalysisAgents:
    # contract_retriver
    def contract_retriver_agent(self):
        return Agent(
            role='Contract Retriever',
            goal='Retrieve and save the available function  of the smart contract.',
            tools=[get_contract],
            backstory=dedent("""
                You are an expert in blockchain technology and smart contract retrieval."""),
            verbose=True,
        )

    def contract_summarizer_agent(self):
        return Agent(
            role='Contract Summarizer',
            goal='RProvide a comprehensive summary of the smart contract\'s purpose.',
            tools=[get_contract],
            backstory=dedent("""
                You are a blockchain analyst with expertise in understanding smart contract functionality in the Clarity language on the Stacks blockchain."""),
            verbose=True,
        )

    def function_analyzer_agent(self):
        return Agent(
            role='Function Analyzer',
            goal='Identify and summarize all functions in the smart contract.',
            tools=[],
            backstory=dedent("""
                You are an expert in blockchain technology and smart contract retrieval."""),
            verbose=True,
        )

    def diagram_creator_agent(self):
        return Agent(
            role='Diagram Creator',
            goal=' Create mermaidjs diagrams for contract control flow.',
            tools=[],
            backstory=dedent("""
                You are a visualization expert specializing in creating clear and informative diagrams of smart contract structures in the Clarity language on the Stacks blockchain."""),
            verbose=True,
        )
    
    def update_analyzer_agent(self):
        return Agent(
            role='Updateability Analyzer',
            goal=' Assess if any parts of the contract can be updated and by whom.',
            tools=[],
            backstory=dedent("""
               You are a smart contract auditor with expertise in contract governance and upgrade mechanisms in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )
    
    def security_analyzer_agent(self):
        return Agent(
            role='Security Analyzer',
            goal='Identify and explain potential security vulnerabilities in the contract',
            tools=[],
            backstory=dedent("""
               You are a blockchain security expert with a keen eye for detecting potential vulnerabilities in smart contracts in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )
    
    def report_compiler_agent(self):
        return Agent(
            role='Report Compiler',
            goal='Compile all analyses into a comprehensive final report.',
            tools=[],
            backstory=dedent("""
               You are a technical writer with expertise in creating clear and concise reports on complex blockchain topics in the Clarity language on the Stacks blockchain.
"""),
            verbose=True,
        )