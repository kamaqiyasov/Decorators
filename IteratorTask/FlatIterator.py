class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        
    def __iter__(self):
        self.item = self.get_items(self.list_of_list)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.item):
            raise StopIteration
        return self.item[self.cursor]
    
    def get_items(self, items):
        result = []
        for item in items:
            if not isinstance(item, list):
                result.append(item)
            else:
                result.extend(self.get_items(item))
        
        return result