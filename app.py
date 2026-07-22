from scanner import scan
from ai import patch

# Read the vulnerable code
code = open("test.py").read()

print("AI Secure Patch Generator")
print()

print("Original Code:")
print(code)

print("\nScanning...\n")

issues = scan(code)

for issue in issues:
    print(issue)

print("\nGenerating Secure Patch...\n")

result = patch(code)

print(result)