import json
import typer
from pydantic import ValidationError
from models.input import Snapshot
from rules.thresholds import THRESHOLDS
from settings import settings

app = typer.Typer(name="infra-metrics-analyzer", add_completion=False)


@app.command()
def run(
    input_file: str = typer.Option(settings.input_file, "--input",   help="Input JSON file path"),
    output_file: str = typer.Option(settings.output_file, "--output", help="Output JSON file path"),
    verbose: bool    = typer.Option(False, "--verbose",               help="Print node execution steps"),
):
    """Run the full analysis pipeline."""
    from app.graph import build_graph

    settings.input_file  = input_file
    settings.output_file = output_file

    pipeline = build_graph()

    if verbose:
        for step in pipeline.stream({}, stream_mode="updates"):
            node = next(iter(step))
            typer.echo(f"[{node}] done")
    else:
        pipeline.invoke({})

    typer.echo(f"Report written to {settings.output_file}")


@app.command()
def validate(
    input_file: str = typer.Option(settings.input_file, "--input", help="Input JSON file path"),
):
    """Validate the input JSON file against the Snapshot schema."""
    with open(input_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    errors = []
    for i, entry in enumerate(raw):
        try:
            Snapshot.model_validate(entry)
        except ValidationError as e:
            errors.append((i, e))

    if errors:
        for i, e in errors:
            typer.echo(f"[snapshot {i}] {e}", err=True)
        raise typer.Exit(code=1)

    typer.echo(f"{len(raw)} snapshots valid.")


@app.command()
def rules():
    """Display active anomaly detection thresholds."""
    for metric, levels in THRESHOLDS.items():
        typer.echo(f"{metric}: low={levels['low']}  medium={levels['medium']}  high={levels['high']}")


if __name__ == "__main__":
    app()