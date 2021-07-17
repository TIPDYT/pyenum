#This is the code for pyenum
#Tutorial on GitHub
#pyenum made by TIPDYT
class enum: #The "enum" class
    def __init__(self, values): #The class constructor(Requires the values for the enum)
        
        length = len(values) #A variable that stores the length of the values requested

        for i in range(0,length,1): #A for loop
            exec("self.%s = \"%s\"" % (values[i], values[i])) #Adds values to self to be accessible