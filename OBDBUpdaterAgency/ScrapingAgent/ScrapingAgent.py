from agency_swarm import Agent


class ScrapingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ScrapingAgent",
            description="Agent for scraping web pages",
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
