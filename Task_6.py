runner_has_done = 2
runner_goal = 10
day = 1
print(f'day {day} - runner has done {runner_has_done} km')

while runner_has_done <= runner_goal:
    runner_has_done = runner_has_done * 1.1
    day += 1
    print(f'day {day} runner has done '+ ('%.2f' % runner_has_done) )
    #git