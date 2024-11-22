#!python

import click
import list
import count

@click.group()

def cli() -> None:
  pass

cli.add_command(list.list)
cli.add_command(count.count)