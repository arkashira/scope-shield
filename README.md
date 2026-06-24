# Scope Shield

A Python project that enforces project scope versioning and prevents contributors from making changes outside the defined scope.

## Usage

1. Create a `ProjectScope` object with the current version and changes.
2. Create a `ScopeShield` object with the `ProjectScope` object.
3. Use the `enforce_scope` method to check if contributor changes are within the defined scope.
4. Use the `update_scope` method to update the project scope with new changes.
5. Use the `get_changelog` method to retrieve the changelog of project scope changes.
