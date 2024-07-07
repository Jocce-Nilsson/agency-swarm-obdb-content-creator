from typing_extensions import override
import re
from agency_swarm.agents import Agent
from agency_swarm.tools import FileSearch
from instructor import llm_validator


class Devid(Agent):
    def __init__(self):
        super().__init__(
            name="Devid",
            description="Devid is an AI software engineer capable of performing advanced coding tasks.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[FileSearch],
            tools_folder="./tools",
            validation_attempts=1,
            temperature=0,
            max_prompt_tokens=25000,
            examples=["Create a file for this brewery: name is Islay Ales, brewery_type is micro, "
                      "address is Islay House Square, city is Bridgend, state_province is Argyll, "
                      "postal_code is PA44 7NZ, country is Scotland, phone is 1496810014, "
                      "website_url is https://www.islayales.com/, longitude is -6.2511858, latitude is 55.7845598"
                      "Based on the input above, you should create or update a CSV file named Argyll.csv "
                      "in folder Scotland with the header columns (only once in the file, yop row): "
                      "id,name,brewery_type,address_1,address_2,address_3,city,state_province,postal_code,country,website_url,phone,longitude,latitude",
                      "and the following data:"
                      ",Islay Ales,micro,Islay House Square,,,Bridgend,Argyll,PA44 7NZ,Scotland,https://www.islayales.com/,1496810014,-6.2511858,55.7845598"],
        )

    @override
    def response_validator(self, message):
        pattern = r'(```)((.*\n){5,})(```)'

        if re.search(pattern, message):
            # take only first 100 characters
            raise ValueError(
                "You returned code snippet. Please never return code snippets to me. "
                "Use the FileWriter tool to write the code locally. Then, test it if possible. Continue."
            )

        llm_validator(statement="Verify whether the update from the AI Developer Agent confirms the task's "
                                "successful completion. If the task remains unfinished, provide guidance "
                                "within the 'reason' argument on the next steps the agent should take. For "
                                "instance, if the agent encountered an error, advise the inclusion of debug "
                                "statements for another attempt. Should the agent outline potential "
                                "solutions or further actions, direct the agent to execute those plans. "
                                "Message does not have to contain code snippets. Just confirmation.",
                      client=self.client)(message)

        return message
