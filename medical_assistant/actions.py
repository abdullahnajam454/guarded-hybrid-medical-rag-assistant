from nemoguardrails.actions import action

@action(name="CheckMedicalTopicAction")
async def check_medical_topic_action(question: str):

    question = question.lower()

    # Check restricted topics FIRST
    programming_keywords = [
        "javascript",
        "python",
        "coding",
        "programming",
        "write code",
        "code for",
        "html",
        "css"
    ]

    for keyword in programming_keywords:
        if keyword in question:
            return False

    # Then check medical topics
    medical_keywords = [
        "medical",
        "health",
        "fever",
        "headache",
        "pain",
        "doctor",
        "medicine",
        "symptoms",
        "disease",
        "infection",
        "temperature",
        "cough"
    ]

    for keyword in medical_keywords:
        if keyword in question:
            return True

    return False