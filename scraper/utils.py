# Helper functions for scraping
import re
def extract_pincode(text):
    match = re.search(r"\b\d{6}\b", text)
    return match.group() if match else None