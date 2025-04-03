# CSV to TXT Converter

A simple GUI application that converts CSV files containing a single column of data into a comma-separated text file.

## Features

- Convert single-column CSV files to comma-separated text format
- Choose between different quote styles:
  - No quotes
  - Single quotes
  - Double quotes
- User-friendly graphical interface
- File browser for easy file selection
- Automatic file extension handling
- Error handling and user feedback

## Requirements

- Python 3.x
- tkinter

## Installation

1. Clone this repository or download the source code
2. Ensure you have Python 3.x installed on your system
3. No additional package installation required as the application uses only standard Python libraries

## Usage

1. Run the application:
   ```
   python csv_to_txt.py
   ```

2. Click "Browse" to select your input CSV file
3. Choose your preferred quote style:
   - No Quotes: Values will be separated by commas without quotes
   - Single Quotes: Values will be wrapped in single quotes
   - Double Quotes: Values will be wrapped in double quotes
4. Click "Convert" to process the file
5. Choose where to save the converted text file
6. The application will show a success message when the conversion is complete

## Input Format

The application expects a CSV file with a single column of data. For example:
```
value1
value2
value3
```

## Output Format

The output will be a text file with all values separated by commas. Depending on the quote style selected:

- No Quotes: `value1,value2,value3`
- Single Quotes: `'value1','value2','value3'`
- Double Quotes: `"value1","value2","value3"`

## Error Handling

The application includes error handling for common issues:
- Missing input file selection
- File reading/writing errors
- Invalid file formats

## License

This project is licensed under the terms included in the LICENSE file.

## Author

Created by Niko Steiber

## Contributing

Feel free to submit issues and enhancement requests!
