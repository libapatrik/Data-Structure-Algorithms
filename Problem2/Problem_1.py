# In the following code, I have implemented two ways of solving;
# Simple (sqrt) and overthinking (sqrt1);
def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number in [0, 1]:
        return number
    else:
        return round((number**0.5), 0) # floor or round to 2 decimal places

# With performing binary search;
def sqrt1(number):
    if number in [0, 1]:
        return number

    bottom = 0
    top = number

    while bottom <= top:
        mid = (bottom + top) // 2
        if mid ** 2 == number or mid ** 2 <= number < (mid + 1) ** 2:
            return mid
        elif mid ** 2 > number:
            top = mid
        else:
            bottom = mid

# Given test cases; `def sqrt()`
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail") # Pass case - its 5.19 -> 5.20
# Check
print("Pass" if (5.20 == sqrt(27)) else "Fail") # Now as a Fail case
print("_____separator line_____")

# Given test cases; `def sqrt1()`
print("Pass" if (3 == sqrt1(9)) else "Fail")
print("Pass" if (0 == sqrt1(0)) else "Fail")
print("Pass" if (4 == sqrt1(16)) else "Fail")
print("Pass" if (1 == sqrt1(1)) else "Fail")
print("Pass" if (5 == sqrt1(27)) else "Fail") 
# Check
print("Pass" if (5.20 == sqrt1(27)) else "Fail") 