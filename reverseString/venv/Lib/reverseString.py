from stack import Stack

def reverse_string(stack, str_in):
    s = Stack()
    for i in  range(len(str_in)):
        s.push(str_in[i])


    rev_str = ""
    while not s.is_empty():
        rev_str += s.pop()

    return rev_str

a = Stack()
str_in = "Hello"

print(reverse_string(a, str_in))






