class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1  # pair l and r together
            # r always boards the boat (either alone or with l)
            r -= 1
            count += 1

        return count
        