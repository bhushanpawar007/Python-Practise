

class PolygonArea():
    def area(self,radius,length,width):
        if (radius is not None):  # @UndefinedVariable
            area=radius*radius  # @UndefinedVariable
            print("Area of Circle is :" , area)  # @UndefinedVariable
        if(length is not None) :  # @UndefinedVariable
            area=length*width
            print("Area of Rectangle is : " , area)     
            
    #def area(self,length,width):  # @DontTrace @DuplicatedSignature
    #    print((length*width))  # @UndefinedVariable
        
    
def main():
   polygon=PolygonArea()
   polygon.area(4,None ,None)
   polygon.area(None,4,5)
   
if __name__=="__main__"  : 
    main()