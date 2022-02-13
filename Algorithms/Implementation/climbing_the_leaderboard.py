# n = int(input())
# ranked = [int(x) for x in input().split()]
# m = int(input())
# player = [int(x) for x in input().split()]
#
# rank = 1
# ranks = {}
#
# for score in ranked:
#     if score not in ranks:
#         ranks[score] = rank
#         rank += 1
#
# player_ranks = []
#
# for player_score in player:
#     for score, rank in ranks.items():
#         if player_score < min(ranks.keys()):
#             player_ranks.append(max(ranks.values()) + 1)
#             break
#         if player_score >= score:
#             player_ranks.append(rank)
#             break
#
# for x in player_ranks:
#     print(x)

# More efficient algorithm:

n = int(input())
ranked = sorted(set([int(x) for x in input().split()]), reverse=True)
m = int(input())
player = [int(x) for x in input().split()]

for player_score in player:
    rank = 1
    for rank_score in ranked:
        if player_score < rank_score:
            rank += 1
        else:
            break
    print(rank)
