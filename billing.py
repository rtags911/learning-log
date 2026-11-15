issues = [
    "billing inquiry",
    "billing payment",
    "billing refund",
    "payment inquiry",
    "payment refund",
    "payment dispute",
    "duplicate charge",
    "unexpected charge",
    "incorrect billing address",
    "billing statement request",
    "refund request",
    "refund status",
    "refund processing time",
    "refund policy clarification",
    "refund not received",
    "partial refund request",
    "full refund request",
    "refund for damaged item",
    "refund for wrong item",
    "refund for late delivery",
    "login issue",
    "password reset",
    "account locked",
    "two-factor authentication problem",
    "unable to access account",
    "forgot username",
    "login error message",
    "session timeout",
    "account recovery process",
    "login page not loading",
]


bills = 0
refunds = 0
logins =  0
other = 0

for item in issues:
    text = item.lower()

    if any(keyword in text for keyword in ["billing", "payment", "charge"]):
        bills += 1
    elif "refund" in text:
        refunds += 1
    elif any(keyword in text for keyword in ["login", "account", "password"]):
        logins += 1
    else:
        other += 1

print("Billing/Payment count =", bills)
print("Refund count =", refunds)
print("Login/Account/Password count =", logins)
print("Other count =", other)
total = bills + refunds + logins + other
print("Total counted:", total, "out of", len(issues))
