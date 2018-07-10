# Decorators 2 - Name Directory
## https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
### Python 3.6

def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key = lambda x: int(x[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')