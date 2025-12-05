class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        for ind, ast in enumerate(asteroids):
            ast_size = abs(ast)
            if ast < 0: # left
                # if we passed not collided asteroids moving right, 
                # go through them from ind-1 to 0
                # until ast_size > asteroids
                for collision_ind in range(ind-1, -1, -1):
                    if not asteroids[collision_ind]:
                        continue
                    
                    if asteroids[collision_ind] < 0:
                        break

                    coll_size = abs(asteroids[collision_ind])
                        
                    if ast_size == coll_size:
                        asteroids[collision_ind] = 0
                        asteroids[ind] = 0
                        break
                    if ast_size < coll_size:
                        asteroids[ind] = 0
                        break

                    asteroids[collision_ind] = 0
        
        return [a for a in asteroids if a]