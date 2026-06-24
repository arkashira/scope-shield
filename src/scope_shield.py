import json
from dataclasses import dataclass
from typing import List

@dataclass
class ProjectScope:
    version: str
    changes: List[str]

class ScopeShield:
    def __init__(self, project_scope: ProjectScope):
        self.project_scope = project_scope

    def enforce_scope(self, contributor_changes: List[str]) -> bool:
        for change in contributor_changes:
            if change not in self.project_scope.changes:
                return False
        return True

    def update_scope(self, new_changes: List[str]) -> None:
        self.project_scope.changes.extend(new_changes)

    def get_changelog(self) -> List[str]:
        return self.project_scope.changes
