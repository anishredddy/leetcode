class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_dist=0
        obs=set()
        for x,y in obstacles:
            obs.add((x,y))
        x=y=0
        directions=[(0,1),(-1,0),(0,-1),(1,0)]
        dirr=0
        for command in commands:
            if command==-2:
                dirr=(dirr+1)%4
            elif command==-1:
                dirr=(dirr+3)%4
            else:
                dx,dy=directions[dirr]
                for _ in range(command):
                    next_x,next_y=x+dx,y+dy
                    if (next_x,next_y) in obs:
                        break
                    x,y=next_x,next_y
                print(x,y)
                max_dist=max(max_dist,x*x+y*y)
        return max_dist