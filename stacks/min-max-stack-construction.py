class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = [] 
        
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        minMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            currentMin = self.minMaxStack[len(self.minMaxStack) - 1]["min"] 
            newMin = min(currentMin, number)
            currentMax = self.minMaxStack[len(self.minMaxStack) - 1]["max"] 
            newMax = max(currentMax, number)
            minMax["min"], minMax["max"] = newMin, newMax 
        self.minMaxStack.append(minMax)
        return self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]