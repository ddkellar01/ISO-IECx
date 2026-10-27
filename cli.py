"""Command Line Interface (CLI) for executing ISO-IECx scout and pipeline routines."""
import click
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer
from workflows.google_flow_video import GoogleFlowVideoGenerator

@click.group()
def cli():
    """ISO-IECx CLI Orchestrator"""
    pass

@cli.command()
@click.option("--standard", prompt="Standard ID", help="ISO/IEC standard identifier (e.g. 27001)")
def scout(standard):
    click.echo(f"Scouting standard ISO/IEC {standard}...")
    crawler = ISOScout()
    result = crawler.scout_standard(standard)
    click.echo(result)

@cli.command()
@click.option("--standard", prompt="Standard ID", help="ISO/IEC standard identifier")
def synthesize(standard):
    click.echo(f"Synthesizing knowledge for ISO/IEC {standard}...")
    crawler = ISOScout()
    data = crawler.scout_standard(standard)
    synthesizer = StandardSynthesizer()
    analysis = synthesizer.analyze_standard(data)
    click.echo(analysis)

if __name__ == "__main__":
    cli()
