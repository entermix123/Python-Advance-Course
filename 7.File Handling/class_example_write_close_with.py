class MessageWriter(object):                    # def tha class

    def __init__(self, file_name):              # autostart function
        self.file_name = file_name              # connect file name

    def __enter__(self):                        # enter file function
        self.file = open(self.file_name, 'w')   # open\create file
        return self.file                        # return file

    def __exit__(self, *args):                  # exit function
        self.file.close()                       # close file


with MessageWriter('SoftUni.txt') as file:          # call class
    file.write('Hello SoftUni \nClass Example')     # add info to file
