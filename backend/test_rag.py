from services.rag_service import retrieve_similar_projects

query = """
Need an AI based hospital management system
with appointment booking, billing,
patient records and pharmacy.
"""

projects = retrieve_similar_projects(query)

for i, project in enumerate(projects, 1):
    print(f"\nProject {i}")
    print(project)