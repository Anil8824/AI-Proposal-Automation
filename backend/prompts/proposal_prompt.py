def build_prompt(requirement, analysis, similar_projects):

    context = ""

    for i, project in enumerate(similar_projects, start=1):

        context += f"""
Project {i}
Title: {project['title']}
Domain: {project['domain']}
Summary: {project['summary']}
Technology Stack: {", ".join(project['tech_stack'])}

"""

    return f"""
You are a Senior Presales Solution Architect.

Generate a professional software proposal based on the client requirement.

==================================================
CLIENT REQUIREMENT
==================================================

{requirement}

==================================================
AI ANALYSIS
==================================================

Domain      : {analysis["domain"]}
Complexity  : {analysis["complexity"]}
Timeline    : {analysis["timeline"]}
Budget      : {analysis["budget"]}

==================================================
SIMILAR PROJECTS
==================================================

{context}

==================================================
IMPORTANT INSTRUCTIONS
==================================================

- Use the retrieved projects only for inspiration.
- Do NOT copy them.
- Do NOT invent fake percentages.
- Do NOT invent ROI.
- Do NOT invent statistics.
- Keep the proposal realistic.
- Use professional consulting language.

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

Generate only the proposal.
"""