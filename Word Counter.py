"""
Billy Knight - February 2022

This module will count each individual word in a sentence
or paragraph, and print out each word alongside it's word count.

All leading/trailing spaces, comma's and full stops will be removed.
"""

# Define some variables here.
word_dict = {}
word_items = {}
words_sorted = {}

try:
    # Use Lorem Ipsum to create a large latin paragraph.
    sentence="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultricies sollicitudin nisl, sit amet aliquam nulla semper a."\
    "Maecenas vulputate iaculis nibh, non sollicitudin est scelerisque id. Vivamus sit amet rutrum lorem. Sed dolor arcu, vestibulum sit amet "\
    "condimentum sed, tristique ac lorem. Nullam a facilisis elit, et venenatis quam. Nullam quis condimentum tortor. Curabitur ac suscipit nibh."\
    "Nulla facilisi. Aenean ligula magna, condimentum et tellus a, commodo dignissim nibh. Ut pretium tincidunt diam, quis egestas lorem molestie "\
    "vitae. Integer vel ultricies ipsum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc ac eros "\
    "ac est tincidunt commodo ac lacinia metus. Mauris fringilla rutrum eros quis posuere. Nam ultrices leo sed mi pharetra, vitae aliquam nunc "\
    "iaculis. Mauris posuere nibh ex, sed consequat risus pellentesque a."

    # Split up all the words in the
    # paragraph and make them all lower case.
    words = sentence.lower().split()

    # Loop through and count each word.
    for word in words:

        # Remove leading/trailing spaces, comma's and full stops.
        word = word.strip().replace(",", "").replace(".", "")

        sentence.count(word)

        word_dict[word] = sentence.count(word)

    # Finally, sort the words into alphabetical order.
    word_items = word_dict.items()
    words_sorted = sorted(word_items)

    # Print
    print("\nSENTENCE: {}\n\nSENTENCE WORD COUNT: {}".format(sentence, words_sorted))

except Exception as e:
    print(e)

finally:
    pass