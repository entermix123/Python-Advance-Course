def forecast(*args):
    dict1 = {}
    for info in args:
        town, status = info
        dict1[town] = status

    sorted_result = {k: v for k, v in sorted(dict1.items(), key=lambda x: x[0])}
    sunny = ''
    cloudy = ''
    rainy = ''
    for key, value in sorted_result.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
