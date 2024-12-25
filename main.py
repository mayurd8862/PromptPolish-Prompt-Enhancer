from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7
)

# Create the agents
prompt_analyzer = Agent(
    role="Prompt Engineering Expert",
    goal="Analyze and identify improvements in prompt engineering",
    backstory="""You are a world-class prompt engineer with deep expertise in NLP 
    and LLM behavior. You excel at identifying what makes prompts effective and
    suggesting concrete improvements.""",
    llm=llm,
    verbose=True
)

prompt_optimizer = Agent(
    role="Prompt Optimization Specialist",
    goal="Transform and enhance prompts for maximum effectiveness",
    backstory="""You are an elite prompt optimization expert who knows how to 
    restructure and refine prompts for optimal results. You understand the nuances 
    of different LLM models and how to craft prompts that yield the best responses.""",
    llm=llm,
    verbose=True
)

# Create the tasks
analysis_task = Task(
    description="""Analyze the provided prompt:
    '{input_prompt}'
    
    Evaluate:
    1. Clarity and specificity
    2. Potential ambiguities
    3. Completeness
    4. Areas for improvement
    """,
    expected_output="""A comprehensive analysis report detailing the prompt's 
    strengths, weaknesses, and specific areas for improvement.""",
    agent=prompt_analyzer
)

optimization_task = Task(
    description="""Using the analysis, enhance the prompt by:
    1. Implementing all suggested improvements
    2. Adding necessary context and constraints
    3. Restructuring for better flow
    4. Ensuring outputs are clearly specified
    
    Provide the optimized prompt""",
    expected_output="""An optimized version of the prompt.""",
    agent=prompt_optimizer
)

# Create the crew
crew = Crew(
    agents=[prompt_analyzer, prompt_optimizer],
    tasks=[analysis_task, optimization_task],
    process=Process.sequential,
    verbose=True
)

# Sample prompt to optimize
input_prompt = """what is machine learning. explain to 10 years old child"""

# Kick off the crew
result = crew.kickoff(inputs={'input_prompt': input_prompt})
print("\nFinal Result:",'\n')
print(result)