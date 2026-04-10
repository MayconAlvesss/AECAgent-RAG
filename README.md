# 🤖 AECAgent-RAG 

**Intelligent Retrieval-Augmented Generation for Technical Building Standards.**

This project bridges the gap between static PDF technical norms (ISO, Eurocode, NBR) and actionable engineering intelligence. Instead of manually searching through 500-page standards, AECAgent-RAG provides a conversational interface that retrieves specific clauses, verifies compliance, and cites sources with pinpoint accuracy.

---

## 🏗️ The Problem: The "Wall of Text" in AEC
Technical standards are the backbone of engineering, yet they are often trapped in flattened PDFs that are difficult to query semantically. A typical "Compliance Check" involves:
1. Finding the right standard version.
2. Manually scanning tables of contents.
3. Interpreting clauses without cross-references.

**AECAgent-RAG** solves this by treating the entire library of standards as a high-dimensional vector space.

### 🧠 Core Methodology
- **Semantic Chunking**: We don't just split by character count; we split by "Technical Article" and "Section" boundaries to preserve engineering context.
- **Hybrid Retrieval**: Combining vector similarity (ChromaDB) with keyword-heavy BM25 to ensure precise article numbers (e.g., "Section 12.3") aren't lost in the latent space.
- **Source-Grounded Synthesis**: Using Gemini 1.5's large context window to compare retrieved snippets before formulating a final engineering advisory.

---

## 📂 Architecture & Progress (Concept / Roadmap)

The repository is structured to evolve from a CLI prototype into a full-scale expert system.

### Intelligence Layers (`/core`)
- **`rag_engine.py`**: The "Brain" — manages the LangChain flow and retrieval strategies.
- **`embeddings.py`**: Vectorization logic using multilingual-e5 models optimized for technical Portuguese and English.

### Data Processing (`/services`)
- **`pdf_processor.py`**: Extracting text from standard PDFs. *[WIP: Moving from simple extraction to layout-aware parsing]*.

### Experimental Lab (`/lab`)
- **Sandbox scripts** for testing embedding density and tokenization strategies.

---

## 🛠️ Tech Stack
This project leverages **LangChain** for orchestration, **ChromaDB** for persistent vector storage, and **Google Gemini 1.5 Flash** for high-speed technical reasoning. 

---

## ⚡ Current Capabilities
You can query the agent locally after indexing your library:
```python
from core.rag_engine import StandardAgent

agent = StandardAgent()
# Example: Querying reinforcement ratios in RC beams
response = agent.ask("What is the minimum reinforcement overlap for C30 concrete according to Eurocode 2?")

print(f"Advice: {response.answer}")
print(f"Source: {response.citations[0].standard_name} | Clause {response.citations[0].article_clause}")
```

---

## 🛣️ 2028 Vision
- [ ] **Recursive Retrieval**: Enabling the agent to "dig deeper" if the first search result is ambiguous.
- [ ] **BIM Plugin**: Integration as a side-panel in Revit or Civil 3D.
- [ ] **Layout-Aware PDF Ingestion**: Correctly reading complex technical tables and diagrams.

---

<div align="center">
  <i>Part of the <b>Nexus-Twin</b> Ecosystem</i><br>
  Engineering Strategy & Implementation by **Maycon Alves**
</div>
