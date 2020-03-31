from ATM_project.Atm import Atm
from ATM_project.AtmAdvanced import AtmAdvanced
from ATM_project.Consumer import Consumer

pavel = Consumer(100000)
avi = Consumer(100)
moshe = Consumer(500)

cons = [pavel, avi, moshe]

atm_basic = Atm(cons)
atm_advanced = AtmAdvanced(cons)

atm_basic.withdraw(pavel, 5000)
atm_basic.deposit(pavel, 6000)
atm_basic.print_balance(moshe)

atm_advanced.withdraw(avi, 5000)
atm_advanced.deposit(avi, 6000)
atm_advanced.check_deposit(moshe, 100)


