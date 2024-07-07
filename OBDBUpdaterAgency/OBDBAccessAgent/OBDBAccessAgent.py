from agency_swarm.agents import Agent
from instructor import llm_validator


class OBDBAccessAgent(Agent):
    def __init__(self):
        super().__init__(
            name="OBDBAccessAgent",
            description="OBDBAccessAgent is an agent with capability to access and search the online Open Brewery "
                        "database.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        llm_validator(statement="Verify whether the update from the OBDBAccessAgent confirms the task's "
                                "successful completion. If the task remains unfinished, provide guidance "
                                "within the 'reason' argument on the next steps the agent should take.",
                      client=self.client)(message)
        return message
