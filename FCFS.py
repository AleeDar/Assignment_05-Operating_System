
no_of_processes = input("\nHow many processes? : ")

Ready_Queue = []

for n in range(no_of_processes):
    process_info = []
    # Process Name --> process_info[0]
    if (n == 0):
        process_info.append(raw_input("\nEnter 1st process NAME : "))
    else:
        process_info.append(raw_input("\nEnter next process NAME : "))
    # Arrival Time --> process_info[1]
    process_info.append(input("Enter process Arrival-Time : "))
    # Burst Time --> process_info[2]
    process_info.append(input("Enter process Burst-Time : "))
    # Process Name --> Ready_Queue[k][0]
    # Arrival Time --> Ready_Queue[k][1]
    # Burst Time --> Ready_Queue[k][2]
    Ready_Queue.append(process_info)
    del process_info

# Sorting w.r.t arrival time
for i in range(no_of_processes-1):
    for j in range(no_of_processes-1-i):
        if Ready_Queue[j][1] > Ready_Queue[j+1][1]:
            temp_process = Ready_Queue[j]
            Ready_Queue[j] = Ready_Queue[j+1]
            Ready_Queue[j+1] = temp_process

print("\npName\tA.T\tB.T")
for k in range(no_of_processes):
    print(Ready_Queue[k][0]),("\t"),(Ready_Queue[k][1]),("\t"),(Ready_Queue[k][2])

print("")
CPU_idle_time = 0
total_CPU_idle_time = 0
exe_time = 0
for k in range(no_of_processes):
    if (exe_time < Ready_Queue[k][1]):
        CPU_idle_time = Ready_Queue[k][1] - exe_time
        total_CPU_idle_time += CPU_idle_time
        exe_time = Ready_Queue[k][1]
    # Start Time --> Ready_Queue[k][3]
    Ready_Queue[k].append(exe_time)
    exe_time += Ready_Queue[k][2]
    # Finish Time --> Ready_Queue[k][4]
    Ready_Queue[k].append(exe_time)
    if (CPU_idle_time != 0):
        print("CPU remains idle for"),(CPU_idle_time),("time units")
    print("Process"),(Ready_Queue[k][0]),("started execution at time:"),(Ready_Queue[k][3]),(" and terminated at time:"),(exe_time)
    # Waiting Time Of Process In FCFS --> Ready_Queue[k][5]
    Ready_Queue[k].append(Ready_Queue[k][3] - Ready_Queue[k][1])
    # Turnaround Time Of Process in FCFS --> Ready_Queue[k][6]
    Ready_Queue[k].append(Ready_Queue[k][4] - Ready_Queue[k][1])

print("\npName\tA.T\tB.T\tS.T\tF.T\tW.T\tT.T")
for k in range(no_of_processes):
    print(Ready_Queue[k][0]),("\t"),(Ready_Queue[k][1]),("\t"),(Ready_Queue[k][2]),("\t"),(Ready_Queue[k][3]),("\t"),(Ready_Queue[k][4]),("\t"),(Ready_Queue[k][5]),("\t"),(Ready_Queue[k][6])

awt = 0.0
att = 0.0
for k in range(no_of_processes):
    awt += Ready_Queue[k][5]
    att += Ready_Queue[k][6]

del Ready_Queue
awt = awt/no_of_processes
att = att/no_of_processes

print("\nAverage Waiting Time:"),(awt)
print("Average Turnaround Time:"),(att)
print("Total CPU idle time till the last process terminated:"),(total_CPU_idle_time)
    
