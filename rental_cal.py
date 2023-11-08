# create a class with __init__(income,expenses,cash_flow,ROI)
# create input questions that must be asked in order to come up with ROI 
# create functions if needed in each argument 
# output the ROI to the user 

class Calculator:
    def __init__(self,income,expenses,flow,invest,percent):
       self.income = income
       self.expenses = expenses
       self.flow = flow
       self.invest = invest
       self.percent = percent
    
    def what_is_income(self):
        amount = input("How much will be the monthly rent? ")
        laundry = input("How much will you make for laundry services? " )
        storage = input("How much will you charge for storage? ")
        misc = input("How much miscellaneous money? ")
        
        total_income = int(amount) + int(laundry) + int(storage) + int(misc)
        self.income = total_income
        return self.income
    

    def expense(self):
        tax = input("How much will be your taxes per month? ")
        insurance = input("How much will you pay in insurance per month? ")   
        utilities = input("How much will you pay on utilities? ")
        hoa = input("How much for HOA fees? ")
        lawn = input("How much will you pay for lawn/snow care? ")    
        vacancy =input("How much will you save per month for vacancy fees? ")
        capex = input("How much will you save for capEX? ")    
        management = input("How much will you pay for property management? ")
        mortgage = input("What is your montly mortgage? ")
        total_expenses = int(tax) + int(insurance) + int(utilities) + int(hoa) + int(lawn)+ int(vacancy) + int(capex) + int(management) + int(mortgage)
        self.expenses = total_expenses
        return total_expenses
        
    
    def cashFlow(self):
        cash_flow = self.income - self.expenses
        print(f'Your cash flow is {cash_flow} ')
        self.flow = cash_flow
        return self.flow
    
    def return_investment(self):
        down_payment = input("How much will your down payment be? ")
        closing_cost = input("How much will your closing cost be? ")
        rehab_budget = input("How much will it cost to get the property ready?  ")
        other = input("How much in other exenses? ")
        investments = int(down_payment) + int(closing_cost) + int(rehab_budget) + int(other)
        self.invest = investments
        return self.invest
    
    def percentage(self):
        annual_cashFlow = self.flow * 12
        percentage = annual_cashFlow / self.invest
        self.percent = percentage
        print(f'Your ROI will be {self.percent}% ')
    
grand = Calculator(0,0,0,0,0)
def run():
    while True:
        grand.what_is_income()
        grand.expense()
        grand.cashFlow()
        grand.return_investment()
        grand.percentage()
        return None
    
run()

    

