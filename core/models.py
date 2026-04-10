"""
AECAgent-RAG — Data Models
==========================
Pydantic schemas for ensuring structured, citation-aware responses
consistent with global engineering standards.
"""

from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class Citation(BaseModel):
    """Reference to a specific technical manual or normative document."""
    standard_name: str = Field(..., help="Title of the norm (e.g., NBR 6118, Eurocode 2)")
    page_number: int
    article_clause: str = Field(..., help="Specific article or clause referenced")
    snippet: str = Field(..., help="The specific text fragment extracted")

class AgentResponse(BaseModel):
    """The structured output of the RAG engine."""
    answer: str = Field(..., help="The natural language answer based on retrieved context")
    citations: List[Citation]
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    metadata: Dict[str, str] = Field(default_factory=dict)

class ChunkMetadata(BaseModel):
    """Metadata for vector-db storage."""
    source_path: str
    last_updated: str
    major_category: str # e.g. 'Structural', 'Fire Safety', 'Accessibility'
