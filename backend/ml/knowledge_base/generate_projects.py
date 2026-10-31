import json
import random

domains = {
    "Healthcare": [
        "Hospital Management System","Telemedicine Platform","Medical Inventory",
        "Patient Portal","Doctor Appointment","Health Insurance System",
        "Laboratory Management","Pharmacy ERP","Medical Billing","EHR Platform"
    ],
    "Finance": [
        "Digital Banking","Investment Platform","Loan Management",
        "Expense Tracker","Accounting ERP","Insurance Portal",
        "Fraud Detection","Tax Management","Trading Platform","Payment Gateway"
    ],
    "Education": [
        "Learning Management","School ERP","University Portal",
        "Online Examination","Virtual Classroom","Attendance System",
        "Student Dashboard","Library Management","Placement Portal","Course Recommendation"
    ],
    "E-commerce": [
        "Marketplace","Inventory System","Vendor Portal",
        "Shopping Platform","Order Management","Warehouse System",
        "Retail ERP","Product Recommendation","Customer Loyalty","Subscription Store"
    ],
    "HR": [
        "HRMS","Payroll","Recruitment Portal",
        "Resume Screening","Performance System","Attendance",
        "Leave Management","Training Portal","HR Analytics","Employee Portal"
    ],
    "Travel":[
        "Hotel Booking","Flight Booking","Cab Booking","Tour Management",
        "Travel Planner","Visa Portal","Holiday Package","Tourism Platform",
        "Travel CRM","Resort Management"
    ],
    "Real Estate":[
        "Property Portal","Rental Management","Construction ERP",
        "Broker CRM","Real Estate Analytics","Property Valuation",
        "Builder Portal","Land Registry","Apartment Management","Housing Society ERP"
    ],
    "Manufacturing":[
        "Factory ERP","Production Planning","Inventory Control",
        "Machine Monitoring","Quality Management","Warehouse Automation",
        "Supply Chain","Procurement","Manufacturing Dashboard","Maintenance System"
    ],
    "Agriculture":[
        "Smart Farming","Crop Monitoring","Farmer Portal",
        "Agri Marketplace","Irrigation Monitoring","Livestock Management",
        "Soil Analytics","Drone Monitoring","Farm ERP","Agri AI"
    ],
    "Government":[
        "Citizen Portal","E-Governance","Municipality ERP",
        "Digital Voting","Police Management","Court Management",
        "Tax Portal","Land Record","Passport System","Public Grievance"
    ]
}

frontends=["React","Angular","Vue","Flutter","Next.js"]

backends=["FastAPI","Spring Boot","Node.js","Django",".NET"]

databases=["PostgreSQL","MongoDB","MySQL"]

projects=[]

pid=1

for domain,names in domains.items():

    for i in range(30):

        title=random.choice(names)

        complexity=random.choice(["Low","Medium","High"])

        if complexity=="Low":
            timeline="2 Months"
            budget="Low"

        elif complexity=="Medium":
            timeline="4 Months"
            budget="Medium"

        else:
            timeline="6 Months"
            budget="High"

        projects.append({

            "id":pid,

            "title":title,

            "domain":domain,

            "summary":f"{title} designed for modern {domain.lower()} organizations with scalability, security, analytics and automation.",

            "tech_stack":[
                random.choice(frontends),
                random.choice(backends),
                random.choice(databases)
            ],

            "complexity":complexity,

            "timeline":timeline,

            "budget":budget

        })

        pid+=1

with open("projects.json","w",encoding="utf8") as f:

    json.dump(projects,f,indent=4)

print(f"{len(projects)} projects generated.")