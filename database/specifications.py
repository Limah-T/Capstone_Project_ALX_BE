GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
STAFF_POSITIONS = [
    ('Admin Secretary', 'Admin Secretary'),
    ('Security', 'Security'),
    ('Cleaner', 'Cleaner'),
]

DIRECTOR_POSITIONS = [
    ("president", "President"),
    ("first_vice_president", "1st Vice President"),
    ("second_vice_president", "2nd Vice President"),
    ("executive_director", "Executive Director"),
    ("executive_secretary", "Executive Secretary"),
    ("finance_secretary", "Finance Secretary/Treasurer"),
    ("publicity_secretary", "Publicity Secretary"),
    ("business_dev", "Director of Business Development"),
    ("legal_secretary", "Legal Secretary"),
    ("legal_advisor", "Legal Advisor"),
    ("treasurer", "Treasurer"),
    ("secretary", "Secretary"),
]

TITLE = [
    # General Titles
    ("Mr", "Mr."),
    ("Mrs", "Mrs."),
    ("Miss", "Miss"),
    ("Ms", "Ms."),
    ("Mx", "Mx."),

    # Professional Titles
    ("Dr", "Dr."),
    ("Engr", "Engr."),
    ("Barr", "Barr."),
    ("Prof", "Prof."),
    ("Arch", "Arch."),

    # Religious Titles
    ("Rev", "Rev."),
    ("Pastor", "Pastor"),
    ("Imam", "Imam"),
    ("Rabbi", "Rabbi"),

    # Military & Government Titles
    ("Gen", "Gen."),
    ("Col", "Col."),
    ("Maj", "Maj."),
    ("Capt", "Capt."),
    ("Lt", "Lt."),
    ("Cmdr", "Cmdr."),
    ("Hon", "Hon."),

    # Royal & Traditional Titles
    ("King", "King"),
    ("Queen", "Queen"),
    ("Prince", "Prince"),
    ("Princess", "Princess"),
    ("Chief", "Chief"),
]

# Nature of Business
NATURE_OF_BUSINESS = [
    # Agriculture & Natural Resources
    ("Agriculture", "Agriculture"),
    ("Forestry", "Forestry"),
    ("Fishing", "Fishing"),
    ("Mining", "Mining"),

    # Manufacturing & Industrial
    ("Food & Beverage Manufacturing", "Food & Beverage Manufacturing"),
    ("Textile & Apparel", "Textile & Apparel"),
    ("Chemical & Pharmaceuticals", "Chemical & Pharmaceuticals"),
    ("Automobile & Machinery", "Automobile & Machinery"),
    ("Electronics & Electrical", "Electronics & Electrical"),
    ("Plastic & Rubber", "Plastic & Rubber"),
    ("Metal & Steel", "Metal & Steel"),
    ("Construction Materials", "Construction Materials"),

    # Trade & Commerce
    ("Wholesale Trade", "Wholesale Trade"),
    ("Retail Trade", "Retail Trade"),
    ("Import & Export", "Import & Export"),
    ("E-commerce", "E-commerce"),

    # Professional & Business Services
    ("Consulting", "Consulting"),
    ("Legal Services", "Legal Services"),
    ("Accounting & Auditing", "Accounting & Auditing"),
    ("Marketing & Advertising", "Marketing & Advertising"),
    ("Real Estate & Property Management", "Real Estate & Property Management"),
    ("Recruitment & HR Services", "Recruitment & HR Services"),
    ("Business Support Services", "Business Support Services"),

    # Financial Services
    ("Banking", "Banking"),
    ("Insurance", "Insurance"),
    ("Investment & Asset Management", "Investment & Asset Management"),
    ("Fintech", "Fintech"),

    # Transportation & Logistics
    ("Road Transport", "Road Transport"),
    ("Air Transport", "Air Transport"),
    ("Maritime & Shipping", "Maritime & Shipping"),
    ("Courier & Delivery Services", "Courier & Delivery Services"),
    ("Warehousing & Logistics", "Warehousing & Logistics"),

    # Energy & Utilities
    ("Oil & Gas", "Oil & Gas"),
    ("Renewable Energy", "Renewable Energy"),
    ("Electricity & Power Supply", "Electricity & Power Supply"),
    ("Water Supply & Waste Management", "Water Supply & Waste Management"),

    # Information & Communication Technology
    ("Software Development", "Software Development"),
    ("Telecommunications", "Telecommunications"),
    ("IT Services & Support", "IT Services & Support"),
    ("Cybersecurity", "Cybersecurity"),

    # Healthcare & Pharmaceuticals
    ("Hospitals & Clinics", "Hospitals & Clinics"),
    ("Pharmaceuticals", "Pharmaceuticals"),
    ("Medical Devices & Equipment", "Medical Devices & Equipment"),
    ("Wellness & Fitness", "Wellness & Fitness"),

    # Hospitality & Tourism
    ("Hotels & Resorts", "Hotels & Resorts"),
    ("Restaurants & Catering", "Restaurants & Catering"),
    ("Travel & Tour Operators", "Travel & Tour Operators"),
    ("Event Planning", "Event Planning"),

    # Media & Entertainment
    ("Publishing & Printing", "Publishing & Printing"),
    ("Film & Television", "Film & Television"),
    ("Music & Performing Arts", "Music & Performing Arts"),
    ("Gaming & Esports", "Gaming & Esports"),

    # Education & Training
    ("Primary & Secondary Schools", "Primary & Secondary Schools"),
    ("Universities & Colleges", "Universities & Colleges"),
    ("Vocational & Technical Training", "Vocational & Technical Training"),
    ("E-learning", "E-learning"),

    # Social & Public Services
    ("Government & Public Administration", "Government & Public Administration"),
    ("Non-Profit & NGOs", "Non-Profit & NGOs"),
    ("Religious Organizations", "Religious Organizations"),
    ("Security Services", "Security Services"),

    # Miscellaneous
    ("Other", "Other"),
]

