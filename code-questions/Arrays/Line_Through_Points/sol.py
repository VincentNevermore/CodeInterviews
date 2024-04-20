def lineThroughPoints(points):
    res = 1
    for i in range(len(points)):
        p1 = points[i]
        count = dict()
        for j in range(i+1, len(points)):
            p2 = points[j]
            if p1[0] == p2[0]:
                slope = float("inf")
            else:
                x1,y1 = p1
                x2,y2 = p2
                slope = (y2 - y1) / (x2 - x1)

            if slope in count:
                count[slope] += 1
            else:
                count[slope] = 1

            res = max(res, count[slope] + 1)

    return res
