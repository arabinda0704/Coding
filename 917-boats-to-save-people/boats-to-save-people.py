class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort()
        # l, r = 0, len(people) - 1
        # count = 0

        # while l <= r:
        #     if people[l] + people[r] <= limit:
        #         l += 1  # pair l and r together
        #     # r always boards the boat (either alone or with l)
        #     r -= 1
        #     count += 1

        # return count

        # Optimal
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
        