# Profession
PROFESSIONS = [
    # Medical & Healthcare
    ("Doctor", "Doctor"),
    ("Nurse", "Nurse"),
    ("Pharmacist", "Pharmacist"),
    ("Dentist", "Dentist"),
    ("Medical Lab Scientist", "Medical Lab Scientist"),
    ("Physiotherapist", "Physiotherapist"),
    ("Surgeon", "Surgeon"),
    ("Veterinarian", "Veterinarian"),
    ("Psychologist", "Psychologist"),
    ("Optometrist", "Optometrist"),
    
    # Engineering & Technology
    ("Civil Engineer", "Civil Engineer"),
    ("Mechanical Engineer", "Mechanical Engineer"),
    ("Electrical Engineer", "Electrical Engineer"),
    ("Software Engineer", "Software Engineer"),
    ("Data Scientist", "Data Scientist"),
    ("Cybersecurity Analyst", "Cybersecurity Analyst"),
    ("Telecommunications Engineer", "Telecommunications Engineer"),
    ("Architect", "Architect"),
    ("Surveyor", "Surveyor"),
    
    # Business & Finance
    ("Accountant", "Accountant"),
    ("Auditor", "Auditor"),
    ("Banker", "Banker"),
    ("Investment Analyst", "Investment Analyst"),
    ("Financial Advisor", "Financial Advisor"),
    ("Tax Consultant", "Tax Consultant"),
    ("Economist", "Economist"),
    
    # Legal & Compliance
    ("Lawyer", "Lawyer"),
    ("Judge", "Judge"),
    ("Legal Consultant", "Legal Consultant"),
    
    # Education & Research
    ("Teacher", "Teacher"),
    ("Professor", "Professor"),
    ("Researcher", "Researcher"),
    ("Librarian", "Librarian"),
    
    # Media & Communication
    ("Journalist", "Journalist"),
    ("Writer", "Writer"),
    ("Editor", "Editor"),
    ("Public Relations Officer", "Public Relations Officer"),
    ("Digital Marketer", "Digital Marketer"),
    
    # Arts & Entertainment
    ("Musician", "Musician"),
    ("Actor", "Actor"),
    ("Film Director", "Film Director"),
    ("Photographer", "Photographer"),
    ("Graphic Designer", "Graphic Designer"),
    ("Fashion Designer", "Fashion Designer"),
    
    # Hospitality & Tourism
    ("Hotel Manager", "Hotel Manager"),
    ("Tour Guide", "Tour Guide"),
    ("Event Planner", "Event Planner"),
    ("Chef", "Chef"),
    
    # Skilled Trades
    ("Electrician", "Electrician"),
    ("Plumber", "Plumber"),
    ("Carpenter", "Carpenter"),
    ("Mechanic", "Mechanic"),
    
    # Security & Law Enforcement
    ("Police Officer", "Police Officer"),
    ("Military Personnel", "Military Personnel"),
    ("Firefighter", "Firefighter"),
    ("Security Guard", "Security Guard"),
    
    # Miscellaneous
    ("Entrepreneur", "Entrepreneur"),
    ("Social Worker", "Social Worker"),
    ("Clergy", "Clergy"),
    ("Other", "Other"),
]

