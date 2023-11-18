a = 5


def greeting_closure():     # main function
    global a                # variable 'a' is out of the main function so we specify the path with 'global varname'
    text = 'Hi'
    a += 5

    def add_my_name_is():   # every information in main function is available for the inner function !!!
        nonlocal text       # if we want to modify variable in main function, specify the path with 'nonlocal varname'

        text += ', my name is'  # modifying the 'text' variable

    add_my_name_is()
    print(text)
    print(a)


greeting_closure()
