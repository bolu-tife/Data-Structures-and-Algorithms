# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.elements = dict()
        self.elem_list = list()
        
        

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements[val] = len(self.elem_list)
        self.elem_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.elements:
            index = self.elements[val]
            last = self.elem_list[-1]
            temp = self.elem_list[index]
            self.elem_list[index] = last
            
            
            
            self.elem_list.pop()
            self.elements[last] = index
            del self.elements[temp]
            return True
        return False
        

    def getRandom(self) -> int:
       
        return self.elem_list[randint(0,len(self.elem_list)-1)]

    
    
#     def __init__(self):
#         self.elements = set()
        

#     def insert(self, val: int) -> bool:
#         if val in self.elements:
#             return False
#         self.elements.add(val)
#         return True
        

#     def remove(self, val: int) -> bool:
#         if val in self.elements:
#             self.elements.remove(val)
#             return True
#         return False
        

#     def getRandom(self) -> int:
#         temp = list(self.elements)
#         return temp[randint(0,len(temp)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()