def score_word(word, scores):
    """
    Calculates the score of a word based on the provided scores dictionary.

    Args:
        word (str): The word to be scored.
        scores (dict): Dictionary containing letter scores.

    Returns:
        int: The score of the word.
    """
    score = 0
    for letter in word:
        score += scores.get(letter.lower(), 0)  # Convert to lowercase to handle uppercase letters
    return score
