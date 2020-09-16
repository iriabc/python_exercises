
def longest_vowel_strings(word):
    """
    Maximise the length of the remaining string after removing at most two substrings of any
    length from the given string such that the remaining string contains only vowels.

    Note that the answer may be 0 if we remove the entire string.
    """

    vowels = ("a", "e", "i", "o", "u")

    # Count the length of each vowel substring
    num_vowels = []
    count = 0
    for char in word:
        # If it is a vowels then count it
        if char in vowels:
            count += 1
        # No more vowels but some in count
        elif count:
            num_vowels.append(count)
            count = 0

    if count != 0:
        num_vowels.append(count)

    # If it contains only vowels then return its length
    if num_vowels and max(num_vowels) == len(word):
        return len(word)

    # If the first char is not a vowel, we need to cut the first chunk
    if word[0] not in vowels:
        num_vowels = [0] + num_vowels

    # If the last char is not a vowel, we need to cut the last chunk
    if word[-1] not in vowels:
        num_vowels = num_vowels + [0]

    # Max length of vowels will be max head + max tail + max middle
    longest = num_vowels[0] + num_vowels[-1] + max(num_vowels[1:-1]) if len(num_vowels) > 2 \
        else sum(num_vowels)

    return longest
