import re

pattern = re.compile("[a-zA-Z]+, \d{4}")

print(pattern.search("Hello, 2026!"))
print(pattern.search("Hello 2026"))
print(pattern.search("Hello, 2026"))
print(pattern.search("Hello, 2025"))
print(pattern.search("Hi, 2026"))
