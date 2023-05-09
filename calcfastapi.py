from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Calculation(BaseModel):
    num1: float
    num2: float
    operator: str


@app.post("/calculate")
async def calculate(calculation: Calculation):
    num1 = calculation.num1
    num2 = calculation.num2
    operator = calculation.operator

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        return {"error": "Invalid operator."}

    return {"result": result}
