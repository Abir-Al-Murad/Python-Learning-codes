#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def chek_plz(lst1, lst2):
    print("Given list:", lst1)
    x = len(lst1)
    if lst1[0] == lst1[x - 1]:
        print("Matched")
    else:
        pass
    print("Given list:", lst2)
    y = len(lst2)
    if lst2[0] == lst2[y - 1]:
        print("Matched")
    else:
        pass


n = chek_plz([10, 20, 30, 40, 10], [75, 65, 35, 75, 30])


# def first_last_same(numberList):
#     print("Given list:", numberList)
#
#     first_num = numberList[0]
#     last_num = numberList[-1]
#
#     if first_num == last_num:
#         return True
#     else:
#         return False
#
#
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
#
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
