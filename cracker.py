import time
import sys

sys.path.insert(0, '.')

real_password = "1234"  # Define real_password globally


# Function to check the password. It simulates the safe's mechanism.
def check_password(password):
  # real_password = "1234"  # Remove this line since real_password is defined globally now

  if len(password) != len(real_password):
    return False
  for x, y in zip(password, real_password):
    time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
    if int(x) != int(y):
      return False
  return True


# Function to crack the password using binary search.
def crack_password():
  password = ""  # Initialize an empty password string.

  # Loop through each digit of the password.
  for turn in range(4):
    print("- - -" + str(turn) + "- - -")

    # Initialize start and end of the binary search range.
    start = 0
    end = 9

    # Perform binary search to find the correct digit.
    while start <= end:
      mid = (start + end) // 2  # Calculate the midpoint.
      print("Mid: " + str(mid))
      guess = password + str(
          mid)  # Construct the guess it's was just a guess .
      print("Guess: " + str(guess))

      # Pad the guess with zeros to ensure it has 4 digits.
      guess += "0" * (4 - len(guess))
      print("Guess Pad: ", guess)

      # Record the start time.
      t1 = int(round(time.time() * 1000))
      print("Time Round", t1)

      # Check if the guess matches the correct password.
      if not check_password(guess):
        # Record the end time.
        t2 = int(round(time.time() * 1000))
        print("Time Round 2", t2)
        # Calculate the elapsed time and round it to the nearest 100 milliseconds.
        elapsedTime = round((t2 - t1) / 100) * 100
        print("Time Elapsed: ", elapsedTime)
        # Check if the elapsed time is greater than the expected time for the current digit.
        if elapsedTime > 100 * (turn + 1):
          # If so, update the password and reset the binary search range.
          password += str(mid)
          break
        else:
          # Update the binary search range based on the comparison.
          if mid < int(real_password[turn]):
            start = mid + 1
          else:
            end = mid - 1
      else:
        # If the guess matches the correct password, update the password and break the loop.
        password += str(mid)
        print("All password: " + password)
        break

  return password


# Main function to run the password cracking process.
def main():
  cracked_password = crack_password()  # Crack the password.
  print("Cracked password:", cracked_password)  # Print the cracked password.


# Check if the script is being run directly.
if __name__ == "__main__":
  main()  # Call the main function.