# Nationality
NATIONALITIES = [
    ("Nigerian", "Nigerian"),
    ("Hungarian", "Hungarian"),
    ("American", "American"),
    ("British", "British"),
    ("Canadian", "Canadian"),
    ("German", "German"),
    ("French", "French"),
    ("Italian", "Italian"),
    ("Spanish", "Spanish"),
    ("Chinese", "Chinese"),
    ("Japanese", "Japanese"),
    ("Indian", "Indian"),
    ("Brazilian", "Brazilian"),
    ("South African", "South African"),
    ("Kenyan", "Kenyan"),
    ("Ghanaian", "Ghanaian"),
    ("Egyptian", "Egyptian"),
    ("Russian", "Russian"),
    ("Australian", "Australian"),
    ("Mexican", "Mexican"),
    ("Saudi Arabian", "Saudi Arabian"),
    ("Argentinian", "Argentinian"),
    ("South Korean", "South Korean"),
    ("Turkish", "Turkish"),
    ("Swiss", "Swiss"),
    ("Dutch", "Dutch"),
    ("Swedish", "Swedish"),
    ("Danish", "Danish"),
    ("Finnish", "Finnish"),
    ("Norwegian", "Norwegian"),
    ("Portuguese", "Portuguese"),
    ("Ukrainian", "Ukrainian"),
    ("Polish", "Polish"),
    ("Thai", "Thai"),
    ("Malaysian", "Malaysian"),
    ("Indonesian", "Indonesian"),
    ("Filipino", "Filipino"),
    ("Pakistani", "Pakistani"),
    ("Bangladeshi", "Bangladeshi"),
    ("Colombian", "Colombian"),
    ("Venezuelan", "Venezuelan"),
    ("Chilean", "Chilean"),
    ("Peruvian", "Peruvian"),
    ("New Zealander", "New Zealander"),
    ("Singaporean", "Singaporean"),
    ("Czech", "Czech"),
    ("Austrian", "Austrian"),
    ("Belgian", "Belgian"),
    ("Greek", "Greek"),
    ("Romanian", "Romanian"),
    ("Vietnamese", "Vietnamese"),
    ("Israeli", "Israeli"),
    ("Emirati", "Emirati"),
    ("Qatari", "Qatari"),
    ("Omani", "Omani"),
    ("Kuwaiti", "Kuwaiti"),
    ("Iraqi", "Iraqi"),
    ("Syrian", "Syrian"),
    ("Lebanese", "Lebanese"),
    ("Jordanian", "Jordanian"),
    ("Moroccan", "Moroccan"),
    ("Tunisian", "Tunisian"),
    ("Algerian", "Algerian"),
    ("Sudanese", "Sudanese"),
    ("Ethiopian", "Ethiopian"),
    ("Ugandan", "Ugandan"),
    ("Zimbabwean", "Zimbabwean"),
    ("Other", "Other"),
]
from django.core.validators import RegexValidator
reg_no_validator = RegexValidator(
    regex=r'^[A-Za-z0-9\-\/\.]+$',  # Allows letters, numbers, hyphens, slashes, and dots
    message="Registration number can only contain letters, numbers, '-', '/', and '.'"
)