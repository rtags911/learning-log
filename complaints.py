customer_complaints = [ 
    "Package arrived three days late.",
    "The item was damaged during shipping.",
    "Wrong size was sent in the order.",
    "Customer support took too long to respond.",
    "Website crashed during checkout.",
    "Promo code did not apply at payment.",
    "Product color looks different from the photo.",
    "Missing instructions in the box.",
    "Charged twice for the same order.",
    "Return label link is broken.",
]

for number , complaint in enumerate(customer_complaints, start=1):
    print(f"Complaint {number}: {complaint}");