def taskAssignment(k, tasks):
    # sort the task
    sorted_task = sorted(list(enumerate(tasks)), key=lambda x: x[1])
    tasks_tuples = []
    for i in range(k):
        tasks_tuples.append((sorted_task[i][0], sorted_task[(len(tasks) - 1 - i)][0]))

    return tasks_tuples
