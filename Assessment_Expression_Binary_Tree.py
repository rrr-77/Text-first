"""
1 This procedure according to the mathematical expression into a binary tree, and then print the binary tree in order.
2 Example: expression: "(2/(7+((6+4)*3))"
3 Middle-order visual printing binary tree: used for testing input rule function:
test Actual running function: run
The core principle is:
1. write a binary tree.
2. Check whether the input expression valid or not.
3. Break them down and form an instance of binary tree.
3. compute the expressions results.
4.  print the result through the middle-order traversal and save it in tree.txt
5. text with unittest module
"""

# set a class first
class Tree:
    # Class initialization & add value/left-node/right-node
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    # The idea of this function is similar to that of the "operator" module
    def calculate(self):
        # A subtree, represented by None if empty  PS: not null (This is python)
        if self.left==None and self.right==None:return self.val
        if isinstance(self.left,Tree):
            num1=self.left.calculate()
        else:
            num1=self.left
        if isinstance(self.right,Tree):
            num2=self.right.calculate()
        else:
            num2=self.right
        op=self.val
        # Perform different operations on different nodes
        if op=='+':new_num=float(num1)+float(num2)
        elif op=='-':new_num=float(num1)-float(num2)
        elif op=='*':new_num=float(num1)*float(num2)
        elif op=='/':new_num=float(num1)/float(num2)

        return new_num
    # Print (tree) for the expression  （use built-in functions __str__）
    def __str__(self):
        res=""
        if self.left != None:res+="("+str(self.left)
        if self.val in opList:
            res += str(self.val)
        else:

            res += str(int(self.val))
        if self.right != None:res+=str(self.right)+")"
        return res
# Visualize binary trees by using recursion (detecting the depth of the tree then recursive)
    def run(s) :
        # EG1
        node = make(s)
        print(node)

        return node
s="(2/(7+((6+4)*3)))"
def pritree(node,deep):
    res=""
    if node==None:return res
    if node.right!=None:res+=pritree(node.right,deep+1)
    res+=("  " * deep)
    if node.val in ["+","-","*","/"]:

        res+=(node.val)+"\n"
    else:

        res +=str(int(node.val))+"\n"
    res+=pritree(node.left,deep+1)
    return res
opList=["+","-","*","/"]
def  judge(s):
    l=0
    for val in s:
        if val=='(':
            l+=1
        elif val==')':
            if l<=0:return "Not a valid expression, brackets mismatched."
            l-=1
    if l!=0:return "Not a valid expression, brackets mismatched."
    nums=0
    ops=0
    brackets=0
    opnum=1
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            if ((i > 0 and s[i - 1] in opList) or (i + 1 < len(s) and s[i + 1] in opList)) == False\
                    and i + 1 < len(s) and s[i+1]=="(":
                return "Not a valid expression, operator missing."
    for i in range(len(s)):
        if s[i] in opList:
            opnum+=1
            ops+=1
        if s[i]=="(" :
            opnum=0
            brackets+=1
        elif  s[i]==')':
            if opnum != 1: return "Not a valid expression, wrong number of operands."
            opnum = 0
    if opnum != 0: return "Not a valid expression, wrong number of operands."
    if nums>ops+1 :return "Not a valid expression, operator missing."
    elif nums==ops+1 and brackets!=nums-1:return "Not a valid expression, operator missing."
    if nums!=brackets:return "Not a valid expression, brackets mismatched."
    return True
def make(s):
    node=creat(s)
    if str(node)==s:return node
    return judge(s)
def creat(s):
    if s[0]=='(' and s[-1]==')':s=s[1:-1]
    if len(s)==1:return Tree(float(s),None,None)
    if len(s)==3:
        left=creat(s[0])
        right=creat(s[2])
        if isinstance(left,str):return left
        if isinstance(right,str):return right
        return Tree(s[1],left,right)
    l=0
    for i in range(len(s)):
        if s[i]=='(':l+=1
        elif s[i]==')':l-=1
        if s[i] in opList and l==0:
            left=creat(s[:i])
            right=creat(s[i+1:])
            if isinstance(left, str): return left
            if isinstance(right, str): return right
            return Tree(s[i],left,right)
# Save the data to a file
# To be added: since module "pickle" can only be saved in binary in my tests(can't open), I choose to onlt use file instead.
# In fact, using pandas can also solve this problem
def save(s,node):
    with open('Tree.txt', 'w') as f:
        f.write(s+"\n")
        res = pritree(node, 0)
        f.write(res)
# build the tree in the txt
def load():
    with open('Tree.txt', 'r') as f:
        line=f.readline().replace("\n","")
        node=creat(line)
        return node
# then I write a function to test the given expressions.
def tests():
    expression="(4*3*2)"
    node1=make(expression)
    print(node1)

    expression = "(4*(2))"
    node2=make(expression)
    print(node2)

    expression = "(4*(3+2)*(2+1))"
    node3=make(expression)
    print(node3)

    expression = "(2*4)*(3+2)"
    node4=make(expression)
    print(node4)

    expression = "((2+3)*(4*5)"
    node5=make(expression)
    print(node5)

    expression = "(2+5)*(4/(2+2)))"
    node6=make(expression)
    print(node6)

    expression = "(((2+3)*(4*5))+(1(2+3)))"
    node7 = make(expression)
    print(node7)
    pass

# Run in the main program, and call the all functions
if __name__ == '__main__':
# #EG1
    s = "(2/(7+((6+4)*3)))"
    node = make(s)
    print(node)
    print(node.calculate())
    # 保存和读取
    save(s, node)
    new_node = load()
    print("NEW-TREE")
    #按照题目例子的格式打印
    print(pritree(new_node, 0))
    tests()

import unittest

# unittest
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("@@@ ALL case Run only once before running! @@@")
    def setUp(self):
        self.test_Tree = Tree()
        print('TEST-STARTS')

    # @classmethod
    @unittest.skip
    def test_EG1(self):
        self.assertIsInstance(self.test_tree.run(s,str,msg='no correct type'))

    def tearDown(self):
        del self.test_Tree
        print("TEST-ENDS")

if __name__ == '__main__':
    unittest.main()


