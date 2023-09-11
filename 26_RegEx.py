import re

# Example text
text = "Hello, my email addresses are john@example.com and jane@email.org. Please contact me there."

# 1. re.search() - Search for a pattern in the text
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print("1. re.search() - Found:", match.group())
else:
    print("1. re.search() - No match found")

# 2. re.findall() - Find all occurrences of a pattern in the text
emails = re.findall(pattern, text)
if emails:
    print("\n2. re.findall() - Found emails:")
    for email in emails:
        print("-", email)

# 3. re.match() - Match a pattern at the beginning of the text
pattern = r'Hello'
match = re.match(pattern, text)
if match:
    print("\n3. re.match() - Found:", match.group())
else:
    print("3. re.match() - No match found")

# 4. re.split() - Split the text based on a pattern
pattern = r',\s'
split_text = re.split(pattern, text)
print("\n4. re.split() - Split text:")
for part in split_text:
    print("-", part)

# 5. re.sub() - Replace a pattern with a string
pattern = r'[\w.]+@\w+\.\w+'
replacement = '[REDACTED]'
redacted_text = re.sub(pattern, replacement, text)
print("\n5. re.sub() - Redacted text:")
print(redacted_text)
