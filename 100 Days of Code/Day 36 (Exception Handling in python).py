# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
#
# except IndexError:
#     print("Index Error")


# a=input("Enter the number:")
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{i}={int(a)*i}")
# except Exception as e:
#     print(e)
# print("Some important line of code")
# print("End of program")



try:
    num=int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError: #amra jodi integer er jaygay char ba onno kisu input dei tahole eta kaj korbe
    print("Invalid Value!!")
except IndexError: #amra jodi ei khetre 0,1 index er bahire kono index input dei tahole eta kaj korbe.(amra system onujayi muloto input e index dibo)
    print("InValid Index!!")