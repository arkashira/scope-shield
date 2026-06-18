import json
from dataclasses import dataclass
from typing import List

@dataclass
class FeatureRequest:
    id: int
    description: str
    scope: str

class ScopeShield:
    def __init__(self, defined_scope: List[str]):
        self.defined_scope = defined_scope

    def restrict_feature_requests(self, feature_requests: List[FeatureRequest]) -> List[FeatureRequest]:
        return [request for request in feature_requests if request.scope in self.defined_scope]

    def alert_maintainers(self, feature_requests: List[FeatureRequest]) -> List[FeatureRequest]:
        potential_scope_creep = [request for request in feature_requests if request.scope not in self.defined_scope]
        if potential_scope_creep:
            print("Potential scope creep detected:")
            for request in potential_scope_creep:
                print(f"Feature request {request.id}: {request.description}")
        return potential_scope_creep
