from agency_swarm import Agency
from OBDBManager import OBDBManager
from OBDBAccessAgent import OBDBAccessAgent
from OBDBCEO import OBDBCEO
from BrowsingAgent import BrowsingAgent
from OBDBProgrammer import OBDBProgrammer
from GoogleSearchAgent import GoogleSearchAgent

ceo = OBDBCEO()
manager = OBDBManager()
programmer = OBDBProgrammer()
browsingAgent = BrowsingAgent()
dbAccessAgent = OBDBAccessAgent()
searchAgent = GoogleSearchAgent()

agency = Agency([ceo, manager,
                 [ceo, manager],
                 [manager, programmer],
                 [manager, searchAgent],
                 [manager, browsingAgent],
                 [manager, dbAccessAgent],
                 ],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.run_demo()
