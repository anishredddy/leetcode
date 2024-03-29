class Node:
    def __init__(self,key,value):
        self.prev=self.next=None
        
        self.key=key
        self.value=value
        self.count=1


class List:
    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.size=0

        self.head.next,self.tail.prev=self.tail,self.head
    def add(self,node):
        next_node=self.head.next

        node.prev=self.head
        node.next=next_node

        next_node.prev=node
        self.head.next = node
        
        self.size+=1



    def delete(self,node):
        next=node.next
        prev=node.prev

        prev.next=next
        next.prev=prev
        
        self.size-=1
    
    def get_last(self):
        return self.tail.prev
    
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.value)
            temp=temp.next

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.current=0
        self.min_freq=0
        self.freq={}
        self.cache={}
    
    def update_freq(self,node):        
        self.freq[node.count].delete(node)

        if node.count==self.min_freq and self.freq[node.count].size==0:
            self.min_freq+=1

        node.count+=1
        if node.count in self.freq:
            self.freq[node.count].add(node)
            
        else:
            freq_list=List()
            freq_list.add(node)
            self.freq[node.count]=freq_list
    
        
    def add_node(self,node):
        if self.current>=self.capacity:
            last=self.freq[self.min_freq].get_last()
            del self.cache[last.key]
            self.freq[self.min_freq].delete(last)
        if 1 not in self.freq:
            freq_list=List()
            freq_list.add(node)
            self.freq[1]=freq_list
            self.min_freq=1
        else:
            self.freq[1].add(node)
            self.min_freq=1
        self.current+=1
        
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.update_freq(self.cache[key])
            
            return self.cache[key].value
        # print("counts")
        
        # for node in self.cache.values():
        #     print(node.count)
        # print("____________ewgs")
        return -1
        

    def put(self, key: int, value: int) -> None:
    
        if key in self.cache:
            self.update_freq(self.cache[key])
            self.cache[key].value=value
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.add_node(node)

        # for node in self.cache.values():
        #     print(node.value)
        # print("________")

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)