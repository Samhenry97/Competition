from random import choice

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        ret = val not in self.s
        self.s.add(val)
        return ret

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        ret = val in self.s
        self.s.discard(val)
        return ret

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()