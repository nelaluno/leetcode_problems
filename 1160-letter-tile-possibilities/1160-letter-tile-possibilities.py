from collections import Counter


class Solution:
    def solve(self, counted_tiles):
        if not any(counted_tiles):
            return 1
        possibilities = len([v for v in counted_tiles.values() if v])
        for letter in counted_tiles:
            if not counted_tiles[letter]:
                continue
            counted_tiles[letter] -= 1
            possibilities += self.solve(counted_tiles)
            counted_tiles[letter] += 1
        return possibilities

    def numTilePossibilities(self, tiles: str) -> int:
        counted_tiles = Counter(tiles)
        return self.solve(counted_tiles)
