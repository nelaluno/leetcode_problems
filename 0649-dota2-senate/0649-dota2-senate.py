RIVALS = {"R": "D", "D": "R"}
FULL_NAMES = {"R": "Radiant", "D": "Dire"}

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        
        to_bane = {"R": 0, "D": 0}
        while True:
            senate_count = {
                "R": senate.count("R"), 
                "D": senate.count("D")
            }
            
            new_senate = []
            banned = {"R": 0, "D": 0}
            voted_with_ban = {"R": 0, "D": 0}
            for party in senate:
                if to_bane[party]:
                    banned[party] += 1
                    to_bane[party] -= 1
                    continue
                
                rival = RIVALS[party]
                rivals_standing = senate_count[rival] - banned[rival] - to_bane[rival]
                if rivals_standing:
                    to_bane[rival] += 1
                    voted_with_ban[party] += 1
                else:
                    return FULL_NAMES[party]

                new_senate.append(party)
                        
            senate = new_senate


