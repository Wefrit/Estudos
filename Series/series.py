def slices(series, length):
    parts = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series: 
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        while len(series) >= length:
            parts.append(series[:length])
            series = series[1:]
    return parts
