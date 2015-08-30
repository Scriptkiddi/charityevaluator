__author__ = 'fritz'
import csv
from charity.models import Charity

def read_tsv_file_to_database():
    with open('charities.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='')
        for row in reader:
            Charity.objects.create(classification=row[0],
                                   name=row[1],
                                   number_of_direct_beneficiaries=row[2],
                                   number_of_indirect_beneficiaries=row[3],
                                   annual_cost=float(row[4][1:].replace(",", "")),
                                   cost_per_direct_beneficiary=float(row[5][1:]),
                                   cost_per_indirect_beneficiary=float(row[6][1:]),
                                   comments=row[7],
                                   source=row[8])