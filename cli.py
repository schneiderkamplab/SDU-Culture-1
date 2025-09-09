import typer
from evaluation.eval import evaluate_dataset

app = typer.Typer()
@app.command()
def eval(
    input: str = typer.Argument(..., help="Input string to be evaluated")
):
    typer.echo("Starting evaluation...")
    result = evaluate_dataset(input)
    typer.echo(f"Evaluation result: {result}")

if __name__ == "__main__":
    app()