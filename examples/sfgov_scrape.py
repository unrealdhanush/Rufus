import asyncio
from Rufus import RufusClient

async def main():
    client = RufusClient(api_key='your_api_key')
    instructions = "We're making a chatbot for the HR in San Francisco."
    documents = await client.scrape("https://sfgov.org", instructions=instructions)

    import json
    with open('sfgov_data.json', 'w') as f:
        json.dump(documents, f, indent=2)

if __name__ == '__main__':
    asyncio.run(main())
