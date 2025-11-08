# 📝 README Summary: Your Password Cracker Project
This summary covers the most important questions about your project: What is it? How do I run it? And how do I know it works?

#### 1. What is the Password Cracker? (The Goal)

What it does: It's a Python script designed to perform a Dictionary Attack. This is a fast way to find the original passwords for stolen MD5 "fingerprints" (hashes) by comparing them to a list of common guesses (wordlist.txt).

The Big Picture: The project's purpose is purely educational ("White Hat"). It proves how ineffective the old MD5 hashing algorithm is, highlighting why strong, modern security methods (like SHA-256) are necessary.

#### 2. How to Run the Cracker (The Execution)

Files Needed: You must have your main script (cracker_script.py), the list of hashes (hashes.txt), and the dictionary of words (wordlist.txt) in the same location.

The Command: You start the program from your terminal:

Bash
python cracker_script.py
The Steps: The script will then ask you to provide the path (or just the file name) for both the hash file and the wordlist. It will output a report showing which passwords were successfully cracked ([+] Cracked:) and which ones failed because the correct password was not in the wordlist ([-] FAILED:).

#### 3. How the "Hashes and Stuff" Work (The Efficiency)

The "Smart Way": Your script uses a high-speed method. It doesn't waste time checking every hash individually.

It loads all the stolen hashes into a super-fast data structure called a Set.

It goes through the wordlist only once, turning each word into its unique MD5 hash.

It instantly checks if that newly generated hash is present in the Set. This method is incredibly quick for large files.

The Secret to Success: The critical step is using the .strip() function when reading files. This removes the invisible "Enter" key press (\n) at the end of every line, which would otherwise ruin the hash comparison.

#### 4. How to Run the Tests (The Verification)

Test Purpose: The separate test file (test_cracker.py) ensures your main script works perfectly. It checks that you crack the right number of passwords and that your script reports errors (like missing files) correctly.

The Command: You run the tests using Python's built-in testing framework:

Bash
python -m unittest test_cracker.py

Result: If all tests PASS, you know your cracking logic is sound, your error handling is correct, and you met all the assignment requirements!
