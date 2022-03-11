"""
Billy Knight - February 2022

This module will spell check a sentence or
paragraph and make any necessary changes.
"""

from textblob import TextBlob

try:

    # Define a few variables here.
    sentence_spell_checked = ""
    word = ""
    counter = 0

    # Get user input to spell check.
    bad_sentence = input("Please input a sentence you want to spell check: ")

    # Break up the sentence into individual words.
    sentence = bad_sentence.split()

    """ 
    Loop to each word and correct it. 
    Append it to the 'sentence_spell_checked' variable. 
    Make sure to put a space after each word except the last one. 
    """
    for word in sentence:
        sentence_spell_checked += str(TextBlob(word).correct())
        sentence_spell_checked += " " if (counter < len(sentence) - 1) else ""
        counter += 1
    
    print(f"Original Sentence: {bad_sentence}\nSpell Checked Sentence: {sentence_spell_checked}"

except Exception as e:
    print(e)

finally:
    pass
