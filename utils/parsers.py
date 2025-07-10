import io
import pandas as pd
import fitz  # PyMuPDF for PDF text parsing
from utils.nurphoto_mhtml_parser import parse_nurphoto_mhtml
from utils.editorialfootage_mhtml_parser import parse_editorialfootage_mhtml

def detect_agency_from_text(file_bytes):
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        first_page_text = doc[0].get_text().lower()
    except:
        first_page_text = file_bytes[:1000].decode(errors="ignore").lower()

    if "nurphoto" in first_page_text:
        return "NurPhoto"
    elif "editorialfootage" in first_page_text or "editorial footage" in first_page_text:
        return "EditorialFootage"
    elif "getty" in first_page_text or "istock" in first_page_text:
        return "Getty/iStock"
    return "Unknown"

def parse_pdf(file_bytes, agency, with_keywords=False, filename=None):
    if agency == "NurPhoto" and filename and filename.lower().endswith(".mhtml"):
        return parse_nurphoto_mhtml(file_bytes), "NurPhoto"
    elif agency == "EditorialFootage" and filename and filename.lower().endswith(".mhtml"):
        return parse_editorialfootage_mhtml(file_bytes), "EditorialFootage"
    return None, agency
