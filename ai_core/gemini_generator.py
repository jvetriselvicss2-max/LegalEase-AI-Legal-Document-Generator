import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing. Add it to your .env file."
            )
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
You are LegalEase, an AI-assisted legal document drafting system.

Create a professional, clearly structured draft for the following document:

Document type: {document_type}
Parties: {parties}
Effective date: {dates}
Terms and conditions: {terms}

Requirements:
1. Use clear professional language.
2. Include a title.
3. Identify the parties and effective date.
4. Organize the document into logical sections and clauses.
5. Incorporate every supplied term without inventing specific facts.
6. Include signature blocks for the relevant parties.
7. Do not claim that the document is guaranteed legally valid.
8. Add this notice at the end:
   "LegalEase disclaimer: This AI-generated draft is for general informational
   and drafting purposes and should be reviewed by a qualified legal professional
   before use."

Return only the document text.
"""
        response = self.model.generate_content(prompt)
        if not response or not getattr(response, "text", None):
            raise RuntimeError("Gemini returned an empty response.")
        return response.text.strip()
