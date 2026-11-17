def validate_input(user_input):

    if not isinstance(user_input, str):
        return False, "Input must be text."
    if not user_input.strip():
        return False, "Input cannot be empty"
    if len(user_input) > 1000:
        return False, "Input cannot exceed 1000 characters."
    return True, "Input is valid"