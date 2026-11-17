def validate_output(response):
    if not isinstance(response, str):
        return False, "Response must be text."
    if not response.strip():
        return False, "Response Cannot be empty"
    if len(response) > 1000:
        return False, "Response cannot be exceed 1000 characters"

    sensitive_keywords = [
        "secret_key",
        "api_key",
        "password"
    ]

    for sensitive in sensitive_keywords:
        if sensitive in response:
            return False, "Sensitive information detected."

    return True, "Output is valid."