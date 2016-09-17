# Nested Lists
N = int(raw_input().strip())
full_list = []

for i in range(0,N):
    student = raw_input().strip()
    mark = float(raw_input())
    full_list.append([student,mark])

min_mark = min(full_list,key = lambda k: k[1])[1]
min_mark_removed = [x for x in full_list if x[1]!= min_mark]
second_lowest_mark = sorted([i[0] for i in min_mark_removed if i[1]==min(min_mark_removed,key = lambda k: k[1])[1]])
print("\n".join(second_lowest_mark))
