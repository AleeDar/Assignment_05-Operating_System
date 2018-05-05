
no_of_processes = input("\nHow many processes? : ")
Quantum_Time = input("\nQuantim Time? : ")

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
Ready_Queue.sort(key = lambda x: x[1])

print("\npName\tA.T\tB.T")
for k in range(no_of_processes):
    print(Ready_Queue[k][0]),("\t"),(Ready_Queue[k][1]),("\t"),(Ready_Queue[k][2])

loop = 0
for k in range(len(Ready_Queue)):
    if(Ready_Queue[k][2] <= Quantum_Time):
        loop = loop + 1
    if(Ready_Queue[k][2] > Quantum_Time):
        mod = 0
        modd = 0
        mod_real = 0.0
        mod = Ready_Queue[k][2] / Quantum_Time
        #print mod
        modd = mod
        #print modd
        mod = mod*1.0
        #print mod
        mod_real = (Ready_Queue[k][2]*1.0) / (Quantum_Time*1.0)
        #print mod_real
        if(mod_real > mod):
            loop = loop + (modd + 1)
        else:
            loop = loop + modd
#print loop 

print("")
CPU_idle_time = 0
total_CPU_idle_time = 0
exe_time = 0
for k in range(loop):
    
    if (exe_time < Ready_Queue[k][1]):
        CPU_idle_time = Ready_Queue[k][1] - exe_time
        total_CPU_idle_time += CPU_idle_time
        exe_time = Ready_Queue[k][1]
        
    # Start Time --> Ready_Queue[k][3]
    #print k
    Ready_Queue[k].append(exe_time)

    if (Ready_Queue[k][2] <= Quantum_Time):
        exe_time = exe_time + Ready_Queue[k][2]
        # Finish/Quantum Time --> Ready_Queue[k][4]
        Ready_Queue[k].append(exe_time)
    else:
        exe_time = exe_time + Quantum_Time
        # Finish/Quantum Time --> Ready_Queue[k][4]
        Ready_Queue[k].append(exe_time)
        remaining_burst_time = Ready_Queue[k][2]- Quantum_Time
        uncomplete_process = []
        uncomplete_process = Ready_Queue[k][:3]
        uncomplete_process[2] = remaining_burst_time
        Ready_Queue.append(uncomplete_process)
        del uncomplete_process
    if (CPU_idle_time != 0):
        print("CPU remains idle for"),(CPU_idle_time),("time units")
    CPU_idle_time = 0
    print("Process"),(Ready_Queue[k][0]),("started execution at time:"),(Ready_Queue[k][3]),(" and stoped at time:"),(exe_time)
    # Waiting Time Of Process In RR --> Ready_Queue[k][5]
    w = Ready_Queue[k][1] + Ready_Queue[k][2]
    Ready_Queue[k].append(Ready_Queue[k][4] - w)
    # Turnaround Time Of Process in RR --> Ready_Queue[k][6]
    Ready_Queue[k].append(Ready_Queue[k][4] - Ready_Queue[k][1])

for m in range(loop):
    print "\t\t\t",str(Ready_Queue[m][3])+"..."+str(Ready_Queue[m][0])+"..."+str(Ready_Queue[m][4])


for m in range(no_of_processes):
    for n in range(no_of_processes, loop):
        if(Ready_Queue[m][0] == Ready_Queue[n][0]):
            if(Ready_Queue[m][4] < Ready_Queue[n][4]):
                Ready_Queue[m][4] = Ready_Queue[n][4]
            if(Ready_Queue[m][6] < Ready_Queue[n][6]):
                Ready_Queue[m][6] = Ready_Queue[n][6]
            

for m in range(no_of_processes):
    # Waiting Time Of Process In RR --> Ready_Queue[k][5]
    w = Ready_Queue[m][1] + Ready_Queue[m][2]
    w = Ready_Queue[m][4] - w
    Ready_Queue[m][5] = w

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
