class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def getArea(self):
        return(self.length*self.width)
    def getPerimeter(self):
        return(2*(self.length+self.width))