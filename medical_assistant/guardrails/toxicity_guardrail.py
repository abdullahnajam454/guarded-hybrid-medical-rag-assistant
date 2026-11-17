def detect_toxicity(user_input):
    question = user_input.lower()

    if not question.strip():
        return False, "Input cannot be empty."

    
    toxic_keywords = [
        "stupid",
        "idiot",
        "useless",
        "shut up"
    ]

    threat_keywords = [
        "kill you",
        "hurt you",
        "attack you"
    ]

    for word in toxic_keywords:
        if word in question:
            return True, "Potentially toxic language detected."

    for threat in threat_keywords:
        if threat in question:
            return True, "Potentially threatening language detected."

    return False, "No listed toxic keywords detected."