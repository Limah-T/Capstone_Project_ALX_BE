Membership Management API Documentation

Capstone Project Submission
Base URL: https:/limahtechnology.pythonanywhere.com/api/

⸻

Overview

This API provides authenticated access to manage three core entities: Directors, Individual Members, and Corporate Members.
	•	Users must register or login to receive an authentication token
	•	Authenticated users can view and manage their own entries for Individual and Corporate members
	•	Director records are read-only

⸻

# Authentication

    ###Register a User
        •	POST /api/register/

    json format
    {
        "username": "yourusername",
        "password": "yourpassword",
        "confirm_password": "repeat thesame password"
    }
    
    Response (json)
    {
        "token": "your-authentication-token"
    }

    ###Login a User
	    •	POST /api/login/

    json format
    {
        "username": "yourusername",
        "password": "yourpassword"
    }

    Response (json)
    {
    "token": "your-authentication-token"
    }

# Use the Token

    Include the token in the Authorization header for all secured endpoints:
    Authorization: Token your-authentication-token

# Returns the main access links:
    /api/list-endpoints/ - GET
    Response(json)

    {
        "directors": "/api/directors/",
        "individual_member": "/api/individual_members/",
        "corporate_member": "/api/corporate_members/"
    }

# Directors Endpoints

    List Directors
        •	GET /api/directors/
        •	Filtering: ?first_name=, ?gender=, ?position_in_chambers=
        •	Searching: ?search=first_name, ?search=last_name, etc.
        •	Ordering: ?ordering=first_name, ?ordering=position_in_chambers

    Retrieve Director
        •	GET /api/director/<int:id>/

    Note: Director data is read-only for all users.

