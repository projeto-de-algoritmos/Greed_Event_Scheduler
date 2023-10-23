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

print(count, visited)

# Priority queue
pq = priorityQueue()
for idx, job in enumerate(jobList):
    pq.push(job, (job["start"], idx))

result2 = maxEmployeesRequired(pq)
print(result2)