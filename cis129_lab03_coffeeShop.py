#This is a Python code snippet for a printed reciept at a shop that sells coffee and muffins with a %6 tax on the subtotals. The number of items are only two but more can be added over time. 

print('*************************************')

#Title 
print('My Coffee and Muffin Shop\n')

#Enter amout of items 
coffees_bought = int(input('Number of coffees bought?\n'))

muffins_bought = int(input('Number of muffins bought?\n'))

cake_bought = int(input('Number of cake slices bought?\n'))

danish_bought = int(input('Number of danish bought?\n'))

print('************************************\n')

# Title.

print('My Coffee and Muffin Shop Receipt\n')

#price per item
coffee_price = 5.00
muffin_price = 4.00
cake_price   = 3.00
danish_price = 4.00

#subtotal per each line item
coffee_Subtotal = coffees_bought * coffee_price
muffin_Subtotal = muffins_bought * muffin_price
cake_Subtotal   = cake_bought    * cake_price
danish_Subtotal = danish_bought  * danish_price


#printing of subtotal

print((coffees_bought),
      'Coffee at $5 each:$',
        coffee_Subtotal)

print(muffins_bought,
       'Muffin at $4 each:$',
         muffin_Subtotal)

print(cake_bought,
      'Cake Slice at $3 each:$',
      cake_Subtotal)

print(danish_bought,
      'Danish at $4 each:$',
      danish_Subtotal )

#Tax amount from Subtotals
tax_total =.06 * (coffee_Subtotal + muffin_Subtotal + cake_Subtotal + danish_Subtotal)

print('6% Tax:$', tax_total )

print('-------------------')

#Total with taxes rounded to two decimal places 
total = (1.06 * (coffee_Subtotal + muffin_Subtotal + cake_Subtotal + danish_Subtotal))
print('Total:$', total)