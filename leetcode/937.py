from typing import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, letter = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit

if __name__ == '__main__':
    print("hello")