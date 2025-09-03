def two_fer(name=None):
    """ Given a name, return a string in the form of "One for X, one for me."
        where X is the given name. If no name is given, use "you" instead.
    """
    who = {0: name, 1: "you"}
    return f"One for {who[0]}, one for me." if name else f"One for {who[1]}, one for me." 
