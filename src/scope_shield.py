import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ProjectScope:
    name: str
    objectives: str
    boundaries: str

class ScopeShield:
    def __init__(self):
        self.scopes = {}

    def create_scope(self, name: str, objectives: str, boundaries: str) -> ProjectScope:
        if name in self.scopes:
            raise ValueError("Project scope with this name already exists")
        scope = ProjectScope(name, objectives, boundaries)
        self.scopes[name] = scope
        return scope

    def validate_input(self, name: str, objectives: str, boundaries: str) -> None:
        if not name or not objectives or not boundaries:
            raise ValueError("All fields are required")

    def store_scope(self, scope: ProjectScope) -> Dict:
        return scope.__dict__

    def get_scope(self, name: str) -> Dict:
        return self.scopes.get(name).__dict__ if self.scopes.get(name) else None
