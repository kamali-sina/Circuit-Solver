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
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class IndependentCurrentSource :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class DependentVoltageSource :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value

class IndependentVoltagetSource :
    def __init__(self, beginning, end, value) :
        self.beginning_position = beginning
        self.end_position = end
        self.value = value