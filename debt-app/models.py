from pydantic import BaseModel, Field
from datetime import date

class DebtProfileCreate(BaseModel):
    """
    Represents the data needed to create a new debt profile.
    """
    name: str = Field(..., min_length=1, description="The name of the debt profile, e.g., 'EASEMONI Loan'")
    initial_debt: float = Field(..., gt=0, description="The starting amount of the debt")
    daily_accrual: float = Field(..., gt=0, description="The amount the debt increases by each day")
    first_payment: float = Field(..., gt=0, description="The first payment amount made by the user")
    created_at: date = Field(default_factory=date.today)