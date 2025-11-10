from typing import List, Dict, Any

# Fibonacci function
def fibonacci(n: int, memo: Dict[int, int] = None) -> int:
    # Base cases
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
    
    # Return value if in memoization table
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    # Add to memiozation table
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Check if string is palindrome
def is_palindrome(s: str) -> bool:
    # Add only alnum chars to cleaned string
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    
    # return if cleaned equals cleaned reversed
    return cleaned == cleaned[::-1]


# Return dictionary with word, and frequency
def word_count(text: str) -> Dict[str, int]:
    words = text.lower().split() # gen list of words
    freq = {}
    
    # add to frequency map
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


# Average of list
def average(values: List[float]) -> float:
    if not values:
        raise ValueError("List cannot be empty")
    return sum(values) / len(values)


# Return maximum 
def find_max(values: List[int]) -> int:
    if not values:
        raise ValueError("List cannot be empty")
    return max(values)


# Return list of unique values
def unique(values: List[Any]) -> List[Any]:
    # create set adding unique values to it
    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


# Convert between fareinheit and celsius
def convert_temp(value: float, to: str) -> float:
    if to == "F":
        return (value * 9/5) + 32
    elif to == "C":
        return (value - 32) * 5/9
    else:
        raise ValueError("to must be 'C' or 'F'")


# Sort dictionary by key value
def sort_dict_by_value(d: Dict[str, int]) -> List[tuple]:
    return sorted(d.items(), key=lambda x: x[1])


# Merge two dictionaries
def merge_dicts(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    result = a.copy()
    result.update(b)
    return result


# Safe division
def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers, raising a helpful error on divide-by-zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
