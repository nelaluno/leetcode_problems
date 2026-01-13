class Square:
    def __init__(self, x, y, l):
        self.x1 = x
        self.y = y
        self.y_top = y + l
        self.area = l*l
        self.l = l

    def get_bottom_area(self, y):
        if self.y > y:
            return 0
        if self.y_top < y:
            return self.area
        return self.area * ((y - self.y)/self.l)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_max = 0
        total_area = 0
        for i, (x, y, l) in enumerate(squares):
            square = Square(x, y, l)
            y_max = max(y_max, square.y_top)
            squares[i] = square
            total_area += square.area
        
        goal = total_area / 2
        y_min = 0
        while y_max - y_min > 1e-5:
            mid = (y_max + y_min) / 2
            bottom_area = 0
            for square in squares:
                bottom_area += square.get_bottom_area(mid)
                if bottom_area > goal:
                    break
            if bottom_area >= goal:
                y_max = mid                
            else:
                y_min = mid
        
        return y_min
        