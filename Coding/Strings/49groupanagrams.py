import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in seen:
                seen[sorted_s] = seen[sorted_s] + [s]
            else:
                seen[sorted_s] = [s]
        return list(seen.values())

    # same as above but compact
    def groupAnagrams1(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w)) 
            d[key] = d.get(key, []) + [w]  # if else in above method is replaced by this 1 line.
        return d.values()

    def groupAnagrams2(self, strs):
        # without sort, use array of 26 lowercase letters, optimize to O(nk) time, and O(nk) space.
        # map the tuple of array to string.
        hmap = collections.defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l) - ord('a')] += 1
            hmap[tuple(array)].append(st)
        return list(hmap.values())

print(Solution().groupAnagrams2(["abc", "cab", "bat"]))
print(Solution().groupAnagrams(["abc"]))
print(Solution().groupAnagrams(["a"]))