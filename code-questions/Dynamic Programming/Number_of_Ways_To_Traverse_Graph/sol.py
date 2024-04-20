def numberOfWaysToTraverseGraph(width, height):
    small = width if width < height else height
    large = height if height > width else width

    graph = [[1 for s in range(1, small+1)] for x in range(2)]

    for i in range(1, large):
        for col in range(1, small):
            graph[1][col] = graph[0][col] + graph[1][col-1]

        graph[0] = graph[1][:]

    return graph[-1][-1]