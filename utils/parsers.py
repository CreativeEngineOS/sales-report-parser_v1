import pandas as pd
from utils.nurphoto_mhtml_parser import parse_nurphoto_mhtml
from utils.editorialfootage_mhtml_parser import parse_editorialfootage_mhtml

def detect_agency_from_text(file_bytes):
    try:
        text = file_bytes[:1000].decode(errors="ignore").lower()
    except:
        text = ""
    if "nurphoto" in text:
        return "NurPhoto"
    elif "editorialfootage" in text or "editorial footage" in text:
        return "EditorialFootage"
    return "Unknown"

def parse_file(file_bytes, agency, filename=None):
    if agency == "NurPhoto" and filename and filename.lower().endswith(".mhtml"):
        return parse_nurphoto_mhtml(file_bytes), "NurPhoto"
    elif agency == "EditorialFootage" and filename and filename.lower().endswith(".mhtml"):
        return parse_editorialfootage_mhtml(file_bytes), "EditorialFootage"
    return None, agency
