## Problem Statement
Implement both the brute-force and recursive algorithms for the maximum-subarray problem on your own computer.

## Context
This exercise compares two approaches to finding the contiguous subarray within a one-dimensional array of numbers which has the largest sum.
* **Brute-force approach:** Computes the sum of all possible subarrays. Time complexity: $O(n^2)$.
* **Divide-and-Conquer approach:** Recursively divides the array in half and finds the maximum subarray crossing the midpoint. Time complexity: $O(n \log n)$.
