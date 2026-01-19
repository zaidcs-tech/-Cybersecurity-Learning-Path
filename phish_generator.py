import time  # This is a library that handles time/delays

# PRINT: This just shows text on the screen
print("--- SOCIAL ENGINEERING EMAIL GENERATOR ---")

# INPUT: This asks the user a question and waits for an answer
# The answer is saved inside a "Variable" called 'victim_name'
victim_name = input("Enter the Victim's Name: ")
company_name = input("Enter the Company Name (e.g. Google): ")
fake_link = input("Enter your Fake Link: ")

print("\n") # This prints an empty line for space
print("[+] Generatng Attack Template...")

# TIME.SLEEP: This makes the program pause for 2 seconds (Looks cool/hacker-ish)
time.sleep(2) 

print("\n--- COPY THE TEXT BELOW ---")

# f-String: This puts your variables inside the text
print(f"Subject: URGENT: Your {company_name} account is locked")
print(f"Hi {victim_name},")
print(f"We detected a login from Russia on your {company_name} account.")
print(f"Please click here immediately to secure your data: {fake_link}")
print("---------------------------")
