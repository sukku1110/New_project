
class Class1:    
    def function1(self,line:str):
        data={}
        line=line.split()
        line.sort()
        for i in line:
            if i in data:
                data[i]=data[i]+1
            else:
                data[i]=1
        print("The answer for First Question is :")
        for k,v in data.items():
            print((k,v))

