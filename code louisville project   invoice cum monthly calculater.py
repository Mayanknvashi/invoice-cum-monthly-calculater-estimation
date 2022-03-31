# create a product and price for three items
product1_name=str(input("Enter product1_name "))
product1_price =float(input("Enter product1_price in $: "))
product2_name =str(input("Enter product2_name "))
product2_price =float(input("Enter product2_price in $: "))
product3_name =str(input("Enter product3_name "))
product3_price =float(input("Enter product3_price in $: "))
sales_tax=float(input(" enter sale tax in $: "))

# create a company name and  customer information
company_name =str(input("Enter company_name "))
company_address =str(input("Enter company_address "))
company_city  =str(input("company_city "))
zip_code=str(input("zip_code name "))
customer_name=str(input(" Custpmer Name "))

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company and customer information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))
print('\t\t{}'.format(zip_code.title()))
print('\t\t{}'.format(customer_name.title()))



# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))
final_price = total + (total*sales_tax/100) 
print('\t\t\t"sales_tax % ')
print('\t\t\t${}'.format(sales_tax))
print('\t\t\tFinal_Price')
print('\t\t\t${}'.format(final_price))


# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)
# loan monthly calculater

cash_payment= float(input(" enter cash_ down payment "))
balance_due= final_price - cash_payment
rate = float(input(" enter rate of interest in %: "))
month = float(input(" enter loan duration months  "))
monthly_installment = ((balance_due)*(rate/1200)*(1 + rate/1200)**month)/((1 + rate/1200)**month-1)
print('\t\t\t" Rate of interest')
print('\t\t\t${}'.format(rate))
print('\t\t\t" loan duration months')
print('\t\t\t${}'.format(month))
print('\t\t\t" balance due')
print('\t\t\t${}'.format(balance_due))
print('\t\t\t"monthly installment')
print('\t\t\t${}'.format(monthly_installment))









