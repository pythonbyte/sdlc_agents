from crewai import Task, Agent


class SDLCTask:

    def __init__(self, development_task: str, test_cases: str):
        self.development_task = development_task
        self.test_cases = test_cases

    def build_sdlc(self, agent: Agent):
        return Task(
            description=f"Create all the CODE for a Software based on the requirements of a user with the variable '{self.development_task}' and the test cases '{self.test_cases}'",
            agent=agent,  # Start with the Product Manager
            expected_output="""
                MUST provide ALL CODE IMPLEMENTED based on the requirements, 
                MUST provide ALL TESTS IMPLEMENTED based on the requirements,
                MUST provide ALL FUNCTIONS IMPLEMENTED based on the requirements,
                MUST provide ALL DOCUMENTATION IMPLEMENTED based on the requirements
                
                The output must be 

                CODE:

                ```<programming language>
                    <code>
                ```

                TESTS:
                    
                ```<programming language>
                    <code>
                ```

                DOCUMENTATION:

                Documentation must be in the form of a markdown file with the following structure and list the structure of the code and the test cases:

                1. <Title>
                    - <Description>
                    - <Code Structure>
                    - <Test Cases Structure>    
                

            """,
            async_execution=False,  # Task will be executed immediately
            context=[],  # No need for context in this example
            callback=None,  # No callback function needed
            tools=[],  # No tools needed for this task
            max_iter=10,
            max_rpm=10,
            verbose=True,
            enable_delegation=True,
        )
