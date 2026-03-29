# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
count = 0
for line in handle:
    #  Filter for lines starting with 'From'
    if not line.startswith('From '): continue
    # Split the line into a list of words
    words = line.split()
    # Find the second word
    email = words[1]
    # Add email to the dictionary
    counts[email] = counts.get(email, 0) + 1

number = None
name = None
for word, count in counts.items():
    if number is None or count > number:
        name = word
        number = count

print(name, number)