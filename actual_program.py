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

jobList = [{"id":2, "start": 10, "end": 10.75}, {"id":3, "start": 10, "end": 11}, {"id":4, "start": 10, "end": 12}]
no_workers = -1

while True:
    print('######Temporary Menu#######')
    print('Selecione uma opção')
    print('1.- Inserir uma job')
    print('2.- Inserir no trabalhadores')
    print('3.- Worker schedule')
    print('4.- Calculate required number of workers')
    print('5.- Show job list')
    print('6.- Sair')
    option = input()
    
    if option == '1':
        start_t = float(input("Enter start time for job"))
        end_t = float(input("Enter end time for job"))
        id_i = randint(0,999)
        new_job = {"id": id_i,"start": start_t, "end": end_t}
        jobList.append(new_job)
    elif option == '2':
        no_workers = int(input("Insert number of workers"))
    elif option == '3':
        if no_workers > 0:
            for x in range(no_workers):
                jobList_c = jobList
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
            print("Starting time:",job["start"]," Ending time:",job["end"])
    elif option == '6':
        break