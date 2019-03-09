def multiply(a,b,answer):
    if answer == 0 and a != 0 and b != 0:
        answer = a
    if a == 1:
        return answer
    elif b == 1:
        return answer
    else:
        answer += a
        return multiply(a,b-1,answer)

#Solution 1
def minProduct(a,b):
    bigger = b if a < b else a #a < b ? b : a
    smaller = a if a < b else b #a < b ? a : b
    return minProductHelper(smaller,bigger)

def minProductHelper(smaller, bigger):
    print("smaller",smaller)
    print("bigger",bigger)
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    # Compute half. If uneven, compute other half. If even, double it
    s = smaller >> 1 # divide by 2
    side1 = minProduct(s,bigger)
    print("side1",side1)
    side2 = side1
    if smaller % 2 == 1:
        print("fawefa")
        print(smaller)
        print(bigger)
        print("finishs")
        side2 = minProductHelper(smaller - s, bigger)

    return side1 + side2

print(5>>1)


print(multiply(5,6,0))
print(minProduct(5,6))
# print(minProduct2(5,6))
# print(minProduct3(5,6))