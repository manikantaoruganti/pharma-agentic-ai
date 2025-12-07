"""Models module for Pharma Agentic AI.

Contains data models for drugs, trials, and predictions.
"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class DrugModel(BaseModel):
    """Data model for drug information."""
    drug_id: str
    name: str
    formula: str
    molecular_weight: float
    properties: dict = {}
    created_at: datetime = datetime.now()


class TrialModel(BaseModel):
    """Data model for clinical trials."""
    trial_id: str
    drug_id: str
    phase: int
    status: str
    participants: int


__all__ = [
    "DrugModel",
    "TrialModel",
]
