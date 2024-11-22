import click
import glob
import re
import sys

@click.command()
@click.argument("dir", default = ".", type=click.Path(exists=True))
def list(dir) -> None:
    pattern = r"s\dxx\/s\d\dx\/s(\d\d\d)-(\w\w)-(.*)"
    for shootdir in glob.glob(f"{dir}/s???/s???/s???-??-*"):
        matches = re.search(pattern, shootdir)
        if matches:
            (shootnum, genre, shootname) = matches.groups()
            click.echo(f"{shootnum},{genre},{shootname}")
        else:
            print(f"ccwp list: unrecognized dir: {shootdir}", file=sys.stderr)
