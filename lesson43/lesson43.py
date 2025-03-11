# Lesson 43
def rdupes(a_list):
    setVer = set(a_list)
    return list(setVer)
print(rdupes([1,1,1,2,2,2,3,3,3,4,4,4]))
def uniLet(a_list):
    result = set()
    for word in a_list:
        temp = set(word)
        result |= temp
    return result
testB = ["hello", "goodbye", "world", "mr. park"]
print(uniLet(testB))
def intersect(a_list):
    if a_list:
        result = a_list[0]

        for example in a_list[1:]:
            result = result & example
        return len(result)
test = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(intersect(test))
