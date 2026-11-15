shifts = [
    "Morning Shift",
    "Afternoon Shift",
    "Night Shift"
]
billing= ["billing inquiry", "billing payment", "billing refund","payment inquiry", "payment refund", "payment dispute" , "duplicate charge","unexpected charge", "incorrect billing address", "billing statement request"]

refund = ["refund request", "refund status", "refund processing time", "refund policy clarification", "refund not received", "partial refund request", "full refund request", "refund for damaged item", "refund for wrong item", "refund for late delivery"]

login =["login issue", "password reset", "account locked", "two-factor authentication problem", "unable to access account", "forgot username", "login error message", "session timeout", "account recovery process", "login page not loading"
]


bills = 0
refunds = 0
logins =  0
for item in billing:
    if "billing" in item.lower():
        bills += 1
print("how many billing count =", bills)

for item in refund:
    if "refund" in item.lower():
        refunds += 1
print("how many refund count =", refunds)

for item in login:
    if "login" in item.lower():
        logins += 1
print("how many login count =", logins)
