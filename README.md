# Mathematical Algorithms

## About
This repository includes all the python programs that I wrote that can be used to solve real world problems in mathematics and computer science. When I was doing university projects, in most cases I was not allowed to use packages such as NumPy and Matplotlib. Hence I am curious as to how one solves such mathematical problems without the help of these packages and therefore I started to code and experiment, trying to use my mathematical knowledge and my current python skills along the way. I wrote these algorithms in my free time, some of which I rewrote from the programming assignments I submitted for the modules I attended at TU Berlin. Below I added a short description to each program. Please note that even though these algorithms run correctly (if you see a mistake, please let me know!), it is not guaranteed that they have optimal running time. 

## Code Description (in alphabetical order)

### evaluate_terms.py
For a given string representing a mathematical term and the algebraic structure on which this term is defined, the algorithm evaluates the expression and gives its value and its depth if the term is a correct term or tells you otherwise that the term is not a correct term.

### inplace_quicksort.py
An in-place implementation of quicksort. The algorithm itself doesn't have direct access to the to-be-sorted list, but rather it has only information on the length of the list, and two functions which task is to compare and swap 2 items from a list respectively.

### savings.py
There are two subroutines here. **`total_savings`** gives you the amount of money you have after you saved it for `time` years, starting with $`starting_saving` and yearly saving $`yearly_savings` with `interest`%. you can specifically know how much money you have after `year` years

### topological_sort.py
The code gives you a topological sort of given items or tells you otherwise if it doesn't exist. The implementation is based on “Elementary Graph Algorithms.” Introduction to Algorithms, by Thomas H.. Cormen et al., 3rd ed., The MIT Press, 2009, pp. 604–613.


