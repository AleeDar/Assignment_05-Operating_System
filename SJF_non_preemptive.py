
no_of_processes = input("\nHow many processes? : ")

Ready_Queue = []
Temp_Queue = []
Real_Ready_Queue = []

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

new_process_came = 0
t = 0
while (t >=0 ):
    for k in range(no_of_processes):
        if (Ready_Queue[k][1] == t):
            Temp_Queue.append(Ready_Queue[k])
            new_process_came += 1
            if(new_process_came == 1):
                Real_Ready_Queue.append(['null',0,0])
    
    if(new_process_came > 0):
        if((Real_Ready_Queue[-1][1]+Real_Ready_Queue[-1][2]) < (t+1)):
            if(len(Temp_Queue) != 0):
                Temp_Queue.sort(key = lambda x: x[2])
                Real_Ready_Queue.append(Temp_Queue.pop(0))
    
    if(len(Real_Ready_Queue) == no_of_processes+1):
        del Temp_Queue
        t = -1
    else:
        t = t+1

del Real_Ready_Queue[0]

"""
# Sorting w.r.t arrival time
    Ready_Que.sort(key = lambda x: x[1])

    # Now sorting w.r.t burst time with same arrival time
    for k in range(no_of_processes):
        if (no_of_processes > 1):
            same = 1
            while (k < no_of_processes-1):
                if(Ready_Que[k][1] < Ready_Que[k+1][1]):
                    same += 1
                    k += 1
                else:
                    k += 1
            # temp_queue contains processes with same A.T but different B.T
            if (same > 1):
                temp_queue = []
                for j in range(same):
                    temp_queue.append(Ready_Que[j])
                temp_queue.sort(key = lambda x: x[2])
                for m in range(same):
                    Ready_Que[m] = temp_queue[m]
                del temp_queue
"""

print("\npName\tA.T\tB.T")
for k in range(no_of_processes):
    print(Real_Ready_Queue[k][0]),("\t"),(Real_Ready_Queue[k][1]),("\t"),(Real_Ready_Queue[k][2])

print("")
CPU_idle_time = 0
total_CPU_idle_time = 0
exe_time = 0
for k in range(no_of_processes):
    if (exe_time < Real_Ready_Queue[k][1]):
        CPU_idle_time = Real_Ready_Queue[k][1] - exe_time
        total_CPU_idle_time += CPU_idle_time
        exe_time = Real_Ready_Queue[k][1]
    # Start Time --> Real_Ready_Queue[k][3]
    Real_Ready_Queue[k].append(exe_time)
    exe_time += Real_Ready_Queue[k][2]
    # Finish Time --> Real_Ready_Queue[k][4]
    Real_Ready_Queue[k].append(exe_time)
    if (CPU_idle_time != 0):
        print("CPU remains idle for"),(CPU_idle_time),("time units")
    CPU_idle_time = 0
    print("Process"),(Real_Ready_Queue[k][0]),("started execution at time:"),(Real_Ready_Queue[k][3]),(" and terminated at time:"),(exe_time)
    # Waiting Time Of Process In SJF --> Real_Ready_Queue[k][5]
    Real_Ready_Queue[k].append(Real_Ready_Queue[k][3] - Real_Ready_Queue[k][1])
    # Turnaround Time Of Process in SJF --> Real_Ready_Queue[k][6]
    Real_Ready_Queue[k].append(Real_Ready_Queue[k][4] - Real_Ready_Queue[k][1])

print("\npName\tA.T\tB.T\tS.T\tF.T\tW.T\tT.T")
for k in range(no_of_processes):
    print(Real_Ready_Queue[k][0]),("\t"),(Real_Ready_Queue[k][1]),("\t"),(Real_Ready_Queue[k][2]),("\t"),(Real_Ready_Queue[k][3]),("\t"),(Real_Ready_Queue[k][4]),("\t"),(Real_Ready_Queue[k][5]),("\t"),(Real_Ready_Queue[k][6])

awt = 0.0
att = 0.0
for k in range(no_of_processes):
    awt += Real_Ready_Queue[k][5]
    att += Real_Ready_Queue[k][6]

del Real_Ready_Queue
awt = awt/no_of_processes
att = att/no_of_processes

print("\nAverage Waiting Time:"),(awt)
print("Average Turnaround Time:"),(att)
print("Total CPU idle time till the last process terminated:"),(total_CPU_idle_time)
    
 
