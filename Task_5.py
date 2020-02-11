revenue = int(input('Please enter the revenue of you\' re company :'))
outgoings = int(input('Please enter the outgoings of you\' re company:'))
number_of_employees = int(input('Please enter the number of you\'re employees:'))
if revenue > outgoings:
    profit = revenue - outgoings
    profitability = int(profit / revenue * 100)
    profit_emmployees = profit/number_of_employees
    print(f'Congratulations, company is working with profit {profit} \n and has the profitability {profitability}% \n also each you\'re employess brought for company {profit_emmployees}')
else:
    print('You are losing the money!')
    #git