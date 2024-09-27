from typing_extensions import override
import re
from agency_swarm.agents import Agent
from agency_swarm.tools import FileSearch
from instructor import llm_validator


class OBDBProgrammer(Agent):
    def __init__(self):
        super().__init__(
            name="OBDBProgrammer",
            description="OBDBProgrammer is an AI software engineer capable of performing advanced coding tasks.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[FileSearch],
            tools_folder="./tools",
            validation_attempts=1,
            temperature=0,
            max_prompt_tokens=25000,
            model="gpt-4o",
        )

    @override
    def response_validator(self, message):
        return message
