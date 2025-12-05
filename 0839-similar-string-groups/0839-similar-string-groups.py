class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        result = 0
        s_len = len(strs[0])
        group = -1
        links = [None] * len(strs)
        for i1, s1 in enumerate(strs):
            for i2, s2 in enumerate(strs[i1+1:], start=i1+1):
                diff_count = 0
                for k in range(s_len):
                    if s1[k] != s2[k]:
                        diff_count += 1
                if diff_count < 3:
                    if links[i1] is not None:
                        if links[i2] is None:
                            links[i2] = links[i1]
                        else:
                            i2_group = links[i2]
                            for j in range(len(strs)):
                                if links[j] == i2_group:
                                    links[j] = links[i1]
                    else:
                        if links[i2] is None: 
                            group += 1
                            links[i2] = group
                            links[i1] = group
                        else:
                            links[i1] = links[i2]
                    # print(links)

        single_count = 0
        for l in links:
            if l is None:
                single_count += 1
        if single_count:
            single_count -= 1
        return len(set(links)) + single_count