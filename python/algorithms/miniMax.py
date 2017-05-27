# Mini-Max Sum
## Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers

arr = map(int, raw_input().strip().split(' '))
print sum(arr) - max(arr), sum(arr) - min(arr)
