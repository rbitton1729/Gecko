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


def test_install_command():
    """Test install command."""
    runner = CliRunner()
    result = runner.invoke(main, ['install'])
    assert result.exit_code == 0
    assert 'Install command' in result.output
