class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)

        for ast in asteroids:
            if ast > mass:
                return False
            mass += ast
        
        return True