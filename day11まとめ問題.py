#関数・繰り返し1
def print_even(numbers):
    for n in numbers:
     if n % 2 == 0:
        print(n)
print_even([1,2,3,4,5])

#関数・繰り返し2
def print_big_numbers(numbers):
   for n in numbers:
      if n > 10:
         print(n)
print_big_numbers([5,12,8,20])

        