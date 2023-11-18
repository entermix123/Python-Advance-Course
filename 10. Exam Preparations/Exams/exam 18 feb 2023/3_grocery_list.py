def shop_from_grocery_list(money, list1, *args):        # create function
    purchased = []              # create list for purchased products
    budget = float(money)       # create budget variable
    list_products = list1       # create list for buying
    products = args             # create list of available products and prices
    result = []                 # create result list
    products_left = []          # create list of not purchased products

    for product, price in products:                                 # iterate true available products
        if product in purchased or product not in list_products:   # if product already purchased ot not in list for buy
            continue                                                # ignore product
        if budget < price:                  # if budget is less than price
            break                           # break cycle
        if budget >= price:                 # if budget is enough
            purchased.append(product)       # add product to purchased list
            budget -= price                 # subtract price for the product of budget

    for pr in list_products:                # iterate true list of products for buying
        if pr not in purchased:             # if product not in purchased list
            products_left.append(pr)        # add product to list of left product to buy

    if all(item in purchased for item in list_products):    # if all product in purchased are in the list of pr to buy
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."  # add wanted string to result
    else:
        # if not all product in the list for buy are purchased, add wanted string to result
        result = f"You did not buy all the products. Missing products: {', '.join(str(x) for x in products_left)}."

    return result       # return result


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))




