import heapq
#Still dont know what to do will start implementing algorithms just in case

#Interval scheduling:
intervals = [[1,3],[7,12],[2,5],[6,18],[14,16]]
intervals.sort(key=lambda x: (x[1],x[0]))
count = 0
visited = []
end = -1
for interval in intervals:
    if end <= interval[0]:
        end = interval[1]
        count += 1
        visited.append(interval)

print(count, visited)

#Interval scheduling with correct format

jobList = [{"start": 10, "end": 10.75}, {"start": 10.5, "end": 11}, {"start": 12, "end": 13}]
jobList.sort(key=lambda x: (x["end"],x["start"]))
count = 0
visited = []
end = -1
for job in jobList:
    if end <= job["start"]:
        end = job["end"]
        count += 1
        visited.append(job)

print(count, visited)

#Interval partitioning:
def sortJobs(jobList):
    jobList.sort(key = lambda x: x['start'])
    return jobList

def maxEmployeesRequired(jobList):
	sortedJobList = sortJobs(jobList)
	customerCare = []
	for call in sortedJobList:
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

jobList = [{"start": 10, "end": 10.75}, {"start": 10.5, "end": 11}]
SjobList = sortJobs(jobList)
result = maxEmployeesRequired(SjobList)
print(result)

#Interval partitioning using priority queue
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

# Priority queue
pq = priorityQueue()
for idx, job in enumerate(jobList):
    pq.push(job, (job["start"], idx))

result2 = maxEmployeesRequired(pq)
print(result2)

