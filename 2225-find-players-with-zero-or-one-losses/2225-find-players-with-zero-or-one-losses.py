class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)

        for match in matches:
            losers[match[1]] += 1

        for match in matches:
            if match[0] not in losers:
                winners.add(match[0])

        winners_list = sorted(list(winners))
        losers_list = [loser for loser, count in losers.items() if count == 1]
        losers_list.sort()

        result = [winners_list, losers_list]
        return result