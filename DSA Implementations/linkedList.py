class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ""  # Initialize llstr
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None) 
        
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        
        return count

if __name__ == '__main__':
    
    ll = LinkedList()
    ll.insert_values(["a","b","c","d"])
    lenght = ll.get_lenght()
    ll.print()
    print(lenght)
