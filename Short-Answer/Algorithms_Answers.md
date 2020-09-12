#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this code snippet is O(n).
This runs linearly. Say for example n=2.. this will have to run twice.
If n=4 it would have to run 4 times. That is why it is O(n).

b) The runtime complexity of this code snippet is O(n log n).
The for loop is O(n) but then it has a while loop within it, 
which is doubling the value of j and incrementing the value of 
sum for each iteration until it reaches the value of n.

c) The runtime complexity of this code snippet is O(n).
In this recursive function, the amount of times it runs is dependent
of how many bunnies there are. It is taking the number of bunnies and 
subtracting 1 until we get to zero which is a linear decrementing iteration.

## Exercise II

I feel like it would be fair for the first pass of this to be O(n) and check every floor,
testing whether or not the egg breaks.. since we are really just trying to find at which
point the eggs start to break.. but that would be awful if the building were very tall. 
It also brings the chance at breaking a lot of eggs, which we are trying to minimize.

I feel the best approach for this in my mind would be a binary search O(log n). We would find the
middle floor, drop an egg.. if it breaks, we are too high. We would then scale down the 
building, cutting the floors (n) in half //2 each time and test whether or not the egg 
breaks. Eventually we will know the breakpoint where the egg would not break vs. where 
the eggs start breaking. This minimizes the number of eggs broken quite a lot from the
first pass.