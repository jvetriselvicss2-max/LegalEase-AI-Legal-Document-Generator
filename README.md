# LegalEase - AI-Powered Legal Document Generator

LegalEase is an AI-assisted legal document drafting application. It uses a Streamlit frontend, FastAPI backend, and Google Gemini for generating editable drafts of legal documents.

## Features

- Employment contracts
- NDAs
- Lease agreements
- Freelance contracts
- General agreements
- Editable preview
- TXT, DOCX and PDF downloads
- Gemini AI integration
- Environment-variable based API key handling
- Legal disclaimer

## Architecture

Streamlit Frontend -> FastAPI Backend -> Gemini AI
                                      -> Document formatting

## Project Structure

```text
LegalEase-AI-Legal-Document-Generator/
├── app.py
├── main.py
├── routes.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
├── utils/
│   ├── __init__.py
│   ├── document_formatter.py
│   └── helpers.py
├── assets/
└── outputs/
```

## Setup

1. Install Python 3.10 or newer.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env`.
5. Add your own Gemini API key to `.env`.

Never upload `.env` or your API key to GitHub.

## Run the backend

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Run the frontend

Open another terminal:

```bash
streamlit run app.py
```

The Streamlit interface will open in your browser.

## API

### GET /

Checks whether the backend is running.

### POST /generate

Example JSON:

```json
{
  "document_type": "NDA",
  "parties": "Jane Doe (Disclosing Party), ABC Corp (Receiving Party)",
  "terms": "Confidentiality must be maintained; No disclosure to third parties",
  "dates": "April 10, 2025"
}
```

## Legal Disclaimer

LegalEase provides AI-generated drafting assistance for general informational purposes. It is not a substitute for advice from a qualified lawyer. Generated documents should be reviewed by an appropriate legal professional before use.
