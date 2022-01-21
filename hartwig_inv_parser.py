"""Return an excel sheet of compounds from their barcodes.
When given a CSV list of barcodes, this module will match it against a local
copy of the Hartwig inventory and subsequently create an excel sheet containing
their name, CAS number, mass, and location. This was namely created to make a
document containing all of our ligands.

Author:  Nicholas Hadler nhadler@berkeley.edu

Created: Jan 20th, 2022
"""

# imports
import pandas as pd  # to handle the csv and data processing
import argparse  # command line arguments


# modules
def prepare_inventory(inventory_csv):
    """Cleans up the barcode and library CSV datasets, returns prepared dataframes.

    Args:
        library_csv (pandas_dataframe):
            csv file that contains the Hartwig inventory database

    Returns:
        df_library (pandas_dataframe):
            dataframe containing cleaned up library
    """
    # Read in inventory and user submitted barcode CSVs
    df_inventory = inventory_csv

    # Adding a catinated 'Mass' Column
    mass = df_inventory["Amount"].str.cat(df_inventory.Unit, sep=" ", na_rep="Missing")
    df_inventory.insert(2, "Mass", mass)

    # Dropping any rows that don't have a barcode assoicated
    df_inventory = df_inventory.dropna(subset=["Barcode"])

    # Removing Amount and Unit Column
    df_inventory = df_inventory.drop(
        columns=["Amount", "Unit", "Type of container", "MolID", "Supplier"]
    )

    return df_inventory


def match_barcodes_return_excel(df_barcode, df_inventory, filename):
    """Creates an excel sheet containing chemicals found on the barcode sheet
    and their pertinent information.

    Args:
        df_barcode (pandas dataframe):
            cleaned dataframe of the barcodes
        df_library (pandas dataframe):
            cleaned dataframe of the iventory
        filename (string):
            user selected filename of exported excel sheet
    """
    # Creates a new dataframe containing barcode chemicals
    df = df_barcode.merge(df_inventory, on="Barcode", how="left")

    # Formats the CSV correctly
    df = df[
        ["Name", "CASNumber", "Mass", "Storage name", "Compartment name", "Barcode"]
    ].rename({"CASNumber": "CAS"}, axis=1)

    filename = filename + ".xlsx"

    # Makes the Excel file.
    df.to_excel(
        filename,
        index=False,
    )


# Run when file is directly called
if __name__ == "__main__":

    # Initializes parser for command line arguments
    parser = argparse.ArgumentParser(
        description="""This script outputs the name, location, and other
        information in an excel sheet of chemicals from a list of barcodes.
        The barcodes must be in a CSV format.""",
    )

    # Adds command line arguments for selecting the barcode and inventory CSV
    parser.add_argument("barcode.csv", help="CSV file containing the barcodes")
    parser.add_argument(
        "inventory.csv", help="CSV file containing the current inventory"
    )
    parser.add_argument(
        "filename", help="Type the filename you want of the generated excel sheet."
    )
    args = vars(parser.parse_args())

    # Read in CSV files
    barcode_csv = pd.read_csv(args["barcode.csv"])
    inventory_csv = pd.read_csv(args["inventory.csv"])

    # Call data clean up function
    df_inventory = prepare_inventory(inventory_csv)

    # Call excel sheet making function
    match_barcodes_return_excel(barcode_csv, df_inventory, args["filename"])
