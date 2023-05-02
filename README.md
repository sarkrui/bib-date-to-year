# Biblatex Date to Year Converter

This script converts the `date` field in a biblatex file to a `year` field. It can handle date fields containing only the year, year-month, or year-month-day formats.

## Usage

To use the script, first make sure you have Python installed on your system.

Then, run the script from the command line, passing the biblatex file as an argument:

```bash
python script_name.py your_biblatex_file.bib
```

Replace script_name.py with the name of your Python script and your_biblatex_file.bib with the name of your biblatex file.

## Example
Suppose you have the following entry in your biblatex file:
```scss
@book{sample,
  author = {Doe, John},
  title = {Sample Book},
  publisher = {Sample Publisher},
  date = {2022-06-13}
}
```

The script will modify the entry as follows:
```scss
@book{sample,
  author = {Doe, John},
  title = {Sample Book},
  publisher = {Sample Publisher},
  year = {2022}
}
```
If the date field contains only the year or year-month, the script will still extract the year and replace the date field with the year field.

