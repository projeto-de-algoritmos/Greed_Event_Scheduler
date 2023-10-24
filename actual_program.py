import heapq

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

jobList = [{"start": 10, "end": 10.75}, {"start": 10, "end": 11}, {"start": 10, "end": 12}]
no_workers = -1

while True:
    print('######Temporary Menu#######')
    print('Selecione uma opção')
    print('1.- Inserir uma job')
    print('2.- Worker schedule')
    print('3.- Calculate required number of workers')
    print('4.- Sair')
    option = input()
    
    if option == '1':
        start_t = float(input("Enter start time for job"))
        end_t = float(input("Enter end time for job"))
        
        new_job = {"start": start_t, "end": end_t}
        jobList.append(new_job)
    elif option == '2':
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
            print(count, visited)
    elif option == '3':
        # Priority queue
        pq = priorityQueue()
        for idx, job in enumerate(jobList):
            pq.push(job, (job["start"], idx))

        result2 = maxEmployeesRequired(pq)
        no_workers = result2
        print(result2)
    elif option == '4':
        break
    elif option == '5':
        break