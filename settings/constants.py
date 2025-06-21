from django.conf import settings
from django.templatetags.static import static

ADKRITY_PROJECT_ID = 1
if settings.DEBUG:
    ADKRITY_PROJECT_ID = 3
SERVER_APP_BASE_URL= "https://adm.adkrity.com/api/v1/"
# SERVER_APP_BASE_URL= "http://127.0.0.1:9999/api/v1/"

TAIGA_TICKET_URL = "https://task.adkrity.com/"
if settings.DEBUG:
    TAIGA_TICKET_URL = "http://127.0.0.1:8000/"

# PLACEHOLDER_IMAGE_LINK = TAIGA_TICKET_URL+"taiga/projects/designers/templates/assets/ad-placeholder-generic.jpg"
PLACEHOLDER_IMAGE_LINK = static("ad-placeholder-generic.jpg")
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
                                                     ],
                                        "team_lead_wp_number": ["919909866863",],
                                        "pending_work": ["Design Req Done",],
                                        # "team_lead_wp_number": ["919975722243",], # testing
                                       }
}

DESIGNER_FONT_FOLDER = 'dfonts'
DESIGNER_MEDIA_FOLDER = 'dm'

CUSTOM_ATTRIBUTE_IDS = {
    "contact_number": 2,
    "connect_to_whatsapp": 31,
    "company_name": 1,
    "category": 3,
    "we_need_to_create_design": 28,
    "fb_integration_status": 29,
    "instagram_connection": 30,
    "ad_type": 27,
    "ad_platforms": 41,
    "payment_amount_received": 26,
    "ad_targeting": 6,
    "old_tickets": 9,
    "logo": 12,
    "design_focus": 14,
    "colour_theme": 15,
    "product_service_details": 43,
    "price_offer_details": 44,
    "missing_data": 45,
    "notes_for_designers": 10,
    "ad_text": 21,
    "design_guidelines": 59,
    "highlight_area": 7,
    "show_phone_number": 8,
    "show_address": 18,
    "layout_1": 22,
    "layout_2": 23,
    "layout_3": 24,
    "other_layouts": 13,
    "social_media_ref": 17,
    "website": 19,
    "ad_start_date": 4,
    "drive_link": 11,
    "caption": 42,
    "headline": 53,
    "age_min": 46,
    "age_max": 47,
    "gender": 48,
    "business_whatsapp_number": 56,
    "lead_form": 49,
    "business_form": 50,
    "lead_tos_url": 51,
    "ad_interest_targeting": 54,
    "fb_audience": 52,
    "ad_issues": 55,
    "ad_id": 60,
    "business_id": 61
}
if settings.DEBUG:
    CUSTOM_ATTRIBUTE_IDS = {
        "contact_number": 2,
        "connect_to_whatsapp": 3,
        "company_name": 4,
        "category": 5,
        "we_need_to_create_design": 6,
        "fb_integration_status": 7,
        "instagram_connection": 8,
        "ad_type": 9,
        "ad_platforms": 10,
        "payment_amount_received": 11,
        "ad_targeting": 12,
        "old_tickets": 13,
        "logo": 14,
        "design_focus": 15,
        "colour_theme": 16,
        "product_service_details": 17,
        "price_offer_details": 18,
        "missing_data": 19,
        "notes_for_designers": 20,
        "ad_text": 21,
        "design_guidelines": 49,
        "highlight_area": 22,
        "show_phone": 23,
        "show_address": 24,
        "layout_1": 25,
        "layout_2": 26,
        "layout_3": 27,
        "other_layouts": 28,
        "social_media_ref": 29,
        "website": 30,
        "ad_start_date": 31,
        "drive_link": 32,
        "caption": 33,
        "headline": 34,
        "age_min": 35,
        "age_max": 36,
        "gender": 37,
        "business_whatsapp_number": 38,
        "lead_form": 39,
        "business_form": 40,
        "lead_tos_url": 41,
        "ad_interest_targeting": 42,
        "fb_audience": 43,
        "ad_issues": 44,
        "ad_id": 50,
        "business_id": 51
    }
