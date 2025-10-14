from django.conf import settings
from django.templatetags.static import static

ADKRITY_PROJECT_ID = 1
if settings.DEBUG:
    ADKRITY_PROJECT_ID = 2
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

WEBHOOK_BLACKLIST_CUSTOM_ATTRS = ["Company Name", "Category", "Tags", "Notes For Designers", "Ad Text", "Colour Theme", "Design Focus", "Business Id", "Ad Id"]
WEBHOOK_BLACKLIST_OTHER_PARAMS = ["description_diff", "assigned_users", "final_attachments", "attachments", "team_requirement", "client_requirement", "due_date"]

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
    "business_id": 61,
    "tags":64,
}
if settings.DEBUG:
    CUSTOM_ATTRIBUTE_IDS = {
        "company_name": 1,
        "contact_number": 2,
        "category": 3,
        "ad_start_date": 4,
        "ad_targeting": 5,
        "highlight_area": 6,
        "show_phone": 7,
        "old_tickets": 8,
        "notes_for_designers": 9,
        "drive_link": 10,
        "logo": 11,
        "other_layouts": 12,
        "design_focus": 13,
        "colour_theme": 14,
        "social_media_ref": 15,
        "show_address": 16,
        "website": 17,
        "ad_text": 18,
        "layout_1": 19,
        "layout_2": 20,
        "layout_3": 21,
        "payment_amount_received": 22,
        "ad_type": 23,
        "we_need_to_create_design": 24,
        "fb_integration_status": 25,
        "instagram_connection": 26,
        "connect_to_whatsapp": 27,
        "ad_platforms": 28,
        "caption": 29,
        "product_service_details": 30,
        "price_offer_details": 31,
        "missing_data": 32,
        "headline": 40,
        "age_min": 33,
        "age_max": 34,
        "gender": 35,
        "lead_form": 36,
        "business_form": 37,
        "lead_tos_url": 38,
        "fb_audience": 39,
        "ad_interest_targeting": 41,
        "ad_issues": 42,
        "business_whatsapp_number": 43,
        "design_guidelines": 44,
        "ad_id": 45,
        "business_id": 46,
        "pixel_id": 47,
        "pixel_sales_event": 48,
        "tags": 49,
    }
