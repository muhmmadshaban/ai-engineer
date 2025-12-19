class Treenode():
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        return 
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        space =' '*self.get_level()*3
        prefix='|__ '+space if self.parent else ""
        print(prefix+ self.data)
        for i in self.children:
            i.print_tree()

def build():
    root= Treenode("Parents")
    child1=Treenode("Child 1")
    child1=Treenode("Child 2")

    root.add_child(child1)
    root.add_child(child1)
    return root

if __name__=="__main__":
    root=build()
    root.print_tree()