class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time=0

        i=0
        current_time=customers[0][0]
        while i<len(customers):
            current_time=max(current_time,customers[i][0])
            waiting_time+=customers[i][1]+(current_time-customers[i][0])
            # print(customers[i][1]+(current_time-customers[i][0]),current_time)
            current_time+=customers[i][1]
            i+=1
        return waiting_time/len(customers)