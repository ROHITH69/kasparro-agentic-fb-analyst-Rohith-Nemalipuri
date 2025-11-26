from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------- Planner → others ----------

@dataclass
class PlanStep:
    id: str
    agent: str
    description: str
    inputs: Dict[str, Any]

@dataclass
class Plan:
    user_query: str
    steps: List[PlanStep]
    columns: List[str]

# ---------- Data Agent → Insight Agent ----------

@dataclass
class TimeSliceMetrics:
    start_date: str
    end_date: str
    roas: float
    ctr: float
    purchases_per_day: float

@dataclass
class OverallSummary:
    baseline: TimeSliceMetrics
    recent: TimeSliceMetrics

@dataclass
class SegmentMetrics:
    spend: float
    revenue: float
    impressions: int
    clicks: float
    purchases: int
    roas: float
    ctr: float

@dataclass
class ClusterMetrics:
    campaign_name: str
    adset_name: str
    spend: float
    revenue: float
    impressions: int
    clicks: float
    purchases: int
    ctr: float
    roas: float

@dataclass
class DataSummaries:
    overall: OverallSummary
    by_audience_type: Dict[str, SegmentMetrics]
    by_creative_type: Dict[str, SegmentMetrics]
    low_ctr_clusters: List[ClusterMetrics]

# ---------- Insight Agent → Evaluator ----------

@dataclass
class HypothesisDraft:
    id: str
    summary: str
    dimension: str
    metrics: Dict[str, Any]
    suspected_causes: List[str] = field(default_factory=list)
    confidence_prior: float = 0.7

# ---------- Evaluator → final outputs ----------

@dataclass
class ValidatedHypothesis:
    id: str
    summary: str
    dimension: str
    metrics: Dict[str, Any]
    suspected_causes: List[str] = field(default_factory=list)
    evidence: List[str] = field(default_factory=list)
    status: str = "partial"  # strong_support | partial | rejected
    confidence_final: float = 0.5
    impact: str = "medium"   # low | medium | high

# ---------- Creative Agent output ----------

@dataclass
class CreativeRecommendation:
    cluster_id: str
    problem: str
    current_examples: List[str]
    diagnosis: List[str]
    recommendations: Dict[str, Any]
