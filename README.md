# Scope Shield

A Python project that restricts feature requests to defined scope and alerts maintainers to potential scope creep.

## Usage

1. Create a `ScopeShield` instance with a list of defined scopes.
2. Use the `restrict_feature_requests` method to filter out feature requests that are not within the defined scope.
3. Use the `alert_maintainers` method to detect potential scope creep and alert maintainers.

## Testing

Run `pytest` to execute the tests.
