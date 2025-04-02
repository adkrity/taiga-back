ADKRITY_PROJECT_ID = 1
SERVER_APP_BASE_URL= "https://adm.adkrity.com/api/v1/"
# SERVER_APP_BASE_URL= "http://127.0.0.1:9999/api/v1/"

# User's List of different teams
DESIGNER_TEAM = ['Ankitmakwana', 'Heta', 'Uttam', '	muktiadkrity', 'JK']
AD_PUBLISH_TEAM = ['Khushbu', '	Jenish2001', 'janviadkrity', 'prince']
CUSTOMER_SUPPORT_TEAM = []

# User Story status list
DESIGNER_STATUS_LIST = ["Client Req Done", 'Req Review Pending', 'Design Req Done', 'In Designing', 'Design Done',
                        'Client Changes', 'Design Approved', 'Ad Changes']
AD_PUBLISH_STATUS_LIST = ['Client Req Done', 'Req Review Pending', 'Client Changes', 'Design Approved',
                          'Ready to Publish', 'Ad Issues', 'Integration Issues', 'Ad Changes', 'Ad Published',
                          'Need Optimization']
CUSTOMER_SUPPORT_STATUS_LIST = []

# Role List
DESIGNER_ROLE_LIST = ["Design"]
AD_PUBLISH_ROLE_LIST = ["Social Media"]
CUSTOMER_SUPPORT_ROLE_LIST = ["Social Media"]

# Custom Attribute field list team wise
DESIGNER_FIELD_LIST = ["Company Name", "Category", "Payment Amount Received", "Logo", "Old Tickets", "Design Focus",
                       "Colour Theme", "Missing Data", "Notes for Designers", "Ad Text", "Highlight Area",
                       "Show Phone Number", "Show Address", "Layout - 1", "Layout - 2", "Layout - 3",
                       "Social media Ref" "Website"]
AD_PUBLISH_FIELD_LIST = ["Contact Number", "Connect To Whatsapp", "Company Name", "Category",
                         "We need to create design",
                         "FB Integration Status", "Instagram Connection", "Ad Type", "Ad Platforms",
                         "Payment Amount Received", "Ad Targeting", "Logo", "Old Tickets", "Design Focus",
                         "Colour Theme", "Product/Service Details", "Price/Offer Details", "Missing Data",
                         "Notes for Designers", "Ad Text", "Highlight Area",
                         "Show Phone Number", "Show Address",
                         "Social media Ref", "Website", "Ad Start Date", "Caption", "Headline", "Age Min",
                         "Age Max", "Gender", "Business Whatsapp Number",
                         "Lead Form", "Business Form", "Lead TOS Url", "Ad Interest Targeting", "FB Audience",
                         "Ad Issues"]
CUSTOMER_SUPPORT_FIELD_LIST = []

GET_MOVED_TICKETS_CONFIG = {"Design": {"to_status": [
                                                     "Design Done",
                                                     # "In Designing",
                                                     ]
                                       }}
