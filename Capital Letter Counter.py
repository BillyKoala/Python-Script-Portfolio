# Billy Knight - February 2022

# This routine will count the number of capital letters in a sentence or paragraph.

# Define some variables.
sentence = "ThiS iS To checK foR Capital lEtteRs"
count = 0

try:
    # Check each character. If it is in the ASCII range between 60 and 90 then increment the counter.
    for i in range(len(sentence)): count += 1 if ord(sentence[i]) in range(65, 90) else 0

    print("There are {} capital letters in the word \'{}\'".format(count, sentence))

except Exception as e:
    print(e)

finally:
    pass