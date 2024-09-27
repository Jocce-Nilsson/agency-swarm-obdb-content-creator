import os
from agency_swarm import Agency
from OBDBManager import OBDBManager
from OBDBAccessAgent import OBDBAccessAgent
from OBDBCEO import OBDBCEO
from OBDBProgrammer import OBDBProgrammer
from WebAgent import WebAgent
from agency_swarm import set_openai_key

open_ai_key: str = os.getenv("OPEN_AI_API_KEY")
if not open_ai_key:
    raise ValueError("OpenAI API key is required. Please set the OPEN_AI_API_KEY environment variable.")
set_openai_key(open_ai_key)

ceo = OBDBCEO()
manager = OBDBManager()
programmer = OBDBProgrammer()
webAgent = WebAgent()
dbAccessAgent = OBDBAccessAgent()

agency = Agency([ceo, manager,
                 [ceo, manager],
                 [manager, programmer],
                 [manager, webAgent],
                 [programmer, webAgent],
                 [manager, dbAccessAgent],
                 ],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.run_demo()
