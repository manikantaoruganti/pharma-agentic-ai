from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime


class DrugQuery(BaseModel):
    """Validates drug search queries"""
    drug_name: str = Field(..., min_length=1, max_length=255)
    indication: Optional[str] = None
    
    @validator('drug_name')
    def validate_drug_name(cls, v):
        if not v.strip():
            raise ValueError('Drug name cannot be empty')
        return v.strip()


class ClinicalTrial(BaseModel):
    """Validates clinical trial data"""
    trial_id: str
    title: str
    status: str
    participants: int = Field(ge=0)
    start_date: Optional[datetime] = None


class PatentInfo(BaseModel):
    """Validates patent information"""
    patent_id: str
    title: str
    filing_date: Optional[datetime] = None
    assignee: Optional[str] = None


class ResearchPaper(BaseModel):
    """Validates research paper metadata"""
    pubmed_id: str
    title: str
    authors: List[str]
    publication_date: Optional[datetime] = None
    abstract: Optional[str] = None
