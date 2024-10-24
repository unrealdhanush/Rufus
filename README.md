# **RufusAIToolkit Documentation**

## **Table of Contents**

1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Installation](#3-installation)
4. [Usage](#4-usage)
   - [Basic Crawling](#basic-crawling)
   - [Advanced Configuration](#advanced-configuration)
5. [Integration into RAG Pipelines](#5-integration-into-rag-pipelines)
6. [License](#6-license)


---

## **1. Introduction**

**RufusAIToolkit** is an intelligent web crawler and data synthesizer designed to extract and structure information from various websites. Built with scalability and flexibility in mind, RufusAIToolkit seamlessly integrates into Retrieval-Augmented Generation (RAG) pipelines, enhancing data retrieval and processing capabilities for diverse applications.

---

## **2. Features**

- **Asynchronous Web Crawling:** Efficiently crawls multiple web pages concurrently using `aiohttp`.
- **Robust Error Handling:** Gracefully manages SSL issues and skips non-HTML content.
- **Intelligent Data Parsing:** Extracts meaningful data while filtering out irrelevant elements.
- **Relevance Assessment:** Utilizes `sentence-transformers` to evaluate content relevance based on user-defined instructions.
- **Scalable Integration:** Easily integrates with RAG pipelines for enhanced data retrieval and generation.


## **3. Installation**

### **Prerequisites**

- Python 3.7 or higher
- pip package manager

### **Install via PyPI**

```bash
pip install RufusAIToolkitToolkit==0.1.0
```

### **Clone the Repository (Optional)**

If you prefer to install directly from the source:

```bash
git clone https://github.com/unrealdhanush/RufusAIToolkitToolkit.git
cd RufusAIToolkit
pip install -e .
```

## **4. Usage**

### **Basic Crawling**

Here's a simple example to get you started with RufusAIToolkit:

```python
from RufusAIToolkitToolkit.core.client import RufusClient
import asyncio

async def main():
    client = RufusClient(api_key='your_api_key_here')
    instructions = "Extract information on government policies and services."
    documents = await client.scrape(
        url="https://sfgov.org",
        instructions=instructions,
        max_depth=2,
        max_pages=5
    )
    for doc in documents:
        print(f"URL: {doc['url']}")
        print(f"Content: {doc['content']}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

### **Advanced Configuration**

Customize RufusAIToolkit's behavior by adjusting parameters:

```python
from RufusAIToolkit.core.client import RufusClient
import asyncio

async def main():
    client = RufusClient(api_key='your_api_key_here')
    instructions = "Extract detailed financial reports."
    documents = await client.scrape(
        url="https://www.example.com",
        instructions=instructions,
        max_depth=3,
        max_pages=50,
        similarity_threshold=0.7
    )
    # Process documents as needed

if __name__ == "__main__":
    asyncio.run(main())
```

## **5. Integration into RAG Pipelines**

Retrieval-Augmented Generation (RAG) pipelines benefit significantly from structured and relevant data. Here's how RufusAIToolkit can be integrated:

### **Architecture Overview**

1. **Data Retrieval:** RufusAIToolkit crawls specified websites, extracting relevant information based on user instructions.
2. **Data Synthesis:** The extracted data is evaluated for relevance and structured into documents.
3. **Knowledge Base Integration:** These documents are indexed and stored in a knowledge base (e.g., FAISS, Elasticsearch).
4. **RAG Model Utilization:** The RAG model queries the knowledge base to retrieve relevant documents, enhancing the generation of accurate and context-aware responses.

### **Step-by-Step Integration**

1. **Crawling and Data Extraction:**

   ```python
   from RufusAIToolkit.core.client import RufusClient
   import asyncio

   async def crawl_data():
       client = RufusClient(api_key='your_api_key_here')
       instructions = "Extract information on government policies and services."
       documents = await client.scrape(
           url="https://sfgov.org",
           instructions=instructions,
           max_depth=2,
           max_pages=10
       )
       return documents
   ```

2. **Indexing Documents:**

   After crawling, index the documents into your preferred knowledge base.

   ```python
   from your_kb_library import KnowledgeBase

   async def index_documents(documents):
       kb = KnowledgeBase()
       for doc in documents:
           kb.add_document(doc['content'], metadata={'url': doc['url']})
       kb.build_index()
   ```

3. **Querying with RAG Model:**

   Integrate the knowledge base with your RAG model to retrieve and utilize the documents.

   ```python
   from your_rag_model import RAGModel

   def generate_response(query, kb):
       retrieved_docs = kb.query(query)
       response = RAGModel.generate(query, retrieved_docs)
       return response
   ```

4. **Putting It All Together:**

   ```python
   async def main():
       documents = await crawl_data()
       await index_documents(documents)
       kb = KnowledgeBase.load_index()
       query = "What are the latest government services available in San Francisco?"
       response = generate_response(query, kb)
       print(response)

   if __name__ == "__main__":
       asyncio.run(main())
   ```

### **Benefits of Integration**

- **Enhanced Data Quality:** Ensures that the RAG model has access to structured and relevant information.
- **Scalability:** Efficient crawling and data processing allow handling large volumes of data.
- **Flexibility:** Easily adjust crawling parameters and instructions to tailor data retrieval to specific needs.

## **6. License**
RufusAIToolkit is distributed and protected under the standard MIT License.

