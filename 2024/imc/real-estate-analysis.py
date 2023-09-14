from collections import defaultdict
from math import sqrt
from bisect import bisect_left

def analyze(area, price, reqArea):
    n = len(area)
    groupings = defaultdict(list)
    grouping_sums = defaultdict(int)
    for aa, pp in zip(area, price):
        groupings[aa].append(pp)
        grouping_sums[aa] += pp
    print(groupings)

    keep_groupings = defaultdict(list)

    for aa, ll in groupings.items():
        groupLen = len(ll)
        if groupLen == 1:
            keep_groupings[aa] = ll
            continue
        if groupLen == 2:
            continue
        for i in range(groupLen):
            curPrice = ll[i]
            compSum = grouping_sums[aa] - curPrice
            compLen = groupLen - 1
            compMean = compSum / compLen
            residualSqMean = sum([(ll[j]-compMean)**2 for j in range(groupLen) if j != i]) / compLen
            compStd = sqrt(residualSqMean)
            if abs(curPrice-compMean) <= 3*compStd:
                keep_groupings[aa].append(curPrice)

    grouping_mean = defaultdict(int)
    for aa, ll in keep_groupings.items():
        grouping_mean[aa] = sum(keep_groupings[aa]) / len(keep_groupings[aa])
    print(keep_groupings, grouping_mean)

    if len(keep_groupings) == 0:
        return 1000
    if reqArea in keep_groupings:
        if len(keep_groupings[reqArea]) == 1:
            return keep_groupings[reqArea][0]
        else:
            return round(sum(keep_groupings[reqArea]) / len(keep_groupings[reqArea]))
    else:
        keep_areas = list(keep_groupings.keys())
        keep_areas.sort()
        print(keep_areas, keep_groupings)
        x1, x2, y1, y2 = 0, 0, 0, 0
        if reqArea < keep_areas[0]: # extrapolate
            x1 = keep_areas[0]
            x2 = keep_areas[1]
        elif reqArea > keep_areas[-1]:
            x1 = keep_areas[-2]
            x2 = keep_areas[-1]
        else: # intrapolate
            idx = bisect_left(keep_areas, reqArea)
            prev = max(0, idx-1)
            x1 = keep_areas[prev]
            x2 = keep_areas[idx]

        y1 = grouping_mean[x1]
        y2 = grouping_mean[x2]
        print(keep_areas, x1, x2, y1, y2)
        print(round(y1 + (reqArea - x1) * (y2 - y1) / (x2 - x1)))
        return round(y1 + (reqArea - x1) * (y2 - y1) / (x2 - x1))







analyze([1200, 1300, 1200, 1300, 1200, 2000], [12000, 24000, 14000, 22000, 13000, 30000], 1500)
