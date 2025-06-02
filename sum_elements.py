MAX = 100

def calculate_sum(arr):
   return sum(arr)

def get_integer(prompt, min_value=None, max_value=None):
   while True:
      try:
         value = int(input(prompt))
         if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
            print(f"Please enter a number between {min_value} and {max_value}.")
            continue
         return value
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   try:
      n = get_integer(f"Enter the number of elements (1-{MAX}): ", 1, MAX)
      arr = []
      print(f"Enter {n} integers:")
      for i in range(n):
         num = get_integer(f"Element {i+1}: ")
         arr.append(num)
      total = calculate_sum(arr)
      print("Sum of the numbers:", total)
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
