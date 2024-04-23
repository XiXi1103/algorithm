ans = 0

source = input()
target = input()

l_source = len(source)
l_target = len(target)

cursor = 0

while cursor < l_target:
    flag = False
    temp = 0
    while temp < l_source:
        if cursor < l_target and target[cursor] == source[temp]:
            flag = True
            cursor += 1
        temp += 1
    if not flag:
        ans = -1
        break
    ans += 1
print(ans)
