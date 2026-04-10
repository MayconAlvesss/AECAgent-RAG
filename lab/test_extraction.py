"""
Lab Script: Test Extraction 🧪
============================
Quick and dirty test to verify if the regex patterns are capturing 
Eurocode vs NBR article formats correctly. 
"""

from services.pdf_processor import PDFProcessor

def run_test():
    processor = PDFProcessor()
    
    # Mock technical text from a standard
    sample_text = """
    Section 1.2 Normative References
    Building materials shall comply with ISO 9001.
    
    Article 12.3 Reinforcement Overlap
    The overlap length shall be no less than 40 diameters.
    
    Item 4 Transition Zones
    Special care must be taken in seismic regions.
    """
    
    print("--- Running Semantic Extraction Test ---")
    chunks = processor._semantic_split(sample_text)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk[:50]}...")
    
    assert len(chunks) == 3
    print("--- SUCCESS: All markers detected correctly ---")

if __name__ == "__main__":
    run_test()
