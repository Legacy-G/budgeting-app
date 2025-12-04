import math

def calculate_months_to_clear(current_debt: float, monthly_payment: float, daily_accrual: float) -> int | None:
    """
    Simulates month by month to find how many months it takes to clear the debt.
    Assumes a 30-day month for simplicity in projection.
    Returns the number of months, or None if the debt is not decreasing.
    """
    # If payment is less than or equal to the average monthly interest, debt will never be paid off.
    if monthly_payment <= daily_accrual * (365.25 / 12):
        return None

    months = 0
    debt = current_debt
    while debt > 0:
        months += 1
        # Accrue interest for 30 days, then make the payment
        interest_for_month = daily_accrual * 30
        debt = debt + interest_for_month - monthly_payment

        if months > 600:  # Safety break to prevent infinite loops
            return None
            
    return months

def project_debt_over_months(current_debt: float, monthly_payment: float, daily_accrual: float, num_months: int) -> list[float]:
    """
    Projects the debt balance over a given number of months.
    Assumes a 30-day month and that payment is made at the end of the month.
    """
    projections = []
    debt = current_debt
    for _ in range(num_months):
        # Accrue interest for 30 days, then make the payment
        interest_for_month = daily_accrual * 30
        debt = debt + interest_for_month - monthly_payment
        
        # Debt cannot be negative
        debt = max(0, debt)
        
        projections.append(debt)
        
    return projections