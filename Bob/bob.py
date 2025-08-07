def is_question(hey_bob):
    """Check if the input string is a question.
    Args:
        hey_bob (str): The input string to check.
    Returns:
        bool: True if the input string is a question, False otherwise.
        """
    return hey_bob.endswith("?")

def is_yelling(hey_bob):
    """Check if the input string is yelling.
    Args:
        hey_bob (str): The input string to check.
    Returns:
        bool: True if the input string is yelling, False otherwise.
    """
    return hey_bob.isupper()

def is_silent(hey_bob):
    """Check if the input string is silent (empty or only whitespace).
    Args:
        hey_bob (str): The input string to check.
    Returns:
        bool: True if the input string is silent, False otherwise.
    """
    return not hey_bob.strip()

def response(hey_bob):
    """Generate a response based on the input string.
    Args:
        hey_bob (str): The input string to respond to.
    Returns:
        str: The appropriate response based on the input string.
    """
    hey_bob = hey_bob.strip()
    if is_question(hey_bob) and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif is_question(hey_bob):
        return "Sure."
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    elif is_silent(hey_bob):
        return "Fine. Be that way!"
    else:
        return "Whatever."
