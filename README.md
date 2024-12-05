# Advent-of-Code-2024
## Day 1
### Part 1
Part 1 is solved by the following steps:
1. Parsing the two input-lists from the provided file by reading the lines and splitting them with the default `split()` method
2. Sorting the lists
3. Computing the difference between corresponding values in the list using the `abs()`-function
4. Adding up all computed differences

### Part 2
In Part 2 the parsing stays the same, so we can just copy the code from Part 1. 

Then we have to find for each value in list 1, the number of occurrences in list 2. We can achieve this by using the builtin `count()`-Method for lists.
Just for the fun of it I added caching to my `count()`-Method by wrapping it in a function with the `@cache`-decorator. That has the benefit of not having to count the same number twice which alone would take $O(n)$ time. Together with the iteration through the first list that would make $O(n^2)$... 

Not very efficient.

When we have found the number of occurrences we can multiply the number by its occurrence and add the result to the total. 

The total of all of that makes up the answer
