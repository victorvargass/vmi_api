from fastapi import APIRouter, Body, Query
from fastapi.params import Depends
from fastapi.encoders import jsonable_encoder
from typing import Optional, Dict

from ..database import (
    get_vmi_report
)
from ..models.vmi import (
    ErrorResponseModel,
    ResponseModel,
    VMISchema
)

router = APIRouter()

@router.get("", response_description="VMI report retrieved")
async def get_vmi(
    id: Optional[str] = Query(None, description="Report ID", max_length=24),
    age_years: int = Query(10, description="Years", ge=3, le=17),
    age_months: int = Query(10, description="Months", ge=0, le=11),
    vmi_natural_scores: int = Query(10, description="VMI Natural Score", ge=0, le=27),
    visual_natural_scores: int = Query(10, description="Visual Natural Score", ge=0, le=27),
    motor_natural_scores: int = Query(10, description="Motor Natural Score", ge=0, le=27),
    ):
    vmi_report = await get_vmi_report(
        id, age_years, age_months, vmi_natural_scores, visual_natural_scores, motor_natural_scores
        )
    if vmi_report:
        return ResponseModel(vmi_report, "VMI report retrieved successfully")
    return ResponseModel(vmi_report, "Empty list returned")