import subprocess
import os


def run_cli_command(command):
    """Helper to run CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)

def test_add_user():
    result = subprocess.run(
        ["python3", "main.py", "add-user", "--name", "Luna", "--email", "alice@example.com"],
        capture_output=True,
        text=True
    )
    assert "User added: Luna." in result.stdout

def test_add_project():
    result = subprocess.run(
        [
            "python3", "main.py", "add-project",
            "--user", "Luna", "--title", "CLI Tool", "--description", "Test CLI", "--due_date", "2025-08-01"
        ],
        capture_output=True,
        text=True
    )
    assert "Task added to project- CLI Tool : Test CLI" in result.stdout


