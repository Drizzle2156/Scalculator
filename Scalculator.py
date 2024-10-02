def add(a, b):
    return a + b


result1 = add(2, 2)
print(result1)


def subtract(c, d):
    return c - d


result2 = subtract(25, 10)
print(result2)


def theproductofresults(result1, result2):
    result3 = result1 * result2
    result3_string = str(result3)

    return result3_string

# To unit test your theproductofresults function, we need to adjust it slightly to make it more testable. Specifically, instead of just printing the result (result3_string), the function should return the value so that it can be tested.


theproductofresults(result1, result2)
