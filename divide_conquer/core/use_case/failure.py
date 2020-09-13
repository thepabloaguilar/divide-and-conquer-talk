from dataclasses import field
from typing import Any, Dict

from pydantic.dataclasses import dataclass


@dataclass
class FailureDetails:
    reason: str
    failure_message: str
    attributes: Dict[str, Any] = field(default_factory=dict)
