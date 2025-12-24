def compute_tax():
    # Tax Rates for 2009
    # Format: [(Limit, Rate)]
    # Source: Assignment Table provided
    
    # Status 0: Single
    rates_0 = [
        (8350, 0.10), (33950, 0.15), (82250, 0.25), 
        (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]
    
    # Status 1: Married Filing Jointly or Qualifying Widow(er)
    rates_1 = [
        (16700, 0.10), (67900, 0.15), (137050, 0.25), 
        (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]
    
    # Status 2: Married Filing Separately
    rates_2 = [
        (8350, 0.10), (33950, 0.15), (68525, 0.25), 
        (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)
    ]
    
    # Status 3: Head of Household
    rates_3 = [
        (11950, 0.10), (45500, 0.15), (117450, 0.25), 
        (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]

    # Map status codes to rate lists
    brackets_map = {0: rates_0, 1: rates_1, 2: rates_2, 3: rates_3}

    print("--- 2009 Personal Income Tax Calculator ---")
    print("0 - Single")
    print("1 - Married Filing Jointly or Qualifying Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")

    try:
        # Get Filing Status
        status = int(input("Enter Filing Status (0-3): "))
        if status not in brackets_map:
            print("Error: Invalid status. Please enter 0, 1, 2, or 3.")
            return

        # Get Income
        income = float(input("Enter Taxable Income: $"))
        if income < 0:
            print("Error: Income cannot be negative.")
            return

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    # Compute Tax
    tax = 0.0
    previous_limit = 0
    selected_brackets = brackets_map[status]

    for limit, rate in selected_brackets:
        if income > limit:
            # Tax the full amount in this bracket
            taxable_amount = limit - previous_limit
            tax += taxable_amount * rate
            previous_limit = limit
        else:
            # Tax the remaining amount in this bracket
            taxable_amount = income - previous_limit
            tax += taxable_amount * rate
            break
    
    print(f"Total Tax: ${tax:,.2f}")

if __name__ == "__main__":
    compute_tax()
