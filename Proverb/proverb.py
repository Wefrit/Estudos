def proverb(*items, qualifier=None):
    lines = []
    if items:
        for item in range(len(items) - 1):
            lines.append(f"For want of a {items[item]} the {items[item+1]} was lost.")
        last_item = items[0]
        if qualifier:
            last_item = f"{qualifier} {last_item}"
        lines.append(f"And all for the want of a {last_item}.")

    return lines
