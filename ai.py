from groq import Groq

# Replace with your NEW Groq API Key
client = Groq(
    api_key="Enter Your Groq API Key Here"
)


def patch(code):

    prompt = f"""
You are an expert Cybersecurity Engineer.

Analyze the following Python code and perform the tasks below:
0.Shows the current passward
1. Find all vulnerabilities.
2. Explain each vulnerability in one line.
3. Assign a severity level:
   - LOW
   - MEDIUM
   - HIGH
   - CRITICAL
4. Explain how an attacker can exploit each vulnerability.
5. Suggest the best fix for each vulnerability.
6. Provide a Security Score out of 100.

SECURITY SCORE: __/100

give me this info the prompt i uploaded in minimal.


{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content