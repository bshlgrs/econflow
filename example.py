import econflow

class Human(econflow.Agent):
    def __init__(self, wage):
        self.wage = wage

    def action_space(self):
        return econflow.floatBetween(0, 10)

    def utility(self, action, worldstate):
        return log()
