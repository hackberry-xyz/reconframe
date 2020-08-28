import click, json, os, pickle
from ptpython.repl import embed
from reconframe import variables
from reconframe.helpers import inform as parseInfo
from reconframe import info_types as default_info_types
from reconframe.project import Project
from reconframe.http import Request, Response, Host, Endpoint, Body, Header
import importlib

@click.group(invoke_without_command=True)
@click.version_option(version=variables.__version__)
@click.pass_context
def cli(ctx):
    """reconframe: A Python framework for web reconnaissance."""
    if ctx.invoked_subcommand is None:
        os.system('clear')
        click.echo(click.style('\n\treconframe v{0}'.format(variables.__version__), bold=True))
        click.echo(click.style('\tDocumentation: https://reconframe.hackberry.xyz'))
        click.echo(click.style('\tAuthor: @0xcrypto (https://twitter.com/0xcrypto)\n'))
        try:
            with open('recon.json', 'r') as project_file:
                config = json.load(project_file)

        except FileNotFoundError:
            cli.warning("Not inside a project directory! Falling back to in memory project.")
            config = {}

        try:
            info_types = importlib.import_module("meta/info_types.py")
        except ImportError:
            cli.warning("No info types found! Falling back to basic info types")
            info_types = default_info_types

        project = Project(config)

        if((type(project) == Project) and project.dsn):
            cli.success("\"{}\" initialized. Access it with variable {}".format(project.name, click.style("project",bold=True)))

        else:
            cli.error("Failed to open project!")
            exit(1)

        embed({
            'project': project,
            'inform': lambda information: parseInfo(information, info_types)
        })


@click.command()
@click.argument('path', default='')
def init(path):
    """Initialize a new project in given directory"""
    if(path):
        real_path = os.path.realpath(path)
        try:
            cli.debug("Creating project at {}...".format(real_path))
            os.mkdir(real_path)
        except FileExistsError:
            pass

        if len(os.listdir(real_path)):
            cli.error("The directory \'{}\' is not empty!".format(path))
            exit(1)
        
        os.chdir(real_path)
        dirname = real_path.split('/')[-1]

        if(dirname):
            project = Project({'name': dirname, 'dsn': 'sqlite://' + real_path + '/sqlite.db'},
                [Request, Response, Host, Endpoint, Body, Header]
            )

            with open('recon.json', 'w') as project_file:
                json.dump(project.toJson(), project_file, indent=4)

            cli.success("Project initialized successfully!")

        else:
            cli.error("Something went wrong!")
            exit(1)

cli.add_command(init)


cli.log = lambda message: click.echo(message)
cli.debug = lambda message: cli.log(click.style("[*] {}".format(message), fg="cyan"))
cli.error = lambda message: cli.log(click.style("[-] {}".format(message), fg="red"))
cli.warning = lambda message: cli.log(click.style("[!] {}".format(message), fg="yellow"))
cli.success = lambda message: cli.log(click.style("[+] {}".format(message), fg="green"))