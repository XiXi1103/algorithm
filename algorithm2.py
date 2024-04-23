stack = []
err_right_index = []

string = input()

for index, c in enumerate(string):
    if c == '(':
        stack.append(index)
    if c == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            err_right_index.append(index)
ans = ""
for i in range(len(string)):
    if i in err_right_index:
        ans += "?"
    elif i in stack:
        ans += "x"
    else:
        ans += " "
print(ans)
