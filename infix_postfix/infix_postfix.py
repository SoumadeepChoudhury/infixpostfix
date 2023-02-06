
class Stack:
    def __init__(self) -> None:
        self.STACK = list()

    def isEmpty(self) -> bool:
        if self.STACK == []:
            return True
        return False

    def push(self, item: str) -> None:
        self.STACK.append(item)

    def pop(self) -> str:
        if self.isEmpty():
            return "Underflow"
        item: str = self.STACK.pop()
        return item

    def peek(self) -> str:
        if self.isEmpty():
            return "Underflow"
        else:
            return self.STACK[-1]


def isHigherPrecedence(val1: str, val2: str) -> bool:
    """Returns True if 1st value have higher precedence than 2nd value."""
    PRECEDENCE: list = ["^", "*/", "+-"]
    val1_index: int = None
    val2_index: int = None
    for i in range(len(PRECEDENCE)):
        if val1 in PRECEDENCE[i]:
            val1_index = i
        if val2 in PRECEDENCE[i]:
            val2_index = i
    if val1_index != None and val2_index != None:
        if val1_index > val2_index or (val1_index == 0 and val2_index == 0):
            return False
        else:
            return True
    else:
        return False


def postfix(infix: str) -> str:
    STACK: object = Stack()
    if infix[0] != "(" or infix[-1] != ")":
        infix = "("+infix+")"
    postfix: str = ""
    for i in infix:
        if i in "(+-*/^":
            while isHigherPrecedence(STACK.peek(), i):
                item: str = STACK.pop()
                if item not in ("Underflow", "(", ")"):
                    postfix += item
            STACK.push(i)
        elif i == ")":
            while STACK.peek() != "(":
                item: str = STACK.pop()
                if item not in ("Underflow", "(", ")"):
                    postfix += item
            item: str = STACK.pop()
            if item not in ("Underflow", "(", ")"):
                postfix += item
        else:
            postfix += i
    return postfix


def infix(postfix: str) -> str:
    STACK: object = Stack()
    for i in postfix:
        if i not in "+-*/^":
            STACK.push(i)
        else:
            after: str = STACK.pop()
            before: str = STACK.pop()
            evaluated: str = "("+before+i+after+")"
            STACK.push(evaluated)
    return STACK.pop()[1:-1]


def main():
    import sys
    if sys.argv[1] == "--infix":
        print(postfix(sys.argv[2]))
    elif sys.argv[1] == "--postfix":
        print(infix(sys.argv[2]))
