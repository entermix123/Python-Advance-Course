def has_permission(page):               # def global function
    def permission(username):           # def internal function
        if username.lower() == 'admin':                         # if lower case input is 'admin'
            return f'{username} has right to open {page}'       # return result
        else:
            return f'{username} does not have right to open {page}'  # else return result

    return permission       # return as a function with no brackets and ask for username from input -> row 12 IMPORTANT !!!


check_name_input = has_permission('Admin page')     # ask global function for page
print(check_name_input('aDmIN'))                    # print variable with nested function of username
