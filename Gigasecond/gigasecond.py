from datetime import timedelta
def add(moment):
    """Add 1 gigasecond (10^9 seconds) to a given moment."""
    return moment + timedelta(seconds=10**9)    
