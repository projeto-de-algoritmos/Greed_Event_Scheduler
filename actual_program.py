import heapq
from random import randint

class priorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        if self.elements:
            return heapq.heappop(self.elements)[1]
        else:
            raise IndexError("pop from empty queue")

    def is_empty(self):
        return len(self.elements) == 0

def maxEmployeesRequired(jobList):
    customerCare = []
    while not jobList.is_empty():
        call = jobList.pop()
        assigned = False
        for employee in customerCare:
            if employee['end'] <= call['start']:
                assigned = True
                employee['end'] = call['end']
                break

        if not assigned:
            newEmployee = {"end": call['end']}
            customerCare.append(newEmployee)
    return len(customerCare)

def is_id_not_in_list(job_list, target_id):
    for job in job_list:
        if job['id'] == target_id:
            return False
    return True

jobList = [{"id":2, "start": 1000, "end": 1075}, {"id":3, "start": 1000, "end": 1100}, {"id":4, "start": 1000, "end": 1200}]
no_workers = -1

while True:
    print('######Temporary Menu#######')
    print('Selecione uma opção')
    print('1.- Inserir uma job')
    print('2.- Inserir no trabalhadores')
    print('3.- Worker schedule')
    print('4.- Calculate required number of workers')
    print('5.- Show job list')
    print('6.- Remove job')
    print('7.- Sair')
    option = input()
    
    if option == '1':
        start_h = input("Enter start time for job")
        start_m = input("Enter start time for job")
        
        if(int(start_h)<0 or int(start_h)>23 or int(start_m)<0 or int(start_m)>60):
            print("Start time invalid")
        else:
            start_t = str(start_h) + str(start_m)
            start_t = int(start_t)
            
            end_h = input("Enter end time for job")
            end_m = input("Enter end time for job")
            
            if(int(end_h)<0 or int(end_h)>23 or int(end_m)<0 or int(end_m)>60):
                print("end time invalid")
            else:
                end_t = str(end_h) + str(end_m)
                end_t = int(end_t)
                if(end_t<start_t):
                    print("end time cant be less tan start time")
                else:
                    #Create and validate id
                    id_i = randint(0,999)
                    checkid = is_id_not_in_list(jobList,id_i)
                    while checkid == False:
                        id_i = randint(0,999)
                        checkid = is_id_not_in_list(jobList,id_i)
            
                    new_job = {"id": id_i,"start": start_t, "end": end_t}
                    jobList.append(new_job)
    elif option == '2':
        no_input = int(input("Insert number of workers"))
        if(no_input < 0):
            print("Number of workers cant be less than 0")
        else:
            no_workers = no_input
    elif option == '3':
        jobList_c = jobList.copy()
        if no_workers > 0:
            for x in range(no_workers):
                # Interval scheduling
                jobList_c.sort(key=lambda x: (x["end"],x["start"]))
                count = 0
                visited = []
                end = -1
                for job in jobList_c:
                    if end <= job["start"]:
                        end = job["end"]
                        count += 1
                        visited.append(job)
                        jobList_c.remove(job)
                print(x+1, visited)
                if len(visited) == 0:
                    print("Warning worker has no jobs")
            if len(jobList_c) != 0:
                count_jl = 0
                for job in jobList_c:
                    count_jl = count_jl + 1
                print("Warning there are",count_jl,"unnasigned jobs left")
        else:
            print("Number of workers not defined")
    elif option == '4':
        # Priority queue
        pq = priorityQueue()
        for idx, job in enumerate(jobList):
            pq.push(job, (job["start"], idx))

        result2 = maxEmployeesRequired(pq)
        no_workers = result2
        print(result2)
    elif option == '5':
        for job in jobList:
            print("Id:",job["id"],"Starting time:",job["start"]," Ending time:",job["end"])
    elif option == '6':
        job_remove = int(input("Type id of job to remove"))
        remove_s = False
        for job in jobList:
            if job['id'] == job_remove:
                jobList.remove(job)
                remove_s = True
                print("Job removed")
        if remove_s == False:
            print("Job doesnt exist")
    elif option == '7':
        break