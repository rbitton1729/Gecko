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
def get():
    """Get and install a package."""
    click.echo("Get command - to be implemented")


@main.command()
def shed():
    """Shed a package."""
    click.echo("Remove command - to be implemented")


@main.command()
def peek():
    """Peek at installed packages."""
    click.echo("List command - to be implemented")


@main.command()
def hunt():
    """Hunt for packages."""
    click.echo("Search command - to be implemented")


@main.command()
def molt():
    """Molt to refresh package information."""
    click.echo("Molt command - to be implemented")


if __name__ == "__main__":
    main()
