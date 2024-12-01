def areAnagrams(self, s1, s2):
    hash_map = {}
    hashy = {}
    for i in s1:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for j in s2:
        if j in hashy:
            hashy[j] += 1
        else:
            hashy[j] = 1
    return hash_map == hashy
