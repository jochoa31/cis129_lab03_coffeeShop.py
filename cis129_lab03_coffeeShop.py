#This is a Python code snippet for a printed reciept at a shop that sells coffee and muffins with a %6 tax on the subtotals. The number of items are only two but more can be added over time. 

print('*************************************')

#Title 
print('My Coffee and Muffin Shop\n')

#Enter amout of items 
coffees_bought = int(input('Number of coffees bought?\n'))

muffins_bought = int(input('Number of muffins bought?\n'))

print('************************************\n')
# Title
print('My Coffee and Muffin Shop Receipt\n')

#price per item
coffee_price = 5.00
muffin_price = 4.00

#subtotal per each line item
coffee_Subtotal = coffees_bought * coffee_price
muffin_Subtotal = muffins_bought * muffin_price

#printing of subtotal
print(int(coffees_bought),
      'Coffee at $5 each:$',
        coffee_Subtotal)

print(muffins_bought,
       'Muffin at $4 each:$',
         muffin_Subtotal)

#Tax amount from Subtotals
tax_total =.06* (coffee_Subtotal + muffin_Subtotal)

print('6% Tax:$', tax_total )

print('-------------------')

#Total with taxes rounded to two decimal places 
total = round(1.06 * (coffee_Subtotal + muffin_Subtotal), 2)

print('Total:$', total)