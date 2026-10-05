import os
import requests
import streamlit as st
from dotenv import load_dotenv
from utils.document_formatter import format_docx, format_pdf, format_txt
from utils.helpers import format_html_preview

load_dotenv()

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")

st.markdown(
    """
    <style>
    .main-title { text-align:center; font-size:42px; font-weight:700; }
    .subtitle { text-align:center; color:#666; margin-bottom:25px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">⚖️ LegalEase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True,
)

backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

if "document" not in st.session_state:
    st.session_state.document = ""

with st.form("legal_form"):
    document_type = st.selectbox(
        "Document Type",
        ["Employment Contract", "NDA", "Lease Agreement",
         "Freelance Work Contract", "General Agreement", "Other"]
    )
    parties = st.text_area(
        "Parties Involved",
        placeholder="Example: Jane Doe (Service Provider), TechNova Inc. (Client)"
    )
    terms = st.text_area(
        "Terms & Conditions",
        placeholder="Separate clauses with semicolons;\nPayment within 30 days; Confidentiality must be maintained;"
    )
    dates = st.text_input("Effective Date", placeholder="April 10, 2025")
    submitted = st.form_submit_button("Generate Document", type="primary")

if submitted:
    if not parties.strip() or not terms.strip() or not dates.strip():
        st.error("Please fill in all required fields.")
    else:
        try:
            response = requests.post(
                f"{backend_url}/generate",
                json={
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates,
                },
                timeout=120,
            )
            response.raise_for_status()
            st.session_state.document = response.json()["document"]
            st.success("Document generated successfully.")
        except requests.RequestException as exc:
            st.error(
                "Could not connect to the FastAPI backend. "
                "Start the backend with: uvicorn main:app --reload"
            )
            st.caption(str(exc))

if st.session_state.document:
    st.subheader("Document Preview")
    edited = st.text_area(
        "Edit Document",
        value=st.session_state.document,
        height=500,
    )
    st.session_state.document = edited

    st.markdown("### Preview")
    st.markdown(format_html_preview(edited), unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            "Download TXT",
            data=format_txt(edited),
            file_name="LegalEase_Document.txt",
            mime="text/plain",
        )
    with col2:
        docx_bytes = format_docx(edited, document_type)
        st.download_button(
            "Download DOCX",
            data=docx_bytes,
            file_name="LegalEase_Document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    with col3:
        pdf_bytes = format_pdf(edited, document_type)
        st.download_button(
            "Download PDF",
            data=pdf_bytes,
            file_name="LegalEase_Document.pdf",
            mime="application/pdf",
        )

st.divider()
st.caption(
    "Legal disclaimer: LegalEase provides AI-generated drafting assistance "
    "for general informational purposes. It is not a substitute for advice "
    "from a qualified lawyer."
)
