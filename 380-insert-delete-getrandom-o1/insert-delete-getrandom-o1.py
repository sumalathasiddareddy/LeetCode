class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.RandomizedSet:
            self.RandomizedSet.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.RandomizedSet:
            self.RandomizedSet.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.RandomizedSet))
        #return self.RandomizedSet[random.randint(0,len(self.RandomizedSet)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()