Problem 1 : Finding the Square Root of an Integers

Considering the simple approach we are performing only elementary operations, since we have a number to the power of 0.5.
Time complexity is O(1) and space complexity is also O(1);

For the binary search procedure. With this approach I look for value mid. Then I check where does the number lies, comapared to mid^2 (to the left or right or is equal). 
And return the floored squared root.
Time c. is O(log(n)) as we are looking to the left and right, eliminating certain intervals of values.
Space c. is O(1); it doesn't require storing of more data.