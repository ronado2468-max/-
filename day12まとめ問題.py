#三の倍数だけ表示
def print_multiples_of_3(numbers):
    for n in numbers:
        if n % 3 == 0:
           print(n)
print_multiples_of_3([1,2,3,4,9])

#for + 条件分岐
def judge_size(moji):
   for n in moji:
      if n >= 20:
        print("large")
      elif n >= 10:
        print("medium")
      else:
        print("small")
judge_size([15])

#カウンタの理解
def count_even(gu):
    count = 0
    for n in gu:
      if n % 2 == 0:
         count += 1
    print(count) 
count_even([1,2,3,4,5])



