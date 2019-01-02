import click
from flask.cli import FlaskGroup
from .app import create_app

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the flaskPythonApp"""

@cli.command("init")
def init():
    """
    Initialize application
    """
    click.echo("Not doing anything...init complete")

@cli.command("test")
def test():
    """
    Test a print
    """
    click.echo("Test print success")

cli.add_command(init)
cli.add_command(test)
