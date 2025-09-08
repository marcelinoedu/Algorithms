class BinarySearch:
    def __init__(self, sorted_list: list[int], goal: int):
        self.sorted_list = sorted_list
        self.goal = goal
        self.found_index = -1 
    
    def search(self) -> int:
        inicio_index = 0
        
        fim_index = len(self.sorted_list) - 1
        
        while inicio_index <= fim_index:
            meio_index = (fim_index + inicio_index) // 2
            actual_number = self.sorted_list[meio_index]
            if actual_number == self.goal:
                self.found_index = meio_index
                break
            elif self.goal < actual_number:
                fim_index = meio_index - 1
            else:
                inicio_index = meio_index + 1
        
        return self.found_index
