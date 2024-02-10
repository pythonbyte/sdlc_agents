from datetime import datetime
from crewai import Process, Crew

from tasks import SDLCTask
from agents import SDLCAgents

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


def main(development_task, test_cases):
    task = SDLCTask(development_task=development_task, test_cases=test_cases)
    agents = SDLCAgents(verbose=True)

    # Form the crew
    pm = agents.get_product_manager_agent(tools=[search_tool])
    qa_engineer = agents.get_qa_software_engineer_agent(tools=[search_tool])
    sr_engineer = agents.get_sr_software_engineer_agent(tools=[search_tool])
    auditor = agents.get_auditor_agent(tools=[search_tool])

    dev_task = task.build_sdlc(agent=pm)

    code_swarm = Crew(
        agents=[pm, qa_engineer, sr_engineer, auditor],
        tasks=[dev_task],
        process=Process.sequential,
    )

    result = code_swarm.kickoff()

    return result


if __name__ == "__main__":
    print("## Welcome to the Code Swarm ##")
    print("-------------------------------")

    development_task = input("What is the development task? ")
    test_cases = input("What are the test cases? ")

    now = datetime.now()

    result = main(development_task, test_cases)

    print(f"## Code Swarm Completed in {datetime.now() - now} ##")

    with open("result.md", "w") as file:
        file.write(result)

    exit()
