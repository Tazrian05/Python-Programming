from wordscore import score_word
from itertools import permutations

def load_valid_words():
    """Load valid Scrabble words from the file."""
    with open("sowpods.txt", "r") as infile:
        return {word.strip().upper() for word in infile}

def generate_possible_combinations(rack):
    wildcard_count = rack.count('*') + rack.count('?')
    if wildcard_count > 2:
        return set()

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possible_combinations = set()

    for i in range(2 - wildcard_count, 8):
        if wildcard_count == 1:
            possible_combinations.update([''.join(p).replace('*', c).replace('?', c) for p in permutations(rack.upper(), i) for c in letters])
        elif wildcard_count == 2:
            possible_combinations.update([''.join(p).replace('*', c1).replace('?', c2) for p in permutations(rack.upper(), i) for c1 in letters for c2 in letters])
        else:
            possible_combinations.update([''.join(p) for p in permutations(rack.upper(), i)])

    return possible_combinations


def run_scrabble(rack):
    """
    Finds valid Scrabble words that can be constructed from the rack.

    Args:
        rack (str): A string of 2 to 7 characters representing the Scrabble rack.

    Returns:
        tuple: A tuple containing two elements -
            1) List of (score, word) tuples, sorted by score and then by word alphabetically.
            2) Total number of valid words.
        3) Error message (if any).
    """

    def generate_error_message(error_type):
        error_messages = {
            "contains_number": "Error: Rack contains a number.",
            "invalid_length": "Error: Rack must contain 2 to 7 characters.",
            "too_many_wildcards": "Error: Rack contains more than 2 wildcards (* or ?).",
            "no_letters": "Error: Rack must contain at least one letter.",
            "invalid_characters": "Error: Rack contains invalid characters."
        }
        return error_messages.get(error_type, "Unknown error.")

    # Convert rack to uppercase
    rack = rack.upper()

    # Error checks
    if any(char.isdigit() for char in rack):
        return generate_error_message("contains_number")

    if not (2 <= len(rack) <= 7):
        return generate_error_message("invalid_length")

    if rack.count('*') + rack.count('?') > 2:
        return generate_error_message("too_many_wildcards")

    if not any(char.isalpha() for char in rack):
        return generate_error_message("no_letters")
    
    if any(char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*?' for char in rack):
        return generate_error_message("invalid_characters")

    # Load the set of valid Scrabble words (in uppercase)
    valid_words = load_valid_words()

    # Precompute scores for valid words
    valid_scores = {word: score_word(word, scores) for word in valid_words}

    # Generate all possible combinations of letters from the rack (including wildcards)
    possible_combinations = generate_possible_combinations(rack)

    # Filter valid words and calculate scores
    valid_scrabble_words = [(valid_scores[word], word) for word in possible_combinations if word in valid_scores]

    # Sort by score and then by word alphabetically
    valid_scrabble_words.sort(key=lambda x: (-x[0], x[1]))

    return valid_scrabble_words, len(valid_scrabble_words)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


