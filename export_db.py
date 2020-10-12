import dataset
import datafreeze
import settings
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--date", help="the date of the database to export (format ddmmyyyy)",
                    type=str, required=True)
parser.add_argument("-f", "--format", help="output format to export the database [json (default) or csv]",
                    type=str, choices=["json", "csv"], required=False, default="json")
args = parser.parse_args()

if not os.path.isfile("db/" + args.date + ".db"):
    print("database not found in '{}'".format("db/" + args.date + ".db"))
    exit()

db = dataset.connect(settings.CONNECTION_STRING.format(args.date))

if args.format == "csv":
    # Export to CSV
    result = db[settings.TABLE_NAME].all()
    print("Exporting DB to CSV... ", end='', flush=True)
    datafreeze.freeze(result, format='csv', filename=settings.CSV_NAME)
else:
    # Export to JSON
    result = db[settings.TABLE_NAME].all()
    print("Exporting DB to JSON... ", end='', flush=True)
    datafreeze.freeze(result, format='json', indent=4, wrap=False, filename=settings.JSON_NAME)

print("DONE!")
