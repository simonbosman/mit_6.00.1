class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranche = None
        self.rightBranche = None
        self.parent = None
    
    def setLeftBranch(self, node):
        self.leftBranche = node
    
    def setRightBranch(self, node):
        self.rightBranche = node
    
    def setParent(self, node):
        self.parent = node
    
    def getLeftBranch(self):
        return self.leftBranche
        
    def getRightBranch(self):
        return self.rightBranche
        
    def getParent(self):
        return self.parent
        
    def getValue(self):
        return self.value
        
    def __str__(self):
        return self.value
 
#Depth First Search
def DFSBinary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        print 'dfs node is ' + str(stack[0].getValue())
        if fcn(stack[0]):
           return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False

#DFS Binary Path
def DFSBinaryPath(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return TracePath(stack[0])
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False
                                    
# Trace path of a node
def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())
        
#DFS Binary Ordered
def DFSBinaryOrdered(root, fcn, ltFcn):
    stack = [root]
    while len(stack) > 0:
        print 'dfs ordered node is ' + str(stack[0].getValue())
        if fcn(stack[0]):
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
    return False
        
# Breadth First Search
def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print'bfs node is ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False
                   
# build a binary three
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)

def find5(node):
    return node.getValue() == 5

def find3(node):
    return node.getValue() == 3
    
def find10(node):
    return node.getValue() == 10

def lt3(node):
    return node.getValue() > 3
    
print DFSBinary(n8, find5)
print DFSBinary(n3, find3) 
print DFSBinary(n5, find10)   

print BFSBinary(n8, find5)
print BFSBinary(n3, find3)
print BFSBinary(n5, find10)

print [el.getValue() for el in DFSBinaryPath(n5, find3)]
print DFSBinaryOrdered(n5, find3, lt3)
