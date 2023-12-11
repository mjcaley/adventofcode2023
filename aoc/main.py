import typer
import part1


app = typer.Typer()
app.add_typer(part1.app, name="part1")


if __name__ == "__main__":
    app()
