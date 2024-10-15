
# Array Search Algorithms: Linear and Binary Search

This project implements two common search algorithms in Python: **Linear Search** and **Binary Search**. The user can input an array of numbers and a target number to search for. The program performs both linear and binary searches, returns the index of the target if found, and measures the runtime for both algorithms.

## Features

- **Linear Search**: Searches through the array one element at a time, regardless of whether the array is sorted.
- **Binary Search**: More efficient search that works only on a sorted array by repeatedly halving the search space.
- **User Input**: The user can input their own array and target number.
- **Timing**: The runtime of each search algorithm is measured and displayed.

## How to Use

1. **Clone the repository** or download the code.
2. **Run the script** using Python 3.

   ```bash
   python array_search.py
   ```

3. **Input an array of numbers** when prompted. The numbers should be separated by commas (e.g., `3,5,7,9,12`).
4. **Input the target number** you wish to search for in the array.
5. The program will display:
   - The sorted array
   - Whether the target was found
   - The index of the target in the array (if found)
   - The time taken to perform the search for both linear and binary searches

## Example

```
Voer de array in (gescheiden door komma's): 1, 3, 5, 7, 9, 11, 13
Voer het getal in dat je wilt zoeken: 9
Gesorteerde array: [1, 3, 5, 7, 9, 11, 13]
Lineair zoeken: gevonden op index 4 in 0.000004 seconden.
Binair zoeken: gevonden op index 4 in 0.000002 seconden.
```

## Requirements

- Python 3.x
- No external libraries are required; the project uses only built-in Python libraries (`time`, `random`).

## Code Explanation

### Linear Search

The `linear_search` function iterates through each element of the array until it finds the target value. If the target is found, the function returns the index of the target; otherwise, it returns `-1`.

### Binary Search

The `binary_search` function works only on a sorted array. It uses a divide-and-conquer approach by comparing the target value with the middle element of the array and reducing the search space by half until the target is found or the search space is empty.

### Timing Function

The `time_function` function wraps around the search functions to measure the execution time of each algorithm. It uses the built-in `time.time()` function to capture the start and end times, then calculates the total time elapsed.

## Future Enhancements

- Allow the user to generate a random array of a specific size.
- Implement additional search algorithms such as **Jump Search** or **Interpolation Search**.

