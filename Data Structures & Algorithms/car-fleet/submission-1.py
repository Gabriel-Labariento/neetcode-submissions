class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {position[i]: speed[i] for i in range(len(position))}
        stack = []
        position.sort(reverse=True)

        for car in position:
            stack.append((target - car) / d[car])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



