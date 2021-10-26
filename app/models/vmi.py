from pydantic import BaseModel
from typing import List

class AgeSchema(BaseModel):
    years: int
    months: int

class StandarScoreSchema(BaseModel):
    vmi: int
    visual: int
    motor: int

class ScaledScoreSchema(BaseModel):
    vmi: int
    visual: int
    motor: int

class PercentileSchema(BaseModel):
    vmi: int
    visual: int
    motor: int

class AgeEquivalenceSchema(BaseModel):
    vmi: List[AgeSchema]
    visual: List[AgeSchema]
    motor: List[AgeSchema]

class PerformanceSchema(BaseModel):
    vmi: str
    visual: str
    motor: str

class VMISchema(BaseModel):
    standard_scores: StandarScoreSchema
    scaled_scores: ScaledScoreSchema
    percentiles: PercentileSchema
    age_equivalences: AgeEquivalenceSchema
    performances: PerformanceSchema

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}