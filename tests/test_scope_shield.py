import pytest
from scope_shield import ScopeShield, FeatureRequest

def test_restrict_feature_requests():
    defined_scope = ["scope1", "scope2"]
    scope_shield = ScopeShield(defined_scope)
    feature_requests = [
        FeatureRequest(1, "Request 1", "scope1"),
        FeatureRequest(2, "Request 2", "scope3"),
        FeatureRequest(3, "Request 3", "scope2")
    ]
    restricted_requests = scope_shield.restrict_feature_requests(feature_requests)
    assert len(restricted_requests) == 2
    assert restricted_requests[0].id == 1
    assert restricted_requests[1].id == 3

def test_alert_maintainers():
    defined_scope = ["scope1", "scope2"]
    scope_shield = ScopeShield(defined_scope)
    feature_requests = [
        FeatureRequest(1, "Request 1", "scope1"),
        FeatureRequest(2, "Request 2", "scope3"),
        FeatureRequest(3, "Request 3", "scope2")
    ]
    potential_scope_creep = scope_shield.alert_maintainers(feature_requests)
    assert len(potential_scope_creep) == 1
    assert potential_scope_creep[0].id == 2

def test_alert_maintainers_no_scope_creep():
    defined_scope = ["scope1", "scope2"]
    scope_shield = ScopeShield(defined_scope)
    feature_requests = [
        FeatureRequest(1, "Request 1", "scope1"),
        FeatureRequest(2, "Request 2", "scope2")
    ]
    potential_scope_creep = scope_shield.alert_maintainers(feature_requests)
    assert len(potential_scope_creep) == 0
