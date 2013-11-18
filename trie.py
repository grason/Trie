
class Node:
    def __init__(self):
        self.__final = False
        self.__nodes = {}
        self.__data = None
    def __bool__(self):
        return self.__final
        
    def __contains__(self, addr):
        try:
            return self[addr]
        except KeyError:
            
            return False
            
    def __iter__(self):
        yield self
        for node in self.__nodes.values():
            yield from node 
            
    def __getitem__(self, addr):
        return self.__search(addr, None)
        
    def create(self, array, data):
        self.__get(array).__data = data
        
    def read(self):
        yield from self.__read([])
        
    def update(self, addr):
        self[addr].__final = True
        
    def delete(self, addr):
        self[addr].__final = False
    def getData(self):
        return self.__data
    def prune(self):
        for key, value in tuple(self.__nodes.items()):
            if not value.prune():
                del self.__nodes[key]
        if not len(self):
            self.delete([])
        return self
    
    def __get(self, array):
        if array:
            head, *tail = array
            if head not in self.__nodes:
                self.__nodes[head] = Node()
            return self.__nodes[head].__get(tail)
        return self
    def __search(self, array,last_d):
        last_data = last_d
        if self.__data:
            last_data= self.getData();
            print("**",self.getData())
            print("**",last_data)
        if array:
            head, *tail = array
            try:
                return self.__nodes[head].__search(tail, last_data)
            except KeyError:
                print("keyerror")
                if last_data:
                    print("last_valid =", last_data)
                    return last_data
                return self.getData()
        return self.getData()
    
    def __read(self, name):
        if self.__data:
            yield name
        for key, value in self.__nodes.items():
            yield from value.__read(name + [key])
            

i = Node()
i.create([1],'a')
i.create([1,1],'e')
i.create([1,1,1],'b')
i.create([1,1,0],'c')
i.create([1,1,0,0,1,1,1],'f')
i.create([2], "hbrup~~~~")
print("done creating")
print("-->",i[[1,1,1,0]])
print("-->",i[[1,1,0,1,1]])
print("-->",i[[3]])
print("-->",i[[1,1,0,1,1,1]])
print("-->",i[[1,1,0,0,1,1,1]])
#pass only significant bits, end everything else
    
   
        
    
    
             
        
   
            
            
         
            
    
        
        
