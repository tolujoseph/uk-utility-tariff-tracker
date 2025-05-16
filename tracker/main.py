from tracker.scraper import get_edf_tariffs, get_britishgas_tariffs
from tracker.analyzer import compare_tariffs
from rich import print
from rich.table import Table

def display_tariffs(tariffs):
    table = Table(title="UK Energy Tariffs")

    table.add_column("Provider", style="cyan")
    table.add_column("Tariff Name", style="magenta")
    table.add_column("Unit Rate", justify="right")
    table.add_column("Standing Charge", justify="right")

    for t in tariffs:
        table.add_row(t["provider"], t["name"], t["unit_rate"], t["standing_charge"])

    print(table)

def main():
    print("[bold green]Fetching tariffs...[/bold green]")
    edf_tariffs = get_edf_tariffs()
    bg_tariffs = get_britishgas_tariffs()

    all_tariffs = edf_tariffs + bg_tariffs
    if not all_tariffs:
        print("[red]No tariff data found.[/red]")
        return

    display_tariffs(all_tariffs)

    cheapest = compare_tariffs(all_tariffs)
    if cheapest:
        print(f"\n[bold yellow]Cheapest Tariff:[/bold yellow] {cheapest['provider']} - {cheapest['name']} costing approx £{cheapest['cost']:.2f} per month.")
    else:
        print("[red]Could not calculate cheapest tariff.[/red]")


if __name__ == "__main__":
    main()
