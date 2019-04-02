# This is a cognitive advisor

class CognitiveAdvisor:
    def __init__(self, mode):
        self.mode = mode

    def displayMode(self):
        print("User Engagement Mode is " + self.mode)

    def changeMode(self, mode):
        self.mode = mode        


class CognitiveAdvisorAssistive(CognitiveAdvisor):
    def __init__(self):
        self.mode = "Assistive"

    def changeMode(self, mode):
        print("Change mode disallowed for this CBA")   

class CognitiveAdvisorAutonomous(CognitiveAdvisor):
    def __init__(self):
        self.mode = "Autonomous"

    def changeMode(self, mode):
        print("Change mode disallowed for this CBA")


cba = CognitiveAdvisor("Unknown")
cba.displayMode()
cba.changeMode("Assistive")
cba.displayMode()
cba.changeMode("Autonomous")
cba.displayMode()

cbaAssitive = CognitiveAdvisorAssistive()
cbaAssitive.displayMode()
cbaAssitive.changeMode("Autonomous")

cbaAutonomous = CognitiveAdvisorAutonomous()
cbaAutonomous.displayMode()
cbaAutonomous.changeMode("Assistive")
