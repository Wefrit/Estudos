import string 
def rows(letter):
  alphabet = string.ascii_uppercase
  size = (alphabet.index(letter) * 2) + 1
  spaces = size - 2


  diamond = []
  middle = 1
  corners = alphabet.index(letter) - 1
  for l in range(alphabet.index(letter) + 1):
    if alphabet[l] == "A":
      diamond.append(alphabet[l].center(size))
    elif alphabet[l] == letter:
      diamond.append(alphabet[l] + (" "*spaces) + alphabet[l])
    else:
      diamond.append(" " * corners + alphabet[l] + " " * middle + alphabet[l] + " " * corners)
      middle += 2
      corners -= 1

  middle -= 2
  corners += 1
  for l in range(alphabet.index(letter) -1, -1, -1):
    if alphabet[l] == "A":
      diamond.append("".join(f"{alphabet[l].center(size)}"))
    elif alphabet[l] == letter:
      diamond.append(alphabet[l] + (" "*spaces) + alphabet[l])
    else:
      diamond.append(" " * corners + alphabet[l] + " " * middle + alphabet[l] + " " * corners)
      middle -= 2
      corners += 1

  return diamond
