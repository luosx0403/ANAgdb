import csv
import logging

# Configure logging
logging.basicConfig(
    filename='filter_log.log',  # Log file to store log messages
    level=logging.INFO,  # Log level: INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Define file paths
input_file = 'all_species_output.tsv'
output_file_contains = 'output_contains.tsv'
output_file_not_contains = 'output_not_contains.tsv'

# Initialize counters for processed rows
total_rows = 0
valid_rows = 0
invalid_rows = 0
contains_count = 0
not_contains_count = 0

try:
    # Open files for processing
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file_contains, 'w', encoding='utf-8', newline='') as outfile_contains, \
            open(output_file_not_contains, 'w', encoding='utf-8', newline='') as outfile_not_contains:
        
        # Create CSV reader and writers
        reader = csv.reader(infile, delimiter='\t')  # Read TSV file
        writer_contains = csv.writer(outfile_contains, delimiter='\t')  # Writer for 'contains' rows
        writer_not_contains = csv.writer(outfile_not_contains, delimiter='\t')  # Writer for 'not contains' rows

        # Process each row
        for row in reader:
            total_rows += 1  # Increment total rows counter

            # Skip rows with fewer than 7 columns
            if len(row) < 7:
                invalid_rows += 1  # Increment invalid rows counter
                logging.warning(f"Skipped invalid row {total_rows}: {row}")
                continue

            valid_rows += 1  # Increment valid rows counter

            # Check if the first column value exists in any of the 4th, 6th, or 7th columns
            if row[0] in row[3] or row[0] in row[5] or row[0] in row[6]:
                writer_contains.writerow(row)  # Write row to 'contains' output file
                contains_count += 1  # Increment 'contains' rows counter
                logging.info(f"Row {total_rows} written to 'contains': {row}")
            else:
                writer_not_contains.writerow(row)  # Write row to 'not contains' output file
                not_contains_count += 1  # Increment 'not contains' rows counter
                logging.info(f"Row {total_rows} written to 'not contains': {row}")

except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
    print("Error: Input file not found. Please check the file path.")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    print("An unexpected error occurred. Please check the log file for details.")

# Log summary of the operation
logging.info(f"Processing complete.")
logging.info(f"Total rows processed: {total_rows}")
logging.info(f"Valid rows: {valid_rows}")
logging.info(f"Invalid rows skipped: {invalid_rows}")
logging.info(f"Rows written to 'contains': {contains_count}")
logging.info(f"Rows written to 'not contains': {not_contains_count}")

# Print summary to the console
print("Processing complete!")
print(f"Total rows processed: {total_rows}")
print(f"Valid rows: {valid_rows}")
print(f"Invalid rows skipped: {invalid_rows}")
print(f"Rows written to 'contains': {contains_count}")
print(f"Rows written to 'not contains': {not_contains_count}")
