import click

@click.command()
@click.argument("shootnum")
@click.option("--bytes")
def count() -> None:
    click.echo("I'm in count")