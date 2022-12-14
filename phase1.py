class Node:
    def __init__(self, index):
        self.child = []
        self.index = index

    def add_child(self, child):
        self.child.append(child)

def read_data():
    case_id = int(input("Please type the id of case: "))
    if(case_id != 0):
        testCase = "testCase" + str(case_id) + ".txt"
    else:
        testCase = "testCase"  + ".txt"

    with open(testCase) as f:
        node_num = int(f.readline())
        node_info = []
        for i in range(node_num):
            string = f.readline()
            if(string != ""):
                node_info.append(string)

    nodes_info = []
    for i in range(len(node_info)):
        nodes = node_info[i].split(" ")
        for j in range(len(nodes)):
            if(nodes[j] != '\n' and nodes[j] != " "):
                nodes[j] = int(nodes[j])
            else:
                nodes.remove(nodes[j])
        nodes_info.append(nodes)

    Node_list = []
    for i in range(node_num):
        node = Node(i+1)
        Node_list.append(node)
    
    for i in range(len(node_info)):
        node = Node_list[nodes_info[i][0]-1]
        if(len(nodes_info[i]) > 1):
            for j in range(1, len(nodes_info[i])):
                node.child.append(Node_list[nodes_info[i][j]-1])
        Node_list[i] = node

    return Node_list[0]

def validate(node):
    if(len(node.child)==0):
        return
    list = []
    list.append(node.index)
    for i in range(len(node.child)):
        child = node.child[i]
        list.append(child.index)
    for x in list:
        print(x, end=" ")
    print('\n')
    for i in range(len(node.child)):
        child = node.child[i]
        validate(child)

node = read_data()
# Validation
# validate(node)