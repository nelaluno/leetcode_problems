from  itertools import cycle
class Solution:
    first_functions = {
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }

    
    def clumsy(self, n: int) -> int:
        operations = cycle(["*", "/", "+", "-"])
        first_prev = n
        result = 0
        for i in range(n-1, 0, -1):
            op = next(operations)
            print(result, first_prev, op, i)
            if op in self.first_functions:
                first_prev = self.first_functions[op](first_prev, i)
            elif op == "+":
                if not result:
                    result = result + first_prev + i
                else:
                    result = result - first_prev + i
                first_prev = 0
            else:
                first_prev = i
        
        if not result:
            result = first_prev
        else:
            result -= first_prev

        return result

