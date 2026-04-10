"""
AECAgent-RAG — PDF Processor
===========================
Handles technical PDF ingestion, OCR (if needed), and semantic chunking
tailored for technical standards (Articles/Items).
"""

import logging
import re
from typing import List, Dict, Any
import PyPDF2

logger = logging.getLogger(__name__)

class PDFProcessor:
    """
    Service for extracting text and structure from AEC documents.
    Optimized for technical standards (Articles/Items).
    """

    def __init__(self, chunk_size: int = 1500, overlap: int = 200):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def process_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Parses a PDF and returns a list of chunks with metadata.
        """
        logger.info(f"Extracting technical data from: {file_path}")
        
        chunks = []
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if not text:
                        continue
                    
                    # Split page into technical articles
                    articles = self._semantic_split(text)
                    for art in articles:
                        chunks.append({
                            "text": art,
                            "metadata": {
                                "page": page_num + 1,
                                "source": file_path.split("/")[-1]
                            }
                        })
        except Exception as e:
            logger.error(f"Failed to process PDF {file_path}: {e}")
            # FIXME: Add fallback to OCR if extract_text fails (scanned PDF)
        
        return chunks

    def _semantic_split(self, text: str) -> List[str]:
        """
        Splits text based on technical markers like 'Article', 'Item', 'Section'.
        TODO: Support multi-line article headers.
        """
        # Split by typical AEC standard identifiers
        pattern = r'(?i)(Article|Art\.|Section|Item|Table|Appendix)\s*\d+[.\d]*'
        tokens = re.split(pattern, text)
        
        # Merge pattern matches back with their groups
        results = []
        for i in range(1, len(tokens), 2):
            content = f"{tokens[i]} {tokens[i+1]}".strip()
            if len(content) > 50: # Avoid tiny noise
                results.append(content)
        
        return results if results else [text]
