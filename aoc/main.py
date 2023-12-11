import typer
import day1
import day2


app = typer.Typer()
app.add_typer(day1.app, name="day1")
app.add_typer(day2.app, name="day2")


if __name__ == "__main__":
    app()
