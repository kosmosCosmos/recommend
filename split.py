import random


def SplitData(data, M, k, seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data.items():
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test

data = {}

for i in range(50):
    data["x"+str(i)] = i
train, test = SplitData(data, 8, 1, 6)
print(train)
print(test)
