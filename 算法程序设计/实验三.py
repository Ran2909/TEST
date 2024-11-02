def min_time_scheduling_GA(tasks):
    machine_1=0
    machine_2=0
    tasks.sort()
    tasks.reverse()
    for task in tasks:
        if machine_1<=machine_2:
            machine_1+=task
        else :
            machine_2+=task
        print(machine_2,machine_1)
    return max(machine_2,machine_1)
tasks=[3, 4, 2, 6, 3, 3, 8, 7, 5, 2]
print(min_time_scheduling_GA(tasks))
