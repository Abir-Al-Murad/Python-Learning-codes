x ={"January":2200,"February":2350,"March":2600,"April":2130,"May":2190}

print("Extra Dollars Spent ->",x['February']-x["January"])
y = list(x.values())
sum = 0
for i in range(3):
    sum = sum+y[i]
print(sum)
flag = False
for key in x.keys():
    if(x[key]==2000):
        print("Yes")
        flag = True
        break
if(flag == False):
    print("No")
# x['June'] = 1980
x.update({'June':1980})
print(x)

x["April"] = x['April']-200
print(x)


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_tail(self,value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
    def display(self):
        temp = self.head
        count = 0
        while(temp !=None):
            print(temp.data,end="--> ")
            count+=1
            temp = temp.next
        print("Null")
        print("Length: ",count)




    def length(self):
        count = 0
        temp = self.head
        while(temp !=None):
            count+=1
            temp = temp.next
        return count


    def display_plus(self):
        temp = self.head
        while temp:
            print(f"Data: {temp.data}, Address: {id(temp)} → Next: {id(temp.next) if temp.next else None}")
            temp = temp.next


    def insert_at_head(self,value):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

            
    def remove_at_index(self,value):
        count =0
        temp = self.head
        if(temp == None):
            print("List is Empty, Nothing to remove")
            return
        if(value == 0):
            self.head = self.head.next
            return
        while(count != value-1):
            temp = temp.next
            count +=1
        temp.next = (temp.next).next

    def insert_at(self,index,value):
        new_node = Node(value)
        if(index ==0):
            self.head = new_node
        else:
            temp = self.head
            max_index = self.length()
            if(index>max_index):
                print("Index is out of range, Insertion of data is failed")
                return
            else:
                count = 0
                while(count != index-1):
                    temp = temp.next
                    count +=1
                new_node.next = temp.next
                temp.next = new_node

    
l1 = LinkedList()
l1.insert_at_tail(20)
l1.insert_at_tail(30)
l1.insert_at_tail(40)
l1.insert_at_head(10)
l1.remove_at_index(1)
l1.display()
l1.remove_at_index(0)
l1.insert_at(2,500)
l1.insert_at(3,56)
l1.insert_at(5,32)
# l1.display()