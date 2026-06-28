class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        for p,s in cars[::-1]:
            t = (target-p)/s
            if not stack or stack[-1]<t:
                stack.append(t)
        return len(stack)