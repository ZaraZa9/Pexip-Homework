# Pexip-Homework
## Andrei Medved

## Problem Summary
My solution addresses a large-scale word search problem, where the task is to find specific words within a 10,000 x 10,000 grid of random ASCII characters. Words can appear only in two directions: horisontally (left to right) or vertically (top to bottom). With up to 1,000,000 words to search for, the main challenge here is scale.

## Approach
### Grid Setup
The grid is represented as a single string of 1,000,000 characters. To make searching easier, I've split the grid into separate row and column arrays - using numpy for convenience.

## Search Strategies Considered
Two main approaches were considered:

### Substring Hash Set:
This approach would involve precomputing and storing all possible substrings (up to 24 characters long) for each row and column in hash sets. This apporached promised search complexity of O(1) for each lookup. However, generating and storing all possible substrings took far too long (O(n²) complexity) and used an excessive amount of memory, so it wasn’t practical for a grid of this sise.

### Linear Search with Index Optimisation:
Instead of precomputing substrings, this approach involves scanning each row and column linearly. The key optimisation here is to look for the first letter of the target word and only then check if the entire substring matches. This approach is slower than a hash set lookup (O(n) complexity) but uses far less memory and consistently outperformed the hash set solution. This was the only solution that was fast and reliable enough to handle the grid's scale.

## Threading Optimisation
To make the search faster, threading was added to run searches on the row and column arrays concurrently. This parallelises the workload, reducing the time it takes to find each word.

## Optimising for Multicore Systems
Whilst threading introduces concurrency, it’s not a full multicore solution. To take advantage of a multicore system, I could have used Python’s multiprocessing module, which allows for true parallel execution across CPU cores.

If I had taken this approach, the solution would've looked as such:

Split the grid into smaller chunks (e.g. dividing rows or columns into segments), so that each process works independently on its assigned section of the grid. Then each process would check for the target word within its portion of the grid, taking full advantage of the CPU’s cores to speed up the search.