import csv

def extract_rows_by_names(filename, artist_names):
    """Extracts rows from a CSV file based on a list of artist names in the "singer" column.

    Args:
        filename: The name of the CSV file.
        artist_names: A list of artist names to search for.

    Returns:
        A list of rows containing the extracted data.
    """

    extracted_rows = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames

        for row in reader:
            singer_name = row['singer'].lower()  # Convert singer name to lowercase for case-insensitive search
            if any(artist_name.lower() in singer_name for artist_name in artist_names):
                extracted_rows.append(row)

    return header, extracted_rows

filename = 'false_data_songs.csv'


artist_names = ['ΔΕΡΜΙΤΖΟΓΙΑΝΝΗΣ', 'ΘΑΝΑΣΗΣ ΣΚΟΡΔΑΛΟΣ']  # Add more names as needed

header, extracted_rows = extract_rows_by_names(filename, artist_names)

# Create a new CSV file to store the extracted data
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(extracted_rows)

print("Extracted data saved to 'extracted_data.csv'")