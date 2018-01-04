#takes str as input
#do math on arbitrary size int as represented by the strings

#"12345"
#"23456"

#6 + 5 => 11
#4 + 5 + 1 => 0
#...

# if strAdd encounters negatives

# strAdd(-, +)
# strAdd(+, -)
    # strSub(+, -)

# strAdd(-, -)
    # -strAdd(+, +)

# params: str, str
# return: str
def strAdd(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    returnNum = ""
    carry = 0
    for i in range(max(len(num1), len(num2))):
        i1 = int(num1[i]) if i < len(num1) else 0
        i2 = int(num2[i]) if i < len(num2) else 0

        res = (i1+i2+carry) % 8
        if i1 + i2 + carry >= 8:
            carry = 1
        else:
            carry = 0

        returnNum += str(res)

    if carry == 1:
        returnNum += "1"

    return returnNum[::-1]

# num1 > num2
def strSub(num1, num2):
    # if num2 > num1:
    #     return "-" + strSub(num2, num1)
    num1 = num1[::-1]
    num2 = num2[::-1]

    returnNum = ""
    carry = 0
    for i in range(max(len(num1), len(num2))):
        i1 = int(num1[i]) if i < len(num1) else 0
        i2 = int(num2[i]) if i < len(num2) else 0

        res = (i1-i2-carry) % 10
        if i1-i2-carry <= 0:
            carry = 1
        else:
            carry = 0

        returnNum += str(res)

    return returnNum[::-1]

print strAdd("6","6")

# print strSub("123","41")
# print strSub("8", "10")

# print strAdd("12345","2356")
# print strAdd("","")
# print strAdd("","123")
# print strAdd("99999","999999")
# print strAdd("000000", "000")
