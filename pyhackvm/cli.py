import typer
from pathlib import Path

app = typer.Typer(name="pyvm")


@app.command(help="List the files in current dir (for testing)")
def ls():
    for f in Path(".").iterdir():
        typer.echo(f)


@app.command(help="Translate a VM file to Jack ASM")
def translate(filename: Path):
    txt = Path(filename).read_text()
    typer.echo(txt)


def main():
    app()


if __name__ == "__main__":
    app()
