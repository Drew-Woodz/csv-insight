import click
from core.analyzer import analyze_csv

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--head', default=5, help='Show top N rows')
@click.option('--missing', is_flag=True, help='Display missing value counts')
def main(filepath, head, missing):
    """
    csv-insight: Simple CLI tool for inspecting CSV files
    """
    analyze_csv(filepath, head=head, show_missing=missing)

if __name__ == '__main__':
    main()
