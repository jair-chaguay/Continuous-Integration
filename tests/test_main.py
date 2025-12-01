"""
Unit tests for the CLI module (main.py), covering Requirements 8, 9, and 10:
- Interactive menu behavior
- Input validation
- Confirmation prompts
- Error handling
- CLI final output
"""

import builtins
from src.main import ask_confirmation, ask_int, run


def test_confirmation_yes(monkeypatch):
    """User enters 'Y' → function returns True."""
    monkeypatch.setattr(builtins, "input", lambda _: "Y")
    assert ask_confirmation("Confirm? ") is True


def test_confirmation_no(monkeypatch):
    """User enters 'N' → function returns False."""
    monkeypatch.setattr(builtins, "input", lambda _: "N")
    assert ask_confirmation("Confirm? ") is False


def test_confirmation_invalid_then_yes(monkeypatch, capsys):
    """
    If the user enters an invalid character first,
    the function should show an error and ask again.
    """
    inputs = iter(["x", "Y"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    assert ask_confirmation("Confirm? ") is True
    output = capsys.readouterr().out

    assert "Enter Y or N" in output




def test_ask_int_valid(monkeypatch):
    """User enters a valid integer → function returns the integer."""
    monkeypatch.setattr(builtins, "input", lambda _: "5")
    assert ask_int("Enter number: ") == 5


def test_ask_int_invalid_then_valid(monkeypatch, capsys):
    """Invalid input first, valid number second."""
    inputs = iter(["abc", "10"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    result = ask_int("Enter number: ")
    output = capsys.readouterr().out

    assert result == 10
    assert "Invalid input" in output


def test_cli_invalid_option(monkeypatch, capsys):
    """
    User enters an invalid menu option ('9'),
    then chooses to exit ('5' + 'Y').
    The CLI must show an error message for the invalid option.
    """
    inputs = iter([
        "9",    # invalid option
        "5",    # exit option
        "Y"     # confirm exit
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run()
    output = capsys.readouterr().out

    assert "Invalid option" in output


def test_cli_full_flow(monkeypatch, capsys):
    """
    Simulate a complete flow:
    - Select plan (Basic)
    - Confirm
    - Add feature (Personal Training)
    - Confirm
    - Set members = 1
    - Calculate total
    """
    inputs = iter([
        # Select plan
        "1",       # menu option
        "Basic",   # plan name
        "Y",       # confirm plan

        # Add feature
        "2",                   # menu
        "Personal Training",   # feature name
        "Y",                   # confirm feature

        # Members
        "3",       # menu
        "1",       # number of members

        # Calculate total
        "4",       # menu option → calculate
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    total = run()
    output = capsys.readouterr().out

    # Basic (50) + Personal Training (50) = 115
    assert total == 115
    assert "TOTAL = 115" in output or "TOTAL = 115.0" in output
