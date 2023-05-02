import re
import argparse

def convert_date_to_year(biblatex_file):
    with open(biblatex_file, 'r') as file:
        biblatex_content = file.read()

    date_pattern = re.compile(r'date\s*=\s*\{(\d{4})(?:-\d{2})?(?:-\d{2})?\}')
    modified_biblatex_content = date_pattern.sub(r'year = {\1}', biblatex_content)

    new_biblatex_file = "modified_" + biblatex_file
    with open(new_biblatex_file, 'w') as file:
        file.write(modified_biblatex_content)

    return new_biblatex_file

def main():
    parser = argparse.ArgumentParser(description='Convert date field to year field in a biblatex file.')
    parser.add_argument('input_biblatex_file', type=str, help='Path to the input biblatex file')

    args = parser.parse_args()

    output_biblatex_file = convert_date_to_year(args.input_biblatex_file)
    print(f"Modified biblatex file saved as: {output_biblatex_file}")

if __name__ == "__main__":
    main()
