n = int(input())
list = list(map(int, input().split()))
target = int(input())
pos =-1 
for i in range(0, len(list)):
    if list[i] == target:
        pos =i
        break
print(pos)