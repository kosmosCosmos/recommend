import pandas as pd
import math
from operator import itemgetter

data = pd.read_csv('own.csv')
X = data['user_id']
Y = data['movie_id']

item_user = dict()
for i in range(X.count()):
    user = X.iloc[i]
    item = Y.iloc[i]
    if item not in item_user:
        item_user[item] = set()
    item_user[item].add(user)

C = {}
N = {}
for i, users in item_user.items():
    for u in users:
        N.setdefault(u, 0)
        N[u] += 1
        C.setdefault(u, {})
        for v in users:
            if u == v:
                continue
            C[u].setdefault(v, 0)
            C[u][v] += 1
W = C.copy()
for u, related_users in C.items():
    for v, cuv in related_users.items():
        W[u][v] = cuv / math.sqrt(N[u] * N[v])


def recommend(user, user_item, W, K):
    rank = dict()
    interacted_items = user_item[user]
    for v, wuv in sorted(W[user].items(), key=itemgetter(1), reverse=True)[0:K]: #从大到小
        for i in user_item[v]:
            if i not in interacted_items:
                rank.setdefault(i, 0)
            rank[i] += wuv
    return rank


rank = recommend(X, Y, W, 3)
print(rank)
