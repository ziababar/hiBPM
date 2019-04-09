# This is a cognitive advisor

class Advisor:
    def __init__(self, mode):
        self.mode = mode

    def displayMode(self):
        print("User Engagement Mode is " + self.mode)

    def changeMode(self, mode):
        self.mode = mode        


class AssistiveAdvisor(Advisor):
    def __init__(self):
        self.mode = "Assistive"

    def changeMode(self, mode):
        print("Change mode disallowed for this CBA")   

class AutonomousAdvisor(Advisor):
    def __init__(self):
        self.mode = "Autonomous"

    def changeMode(self, mode):
        print("Change mode disallowed for this CBA")


cba = Advisor("Unknown")
cba.displayMode()
cba.changeMode("Assistive")
cba.displayMode()
cba.changeMode("Autonomous")
cba.displayMode()

cbaAssitive = AssistiveAdvisor()
cbaAssitive.displayMode()
cbaAssitive.changeMode("Autonomous")

cbaAutonomous = AutonomousAdvisor()
cbaAutonomous.displayMode()
cbaAutonomous.changeMode("Assistive")
