"""
AECAgent-RAG — Standard Expert Agent
===================================
A prompt-engineered AI agent with a persona tailored for technical
AEC consulting and standard interpretation.
"""

from typing import List

class StandardExpertAgent:
    """
    Orchestration layer for a persona-driven technical agent.
    """

    def __init__(self):
        self.system_instructions = (
            "You are an elite AEC Standard Expert. You maintain a professional, "
            "precise, and technically grounded tone. You prioritize safety and "
            "regulatory compliance in all your answers. Always cite page and article."
        )

    def format_prompt(self, query: str, context: List[str]) -> str:
        """
        Builds the final prompt for the LLM using the retrieved context.
        """
        context_block = "\n---\n".join(context)
        return (
            f"{self.system_instructions}\n\n"
            f"TECHNICAL CONTEXT FROM NORM:\n{context_block}\n\n"
            f"USER QUERY: {query}\n\n"
            "DETAILED ANSWER:"
        )

    def parse_response(self, raw_llm_response: str) -> str:
        """
        Cleans and formats the LLM output for the end-user.
        """
        # Placeholder for post-processing logic
        return raw_llm_response.strip()
