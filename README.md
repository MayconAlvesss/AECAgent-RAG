<p align="center">
  <img src="https://img.icons8.com/wired/128/007ACC/artificial-intelligence.png" width="80" />
</p>



# <p align="center">AECAgent-RAG</p>

> [!IMPORTANT]
> **Project Status: Concept / Scaffold (2028+)**
> This repository is part of Maycon Alves' technical vision for the AEC Tech ecosystem. It is currently in the **concept and initial architecture phase**. Full development and core implementation will resume after the author returns from his mission in **2028**.


<p align="center">
  <strong>Intelligent Retrieval-Augmented Generation for Technical Building Standards.</strong><br>
  An engineering-centric AI agent designed to navigate, interpret, and verify compliance across ISO, Eurocode, and NBR documentation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Engine-LangChain-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/LLM-Gemini_1.5_Pro-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/VectorDB-ChromaDB-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Prototype-444444?style=flat-square" />
</p>

---

## 🧠 Technical Abstract
AECAgent-RAG addresses the "Normative Retrieval Gap" in the AEC industry. By vectorizing complex, unstructured PDF technical standards and applying **Semantic Chunking**, the agent provides high-fidelity, citation-grounded answers to critical engineering compliance questions.

### Core Intelligence
- **Latent Vector Search**: Finds semantic matches even when terminology differs across global standards.
- **Source-Grounded Synthesis**: Every response is cross-referenced with specific article numbers (e.g., *Section 12.3*) to prevent hallucinations.
- **Hybrid Retrieval (BM25 + Vector)**: Optimized for capturing both structural concepts and exact normative keys.

## 🏗️ Internal Architecture

### 1. The Kernel (`/core`)
- **`rag_engine.py`**: The agent's brain. Manages the orchestration between the document store and the LLM synthesis layer.
- **`embeddings.py`**: Vectorization logic using technical-domain models.

### 2. Processing (`/services`)
- **`pdf_processor.py`**: Specialized extraction logic focused on identifying article boundaries in multi-column PDF layouts.

### 3. Experimental Lab (`/lab`)
- **`test_extraction.py`**: Evaluation scripts for measuring retrieval accuracy against mock engineering scenarios.

---

## 🚀 Getting Started

```bash
# Setup Environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run a Compliance Query
python -m core.rag_engine --query "What is the minimum overlap for C25 concrete?"
```

---
<p align="center">
  <i>Part of the <b>Nexus-Twin</b> Ecosystem | Engineering Strategy by <b>Maycon Alves</b></i>
</p>
