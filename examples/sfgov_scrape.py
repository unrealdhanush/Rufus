import asyncio
from Rufus import RufusClient

async def main():
    client = RufusClient(api_key='your_api_key')
    instructions = (
    "Information about human resources policies, employee benefits such as health insurance, "
    "retirement plans, vacation leave, and current job opportunities or openings at the City and County of San Francisco."
    )

    documents = await client.scrape("https://sfgov.org", instructions=instructions)

    import json
    with open('sfgov_data.json', 'w') as f:
        json.dump(documents, f, indent=2)

if __name__ == '__main__':
    asyncio.run(main())