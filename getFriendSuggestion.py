def getFriendSuggestion(friends, person):
    candidates = set()
    for friend in friends[person]:
        for ff in friends[friend]:
            if ff not in friends[person]:
                candidates.add(ff)


    max = 0
    res = None
    print(candidates)
    for candidate in candidates:
        tmp = 0
        for cand in friends[candidate]:
            if cand in friends[person]:
                tmp += 1

        if tmp >= max:
            max = tmp
            res = candidate
    return res

friends = {
    1: set([2, 4]),
    2: set([3]),
    3: set([2, 4]),
    4: set([3, 5]),
    5: set([4])
}

print(getFriendSuggestion(friends, 1))
