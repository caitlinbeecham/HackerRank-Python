#!/bin/python
from copy import deepcopy
import sys
import math

class LinkedList(object):
    def __init__(self,top=None):
        self.top = top
        
    def insert_at_start(self,data):
        new_node = ListNode(data)
        new_node.Next = self.top
        self.top = new_node

class ListNode(object):
    def __init__(self,data,Next=None):
        self.data = data
        self.Next = Next
        
def BinarySearchReversed(a,val,lo=None,hi=None):
    if lo == None:
        lo = 0
    if hi == None:
        hi = len(a)-1
    if lo > hi:
        return False
    mid = int(math.floor((lo+hi)/2.0))
    if (a[mid] == val):
        return True
    elif a[mid] > val:
        return BinarySearchReversed(a,val,mid+1,hi)
    else:
        return BinarySearchReversed(a,val,lo,mid-1)       
  
              
    #a is in descending order
    #returns False if val not in a
    #returns True if val in a
    

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
#try not to do this
"""
j1 = [h1[i] for i in range(len(h1)-1,-1,-1)]
j2 = [h2[i] for i in range(len(h2)-1,-1,-1)]
j3 = [h3[i] for i in range(len(h3)-1,-1,-1)]
#will calculate a list of running sums for each list
rs_1 = [0 for i in range(len(h1))]
tally = 0
for i in range(len(j1)):
    tally += j1[i]
    rs_1.append(tally)
rs_2 = []
tally = 0
for i in range(len(j2)):
    tally += j2[i]
    rs_2.append(tally)
rs_3 = []
tally = 0
for i in range(len(j3)):
    tally += j3[i]
    rs_3.append(tally)
"""
#rs_1 = [0 for i in range(len(h1))]
rs_1 = LinkedList()
tally = 0
for i in range(len(h1)-1,-1,-1):
    tally += h1[i]
    rs_1.insert_at_start(tally)
    #print("rs_1.top.data")
    #print(rs_1.top.data)
rs_2 = LinkedList()    
#rs_2 = [0 for i in range(len(h2))]
tally = 0
for i in range(len(h2)-1,-1,-1):
    tally += h2[i]
    rs_2.insert_at_start(tally)
rs_3 = LinkedList()
#rs_3 = [0 for i in range(len(h3))]
tally = 0
for i in range(len(h3)-1,-1,-1):
    tally += h3[i]
    rs_3.insert_at_start(tally)
#now we want to find the highest number in all of rs_1 rs_2 and rs_3
#if there are no elts in common
#return 0
max_elt_in_common = 0
new_elt_in_common = None
broken = False
"""
print("rs_1")
print(rs_1)
print("rs_2")
print(rs_2)
print("rs_3")
print(rs_3)
"""
"""
for i in range(len(rs_1)):
    for j in range(len(rs_2)):
        for k in range(len(rs_3)):
            if rs_1[i] == rs_2[j] and rs_1[i] == rs_3[k]:
                new_elt_in_common = rs_1[i]
                print(new_elt_in_common)
                broken = True
                break
                #if i > max_elt_in_common:
                    #max_elt_in_common = i
        if broken:
            break
    if broken:
        break
if broken == False:
    print(0)
"""
#just figured out a thing
#of what to do
#lemme do it with arrays first
#then with linked list if possible
"""
okay so we can optimize a bit
if rs_1.top is bigger than rs_2.top we can not even look at the other two lists
because rs_1 will not be in rs_2 because these rs lists are strictly decreasing
"""
"""
found = False
current1 = rs_1.top
while current1 != None:
    if current1.data <= rs_2.top.data and current1.data <= rs_3.top.data:
        current2 = rs_2.top
        while current2 != None:
            if current2.data <= rs_3.top.data and current2.data <= rs_1.top.data:
                current3 = rs_3.top
                while current3 != None:
                    if current1.data == current2.data and current2.data == current3.data:
                        print(current1.data)
                        found = True
                        break
                    current3 = current3.next
                if found:
                    break
            current2 = current2.next
        if found:
            break
    current1 = current1.next
if not found:
    print(0)
"""
list1 = []
current1 = rs_1.top
while current1 != None:
    list1.append(current1.data)
    current1 = current1.Next
list2 = []
current2 = rs_2.top
while current2 != None:
    list2.append(current2.data)
    current2 = current2.Next
list3 = []
current3 = rs_3.top
while current3 != None:
    list3.append(current3.data)
    current3 = current3.Next

lists = [list1,list2,list3]
"""
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
"""
smallest_list = list1
for thing in lists:
    if len(thing) < len(smallest_list):
        smallest_list = thing
other_lists = deepcopy(lists)
other_lists.remove(smallest_list)
found = False
#print("smallest_list")
#print(smallest_list)
"""
for listy in other_lists:
    print("another list")
    print(listy)
"""
for i in range(len(smallest_list)):
    #bst to see if smallest_list[i] in other_lists[0]
    """
    print("smallest_list[i]")
    print(smallest_list[i])
    print("other_lists[0]")
    print(other_lists[0])
    print("other_lists[1]")
    print(other_lists[1])
    """
    in_other_list1 = BinarySearchReversed(other_lists[0],smallest_list[i])
    in_other_list2 = BinarySearchReversed(other_lists[1],smallest_list[i])
    #bst to see if smallest_list[i] in other_lists[0]
    #if in both
    #print("in_other_list1")
    #print(in_other_list1)
    
    #print("in_other_list2")
    #print(in_other_list2)
    
    if in_other_list1 and in_other_list2:
        found = True
        print(smallest_list[i])
        break
    #break out of this loop and return smallest_list[i]
#print(max_elt_in_common)
if not found:
    print(0)

#need to catch the case where there is an empty stack
#just don't know how that input would look
#they haven't outlined what an empty stack would look like in the input
#would we have an empty line? is there such a thing
#or a line with a 0? -1?
