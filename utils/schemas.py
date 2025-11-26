from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TimeWindow:
    baseline_days: int
    comparison_days: int

@dataclass
class Hypothesis:
    id: str
    summary: str
    dimension: str
    metrics: Dict[str, Any]
    suspected_causes: List[str] = field(default_factory=list)
    evidence: List[str] = field(default_factory=list)
    status: Optional[str] = None
    confidence_final: Optional[float] = None
    impact: Optional[str] = None
