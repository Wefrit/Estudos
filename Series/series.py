def slices(series, length):
    parts = []
    while len(series) >= length:
        parts.append(series[:length])
        series = series[1:]
    return parts
print(slices("123456", 4))