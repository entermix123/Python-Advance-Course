def shopping_cart(*args):
    meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    for x in args:
        if x == 'Stop':
            break
        else:
            name, material = x
            if material not in meals[name]:
                if len(meals[name]) < limits[name]:
                    meals[name] += [material]

    final_meals = {key: value for key, value in sorted(meals.items(), key=lambda h: (-len(h[1]), h[0]))}

    result = []
    for value in final_meals.values():
        if len(value) > 0:
            break
        else:
            return f"No products in the cart!"

    for key, value in final_meals.items():
        result.append(f'{key}:')
        if value:
            for o in sorted(value):
                result.append(f' - {o}')

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