# Individual Members

    List Individual Members
        •	GET /api/individual_members/
        •	Filtering: ?first_name=, ?last_name=, ?gender=, ?sponsor=
        •	Searching: ?search=first_name, ?search=last_name, ?search=gender, ? search=sponsor
        •	Ordering: ?ordering=first_name, ?ordering=last_name ?ordering=sponsor 

    Retrieve Individual Member
        •	GET /api/individual_member/<int:id>/
        •	If creator: full data returned (email, address, etc.)
        •	If not creator: only public data (e.g. first_name, last_name, gender, sponsor)

    Register Individual Member
        •	POST /api/individual_member/register/

    json format
    {
        "first_name": "",
        "last_name": "",
        "email": "",
        "address": "",
        "phonenumber":"",
        "gender": "Check for available choices below",
        "nationality": "Check for available choices below",
        "title": "Check for available choices below",
        "profession": "Check for available choices below",
        "sponsor": "a director's id"
    }

    Update Individual Member (Get the member's ID to retrieve first)
        •	PUT/PATCH /api/individual_member/<id>/update/
        •	Only creator can update

    Delete Individual Member (Get the member's ID to retrieve first)
        •	DELETE /api/individual_member/<id>/delete/
        •	Only creator can delete

# Corporate Members

    List Corporate Members
        •	GET /api/corporate_members/
        •	Filtering: ?first_name=, ?last_name=, ?gender=, ?sponsor=
        •	Searching: ?search=first_name, ?search=last_name, ?search=gender, ?search=sponsor
        •	Ordering: ?ordering=first_name, ?ordering=last_name ?ordering=gender ?ordering=sponsor

    Retrieve Corporate Member
        •	GET /api/corporate_member/<id>/
        •	If creator: full data returned
        •	If not creator: only public fields

        json format
        {
            "first_name": "",
            "last_name": "",
            "email": "",
            "address": "",
            "phonenumber":"",
            "gender": "Check for available choices below",
            "nationality": "Check for available choices below",
            "title": "Check for available choices below",
            "company_name": "",
            "core_line_of_business": "Check for available choices below",
            "company_interest_in_hungary": ""
            "company_location": ""
            "position_in_company": ""
            "date_of_establishment": "2024-01-01",
            "reg_no": "",
            "sponsor": "a director's id"
        }

    Register Corporate Member
        •	POST /api/corporate_member/register/

    Update Corporate Member
        •	PUT/PATCH /api/corporate_member/<id>/update/
        •	Only creator can update

    Delete Corporate Member
        •	DELETE /api/corporate_member/<id>/delete/
        •	Only creator can delete

# Error Handling
    Unauthorized
    {
        "detail": "Permission denied."
    }

    Unauthenticated
    {
       "detail": "Authenticated credentials were not provided." 
    }

# Filtering / Searching / Ordering
    ---Directors---

    /api/directors/?first_name=Jane
    /api/directors/?search=chambers
    /api/directors/?ordering=last_name

    ---Individual_member---

    /api/individual_members/?gender=Female
    /api/individual_members/?search=John
    /api/individual_members/?ordering=first_name

    ---Corporate member---

    /api/corporate_members/?sponsor=XYZ
    /api/corporate_members/?search=Mary
    /api/corporate_members/?ordering=sponsor

# Permissions Matrix
Endpoints
Method(s)
Auth Required
Creator-Only Access
Description

---Detailed of each endpoint---

# Endpoints for both authenticated and unauthenticated
    /api/list-endpoints/ - GET

# Register new user 
    /api/register/ - POST
    return token in json format for authenticated user

# login
    /api/login/ - POST
    return token in json format for authenticated user

# Get token 
    /api/directors/ - GET

# View all directors
    /api/directors/- GET

# View director by ID
    /api/director/<int:id> - GET

# View all individual members
    /api/individual_members/ - GET

# View individual member by ID
    /api/individual_member/<int:id> - GET
    return full details if creator, else public

# Register a new individual member
    /api/individual_member/register/ - POST

# Update an individual member details
    if creator: /api/individual_member/<int:id>/update/ - PUT/PATCH

# Delete an individual member details
    if creator: /api/individual_member/<int:id>/delete/ - DELETE

# View all corporate members
    /api/corporate_members/ - POST

# View corporate member by ID
    /api/corporate_members/<int:id>/ - GET
    return full details if creator, else public

# Register a new corporate member
    /api/corporate_member/<int:id>/register/ - POST

# Update corporate member by ID
    if creator: /api/corporate_member/<int:id>/update/ - PUT/PATCH

# Delete corporate member by ID
    if creator: /api/corporate_member/<id>/delete/ - DELETE

### Accepted Field Values ###

---Gender choices--- 
    > 'Male',
    > 'Female'

---TITLE Choices---
    > "Arch"  
    > "Barr"  
    > "Capt"  
    > "Chief"  
    > "Col"  
    > "Dr"  
    > "Engr"  
    > "Gen"  
    > "Hon"  
    > "Imam"  
    > "King"  
    > "Lt"  
    > "Maj"  
    > "Miss"  
    > "Mr"  
    > "Mrs"  
    > "Ms"  
    > "Mx"  
    > "Pastor"  
    > "Prince"  
    > "Princess"  
    > "Prof"  
    > "Rabbi"  
    > "Queen"  
    > "Rev"  

---NATIONALITY Choices---
    > "Algerian"  
    > "American"  
    > "Argentinian"  
    > "Australian"  
    > "Austrian"  
    > "Bangladeshi"  
    > "Belgian"  
    > "Brazilian"  
    > "British"  
    > "Canadian"  
    > "Chilean"  
    > "Chinese"  
    > "Colombian"  
    > "Czech"  
    > "Danish"  
    > "Dutch"  
    > "Egyptian"  
    > "Emirati"  
    > "Ethiopian"  
    > "Finnish"  
    > "Filipino"  
    > "French"  
    > "German"  
    > "Ghanaian"  
    > "Greek"  
    > "Hungarian"  
    > "Indian"  
    > "Indonesian"  
    > "Iraqi"  
    > "Israeli"  
    > "Italian"  
    > "Japanese"  
    > "Jordanian"  
    > "Kenyan"  
    > "Kuwaiti"  
    > "Lebanese"  
    > "Malaysian"  
    > "Mexican"  
    > "Moroccan"  
    > "Nigerian"  
    > "New Zealander"  
    > "Norwegian"  
    > "Omani"  
    > "Other"  
    > "Pakistani"  
    > "Peruvian"  
    > "Polish"  
    > "Portuguese"  
    > "Qatari"  
    > "Romanian"  
    > "Russian"  
    > "Saudi Arabian"  
    > "Singaporean"  
    > "South African"  
    > "South Korean"  
    > "Spanish"  
    > "Sudanese"  
    > "Swedish"  
    > "Swiss"  
    > "Syrian"  
    > "Thai"  
    > "Turkish"  
    > "Tunisian"  
    > "Ukrainian"  
    > "Ugandan"  
    > "Venezuelan"  
    > "Vietnamese"  
    > "Zimbabwean"  

---NATURE_OF_BUSINESS Choices---
    > "Accounting & Auditing"  
    > "Agriculture"  
    > "Automobile & Machinery"  
    > "Banking"  
    > "Business Support Services"  
    > "Chemical & Pharmaceuticals"  
    > "Construction Materials"  
    > "Consulting"  
    > "Courier & Delivery Services"  
    > "E-commerce"  
    > "Electricity & Power Supply"  
    > "Electronics & Electrical"  
    > "Event Planning"  
    > "Fashion Designer"  
    > "Film & Television"  
    > "Fintech"  
    > "Fishing"  
    > "Food & Beverage Manufacturing"  
    > "Gaming & Esports"  
    > "Government & Public Administration"  
    > "Healthcare & Pharmaceuticals"  
    > "Hospitality & Tourism"  
    > "Hotels & Resorts"  
    > "Import & Export"  
    > "Information & Communication Technology"  
    > "Insurance"  
    > "Investment & Asset Management"  
    > "IT Services & Support"  
    > "Legal Services"  
    > "Manufacturing & Industrial"  
    > "Marketing & Advertising"  
    > "Media & Entertainment"  
    > "Medical Devices & Equipment"  
    > "Metal & Steel"  
    > "Mining"  
    > "Non-Profit & NGOs"  
    > "Oil & Gas"  
    > "Other"  
    > "Plastic & Rubber"  
    > "Primary & Secondary Schools"  
    > "Publishing & Printing"  
    > "Real Estate & Property Management"  
    > "Recruitment & HR Services"  
    > "Religious Organizations"  
    > "Renewable Energy"  
    > "Retail Trade"  
    > "Road Transport"  
    > "Security Services"  
    > "Software Development"  
    > "Telecommunications"  
    > "Textile & Apparel"  
    > "Trade & Commerce"  
    > "Transportation & Logistics"  
    > "Universities & Colleges"  
    > "Vocational & Technical Training"  
    > "Warehousing & Logistics"  
    > "Water Supply & Waste Management"  
    > "Wholesale Trade"  
    > "Wellness & Fitness"  

---PROFESSION Choices---
    > "Accountant"  
    > "Actor"  
    > "Architect"  
    > "Auditor"  
    > "Banker"  
    > "Carpenter"  
    > "Chef"  
    > "Civil Engineer"  
    > "Cybersecurity Analyst"  
    > "Data Scientist"  
    > "Dentist"  
    > "Doctor"  
    > "Economist"  
    > "Electrical Engineer"  
    > "Entrepreneur"  
    > "Fashion Designer"  
    > "Financial Advisor"  
    > "Investment Analyst"  
    > "Journalist"  
    > "Lawyer"
    > "Librarian"
    > "Medical Lab Scientist"
    > "Musician"
    > "Nurse"
    > "Photographer"
    > "Software Engineer"
    > "Teacher"
    > "Writer"