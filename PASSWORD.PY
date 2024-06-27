import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_symbols=True):
  """Generates a strong, random password of the specified length.

  Args:
      length (int): The desired length of the password.
      include_uppercase (bool, optional): Whether to include uppercase letters. Defaults to True.
      include_numbers (bool, optional): Whether to include numbers. Defaults to True.
      include_symbols (bool, optional): Whether to include symbols. Defaults to True.

  Returns:
      str: The generated password.
  """

  all_chars = ""

  if include_uppercase:
    all_chars += string.ascii_uppercase
  if include_numbers:
    all_chars += string.digits
  if include_symbols:
    all_chars += string.punctuation + string.printable.isascii()  # Include more symbols if desired

  if not all_chars:
    raise ValueError("Password must include at least one character type (uppercase, numbers, or symbols).")

  password = "".join(random.sample(all_chars, length))
  return password

def main():
  """Prompts the user for the number of passwords and their desired lengths,
  then generates and displays those passwords.
  """

  num_passwords = int(input("How many passwords do you want to generate? "))

  print("Generating", num_passwords, "passwords...")

  for i in range(num_passwords):
    length = int(input("Enter the desired length for Password #{}: ".format(i + 1)))
    while length < 6:
      print("Password length should be at least 6 characters. Please enter a higher value:")
      length = int(input())

    include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    print("Password #{}: {}".format(i + 1, password))

if __name__ == "__main__":
  main()
