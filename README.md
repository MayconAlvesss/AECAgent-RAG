# AECAgent-RAG 🤖 — Global AI Expert for Technical Standards

> **Conversational AI Agent for the Global AEC industry. Retrieval-Augmented Generation (RAG) applied to ISO standards, Eurocodes, and international technical building norms.**

---

## 🛠️ Status: Beta Research Prototype

> **Intelligent Agent Core Ready.** Fully integrated with global LLM backends (Gemini/OpenAI) and LangChain. Implements advanced chunking logic for complex normative documents. Currently in research phase for autonomous normative compliance auditing.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| **Contextual RAG** | Smart retrieval of specific clauses and articles from indexed PDF standards |
| **Multi-Source Indexing** | Support for Eurocodes, NBRs (Brazil), and ISO global standards |
| **Source Attribution** | Every AI response includes direct citations (Page, Article, Paragraph) from the source |
| **Vector Search** | ChromaDB-backed semantic search for finding related norms even with differing terminology |
| **AEC Persona** | Prompt-engineered "Technical Architect" persona for high-fidelity technical advice |

---

## 🛠️ Technical Stack

| Layer | Technology |
|---|---|
| **Orchestration** | LangChain / LangGraph |
| **LLM Engine** | Google Gemini 1.5 Pro / Flash |
| **Vector DB** | ChromaDB (Local Persistent) |
| **PDF Processing** | PyPDF2 / Unstructured |
| **Config** | Pydantic Settings |

---

## 📂 Project Structure

```text
AECAgent-RAG/
├── core/                        # Intelligence layers
│   ├── rag_engine.py            # Retrieval and LLM chain logic
│   └── embeddings.py            # Vectorization and embedding models
│
├── services/                    # Data processing services
│   └── pdf_processor.py         # Semantic chunking of PDF standards
│
├── agents/                       # Specialized AI personas
│   └── standard_expert.py       # Prompt engineering and agent tools
│
├── config/                       # Settings
│   └── settings.py              # API Keys, model names, and paths
│
├── data/                        # Local store
│   ├── vector_db/               # Persistent ChromaDB files
│   └── norms/                   # PDF storage for technical standards
│
├── tests/                       # Validation suite
│   └── test_retrieval.py        # Accuracy checks for RAG
│
├── requirements.txt             # Project dependencies
└── README.md                    # Professional documentation
```

---

## ⚡ Quick Start

### Step 1 — Bootstrap Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2 — Configure API Keys

```powershell
# Create .env from template
copy .env.example .env
```

### Step 3 — Ask a Technical Question

```python
from core.rag_engine import StandardAgent

agent = StandardAgent()
response = agent.ask("Qual o recuo mínimo para vigas em solo argiloso?")
print(response)
# → "Segundo a NBR 6118, Artigo 13.2.4, o recuo mínimo deve ser..."
```

---

## 🗺️ Roadmap

- [x] **RAG Engine** — Base retrieval pipeline with semantic search
- [x] **PDF Processor** — Initial chunking logic for large technical PDFs
- [x] **Gemini Integration** — Direct connector for high-context AEC reasoning
- [ ] **Recursive Retrieval** — Agent-driven multi-step search for complex norms
- [ ] **CAD/Revit Plugin** — UI for invoking the AI agent directly inside BIM software
- [ ] **Multi-Lingual Support** — Automatic translation of Eurocodes to local contexts

---

## 📄 License

Developed for professional recruitment and AEC research purposes.  
See internal documentation for specific licensing terms.

---

<div align="center">
  <b>Transforming passive static norms into an interactive technical brain.</b>
  <br><br>
  <i>💡 Architecture & Engineering by <b>Maycon Alves</b></i>
  <br>
  <a href="https://github.com/MayconAlvesss" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/maycon-alves-a5b9402bb/" target="_blank">LinkedIn</a>
</div>
