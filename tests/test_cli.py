"""Test CLI functionality."""
import pytest
from click.testing import CliRunner
from gecko.cli import main


def test_version():
    """Test version command."""
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert '0.1.0' in result.output


def test_get_command():
    """Test get command."""
    runner = CliRunner()
    result = runner.invoke(main, ['get'])
    assert result.exit_code == 0
    assert 'Get command' in result.output
