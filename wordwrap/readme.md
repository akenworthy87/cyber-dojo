## Wordwrap 
Exercise space ID: A63thL


### Outline

The task was to create a word wrap function, the outline was given as follows:

> Your task is to write a function that takes two arguments, a string and an integer width.
>
> The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries.
> 
> Like a word processor, break the line by replacing the last space in a line with a newline.


### Purpose

The point of this attempt was more to play around with the Cyber-Dojo platform and practice TDD rather than design an efficient algorithm.

### Post Mortem

It is a functional function, made via TDD methodology, which meets the requirements set out in the Outline, however:

1. The algorithm is inefficient as it will always search all characters in a section, this could be improved drastically by starting at the breakpoint and searching backwards 
2. It will probably break in an edge case scenario where a really long word is longer than a narrow line width, I believe the output would either have a line is too long or a section of text will be repeated