import typer
import day1
import day2
import day3
import day4


app = typer.Typer()
app.add_typer(day1.app, name="day1")
app.add_typer(day2.app, name="day2")
app.add_typer(day3.app, name="day3")
app.add_typer(day4.app, name="day4")


if __name__ == "__main__":
    app()
