An implementation using [VRSEN agency-swarm](https://github.com/VRSEN/agency-swarm) to create agents for updating the [Open Brewery DB](https://www.openbrewerydb.org/)

Usage:
```bash
export OPEN_AI_API_KEY=<your_open_ai_api_key>
export GOOGLE_SEARCH_API_KEY=<your_google_search_api_key>
export GOOGLE_SEARCH_ENGINE_ID=<your_google_search_engine_id>
export GITHUB_ACCESS_TOKEN=<your_github_access_token>

python -m pip install -r requirements.txt
python OBDBUpdaterAgency/agency.py
```

You will see an update or creation of agents in OpenAI. Then a prompt to add your commands.

- Enter the name of the county and country you want to update the breweries for. 
- Specify also the owner and repository name for your fork of the Open Brewery DB repository. Default is `Jocce-Nilsson/openbrewerydb`.

The agent will search for breweries in the given country and update the CSV file with the details via a pull request to your main branch.
