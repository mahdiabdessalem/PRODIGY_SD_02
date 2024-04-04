import random

if __name__ == "__main__":

  min_val = 0
  max_val = 100
  computer_num = random.randint(min_val, max_val)
  user_input = None
  num_guesses = 0  # Initialize a variable to count attempts

  while user_input != computer_num:
    try:
      user_input = int(input(f"Guess a number between {min_val} and {max_val}: "))
      num_guesses += 1  # Increment attempts on each guess

      if user_input > computer_num:
        print("Too Big")
      elif user_input < computer_num:
        print("Too Small")
    except Exception:
      print('ERROR: Please provide a number not any characters')
      user_input = None

  print(f"YOU DID IT! {computer_num} was the correct number in {num_guesses} attempts!")
