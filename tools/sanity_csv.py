"""
There can come some articats in the CSV files where double quotes ("") are used instead of single quotes (").
This script will preprocess the CSV files to convert double quotes to single quotes.
It can either process a single file or all CSV files in a directory.
"""

import typer
import os

app = typer.Typer()

def preprocess_csv_quotes(input_file, output_file=None, output_dir=None):
    """
    Preprocess CSV file to convert double quotes ("") to single quotes (")
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file (optional, defaults to input_file with '_processed' suffix)
    
    Returns:
        str: Path to the processed file
    """
    if output_file is None:
        # Create output filename by adding '_processed' before file extension
        name, ext = os.path.splitext(input_file)
        output_file = f"{name}.{ext}"
    if output_dir is not None:
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, os.path.basename(output_file))
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace double quotes with single quotes
        # This pattern looks for two consecutive double quotes
        processed_content = content.replace('""', '')
        processed_content = processed_content.replace('",', ';')  # Remove quotes before commas
        processed_content = processed_content.replace(',"', ';')  # Remove quotes after commas
        processed_content = processed_content.replace('?,', '?;') # Remove quotes after questionmark
        processed_content = processed_content.replace('"', '')  # Remove any remaining quotes at line start/end

        print(f"Processed content for {input_file}:")
        

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f"Successfully processed {input_file}")
        print(f"Output saved to: {output_file}")
        return output_file
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        return None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None


def preview_changes(input_file, num_lines=5):
    """
    Preview the changes that would be made to a CSV file
    
    Args:
        input_file (str): Path to input CSV file
        num_lines (int): Number of lines to preview
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"Preview of changes for {input_file}:")
        print("=" * 50)
        
        for i, line in enumerate(lines[:num_lines]):
            original = line.rstrip()
            processed = line.replace('""', '"').rstrip()
            
            print(f"Line {i+1}:")
            print(f"  Original:  {original}")
            print(f"  Processed: {processed}")
            if original != processed:
                print("  >>> CHANGED")
            else:
                print("  >>> NO CHANGE")
            print()
            
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

def process_directory(directory_path, output_dir="processed_files", preview_only=False):
    """
    Process all CSV files in a directory
    
    Args:
        directory_path (str): Path to directory containing CSV files
        preview_only (bool): If True, only preview changes without processing
    
    Returns:
        list: List of processed file paths (empty if preview_only=True)
    """
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} not found")
        return []
    
    # Find all CSV files in directory
    csv_files = []
    for file in os.listdir(directory_path):
        if file.lower().endswith('.csv'):
            csv_files.append(os.path.join(directory_path, file))
    
    if not csv_files:
        print(f"No CSV files found in {directory_path}")
        return []
    
    print(f"Found {len(csv_files)} CSV files:")
    for file in csv_files:
        print(f"  - {os.path.basename(file)}")
    print()
    
    if preview_only:
        # Preview changes for all files
        for csv_file in csv_files:
            preview_changes(csv_file, num_lines=3)
            print("-" * 50)
        return []
    
    # Process all files
    processed_files = []
    for csv_file in csv_files:
        processed_file = preprocess_csv_quotes(csv_file, output_dir=output_dir)
        if processed_file:
            processed_files.append(processed_file)
    
    return processed_files


# directory = "/Users/jacobnielsen/Documents/datasets/SDU-Culture-1/SDU-Culture-1"
@app.command()
def cli(
    input_dir : str = typer.Argument(..., help="Directory containing CSV files to process"),
    output_dir : str = typer.Option("processed_files", help="Directory to save processed CSV files"),
    preview_only : bool = typer.Option(False, help="If True, only preview changes without processing")
):
    typer.echo("Welcome to the SDU-CULTURE-1 CSV Processor!")    
    typer.echo("=== PREVIEW MODE ===")
    process_directory(input_dir, preview_only=preview_only)
    
    # Ask user confirmation
    response = typer.prompt("\nDo you want to process all CSV files? (y/n): ").lower().strip()

    if response in ['y', 'yes']:
        typer.echo("\n=== PROCESSING FILES ===")
        processed_files = process_directory(input_dir, output_dir=output_dir)
        typer.echo(f"\nSuccessfully processed {len(processed_files)} files!")
        typer.echo("\nProcessed files:")
        for file in processed_files:
            typer.echo(f"  - {os.path.basename(file)}")
    else:
        typer.echo("Processing cancelled.")


if __name__ == "__main__":
    app()   