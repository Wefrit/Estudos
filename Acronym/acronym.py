import re
def abbreviate(words):
    words = re.sub(r"[^a-zA-Zá-úÁ-Ú']", " ", words)
    return "".join([w[0].upper() for w in words.split()])
