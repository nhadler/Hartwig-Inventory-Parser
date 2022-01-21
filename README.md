# Hartwig Inventory Parser

The *Hartwig Inventory Parser* is a python script that takes a list of chemical barcodes and returns an excel sheet with their names, location, and other information in the JFH inventory.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install .
```
Or call on the script makefile.

```
make setup
```

## Usage

Call the script as shown below. The arguments `barcode.csv` and `inventory.csv` need to be the name/location of said files and `filename` is name of the generated excel document. 

```bash
python hartwig_inv_parser.py [-h] barcode.csv inventory.csv filename

positional arguments:
  barcode.csv    CSV file containing the barcodes
  inventory.csv  CSV file containing the current inventory
  filename       Type the filename you want of the generated excel sheet.

optional arguments:
  -h, --help     show the help message
```
### Getting the inventory.csv file:

The `inventory.csv` file is obtained from [open-enventory](https://inventory-cchem.berkeley.edu/) by going to `settings`, then `Direct Data Export`. 

Make sure to select `RS_style` and leave the option `Room numbers separated by semicolons` blank.

Click down and save the text file. Open this file with Microsoft Excel and then `Save As` as a CSV file. This is then ready to be used by the script.

### Preparing the barcode.csv file:

The `barcode.csv` file should be a single column CSV file with the first row containg `Barcode`. All other rows should only contain one **barcode**.

### Example:

```bash
python hartwig_inv_parser.py barcodes.csv 01202022.csv ligands
```

This creates an excel file named ligands.xlsx.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or email me at nhadler@berkeley.edu.

## License
MIT License

Copyright (c) 2022 Nicholas Hadler