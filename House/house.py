poem = {1: "This is the house that Jack built.",

2: "This is the malt"
"that lay in the house that Jack built.",

3: "This is the rat"
"that ate the malt"
"that lay in the house that Jack built.",

4: "This is the cat" 
"that killed the rat"
"that ate the malt " 
"that lay in the house that Jack built.",

5: "This is the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

6: "This is the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

7: "This is the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

8: "This is the man all tattered and torn"
"that kissed the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

9: "This is the priest all shaven and shorn"
"that married the man all tattered and torn"
"that kissed the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

10: "This is the rooster that crowed in the morn"
"that woke the priest all shaven and shorn"
"that married the man all tattered and torn"
"that kissed the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

11: "This is the farmer sowing his corn"
"that kept the rooster that crowed in the morn"
"that woke the priest all shaven and shorn"
"that married the man all tattered and torn"
"that kissed the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built.",

12: "This is the horse and the hound and the horn"
"that belonged to the farmer sowing his corn"
"that kept the rooster that crowed in the morn"
"that woke the priest all shaven and shorn"
"that married the man all tattered and torn"
"that kissed the maiden all forlorn"
"that milked the cow with the crumpled horn"
"that tossed the dog"
"that worried the cat"
"that killed the rat"
"that ate the malt"
"that lay in the house that Jack built."}

def recite(start_verse, end_verse):
    """Recite the verses of the song 'This is the House that Jack Built'.

    :param start_verse: int - the verse to start reciting from.
    :param end_verse: int - the verse to end reciting at.
    :return: list of str - the verses of the song from start to end.    
    """
    return [poem[i] for i in range(start_verse, end_verse+1)]

print(recite(1,2))
