Problem 5 : Autocomplete with Tries

Assuming we have some set of words.
Given the initial letter the code needs to offer me all the words which starts with the initial letter.
Exactly as in your phone.
We are using TrieNode and Trie class to tackle this problem. 
The fun part begins within second `class TrieNode` where we add the code for suffixes.

Time complexity for `def insert()` is O(n), also O(n) space. For `def find` we have O(n) time and space. Where n is length of word.
For `def suffixes()` its the same O(n) time and space.
