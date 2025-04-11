import statistics

# list = [2,32,2,2,5,5,31,7]
# m = sum(list)/len(list)
# print(m)
# n  = statistics.mean(list)
# print(n)

list = [7,8,2,1,3,4,5,6]
m = list.sort()
median = list[len(list)//2]
print(median)
n = statistics.median(list)
print(n)