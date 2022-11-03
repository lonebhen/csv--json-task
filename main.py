import typer
import json
import csv
from Operations.csv_operations import create_new_csv_file,write_to_csv_file
from Operations.hash import calculate

app = typer.Typer()

@app.command()
def magic():
    FILENAME = "HNGi9-CSV-FILE.csv"

    with open(FILENAME) as csv_file:
        print("Working on csv file...")
        csv_reader = csv.reader(csv_file, delimiter=',')
        count_rows = 0
        json_format = {"format": "CHIP-0007"}

        for row in csv_reader:

            if count_rows == 0:
                column_names = [*row]
                fieldnames = [*column_names, "sha256"]
                csv_filename = "HNGi9-CSV-FILE.output.csv"
                create_new_csv_file(csv_filename, fieldnames)
                count_rows += 1

            else:
                if not row[0].isnumeric():
                    continue

                filename = row[1]
                entry_dict = json_format.copy()

                for j in range(len(column_names)):
                    entry_dict[f"{column_names[j]}"] = row[j]
                json_object = json.dumps(entry_dict, indent=4)

                try:
                    json_filename = f"./{filename}.json"
                    with open(json_filename, "w") as outfile:
                        outfile.write(json_object)

                    sha256 = calculate(json_filename)

                    data = [*row, sha256]
                    write_to_csv_file(csv_filename, data)
                except Exception as error:                    
                    print(error)

                count_rows += 1
        print("Completed ......")
        print(f'Counted {count_rows} rows.')






if __name__ == "__main__":
    app()