# Find the Second Largest Number
## Find the second largest number in an integer array

N, int_array = int(raw_input().strip()), map(int, raw_input().strip().split())
print max([x for x in int_array if x != max(int_array)])
