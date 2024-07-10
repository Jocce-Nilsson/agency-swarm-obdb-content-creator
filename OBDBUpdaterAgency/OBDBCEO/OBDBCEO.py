from agency_swarm.agents import Agent


class OBDBCEO(Agent):
    def __init__(self):
        super().__init__(
            name="OBDBCEO",
            description="Oversees the entire operation of the OBDBUpdaterAgency, ensuring that all tasks are completed efficiently and accurately.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-3.5-turbo",
        )
        
    def response_validator(self, message):
        return message
