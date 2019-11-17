import click
from pathlib import Path

@click.group()
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode.")
@click.pass_context
def cli(ctx: click.Context, debug: bool):
    ctx.obj = {}
    ctx.obj['DEBUG'] = debug
    if debug:
        click.echo("Debug mode is %s" % 'on' if debug else 'off')

@cli.command()
@click.argument("filename", type=click.Path(exists=True, resolve_path=True))
@click.pass_context
def translate(ctx: click.Context, filename):
    txt = Path(filename).read_text()
    click.echo(txt)

if __name__ == "__main__":
    cli()