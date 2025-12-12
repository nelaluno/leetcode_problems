from collections import defaultdict
import numpy as np

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda x: (int(x[1]), x[0] != "OFFLINE"))
        mentions = np.zeros(numberOfUsers, dtype=np.uint32)
        online = np.ones(numberOfUsers, dtype=np.uint32)
        all_users = np.ones(numberOfUsers, dtype=np.uint32)
        online_events = [] # timepstamp (int), users (list)
        
        for ev_name, timestamp, users in events:
            timestamp = int(timestamp)
            while online_events and online_events[0][0] <= timestamp:
                _,  back_online = online_events.pop(0)
                for user in back_online:
                    online[user] = 1

            if ev_name == "MESSAGE":
                if users == "HERE":
                    mentions += online
                elif users == "ALL":
                    mentions += all_users
                else:
                    for u_id in users.split(" "):
                        mentions[int(u_id[2:])] += 1
            else:
                offline_users = [int(i) for i in users.split(" ")]
                online_events.append((timestamp + 60, offline_users))
                for i in offline_users:
                    online[i] = 0

        return mentions.tolist()


