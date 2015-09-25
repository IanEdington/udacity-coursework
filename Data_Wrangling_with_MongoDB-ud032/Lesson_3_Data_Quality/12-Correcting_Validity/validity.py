"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
from pprint import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def row_valid(row):
    '''row is a dict from

    - check if the field "productionStartYear" contains a year
    - check if the year is in range 1886-2014
    - convert the value of the field to be just a year (not full datetime)
    - the rest of the fields and values should stay the same
    - if the value of the field is a valid year in range, as described above, write that line to the output_good file
    - if the value of the field is not a valid year, write that line to the output_bad file
    - discard rows (neither write to good nor bad) if the URI is not from dbpedia.org

    return: valid, modified_row
    valid:
        0 - good
        1 - bad
        2 - discard
    '''
    try:
        row['productionStartYear'] = int(row['productionStartYear'][0:4])
    except:
        pass
    if 'dbpedia.org' not in row['URI']:
        return 2, row
    if row['productionStartYear'] not in range(1886,2014):
        return 1, row
    return 0, row

def process_file(input_file, output_good, output_bad):
    input_file = INPUT_FILE
    output_good_data = []
    output_bad_data = []
    # output_delete = []

    with open(input_file, "r") as f:
        # f = open(input_file, "r")
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            valid, rowi = row_valid(row)
            if valid == 0:
                output_good_data.append(rowi)
            elif valid == 1:
                output_bad_data.append(rowi)
            # else:
            #     output_delete.append(rowi)

    with open(output_good, "w") as f_out:
        writer = csv.DictWriter(f_out, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in output_good_data:
            writer.writerow(row)

    with open(output_bad, "w") as f_out:
        writer = csv.DictWriter(f_out, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in output_bad_data:
            writer.writerow(row)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
