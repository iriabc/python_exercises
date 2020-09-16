from math import pow, sqrt


def nearest_post_offices(n, location, post_office_locations):
    """
    Find the n post offices located closest to your location using euclidean distance calculation.

    Parameters
    ----------
    n: int
        Number of nearest post offices to return
    location: list[int]
        List of two elements X, Y with the coordinates of your location
    post_office_locations: list[location]
        List of locations for all available post offices

    Return
    ------
    A list containing the locations of the n nearest post offices
    """

    x = location[0]
    y = location[1]

    distances = [
        (index, sqrt(pow(x - loc[0], 2) + pow(y - loc[1], 2))) for index, loc
        in enumerate(post_office_locations)
    ]

    sorted_distances = sorted(distances, key=lambda element: element[1])
    nearest = [post_office_locations[office[0]] for office in sorted_distances[:n]]

    return nearest


