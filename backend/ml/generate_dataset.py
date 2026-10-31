import pandas as pd
import random

domains = {
    "Healthcare": ["Hospital Management System", "AI Disease Prediction", "Patient Portal", "Medical Appointment App"],
    "Finance": ["Fraud Detection", "Online Banking", "Loan Management", "Insurance Platform"],
    "Education": ["Learning Management System", "Online Examination", "Student Portal", "Virtual Classroom"],
    "E-commerce": ["Shopping Website", "Online Marketplace", "Inventory System", "Payment Gateway"],
    "Travel": ["Hotel Booking", "Flight Reservation", "Travel Planner", "Tourism Portal"],
    "AI": ["AI Chatbot", "Resume Screening", "Image Classification", "Recommendation System"],
    "Retail": ["Inventory Management", "POS System", "Warehouse Automation", "Billing Software"]
}

complexity_map = {
    "Healthcare": "High",
    "Finance": "High",
    "Education": "Medium",
    "E-commerce": "Medium",
    "Travel": "Medium",
    "AI": "High",
    "Retail": "Low"
}

timeline_map = {
    "Low": "1 Month",
    "Medium": "3 Months",
    "High": "6 Months"
}

budget_map = {
    "Low": "Low",
    "Medium": "Medium",
    "High": "High"
}

tech = {
    "Healthcare": "Python,FastAPI,React,PostgreSQL",
    "Finance": "Python,Django,React,MySQL",
    "Education": "React,Node.js,MongoDB",
    "E-commerce": "React,Node.js,MongoDB",
    "Travel": "React,FastAPI,MySQL",
    "AI": "Python,FastAPI,PyTorch",
    "Retail": "React,Node.js,MySQL"
}

rows = []

for _ in range(5000):
    domain = random.choice(list(domains.keys()))
    project = random.choice(domains[domain])

    requirement = (
        f"Develop a {project} with secure login, dashboard, "
        f"report generation, API integration and responsive UI."
    )

    complexity = complexity_map[domain]

    rows.append({
        "requirement": requirement,
        "domain": domain,
        "complexity": complexity,
        "timeline": timeline_map[complexity],
        "budget": budget_map[complexity],
        "tech_stack": tech[domain]
    })

df = pd.DataFrame(rows)

df.to_csv("dataset/requirements_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())