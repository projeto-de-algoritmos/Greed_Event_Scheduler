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
#Interval partitioning:
#need to implement priority queue
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