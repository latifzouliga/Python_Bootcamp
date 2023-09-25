"""
format specifiers = {value:flags} format a value based on what flags are included

   .(number)f = round to that many decimal places (fixed point)
   :(number) = allocate that many spaces
   :03 = allocate and zero pad that may spaces
   :<  = left justify
   :>  = right justify
   :^  = center justify
   :+  = use a plus sign to  indicate positive value
   :=  = place sign to leftmost position
   :   = insert a space before positive numbers
   :,  = comma seperator


"""
price_1 = 3.1234
price_2 = -934.2323
price_3 = 12.2323

print('decimal point precision')
print(f'Price 1 is ${price_1:.2f}')
print(f'Price 2 is ${price_2:.1f}')
print(f'Price 3 is ${price_3:.3f}')

print()
print('allocate space')
print(f'Price 1 is ${price_1:20}')

print()
print('0 padded')
print(f'Price 1 is ${price_1:020}')

print()
print('justifies')
print(f'Price 1 is ${price_1:<20}')  # left
print(f'Price 2 is ${price_2:>20}')  # right
print(f'Price 3 is ${price_3:^20}')  # center

print()
print('showing positive sign for positive number')
print(f'Price 1 is ${price_1:+}')

print()
print('align number evenly even if we have a negative number')
print(f'Price 1 is ${price_1: }')
print(f'Price 2 is ${price_2: }')
print(f'Price 3 is ${price_3: }')

price_1 = 3000.1234
price_2 = -9340.2323
price_3 = 1200.2323

print()
print('separate numbers by comma')
print(f'Price 1 is ${price_1:,}')
print(f'Price 2 is ${price_2:,}')
print(f'Price 3 is ${price_3:,}')

print()
print('Mix and match ')
# align evenly,
# separate by comma,
# precision by 2 decimal numbers,
# precede each number with positive
# sign if it is positive #
print(f'Price 1 is ${price_1:+,.2f}')
print(f'Price 2 is ${price_2:+,.2f}')
print(f'Price 3 is ${price_3: ,.2f}')
