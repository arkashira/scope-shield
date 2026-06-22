from scope_shield import ScopeShield, ProjectScope

def test_create_scope():
    shield = ScopeShield()
    scope = shield.create_scope("Test Project", "Test objectives", "Test boundaries")
    assert scope.name == "Test Project"
    assert scope.objectives == "Test objectives"
    assert scope.boundaries == "Test boundaries"

def test_create_scope_duplicate_name():
    shield = ScopeShield()
    shield.create_scope("Test Project", "Test objectives", "Test boundaries")
    try:
        shield.create_scope("Test Project", "Test objectives", "Test boundaries")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Project scope with this name already exists"

def test_validate_input():
    shield = ScopeShield()
    try:
        shield.validate_input("", "Test objectives", "Test boundaries")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "All fields are required"

def test_store_scope():
    shield = ScopeShield()
    scope = shield.create_scope("Test Project", "Test objectives", "Test boundaries")
    stored_scope = shield.store_scope(scope)
    assert stored_scope["name"] == "Test Project"
    assert stored_scope["objectives"] == "Test objectives"
    assert stored_scope["boundaries"] == "Test boundaries"

def test_get_scope():
    shield = ScopeShield()
    shield.create_scope("Test Project", "Test objectives", "Test boundaries")
    scope = shield.get_scope("Test Project")
    assert scope["name"] == "Test Project"
    assert scope["objectives"] == "Test objectives"
    assert scope["boundaries"] == "Test boundaries"

def test_get_nonexistent_scope():
    shield = ScopeShield()
    scope = shield.get_scope("Nonexistent Project")
    assert scope is None
