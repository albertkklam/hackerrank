# Grading Students
## https://www.hackerrank.com/challenges/grading

n = int(raw_input().strip())

def solve(grades):
    return [g + 5 - (g%5) if (g%5 >= 3) & (g >= 38) else g for g in grades]
    
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
