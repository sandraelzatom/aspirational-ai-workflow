# JurisPrism Architecture
1. **Ingestion:** PDF parsing into Markdown.
2. **Indexing:** Recursive character splitting + Neo4j Graph relations.
3. **Retrieval:** Hybrid Search (Vector + Cypher Query).
4. **Generation:** GPT-4o with Pydantic enforcement.
