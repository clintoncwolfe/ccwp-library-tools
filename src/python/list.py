import click

@click.command()
def list() -> None:
    click.echo("I'm in list")
