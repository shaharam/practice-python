#from ATM_project.Atm import Atm


class AtmAdvanced(Atm):
    def __init__(self, consumers):
        super(AtmAdvanced, self).__init__(consumers)

    def check_deposit(self, consumer, amount):
        if self.deposit(consumer, amount):
            print "The chess deposit was successful"
