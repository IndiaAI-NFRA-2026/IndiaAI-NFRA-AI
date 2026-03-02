from pydantic import BaseModel, Field
from typing import List, Literal

class Rule(BaseModel):
    rule_id: str
    description: str
    full_text: str
    mapped_paragraphs: str
    type: str

class ValidationRequest(BaseModel):
    framework: str
    file_name: str
    rules: List[Rule]

class ComplianceResult(BaseModel):
    status: Literal["Pass", "Fail", "Partial"]
    explanation: str
    evidence_quote: str
    risk: Literal["High", "Medium", "Low", "None"]
    conf: float = Field(ge=0.0, le=1.0)

# For the /validate response we may include the rule_id
class ValidationResponseItem(BaseModel):
    rule_id: str
    status: Literal["Pass", "Fail", "Partial"]
    explanation: str
    evidence: str
    description: str
    risk: Literal["High", "Medium", "Low", "None"]
    conf: float

class IngestResponse(BaseModel):
    status: str
    file_name: str
    framework: str
    chunks_indexed: int