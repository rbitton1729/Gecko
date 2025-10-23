#!/usr/bin/env python3
"""Gecko CLI - Command-line interface for the Gecko package manager."""

import click
from gecko import __version__


@click.group()
@click.version_option(version=__version__)
def main():
    """Gecko - A portable package manager for Linux From Scratch and other Unix-like systems."""
    pass


@main.command()
def install():
    """Install a package."""
    click.echo("Install command - to be implemented")


@main.command()
def remove():
    """Remove a package."""
    click.echo("Remove command - to be implemented")


@main.command()
def search():
    """Search for packages."""
    click.echo("Search command - to be implemented")


@main.command()
def update():
    """Update package information."""
    click.echo("Update command - to be implemented")


if __name__ == "__main__":
    main()
