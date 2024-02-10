from crewai import Agent
from langchain_openai import ChatOpenAI


class SDLCAgents:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def get_product_manager_agent(
        self,
        tools: list,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
    ):
        # Product Manager
        return Agent(
            role="Product Manager",
            goal="Identify user requirements and coordinate the software development process.",
            backstory="An experienced product manager with a knack for understanding user needs and translating them into actionable development tasks.",
            tools=tools,
            max_iter=10,
            max_rpm=10,
            verbose=self.verbose,
            allow_delegation=True,
            llm=ChatOpenAI(model_name=model_name, temperature=temperature),
        )

    def get_qa_software_engineer_agent(
        self,
        tools: list,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
    ):
        # QA Software Engineer
        return Agent(
            role="QA Software Engineer",
            goal="Create a comprehensive test suite and Implement the code for all the test cases.",
            backstory="A meticulous QA engineer with a keen eye for detail and a passion for delivering high-quality software.",
            tools=tools,
            max_iter=10,
            max_rpm=10,
            verbose=self.verbose,
            allow_delegation=True,
            llm=ChatOpenAI(model_name=model_name, temperature=temperature),
        )

    def get_sr_software_engineer_agent(
        self,
        tools: list,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
    ):
        # Sr Software Engineer
        return Agent(
            role="Sr Software Engineer",
            goal="Write the code to implement the features based on requirements.",
            backstory="A seasoned software engineer with a wealth of experience in developing software solutions across various domains.",
            tools=tools,
            max_iter=10,
            max_rpm=10,
            verbose=self.verbose,
            allow_delegation=True,
            llm=ChatOpenAI(model_name=model_name, temperature=temperature),
        )

    def get_auditor_agent(
        self,
        tools: list,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
    ):
        # Auditor
        return Agent(
            role="Auditor",
            goal="Evaluate the software and ensure it meets the specified requirements.",
            backstory="A diligent auditor with a strong background in software development and quality assurance, committed to delivering high-quality software.",
            tools=tools,
            max_iter=10,
            max_rpm=10,
            verbose=self.verbose,
            allow_delegation=True,
            llm=ChatOpenAI(model_name=model_name, temperature=temperature),
        )
