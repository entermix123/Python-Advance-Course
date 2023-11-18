# def concatenate(*args, **kwargs):
#     result = ''.join([str(x) for x in args])
#     for key in kwargs.keys():
#         if key in result:
#             result = result.replace(key, kwargs[key])
#     return result

def concatenate(*args, **kwargs):
    result = ''.join(args)                              # create string from arguments
    for key in kwargs:                                  # iterate true kwargs
        result = result.replace(key, kwargs[key])       # if key in string, replace with value of the kwargs
    return result                                       # result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
