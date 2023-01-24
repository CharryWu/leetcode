
class TwoSum:

    def __init__(self):
        self.table = {}

    def add(self, number: int) -> None:
        if number in self.table:
            self.table[number] += 1
        else:
            self.table[number] = 1
        

    def find(self, value: int) -> bool:
        for key in self.table:
            complement = value-key
            
            if key != complement:
                if complement in self.table:
                    return True
            elif self.table[key] > 1:
                return True
        return False

