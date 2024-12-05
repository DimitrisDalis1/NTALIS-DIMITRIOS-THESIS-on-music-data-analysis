import csv
import unidecode

def extract_rows_by_name(filename, name1, name2):
    """Extracts rows from a CSV file based on two specific names in the last column, including the artist's name.

    Args:
        filename: The name of the CSV file.
        name1: The first name to search for.
        name2: The second name to search for.

    Returns:
        A list of rows containing the extracted data, including the artist's name.
    """

    extracted_rows = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            last_column = row[-1]
            if name1.lower() in last_column.lower() or name2.lower() in last_column.lower():
                extracted_row = row
                extracted_rows.append(extracted_row)

    return header, extracted_rows

filename = 'resultsWithALotOfFeatures.csv'
name1 = 'ΑΝΔΡΕΑΣ ΡΟ'
name2 = 'ΔΕΡΜΙΤΖΟΓΙ'

header, extracted_rows = extract_rows_by_name(filename, name1, name2)

# Create a new CSV file to store the extracted data
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)
    writer.writerows(extracted_rows)

print("Extracted data saved to 'extracted_data.csv'")
