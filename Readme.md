Count Occurrences Function with Unit Tests

Overview
The goal of this script is to count how many times each element appears in an iterable (e.g., a string, list, tuple, or set). This is done by building a dictionary where the keys are elements from the iterable, and the values are their corresponding counts.
A suite of tests is provided to verify the behavior of the function when given different types of input.
Function Details

count_occurrences(iterable: Any) -> Dict[Any, int]
The count_occurrences function takes any iterable (such as a string, list, tuple, or set) and returns a dictionary that maps each element to the number of times it occurs in the input iterable.

Running Tests
You can run the tests using the unittest framework.
1. Ensure you have Python installed.
2. Save the code to a file (e.g., test_coding_challenge.py).
3. Run the following command:  python -m unittest test_coding_challenge.py
Test Cases
The following test cases are included to verify the correctness of the count_occurrences function:
1. String input:
o Input: "hello"
o Expected Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
2. List of integers:
o Input: [1, 2, 2, 3, 1, 1]
o Expected Output: {1: 3, 2: 2, 3: 1}
3. Tuple input:
o Input: ('hello', 'hai', 'hello', 'welcome')
o Expected Output: {'hello': 2, 'hai': 1, 'welcome': 1}
4. Set input:
o Input: {50, 10, 50, 10, 20}
o Expected Output: {50: 1, 10: 1, 20: 1}
5. Mixed types list:
o Input: [1, 'a', 'a', 2, 1, 'b', 2]
o Expected Output: {1: 2, 'a': 2, 2: 2, 'b': 1}
6. Empty input:
o Input: []
o Expected Output: {}
7. Single element list:
o Input: [10]
o Expected Output: {10: 1}
8. None type input:
o The function is expected to raise a TypeError when None is passed.
Installation
To set up and run this project:
1. Clone the repository or download the script.
2. Ensure that Python 3.x is installed on your machine.
3. Install unittest (if not already available) using: pip install unittest
4. Run the tests as described in the "Running Tests" section.




![image](https://github.com/user-attachments/assets/4c789366-03a7-4cc8-a139-46acb7f20e22)
