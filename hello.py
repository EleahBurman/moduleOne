#print my name
print("Aloha, Eleah")

#showing that a number is a number vs a string is a string
x = 5
print(x)
print("Aloha", x)

#showing how modulo work with the resulting value being the remainder
x = 5 % 2
print("this is the modulo - ", x)

#explaining floor and going to the lowest value
x = 5 // 2
print("this is floor - ", x)

#showing concatenation
print("Aloha " + "World")

#showing operators on strings
print("Aloha" * 5)

#showing f strings and how they work
print("Aloha World ++++")
plus = "+" * 4
print(f"Aloha World {plus}")

#showing functions - put in a number return a string
def aloha_chars(number: int) -> str:
  """
  this aloha takes aloha plus '+' signs equals to number.
  examples aloha_chars(5), "aloha +++++"
  args:
    number(int): numbers of pluses i need
    returns: str: aloha plus pluses
  """
  pluses = '+' * number
  return f"Aloha {pluses}"

#showing the function working
print("pluses is 5 - ", aloha_chars(5))
print("pluses is 10 - ", aloha_chars(10))