import click, json, os, pickle
from ptpython.repl import embed
from reconframe import variables
from reconframe.project import Project
from reconframe.http import Request, Response, Host, Endpoint, Body, Header

@click.group(invoke_without_command=True)
@click.version_option(version=variables.__version__)
@click.pass_context
def cli(ctx):
    """reconframe: A Python framework for web reconnaissance."""
    if ctx.invoked_subcommand is None:
        click.echo(click.style('\n\treconframe v{0}'.format(variables.__version__), bold=True))
        click.echo(click.style('\tDocumentation: https://reconframe.hackberry.xyz'))
        click.echo(click.style('\tAuthor: @0xcrypto (https://twitter.com/0xcrypto)\n'))
        try:
            with open('recon.json', 'r') as project_file:
                print(project_file.read())
                
        except FileNotFoundError:
            config = {}
            info_types = [Request, Response, Host, Endpoint, Body, Header]

        project = Project(config)

        click.echo("{} initialized. Access it with variable project")
        embed(globals(), locals())
           

@click.command()
@click.argument('path', default='')
def init(path):
    """Initialize a new project in given directory"""
    if(path):
        real_path = os.path.realpath(path)
        try:
            click.echo('Creating project at {}...'.format(real_path))
            os.mkdir(real_path)
        except FileExistsError:
            pass

        if len(os.listdir(real_path)):
            click.echo(click.style('[FileExistsError] The directory \'{}\' is not empty!'.format(path), fg='red'))
            exit(1)
        
        os.chdir(real_path)
        dirname = real_path.split('/')[-1]

        if(dirname):
            project = Project({'name': dirname, 'dsn': 'sqlite://' + real_path + '/sqlite.db'},
                [Request, Response, Host, Endpoint, Body, Header]
            )

            with open('recon.json', 'w') as project_file:
                json.dump(project.toJson(), project_file, indent=4)

            click.echo(click.style('[Success] Project initialized successfully!', fg='green'))
            click.echo(click.style('Information is sacred. Use it wisely.', fg='green', bold=True))

        else:
            click.echo(click.style('[UnknownError] Something went wrong!', fg='red'))


cli.add_command(init)
