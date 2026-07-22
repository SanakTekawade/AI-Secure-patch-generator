def scan(code):

    issues = []

    if "eval(" in code:
        issues.append("Unsafe eval found!")

    if "exec(" in code:
        issues.append("Unsafe exec found!")

    if "password =" in code:
        issues.append("Hardcoded password found!")

    return issues