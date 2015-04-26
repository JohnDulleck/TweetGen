# ExpandList.py

class ExpandList ( object ) :
    def __init__ ( slef, list ) :
        self.list = list
        self.counter = 0
        self.length = len ( list )

    def get () :
        ret = list [ self.counter % self.length ]
        self.counter += 1
        return ret

    def carry () :
        return 0 == self.counter % self.length

        
