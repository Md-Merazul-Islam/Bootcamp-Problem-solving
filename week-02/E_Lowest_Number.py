n = int(input())
a = list(map(int, input().split()))
min_value = min(a)
min_index = a.index(min_value) 
print(min_value, min_index + 1)