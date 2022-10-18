

class Node():
    def __init__(self,name,_id,prev,succ) -> None:
        self.name=name
        self.id = _id
        if(prev):
            self.prev = [prev]
        else:    
            self.prev = []
        if(succ):
            self.succ = [succ]
        else:
            self.succ = []


    def set_prev(self,prev):
        self.prev.append(prev)

    def set_succ(self.succ):
        self.succ.append(succ)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_prev(self):
        return self.prev

    def get_succ(self):
        return self.succ



class Linked_Tree():
    def __init__(self,name,_id) -> None:
        self.root = Node(name,_id,None,None)
        pass


    def add_node(self,name,_id,prev):
        prev_node = self.search_by_id(_id)
        new_node = Node(name,_id,prev_node,None)
        prev_node.set_succ(new_node)


    def search_by_id(self,_id):
        fork = []
        curr = self.root
        while(True):
            if curr.get_id()==_id:
                return curr
            else: 
                curr_child = curr.get_succ()
                if len(curr_child)==0:
                    if(len(fork)==0):
                        return -1
                    else:
                        curr = fork.pop(0)
                else:
                    for cc in curr_child:
                        fork.append(curr)
                    curr = fork.pop(0)


    # PRINTA LA LISTA CON I FORK IN PARALLELO
    def print_list(self):
        curr = self.root
        fork = []
        while(True):
            print(curr.get_name())
            print()
            curr_child = curr.get_succ()
            