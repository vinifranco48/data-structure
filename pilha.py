class stack:
    def __init__(self) :
        self.items = []
    
    def isEmpty (self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        print(f'item: {item} foi colocado na lista')