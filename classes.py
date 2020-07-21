class Part:
    def __init__(self,_type, start,end,value,value_source = None , bias = 0):
        self.type = _type
        self.start = start
        self.end = end
        self.value = value
        self.value_source = value_source
        self.bias = bias

class Resistance :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class Capacitor :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class Inductor :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class DependentCurrentSource :
    def __init__(self, beginning, end,source,bias, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value
        self.bias = bias
        self.source = source

class IndependentCurrentSource :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value


class DependentVoltageSource :
    def __init__(self, beginning,source,bias, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value
        self.bias = bias
        self.source = source

class IndependentVoltagetSource :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value
        

class Wire :
    def __init__(self, beginning, end) :
        self.beginning_position = beginning
        self.end_position = end
