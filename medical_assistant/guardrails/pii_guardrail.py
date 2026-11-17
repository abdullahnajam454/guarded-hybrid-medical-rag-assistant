import re

def protect_pii(user_input):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    phone_pattern = r"(?<!\d)(?:(?:\+92)|(?:0092)|(?:92)|(?:0))?3[0-9]{9}(?!\d)"

    # Detect PII
    emails = re.findall(email_pattern, user_input)
    phone_numbers = re.findall(phone_pattern, user_input)

    # Mask PII
    masked_text = re.sub(email_pattern, "[EMAIL_MASKED]", user_input)
    masked_text = re.sub(phone_pattern, "[PHONE_MASKED]", masked_text)

    return {
        "emails": emails,
        "phone_numbers": phone_numbers,
        "masked_text": masked_text
    }