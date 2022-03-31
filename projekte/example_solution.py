import random


def main():
  try:
    userInputMin = int(input("userInputMin: "))
    userInputMax = int(input("userInputMax: "))
    userInputNum = int(input("userInputNum: "))
  except Exception as e:
    print(f"Error: {type(e)}; please try again.")
    return main()

  nums = []
  for _ in range(userInputNum):
    rand = random.randint(userInputMin, userInputMax)
    nums.append(rand)
  if __debug__:
    print(f"\nGenerated values are - {nums}")

  num_dict = {}
  for num in nums:
    if num in num_dict:
      num_dict[num] += 1
    else:
      num_dict[num] = 1
  if __debug__:
    print(f"Sorted dictionary of values - {num_dict}")

  biggest_count = max(num_dict.values())
  if __debug__:
    print(f"Biggest count is {biggest_count}")

  two_dimensional = []
  for i in range(biggest_count + 1):
    two_dimensional.append([])

  for key, value in sorted(num_dict.items()):
    len_of_key = len(str(key))
    two_dimensional[0].append(str(key))
    for val_iter in range(value):
      two_dimensional[val_iter + 1].append("x".ljust(len_of_key, " "))

  two_dimensional.reverse()
  print() # separate result from debug code
  for level in two_dimensional:
    joined = ' '.join(level)
    print(joined)

main()