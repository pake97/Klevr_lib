import re
from anytree import Node, RenderTree, PostOrderIter
from anytree.exporter import DotExporter
from anytree.search import find, findall



class HierarchyTree():
    def __init__(self,rootname) -> None:
        self.root = Node(rootname)

    def add_node_and_return(self,parent,child_name):
        child = Node(child_name,parent=parent)
        return child

    def get_children_by_name(self,parent,child_name):
        for child in parent.children:
            if child.name == child_name:
                return child

    def add_node(self,parent,child_name):
        
        try:
            parent = self.find_by_name(parent)
            child = Node(child_name,parent=parent)
        except Exception as e:
            parents = findall(self.root, lambda node: node.name ==parent) 
            for p in parents:
                child = Node(child_name,parent=p)
            
    def get_root(self):
        return self.root

    def list_children(self,parent):
        return parent.children

    def get_parent(self,child):
        return child.parent

    def find_by_name(self,name):
        return find(self.root, lambda node: node.name == name)

    def print_tree(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))


    # install graphviz https://www.graphviz.org/download/
    # then run dot filename.dot -T png -o filename.png

    def export_to_dot(self,filename):
        DotExporter(self.root).to_dotfile(filename)

    def visit(self):
        return [node.name for node in PostOrderIter(self.root)]

    def sub_obj_visit(self):
        ret = {self.root.name:{}}
        self.recursive_visit(self.root,ret[self.root.name])
        return ret

    def recursive_visit(self,current,so):
        for child in current.children:
            so[child.name]={}
            self.recursive_visit(child,so[child.name])