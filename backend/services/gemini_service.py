import os
from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Load Gemini API
# --------------------------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# --------------------------------------------------
# Document Classification
# --------------------------------------------------

def classify_document(document_text):

    prompt = f"""
You are an AI document classifier.

Classify the uploaded document into ONLY ONE of the following categories:

Requirement
Resume
Certificate
Business Proposal
Other

Requirement documents generally contain:
- Client requirements
- Functional requirements
- Non-functional requirements
- Business requirements
- Software requirements
- System requirements
- Scope of work
- Project scope

Return ONLY the category name.

Document:

{document_text[:4000]}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print(f"Gemini Classification Error: {e}")

        return "Other"


# --------------------------------------------------
# Proposal Generation
# --------------------------------------------------

def generate_proposal(requirement):

    prompt = f"""
You are an expert Software Solution Architect and Proposal Writer.

Generate a professional software project proposal based on the client's requirements.

Client Requirement:

{requirement}

Generate the proposal using the following sections:

1. Executive Summary
2. Problem Statement
3. Proposed Solution
4. Scope of Work
5. Key Features
6. Deliverables
7. Technology Stack
8. Project Timeline
9. Team Structure
10. Assumptions
11. Risks & Mitigation
12. Terms & Conditions
13. Conclusion

Write the proposal in a professional and well-structured format.
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini API Error: {str(e)}"