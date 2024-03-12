**Password Cracking Script******


This Python script demonstrates a method for cracking a password using a `binary search algorithm`. It simulates the process of guessing a password by interacting.


`check_password Function:`

This function simulates the mechanism of a mobile by comparing a given password with a pre-defined real password.
It checks if the length of the given password matches the length of the real password, and then iterates through each digit to compare them.
It introduces a slight delay to simulate the time taken by the mobile's mechanism.

`crack_password Function:`

This function implements a binary search algorithm to crack the password digit by digit.
It iterates through each digit of the password, performing a binary search to find the correct digit.
The search range is adjusted dynamically based on the elapsed time of the check_password function.


The script is designed to be run directly, so the main function is called when the script is executed.

