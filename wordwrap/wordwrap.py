'''
Your task is to write a function that takes two arguments,
a string and an integer width.

The function returns the string, but with line breaks inserted
at just the right places to make sure that no line is longer
than the column number. You try to break lines at word boundaries.

Like a word processor, break the line by replacing
the last space in a line with a newline.
'''


def find_breakpoints(input_string, width):
    """ Finds the breakpoints by finding last space
        before line width limit
    """
    breakpoints = []
    last_space_char = 0
    line_length = 0
    chars_since_last_space = 0
    for i in range(len(input_string)):
        # print(input_string[i], ":", i, "-", j)
        if input_string[i] == " ":
            last_space_char = i
            chars_since_last_space = 0
        if line_length == width:
            line_length = 0 + chars_since_last_space
            breakpoints.append(last_space_char)
        line_length += 1
        chars_since_last_space += 1
    return breakpoints


def wordwrap(input_string, width):
    """ Takes a string and a line width limit.
        Outputs string, replacing last space char
        before width limit with linebreak.
    """
    # If string is smaller than width limit then just
    # return the input back as nothing needs to be done
    if len(input_string) - 1 <= width:
        return input_string
    
    # init
    # the string that will be built and outputted
    output_string = ""
    # list containing the last space char before width limit
    breakpoints = find_breakpoints(input_string, width)
    
    for i in range(len(breakpoints)):
        if i != 0:
            start = breakpoints[i - 1] + 1
        end   = breakpoints[i]
 
        if i == 0:
            output_string += input_string[:end] + "\n"
        else:
            output_string += input_string[start:end] + "\n"

    start = breakpoints[-1] + 1
    output_string += input_string[start:]

    return output_string
