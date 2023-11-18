def movie_organizer(*args):
    organizer = {}
    result = []
    for name, genre in args:
        if genre not in organizer:
            organizer[genre] = []
            organizer[genre].append(name)
        else:
            organizer[genre].append(name)

    # first sort descending by quantity of keys, then by values alphabetically ascending
    organizer = sorted(organizer.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in organizer:
        result.append(f'{key} - {len(value)}')
        for y in sorted(value):
            result.append(f'* {y}')
    return '\n'.join(result)


# print(movie_organizer(("The Matrix", "Sci-fi")))
# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

