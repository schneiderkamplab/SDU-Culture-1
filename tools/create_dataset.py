from io import StringIO
import os
import pandas as pd
import typer

app = typer.Typer()
@app.command()
def create(
    input_dir: str = typer.Argument(..., help="Directory to load from"),
    output_dir: str = typer.Argument(default="dataset_files", help="Directory to save processed files"),
    engine = typer.Argument("pyarrow", help="Parquet engine to use, either 'pyarrow' or 'fastparquet'")
):
    os.makedirs(output_dir, exist_ok=True)
    typer.echo(f"Creating dataset... Loading from: {input_dir}")

    questions_list = []
    answers_list = []
    combined_list = []

    global_id = 0
    for file in os.listdir(input_dir):
        print(f"Processing file: {file}")
        if file.endswith(".csv"):
            filepath = os.path.join(input_dir, file)
            subject = os.path.splitext(file)[0]  # filename without extension
            df = pd.read_csv(filepath, sep=';')
            print(f"Columns: {df.columns.tolist()}")
            print(f"Columnsd: {df}")
            print("---"*52)
            
            for _, row in df.iterrows():
                global_id += 1 # Assign global id

                questions_list.append({
                    "id": global_id,
                    "Question": row["Question"],
                    "Subject": subject
                })
                
                answers_list.append({
                    "id": global_id,
                    "Answer": row["Answer"],
                    "Subject": subject
                })
                
                combined_list.append({
                    "id": global_id,
                    "Question": row["Question"],
                    "Answer": row["Answer"],
                    "Subject": subject
                })

    # Convert to DataFrames
    questions_df = pd.DataFrame(questions_list)
    answers_df = pd.DataFrame(answers_list)
    combined_df = pd.DataFrame(combined_list)

    # Save to CSV
    questions_df.to_csv(os.path.join(output_dir, "questions.csv"), index=False)
    answers_df.to_csv(os.path.join(output_dir, "answers.csv"), index=False)
    combined_df.to_csv(os.path.join(output_dir, "combined.csv"), index=False)

    # Save to Parquet
    questions_df.to_parquet(os.path.join(output_dir, "questions.parquet"), engine=engine, index=False)
    answers_df.to_parquet(os.path.join(output_dir, "answers.parquet"), engine=engine, index=False)
    combined_df.to_parquet(os.path.join(output_dir, "combined.parquet"), engine=engine, index=False)

    print("✅ Created CSV + Parquet files with global id")


if __name__ == "__main__":
   app()