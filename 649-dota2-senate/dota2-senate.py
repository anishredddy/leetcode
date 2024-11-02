class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        count = {'R': 0, 'D': 0}
        for char in senate:
            count[char] += 1
    
        senate = list(senate)
        while count['R']  > 0 and count['D'] > 0:
            if senate[i] == "D":
                flag = False
                for j in range(i+1, len(senate)): #check right first
                    if senate[j] == 'R':
                        senate[j] = 'X'
                        count['R'] -= 1
                        flag = True
                        break
                if not flag: #if not found in right check left
                    for j in range(0, i):
                        if senate[j] == 'R':
                            senate[j] = 'X'
                            count['R'] -= 1
                            break
            elif senate[i] == "R":
                flag = False
                for j in range(i+1, len(senate)):
                    if senate[j] == 'D':
                        senate[j] = 'X'
                        count['D'] -= 1
                        flag = True
                        break
                if not flag:
                    for j in range(0, i):
                        if senate[j] == 'D':
                            senate[j] = 'X'
                            count['D'] -= 1
                            break
            if i == len(senate) - 1: #if on last index start again from 0
                i = 0
            else:
                i += 1
        for i, v in count.items():
            if v > 0:
                if i == 'R':
                    return "Radiant"
                return "Dire"
                

