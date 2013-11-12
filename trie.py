
class Node:
    def __init__(self):
        self.__final = False
        self.__nodes = {}
        self.__data = 0
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
        return self.__get(addr, False)
        
    def create(self, array, data):
        self.__get(array, True).__data = data
        
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
    
    def __get(self, array, create=False):
        if array:
            head, *tail = array
            if create and head not in self.__nodes:
                self.__nodes[head] = Node()
            return self.__nodes[head].__get(tail, create)
        return self
    
    def __read(self, name):
        if self.__data:
            yield name
        for key, value in self.__nodes.items():
            yield from value.__read(name + [key])
            

i = Node()
i.create({1,10,11,10},"123.123.123.123")
i.create({2}, "hbrup~~~~")
k = i.read()
for p in k:
    print(p, i[p].getData())
#pass only significant bits, end everything else
    
   
       
        
    
    
             
        
   
            
            
         
            
    
        
        
