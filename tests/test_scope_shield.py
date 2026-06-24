from scope_shield import ScopeShield, ProjectScope

def test_enforce_scope():
    project_scope = ProjectScope("1.0", ["change1", "change2"])
    scope_shield = ScopeShield(project_scope)
    contributor_changes = ["change1", "change2"]
    assert scope_shield.enforce_scope(contributor_changes) == True

def test_enforce_scope_outside_scope():
    project_scope = ProjectScope("1.0", ["change1", "change2"])
    scope_shield = ScopeShield(project_scope)
    contributor_changes = ["change1", "change3"]
    assert scope_shield.enforce_scope(contributor_changes) == False

def test_update_scope():
    project_scope = ProjectScope("1.0", ["change1", "change2"])
    scope_shield = ScopeShield(project_scope)
    new_changes = ["change3", "change4"]
    scope_shield.update_scope(new_changes)
    assert scope_shield.get_changelog() == ["change1", "change2", "change3", "change4"]

def test_get_changelog():
    project_scope = ProjectScope("1.0", ["change1", "change2"])
    scope_shield = ScopeShield(project_scope)
    assert scope_shield.get_changelog() == ["change1", "change2"]
