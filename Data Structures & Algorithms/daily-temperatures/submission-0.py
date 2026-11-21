class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each day, append it to the stack if its following day is not warmer.
        Stacks lets us defer decisions and resolve them in reverse order, exactly what we need here.
        
        We'll decide later on whether a future day is warmer than the current.

        Pop when we reach a day that's warmer than the top of the stack.
        Append the (day / index i, temp) otherwise. Hence, the stack will keep indices in a monotonically decreasing order (always eq or decreasing).

        Use an array of default values 0 of size len(temperatures) which we can return as output of function.
        """
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            # Pop condition: current day is warmer than what's at the top of the stack.
            while stack and t > stack[-1][1]:

                # We have met a temperature warmer than the current day.
                # Set the distance between the days to res[day].
                day, temp = stack.pop()
                res[day] = i - day

            # Since current day is not warmer than the top of the stack,
            # append it. Therefore, the stack would only contain monotonically
            # decreasing temperatures and their indices.
            stack.append((i, t))

        return res