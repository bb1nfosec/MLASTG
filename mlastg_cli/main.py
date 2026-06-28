import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import List, Optional
import json
import os
from .orchestrator import run_test_suite
from .reporter import generate_report

console = Console()

@click.group()
@click.version_option(version="0.2.0")
def cli():
    """MLASTG Automated Security Testing CLI."""
    pass

@cli.command()
@click.option('--target', required=True, help="Target URL, API endpoint, or local path to scan.")
@click.option('--category', type=click.Choice(['model', 'llm', 'data', 'supply', 'infra', 'pipeline', 'gov', 'all']), default='all', help="Test category to execute.")
@click.option('--demo', is_flag=True, help="Run in demo mode (uses dummy/local stubs instead of real API calls).")
@click.option('--output', default='mlastg_report.json', help="Output file for the raw JSON results.")
@click.option('--format', type=click.Choice(['json', 'markdown', 'both']), default='both', help="Report output format.")
def scan(target: str, category: str, demo: bool, output: str, format: str):
    """Run security tests against a target ML system."""
    console.print(Panel(f"[bold blue]MLASTG Security Scanner[/bold blue]\nTarget: {target}\nCategory: {category.upper()}", expand=False))
    
    with console.status(f"[bold green]Running {category.upper()} tests...[/bold green]"):
        results = run_test_suite(target, category, demo=demo)
    
    console.print(f"[bold green]✓ Scan completed. {len(results)} tests executed.[/bold green]")
    
    # Generate reporting
    generate_report(results, output, format_type=format)
    console.print(f"Report saved to [bold cyan]{output}[/bold cyan]")

@cli.command()
@click.option('--input', required=True, help="Path to raw JSON results file.")
@click.option('--output', default='mlastg_report.md', help="Output file for the Markdown report.")
def report(input: str, output: str):
    """Generate a Markdown compliance report from an existing JSON results file."""
    if not os.path.exists(input):
        console.print(f"[bold red]Error: File {input} not found.[/bold red]")
        return
        
    with open(input, 'r') as f:
        results = json.load(f)
        
    generate_report(results, output, format_type='markdown')
    console.print(f"[bold green]✓ Markdown report generated at {output}[/bold green]")

if __name__ == '__main__':
    cli()
