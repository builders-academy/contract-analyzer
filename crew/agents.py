from textwrap import dedent
from crewai import Agent
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

class SmartContractAnalysisAgents:
    # contract_retriver

    def contract_summarizer(self):
        print("Running contract_summarizer...")
        return Agent(
            role='Contract Summarizer',
            goal='Summarize the smart contract\'s purpose',
            backstory=dedent("""
                You are a blockchain analyst with expertise in understanding smart contracts on the Stacks blockchain.
                Your role is to provide a clear summary of the contract\'s purpose based on the provided code and documentation."""),
            verbose=True,
            allow_delegation=True
        )

    def function_analyzer(self):
        print("Running function_analyzer...")
        return Agent(
            role='Function Analyzer',
            goal='Analyze and describe all functions in the smart contract',
            backstory=dedent("""
                You are a smart contract developer specializing in analyzing contract functions on the Stacks blockchain.
                Your task is to identify and describe the function's purpose and interactions based on the summary of the code provided."""),
            verbose=True,
            allow_delegation=True
        )
    
    # digram retriver

    def updateability_analyzer(self):
        print("Running updateability_analyzer...")
        return Agent(
            role='Updateability Analyzer',
            goal='Assess the contract’s updateability and governance',
            backstory=dedent("""
                You are a smart contract auditor with expertise in contract governance on the Stacks blockchain. Your job is to evaluate the contract's updateability and identify who can make changes."""),
            verbose=True,
            allow_delegation=True
        )

    def security_analyzer(self):
        print("Running security_analyzer...")
        return Agent(
            role='Security Analyzer',
            goal='Identify and explain potential security vulnerabilities in the contract',
            backstory=dedent("""
                You are a blockchain security expert with experience in identifying vulnerabilities in smart contracts on the Stacks blockchain. Your task is to detect and explain any potential security issues in the contract."""),
            verbose=True,
            allow_delegation=True
        )

    def report_compiler(self):
        print("Running report_compiler...")
        return Agent(
            role='Report Compiler',
            goal='Compile analyses into a comprehensive final report',
            backstory=dedent("""
                You are a technical writer skilled in creating clear reports on blockchain topics related to the Stacks blockchain.
                Your role is to compile all analyses into a cohesive final report, synthesizing the findings from various experts."""),
            verbose=True,
        )
