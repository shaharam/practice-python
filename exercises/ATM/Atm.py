class Atm(object):
    def __init__(self, consumers):
        self.consumers_list = consumers

    def withdraw(self, consumer, amount):
        if self.recognized_consumer(consumer):  # Check if consumer exists by
            if amount <= consumer.balance:  # Check if there is enough money
                consumer.balance -= amount
                self.print_balance(consumer)
            else:
                print "There is not enough money"

    def deposit(self, consumer, amount):
        if self.recognized_consumer(consumer):
            consumer.balance += amount
            self.print_balance(consumer)
        else:
            return False

    def print_balance(self, consumer):
        if self.recognized_consumer(consumer):
            print ("The balance is %d" % consumer.balance)

    def recognized_consumer(self, consumer):
        if consumer in self.consumers_list:
            return True
        else:
            print "ERROR: unrecognized consumer, can't proceed."
