class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True 
        
        prev_pot = None
        new_pots = 0
        for pot_i in range(len(flowerbed)):           
            if not flowerbed[pot_i] and not prev_pot and (pot_i == len(flowerbed) - 1 or not flowerbed[pot_i+1]):
                new_pots += 1
                if new_pots >= n:
                    return True
                prev_pot = 1
            else:
                prev_pot = flowerbed[pot_i]
        return False