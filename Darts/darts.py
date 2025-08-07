def score(x, y):
    """Calculate the score of a dart throw given its (x, y) coordinates.
    The scoring regions are defined as follows:
    - 10 points for a radius <= 1
    - 5 points for a radius <= 5
    - 1 point for a radius <= 10
    - 0 points for a radius > 10
    Args:
        x (float): The x-coordinate of the dart throw.
        y (float): The y-coordinate of the dart throw.
    Returns:
        int: The score based on the dart's distance from the center.
    """
    radius = (x**2 + y**2)**0.5
    if radius <= 1:
        return 10
    elif radius <= 5:
        return 5
    elif radius <= 10:
        return 1
    else:
        return 0
    