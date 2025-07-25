def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None # return (None, None)

    min_value = None
    max_value = None

    for index, value in enumerate(ints):
        if index == 0:
            min_value = value
            max_value = value
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    return min_value, max_value

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l) # random numbers generated
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Pass case;
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
# Pass case;
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
