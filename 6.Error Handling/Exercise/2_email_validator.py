from re import findall      # import regex findall function


class NameTooShortError(Exception):     # create class for too short name
    pass


class MustContainAtSymbolError(Exception):      # create class for too short name
    pass


class InvalidDomainError(Exception):            # create class for wrong domain
    pass


class MoreThanOneAtSymbolError(Exception):      # create class for existing @
    pass


class InvalidNameError(Exception):              # create class for wrong name
    pass


pattern_name = r'[\w+\.]+'      # regex for name
pattern_domain = r'\.[a-z]+'    # regex for domain
MIN_LENGTH = 4                  # minimum characters for name
valid_domains = ['.com', '.bg', '.org', '.net']     # valid domains

email = input()                 # user input
while email != 'End':           # while input is different of 'End'
    try:                        # try for errors
        if email.count('@') > 1:                                                # if @ in input is more than 1
            raise MoreThanOneAtSymbolError('Email should contain only one @!')  # raise error
        if len(email.split('@')[0]) <= MIN_LENGTH:                              # if length of the name is less than 4 chars
            raise NameTooShortError('Name must be more than 4 characters')      # raise error
        if findall(pattern_name, email)[0] != email.split('@')[0]:              # if name do not match name regex
            raise InvalidNameError('Name can only contain numbers, letters, underscores and dots')      # raise error
        if '@' not in email:                                                    # if @ is not in email
            raise MustContainAtSymbolError('Email must contain @')              # raise error
        if findall(pattern_domain, email)[-1] not in valid_domains:             # if domain is not in valid domains
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')    # raise error

    except IndexError:              # if error not in error classes, raise index error
        print('Invalid email!')     # print Invalid error

    else:                           # if mail is valid
        print('Email is valid')     # print email is valid
    email = input()                 # user input for while loop
