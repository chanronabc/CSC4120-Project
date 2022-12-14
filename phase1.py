class Node:
    def __init__(self, index):
        self.child = []
        self.index = index

    def add_child(self, child):
        self.child.append(child)

def read_data():
    case_id = input("Please type the id of case: ")
    if(case_id != 0):
        testCase = "testCase" + case_id + ".txt"
    else:
        testCase = "testCase"  + ".txt"
    print(testCase)
    with open(testCase) as f:
        
read_data()