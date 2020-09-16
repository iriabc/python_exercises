
def most_occurring_element(elements):

    count_elements = [(elements.count(element), element) for element in set(elements)]
    max_count = max(count_elements, key=lambda n: n[0])[0]

    result = [element[1] for element in count_elements if element[0] == max_count]

    return result


def get_favourite_genres(users, genres):
    """
    Calculates a dictionary where the key is a username and the value is a list of the user's
    favourite genres (with the most songs).
    """

    result = {}
    # Generate a list with the genres of their favourite songs
    for user, user_songs in users.items():
        user_genres = []

        for genre, genre_songs in genres.items():
            genre_songs = [genre for song in user_songs if song in genre_songs]
            user_genres += genre_songs

        result[user] = most_occurring_element(user_genres)

    return result
