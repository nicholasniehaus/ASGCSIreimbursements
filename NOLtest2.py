rso_code = input("rso code: ")
from more_itertools import locate
import json
import gspread
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)

client = gspread.authorize(credentials)

sheet = client.open("ASG_CSI_Reimbursements").sheet1
sheet2 = client.open("ASG_CSI_Reimbursements").worksheet(
    "Approved_NOL_Receipts")
sheet3 = client.open("ASG_CSI_Reimbursements").worksheet("ASG_Funding_Tracker")

total_spent = input("Total Amount Spent on purchase:\n> $")

print(
    "\nDiscretionary funds are funds that your RSO requested from ASG's discretionary balance. If you were awarded funds from here, you were given a Notice of Legislation (NOL). \n\nIMPORTANT!!!!!!!! ENTER ZERO (0) for Discretionary Funds if you do not have an NOL."
)
discr_funds = float(input("\nAmount of Discretionary funds spent: \n> $"))

if discr_funds > 0.00:
    while True:
        try:
            nol_number = int(input("\nPlease enter your NOL number: \n> "))
        except ValueError:
            print("An NOL number must be a number.")
        else:
            break
    nol_number = str(nol_number)
    nol_clubs2 = sheet2.col_values(2)
    nol_numbers1 = sheet2.col_values(3)
    nol_amounts3 = sheet2.col_values(4)

    print("NOL Clubs: ", nol_clubs2)

    nol_number_index = (nol_numbers1.index(nol_number))
    print(nol_number_index)
    club_indexes = list(locate(nol_clubs2, lambda a: a == rso_code))
    print("RSO code: {}".format(rso_code))

    if nol_number not in nol_numbers1 and discr_funds > 0.00:
        print(
            "This NOL number has not been assigned. It is possible that the dataset has not been updated. Email knandrews@scu.edu with questions. Discretionary funds have been set to $0.00 for now. It can be edited later."
        )
        discr_funds = 0.00

    print(club_indexes)
    if nol_number_index not in club_indexes:
        print(
            "NOL #{} is not assigned to {}. Discretionary funds have been set to $0.00. You can edit this in following steps. Double check that your RSO code is correct."
            .format(nol_number, rso_code))
        discr_funds = 0.00

    for i in range(1, len(nol_amounts3)):
        nol_amounts3[i] = float(nol_amounts3[i])
    print(nol_amounts3)
    if discr_funds > nol_amounts3[nol_number_index]:
        print(
            "This discretionary fund request exceeds what was assigned to this RSO in NOL #{}. Discretionary funds have been set to $0.00. You can edit this in following steps."
            .format(nol_number))
        discr_funds = 0.00
