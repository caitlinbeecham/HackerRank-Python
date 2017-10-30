import math

class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def addNum(self,num):
        parent = None
        current = self
        while current != None:
            if current.data > num:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        new_node = TreeNode(num)
        if parent.data < num:
            parent.right = new_node
        else:
            parent.left = new_node

    def deleteNum(self,num):
        #find num in bstree
        #keeping track of parent
        parent = None
        current = self
        while current.data != num:
            if current.data < num:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        #once find num
        #if num has zero children just make parent point to None instead of num node
        #if has one child make parent point to that one child
        #else has two children
        #find smallest elt in subtree of right child
        #make the current node containt that data then delete where that data was before
        #using this method so it will need to be recursive
        #stop condition should be if num is at a leaf
        #or if it only has 1 child
        #if it has two children the recursing will need to keep happening
        if current.left == None and current.right == None:
            if parent.data < current.data:
                #current is a right child
                parent.right = None
            else:
                #current is a left child
                parent.left = None
        elif current.left == None:
            #and current.right != None
            if parent.data < current.data:
                #current is a right child
                parent.right = current.right
            else:
                #current is a left child
                parent.left = current.right
        elif current.right == None:
            #and current.left != None
            if parent.data < current.data:
                #current is a right child
                parent.right = current.left
            else:
                #current is a left child
                parent.left = current.left
        else:
            #current has two children
            self.findSmallestInSubtreeAndUpdateCurrentVal(current)
            

    def findSmallestInSubtreeAndUpdateCurrentVal(self,current_node):
        parent_of_smallest = None
        smallest_data = math.inf
        queue = [[None,current_node]]
        while len(queue) > 0:
            [parent,current] = queue.pop(0)
            if current < smallest_data:
                parent_of_smallest = parent
                smallest_data = current
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        current.node.data = smallest_data
        return smallest_data
            

def iterativelyFindMids(sorted_array):
    length = len(sorted_array)
    queue = []
    queue.append([0,length])
    idxs = []
    while len(queue) > 0:
        [start,end] = queue.pop(0)
        mid = math.floor((start + end)/2.0)
        idxs.append(mid)
        if start<mid:
            queue.append([start,mid])
        if mid+1<end:
            queue.append([mid+1,end])
    ret = []
    for idx in idxs:
        ret.append(sorted_array[idx])
    return ret


def constructBST(sorted_array):
    list_to_add = iterativelyFindMids(sorted_array)
    root = TreeNode(list_to_add[0])
    for i in range(1,len(list_to_add)):
        root.addNum(list_to_add[i])
    return root

def lca(root , v1 , v2):
  #Enter your code here
    #v1 and v2 are the data not the nodes containing that data
    #find path leading to v1
    #find path leading to v2
    #iterate backwards from the end of the shorter path until find a node that is in the other path
    #return this node
    path1 = []
    current = root
    while current.data != v1:
        if current.data < v1:
            path1.append(current)
            current = current.right
        else:
            path1.append(current)
            current = current.left
    path1.append(current)
    path2 = []
    current = root
    while current.data != v2:
        if current.data < v2:
            path2.append(current)
            current = current.right
        else:
            path2.append(current)
            current = current.left
    path2.append(current)
    print("path 1")
    print([itm.data for itm in path1])
    print("path 2")
    print([itm.data for itm in path2])
    if len(path1) < len(path2):
        for i in range(len(path1)-1,-1,-1):
            #look for path1[i] in path2 starting from back
            #if find return this node
            for j in range(len(path2)-1,-1,-1):
                if path2[j] == path1[i]:
                    return path1[i]
    else:
        for i in range(len(path2)-1,-1,-1):
            #look for path1[i] in path2 starting from back
            #if find return this node
            for j in range(len(path1)-1,-1,-1):
                if path1[j] == path2[i]:
                    return path2[i]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
root = constructBST(a)
print(lca(root,1,6).data)
print(lca(root,1,4).data)
print(lca(root,5,12).data)
print(lca(root,9,14).data)
print(lca(root,13,15).data)
