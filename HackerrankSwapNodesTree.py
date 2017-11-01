class Tree(object):
    def __init__(self,root=None,data_to_nodes=None):
        if root == None:
            root = TreeNode(1)
        self.root = root
        data_to_nodes = {1:self.root}
        #this will be useful in traversing the tree to add nodes
        #wait maybe not nvmnd will just traverse down tree
        #will think about it finding each node to add its children each time could be costly
        #could keep hashmap of data to nodes yeah that will help

    def swapNodes(self,k,level_lists):
        #not convinced this will work but might so I'll run it and see
        levels = [i for i in range(1,len(level_lists)) if (i%k == 0)]
        for level in levels:
            #print("current level")
            #print([node.data for node in level_lists[level]])
            for node in level_lists[level]:
                if node.data != -1:
                    temp = node.left
                    node.left = node.right
                    node.right = temp
        
        
class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        #note when populating the tree will actually want to leave left and right as None NOT a node containing none at first will update later 

    def printInOrder(self):
        #node is a treenode
        if self != None and self.data != -1:
            self.left.printInOrder()
            print(self.data),
            self.right.printInOrder()

"""
nevermind doing this a different way
basically for each l_child,r_child pair will find place to add these to
would be really nice to use a heap for this part, but then is nice to have a tree for the second part
i suppose i could start by making a heap and then write a method to turn it into a tree 
"""        
t = Tree()
num_nodes = int(input().strip())
i = 0
current_parent_node_list = [t.root]
cpn_idx = 0
level_lists = [None]
#so that we have our indexing right
while i < num_nodes:
    current_parent = current_parent_node_list[cpn_idx]
    if cpn_idx == 0:
        new_parent_node_list = []
    #print("i")
    #print(i)
    if current_parent.data != -1:
        [l_child_data, r_child_data] = input().strip().split(' ')
        i += 1
        [l_child_data, r_child_data] = [int(l_child_data), int(r_child_data)]
        """
        print()
        print("current parent data != -1")
        print("cpn_idx")
        print(cpn_idx)
        print("current_parent_node_list")
        print([node.data for node in current_parent_node_list])
        print("current_parent.data")
        print(current_parent.data)
        print("left and right childs data")
        print([l_child_data, r_child_data])
        """
        [l_child,r_child] = [TreeNode(l_child_data), TreeNode(r_child_data)]
        #print("new parent node list before")
        #print([node.data for node in new_parent_node_list])
        new_parent_node_list.append(l_child)
        new_parent_node_list.append(r_child)
        #print("new parent node list after")
        #print([node.data for node in new_parent_node_list])
        current_parent.left = l_child
        current_parent.right = r_child
    #else:
        """
        print()
        print("currrent parent data is -1")
        print("cpn_idx")
        print(cpn_idx)
        print("current_parent_node_list")
        print([node.data for node in current_parent_node_list])
        print("current_parent.data")
        print(current_parent.data)
        """
    if cpn_idx < len(current_parent_node_list)-1:
        cpn_idx += 1
    else:
        cpn_idx = 0
        level_lists.append(current_parent_node_list)
        current_parent_node_list = new_parent_node_list
    
num_queries = int(input().strip())
for j in range(num_queries):
    k = int(input().strip())
    t.swapNodes(k,level_lists)
    t.root.printInOrder()
    print()
