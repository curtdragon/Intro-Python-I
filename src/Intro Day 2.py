#Argument is passed by value
def doublke(x):
    return x*2

num=double(10)
val=double("something")

print(num)
print(val)

# define a doubling function that doubles every element in a list
#Argument is passed by reference
# def double_list(li):
#     for i in range(o, len(li))
#         li[i] *= 2

# num_list =[1,2,3,4,5]
# print(num_list)
# double_list(num_list)
# print(num_list)


def double_list(li):
        for i in range(0, len(li)):
            li[i] *=2

num_list =[1,2,3,4,5]
print(num_list)
double_list(num_list)
print(num_list)

def append_to_list(li,val):
    li.append(val)

append_to_list(num_list, "something new")
print(num_list)

#pass a collection by value
import copy

num_list=[1,2,3,4,5]
print(num_list)
num_list=double_list(copy.copy(num_list))
print(num_list)
