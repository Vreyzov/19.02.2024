num_integers = int(input())
sum_rocks = 0
max_forests = 0
min_seas = 0


for i in range(num_integers):
  integer = int(input())
  if integer % 2 == 0 and integer > 0:
    sum_rocks += integer
  elif integer % 2 == 1 and integer > 0:
    if integer > max_forests:
      max_forests = integer
  elif integer < 0:
    if integer < min_seas:
        min_seas = integer

print("In the rocks:", sum_rocks)
print("In the forests:", max_forests)
print("In the seas:", min_seas)