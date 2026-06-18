import pytest
import sys
from src.scope_shield import load_configuration, analyze_scope, print_summary, ScopeBoundary, main
from io import StringIO
import json

def test_load_configuration():
    configuration = {
        "module1": {
            "todos": ["todo1", "todo2"],
            "open_issues": ["issue1", "issue2"]
        },
        "module2": {
            "todos": ["todo3", "todo4"],
            "open_issues": ["issue3", "issue4"]
        }
    }
    with open('test_config.json', 'w') as file:
        json.dump(configuration, file)
    loaded_config = load_configuration('test_config.json')
    assert loaded_config == configuration

def test_analyze_scope():
    configuration = {
        "module1": {
            "todos": ["todo1", "todo2"],
            "open_issues": ["issue1", "issue2"]
        },
        "module2": {
            "todos": ["todo3", "todo4"],
            "open_issues": ["issue3", "issue4"]
        }
    }
    scope_boundaries = analyze_scope(configuration)
    assert len(scope_boundaries) == 2
    assert scope_boundaries[0].module == "module1"
    assert scope_boundaries[0].todos == ["todo1", "todo2"]
    assert scope_boundaries[0].open_issues == ["issue1", "issue2"]

def test_print_summary(capsys):
    scope_boundaries = [
        ScopeBoundary("module1", ["todo1", "todo2"], ["issue1", "issue2"]),
        ScopeBoundary("module2", ["todo3", "todo4"], ["issue3", "issue4"])
    ]
    print_summary(scope_boundaries)
    captured = capsys.readouterr()
    assert "Detected Scope Boundaries:" in captured.out
    assert "Module: module1" in captured.out
    assert "Todos: ['todo1', 'todo2']" in captured.out
    assert "Open Issues: ['issue1', 'issue2']" in captured.out

def test_main(capsys):
    configuration = {
        "module1": {
            "todos": ["todo1", "todo2"],
            "open_issues": ["issue1", "issue2"]
        },
        "module2": {
            "todos": ["todo3", "todo4"],
            "open_issues": ["issue3", "issue4"]
        }
    }
    with open('test_config.json', 'w') as file:
        json.dump(configuration, file)
    sys.argv = ['scope_shield', '--config', 'test_config.json']
    main()
    captured = capsys.readouterr()
    assert "Detected Scope Boundaries:" in captured.out
    assert "Module: module1" in captured.out
    assert "Todos: ['todo1', 'todo2']" in captured.out
    assert "Open Issues: ['issue1', 'issue2']" in captured.out
