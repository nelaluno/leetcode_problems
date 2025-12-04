class Solution:
    def countCollisions(self, directions: str) -> int:
        left_collision = -1 # -1 - no, 0 - yes, 1 - moving right
        result = 0

        for d in directions:
            if d == "L":
                if left_collision >=0:
                    result += left_collision + 1
                    left_collision = 0 # stopped
            elif d == "R":                
                if left_collision >= 0: # smth moving
                    left_collision += 1
                else:
                    left_collision = 1
            else:
                if left_collision > 0:
                    result += left_collision
                left_collision = 0 # not moving

        return result