from collections import defaultdict


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = [False] * len(rooms)
        unlocked[0] = True
        to_visit = [0]

        while to_visit:
            curr_room = to_visit.pop()
            for key in rooms[curr_room]:
                if unlocked[key]:
                    continue
                unlocked[key] = True
                to_visit.append(key)

        return all(unlocked)



                    