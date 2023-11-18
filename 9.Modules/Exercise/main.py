from authentication import render_entry
from canvas import root


if __name__ == '__main__':      # make main loop if condition. prevent overlapping loops
    render_entry()              # call function
    root.mainloop()             # good practice to be executed last in main


