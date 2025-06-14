rag_mcp_bot/
│
├── root_agent/
│   ├── __init__.py
│   ├── agent.yaml
│   └── root_logic.py
│
├── agents/
│   ├── agent_a_intent/
│   │   ├── __init__.py
│   │   ├── agent.yaml
│   │   └── classify_intent.py
│   │
│   ├── agent_b_retriever/
│   │   ├── __init__.py
│   │   ├── agent.yaml
│   │   └── retrieve_chunks.py
│   │
│   └── agent_c_llm/
│       ├── __init__.py
│       ├── agent.yaml
│       └── generate_response.py
│
├── vector_db/
│   ├── build_faiss_index.py
│   └── forex_index.faiss
│   └── vector.index
│
└── tools/
    └── shared.py  # (utils, loading FAISS, etc.)


Phase	Goal	Status
0	Setup Project	✅
1	Build Intent Classifier	⏳
2	FAISS Index	⏳
3	Build Retriever	⏳
4	Build LLM Responder	⏳
5	Orchestrate All via RootAgent	⏳
6	Test End-to-End	⏳
7	Improve & Scale	⏳
8	Deploy	⏳



to run this go to root folder and do adk web