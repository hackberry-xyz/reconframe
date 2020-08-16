import click
from ptpython.repl import embed
from reconframe import version

@click.group()
@click.version_option(version=version.__version__)
def cli():
    """reconframe: A Python framework for web reconnaissance."""
    pass

@click.command()
def start():
    """Open the ptpython REPL with reconframe integrations"""
    click.echo(click.style('\n\treconframe v{0}'.format(version.__version__), bold=True))
    click.echo(click.style('\tDocumentation: https://reconframe.hackberry.xyz'))
    click.echo(click.style('\tAuthor: @0xcrypto (https://twitter.com/0xcrypto)\n'))
    embed(globals(), locals())

cli.add_command(start)

cli()