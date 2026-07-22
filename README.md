# AI-Secure-patch-generator
AI-powered cybersecurity tool for vulnerability detection, password analysis, and secure code patch generation using Python and Groq Llama 3.3.

# AI Secure Patch Generator

## Overview
AI Secure Patch Generator is an AI-powered cybersecurity project developed using Python. The tool analyzes Python source code, identifies security vulnerabilities, provides detailed explanations, assigns severity levels, and generates secure patched versions of the code using Groq's Llama 3.3 Large Language Model.

The project also includes a Password Strength Checker and a Secure Authentication System using Bcrypt hashing.

## Features
- Detects common Python vulnerabilities.
- Finds:
  - Hardcoded Passwords
  - Unsafe `eval()`
  - Unsafe `exec()`
  - Weak Passwords
  - Missing Input Validation
  - Authentication Issues
- Generates secure patched code using AI.
- Provides:
  - Vulnerability Reports
  - Severity Levels
  - Security Scores
  - Recommendations
- Password Strength Analysis.
- Secure password storage using Bcrypt.
- Error handling and input validation.
---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| Groq API | AI Integration |
| Llama 3.3 70B | Large Language Model |
| Bcrypt | Password Hashing |
| VS Code | Development Environment |
| Git/GitHub | Version Control |
---
## Project Structure

```text
AI-Secure-Patch-Generator/
│
├── app.py
├── ai.py
├── scanner.py
├── test.py
├── password_checker.py
├── README.md
├── LICENSE
├── requirements.txt

## File Descriptions
```
### 1. app.py

This is the main file of the project.

Responsibilities:

- Reads Python source code from `test.py`
- Calls `scanner.py`
- Sends code to `ai.py`
- Displays:
  - Vulnerability Reports
  - Security Score
  - AI-generated Secure Patch

### 2. ai.py

Responsible for communicating with Groq AI.

Features:

- Connects to Groq API.
- Uses:
  - Llama 3.3 70B Versatile
- Generates:
  - Vulnerability Analysis
  - Severity Levels
  - Attack Scenarios
  - Secure Patched Code
  - Recommendations

Example:

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile"
)
```

---

### 3. scanner.py

Static vulnerability scanner.

Detects:

- `eval()`
- `exec()`
- Hardcoded passwords

Example:

```python
eval(user)
exec("print('Hello')")
password = "12345"
```

Output:

```text
Unsafe eval found!
Unsafe exec found!
Hardcoded password found!
```

---

### 4. test.py

Contains the Python code to be analyzed.

Purpose:

- Demonstrates vulnerable code.
- Demonstrates secure code.
- Tests the AI Secure Patch Generator.

Example:

```python
password = "12345"
eval(user)
```

---

### 5. password_checker.py

Password analysis tool.

Features:

- Password Strength Analysis:
  - Weak
  - Medium
  - Strong
  - Very Strong

Detects:

- Short passwords
- Missing uppercase letters
- Missing lowercase letters
- Missing numbers
- Missing special characters

Example:

```text
Password: 12345

Strength: WEAK

Vulnerabilities:
- Password too short
- Only numbers used
- Easy to guess
```

---

### 6. README.md

Project documentation.

Contains:

- Project overview
- Installation steps
- Features
- Technologies
- Usage instructions

---

### 7. LICENSE

MIT License.

Allows others to:

- Use
- Modify
- Share
- Improve

the project.

---

### 8. requirements.txt

Contains required Python packages.

```text
groq
bcrypt
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone Repository

```bash
git clone https://github.com/USERNAME/AI-Secure-Patch-Generator.git
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Run the Application

```bash
python app.py
```

---

## Usage

### Run Vulnerability Scanner

```bash
python app.py
```

### Run Secure Authentication System

```bash
python test.py
```

### Run Password Checker

```bash
python password_checker.py
```

---

## Example Output

```text
AI Secure Patch Generator

Scanning...

Unsafe eval found!
Unsafe exec found!
Hardcoded password found!

Security Score: 95/100
```

---

## Future Improvements

- Web Interface
- File Upload Support
- Multi-language Support
- SQL Injection Detection
- Command Injection Detection
- Docker Support
- CI/CD Integration

---

## Author

**Sanak Santosh Tekawade**

- B.Tech (Artificial Intelligence and Data Science)
- Python Developer

---

## License

This project is licensed under the MIT License.
