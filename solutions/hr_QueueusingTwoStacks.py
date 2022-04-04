# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    de = deque()

    for tests_itr in range(tests):
        action = input()
        if action[0] == '1':
            number = action[1:].strip()
            de.append(number)
        elif action[0] == '2':
            de.popleft()
        elif action[0] == '3':
            fptr.write(de[0] + '\n')

    fptr.close()
