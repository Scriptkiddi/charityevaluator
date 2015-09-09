__author__ = 'fritz'
import csv
from charity.models import Charity

def read_tsv_file_to_database():
    with open('charities.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)
        for row in reader:
            try:
                nofdb = int(row[2].replace(",", ""))
            except ValueError:
                nofdb = None
            try:
                nofib = int(row[3].replace(",", ""))
            except ValueError:
                nofib = None
            try:
                annual_cost = float(row[4][1:].replace(",", ""))
            except ValueError:
                annual_cost = None
            try:
                cpdb = float(row[5][1:].replace(",", ""))
            except ValueError:
                cpdb = None
            try:
                cpib = float(row[6][1:].replace(",", ""))
            except ValueError:
                cpib = None

            Charity.objects.create(classification=row[0],
                                   name=row[1],
                                   number_of_direct_beneficiaries=nofdb,
                                   number_of_indirect_beneficiaries=nofib,
                                   annual_cost=annual_cost,
                                   cost_per_direct_beneficiary=cpdb,
                                   cost_per_indirect_beneficiary=cpib,
                                   comments=row[7],
                                   source=row[8])