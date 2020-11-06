from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break
                distance = i - stack[-1] - 1
                min_high = min(height[i], height[stack.pop()]) * distance
                volume += min_high
            stack.append(i)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Solution.trap()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
