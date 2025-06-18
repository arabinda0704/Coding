class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i=k=0
        for j in range(len(trainers)):
            if i < len(players) and players[i]<=trainers[j]:
                k+=1
                i+=1
        return k
        #Using While
        # players.sort()
        # trainers.sort()
        # i=j=k=0
        # while i<len(players) and j<len(trainers):
        #     if players[i]<=trainers[j]:
        #         k+=1
        #         i+=1
        #     j+=1
        # return k 