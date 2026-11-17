def topic_guardrail(user_input):
    question = user_input.lower()

    if not question.strip():
        return False, "Input cannot be empty."

    programming_keywords = [
        "javascript", "python", "coding",
        "programming", "write code", "code for"
    ]

    for keyword in programming_keywords:
        if keyword in question:
            return False, "Programming questions are not allowed."

    medical_keywords = [
        "medical", "health", "fever", "headache",
        "pain", "doctor", "medicine", "symptoms",
        "disease", "infection", "temperature", "cough",
        "diabetes", "blood sugar", "insulin", "glucose", 
        "hypertension", "blood pressure", "asthma", "cancer","dehydration",
        "cold"
    ]

    for keyword in medical_keywords:
        if keyword in question:
            return True, "Medical-related question detected."

    return False, "I can only answer medical-related questions."