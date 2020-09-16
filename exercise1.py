from itertools import permutations


def select_movies_pair(movie_duration, flight_duration):
    """
    Select two movies for which the total duration is maximum but less than the
    flight duration minus half an hour.

    Parameters
    ----------
    movie_duration: list(int)
        List containing all movie durations
    flight_duration: int
        Duration of the flight in minutes
    """

    # Group the movies in pairs
    pair_movies = list(permutations(movie_duration, 2))

    # Calculate the duration of each pair of movies and filter on the given condition
    durations = [(n, element[0] + element[1]) for n, element in enumerate(pair_movies)]
    valid_durations = [element for element in durations if element[1] < flight_duration - 30]
    max_duration = max(valid_durations, key=lambda duration_pair: duration_pair[1])[1]
    selected_pairs = [pair for pair in valid_durations if pair[1] == max_duration]

    # Raise error if none found
    if len(selected_pairs) == 0:
        raise ValueError("All movies are too long to watch two")

    elif len(selected_pairs) == 1:
        return pair_movies[selected_pairs[0]]

    else:
        selected_pair = max(selected_pairs, key=lambda selected_pair: selected_pair[1])
        return pair_movies[selected_pair[0]]
