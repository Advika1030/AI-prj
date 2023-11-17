# AI-prj
Problem Solving by Classical Searching


Objective
Generate all possible combinations of a given list of substrings, where each pair of adjacent substrings overlaps by a specified number of characters.

Input
substrings: A list of string segments to combine.
overlap: The number of overlapping characters required between each pair of adjacent substrings (default is 2).

Output
A list containing all possible combinations of substrings with the specified overlap.
Steps
Initialize a List for Combinations:

Create an empty list named combined_strings to store the final combinations.
Define a Recursive Helper Function - add_combinations:

This function is used to build combinations recursively.


Parameters:
current: A string representing the current combination.
index: An integer indicating the position in the substrings list to process next.


Process:
Base Case: If index equals the length of substrings, add current to combined_strings and return.
Recursive Case: Iterate over each possible overlapping part of the substring at index (from overlap to the full length of the substring). For each part, call add_combinations with the new combination (current + overlapping part) and the next index (index + 1).


Start the Combination Process:

Call add_combinations with an empty string and the starting index 0. This initiates the process of combination generation.

Return the Combinations:

After the recursive process completes, return the combined_strings list containing all the combinations.


Example Usage
Given the list ["SNU ", "U CH", "CHEN", "ENNA", "NAI."], the algorithm will generate and return all the possible combinations where each pair of adjacent substrings overlaps by 2 characters.