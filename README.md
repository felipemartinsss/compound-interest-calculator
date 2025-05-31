# Compound Interest Calculator

A project to calculate revenue of investments based on providen data
like initial capital, interest rate and time of investment.

The API is developed for studies with Python/Flask. 
The endpoints and request data are:

POST /calculate

Body - The body should be provided in json with the following fields:
- initial_capital: float
- interest_rate: float
- time_unit: string. valid_values: 'PY' (per year), 'PM' (per month)
- time: int (should respect time_unit)
  - example 1: if time_unit == 'PY' and time == 2, we are talking about 2 years == 24 months
  - example 2: if time_unit == 'PM' and time == 6, we are talking about 6 months.
- investment_frequency: string. valid_values: 'unique', 'monthly'

Result - The result is going to have the following fields:
- final_value: the total value after the time of investment.
- revenue: the difference between final_value and the total invested capital.
