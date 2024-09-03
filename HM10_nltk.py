import requests

def match_synonyms(word, word_list):
    """
    Matches the synonyms of a word with a list of words.

    Args:
        word: The word to match synonyms for.
        word_list: The list of words to match against.

    Returns:
        A list of words that are synonyms of the given word.
    """

    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    data = response.json()

    synonyms = [entry['word'] for entry in data]

    matched_words = [w for w in word_list if w.lower() in synonyms]
    return matched_words

category = ['Honeymoon','Nature','Mountain','Beaches','Ancient']
search_word = ''

matched_categories = match_synonyms(search_word, category)
print(matched_categories)
