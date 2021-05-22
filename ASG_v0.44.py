#Google API

#Spending category dictionary
spending_categories = {
    "Supplies": 6502,
    "Food": 7002,
    "Domestic Travel": 6810,
    "Gas Expense": 6526,
    "Membership Dues": 7402,
    "Gifts/Prizes/Awards": 7008,
    "Equipment Rental": 7208,
    "Fundraising Expense": 7022,
    "Student Wages": 6200,
    "Other Non-Dept Transfers": 9502,
    "Facilities Permits & Fees": 7726,
    "Vehicle Purchase": 7667,
    "Peripherals Over $5,000": 7666,
    "Software Over $5,000": 7665,
    "Computers Over $5,000": 7663,
    "Equipment Over $5,000": 7662,
    "Furniture Over $5,000": 7661,
    "Misc Expense-Internal": 7496,
    "Rental Exp-Internal": 7495,
    "Department Transfer Out": 7490,
    "Cost of Goods Sold": 7902,
    "Miscellaneous Expenses": 7410,
    "Subscriptions & Publications": 7404,
    "On-Line Services": 7308,
    "Facility Rental": 7202,
    "Marketing & Advertising": 7105,
    "Outside Services": 7103,
    "Professional Services": 7102,
    "Other Departmental Chgbcks": 7080,
    "Custodial Chargeback": 7072,
    "Maintenance Chgbcks": 7068,
    "Repair & Maint-Equip & Other": 7054,
    "Repair & Maint-Facilities": 7052,
    "Fundraising Expense": 7022,
    "Entertainment": 7006,
    "Room Charges": 7004,
    "Employee Relocation": 6860,
    "Recruiting Travel": 6840,
    "Domestic Travel": 6810,
    "Advances": 6805,
    "Conference & Seminar Fees": 6801,
    "Mailing Chargebacks": 6780,
    "Mail/UPS/Federal Express": 6758,
    "Postage Charges": 6752,
    "Copy/Printing Chgbacks": 6730,
    "Printing Expense": 6706,
    "Copying Expense": 6702,
    "Telephone Chargebacks": 6640,
    "Installation-Telephone": 6638,
    "Telephone Charges": 6612,
    "Benefits": 6350,
    "Student Stipends": 6210,
    "Student - Need Based Aid": 6205,
    "Misc Income-Internal": 5896,
    "Non-taxable Sales-Internal": 5893,
    "Department Transfer In": 5890,
    "Miscellaneous Income": 5810,
    "Sponsorship Payments": 5599,
    "Commissions": 5580,
    "Program Sales": 5564,
    "Advertising Sales": 5563,
    "Ticket Sales": 5561,
    "Department Sales": 5555,
    "Sales-Nontaxable": 5552,
    "Sales-Taxable": 5551,
    "Gifts/Donations (non-devel)": 5159,
    "Gifts-Cash": 5152,
}
#basicinfo
form_filler = ""
reimbursee = ""
reimbursee_email = ""
phone_number = ""
rso_name = ""
rso_code = ""
cash = False
check = False
directdeposit = False
expensetransfer = False
expt_accountingstring = ""

reimbursee_address = ""
reimbursee_address2 = ""

#purchaseinfo
purchase_date = ""
purchase_category = ""
description_of_purchase = ""

#fundsinfo
asg_funds = ""
discr_funds = ""
club_funds = ""
total_spent = ""
total_requested = ""
reimbursement_method = ""

user_choice = ""


#definitions
def basicinfo(form_filler, reimbursee, reimbursee_email, phone_number,
              rso_code, rso_name):
    form_filler = input("Name of person filling out form:\n> ")
    reimbursee = input("Name of person to be reimbursed:\n> ")
    reimbursee_email = input("Email of person to be reimbursed:\n> ")
    phone_number = input("Phone number of person to be paid 'XXX-XXX-XXXX': ")
    rso_name = input("Please enter in your RSO name:\n> ")
    print(
        "Please enter in your RSO code. If you don't know your RSO code, it can be found here:\n\nhttps://docs.google.com/spreadsheets/d/1kcaqMpZrexMZ29sRJdaeHU-J3IFA31OXtGswYS3RLCc/edit?usp=sharing\n\nAlternatively, you can type a code, which will list the available codes. These may be outdated, so the online method is better."
    )
    rso_code = input("RSO code:\n> ")

    return form_filler, reimbursee, reimbursee_email, phone_number, rso_code, rso_name


def purchaseinfo(spending_categories, purchase_date, purchase_category,
                 description_of_purchase):

    purchase_date = input("\nDate on receipt/invoice (mm-dd-yy):\n> ")
    description_of_purchase = input("Description of Purchase:\n> ")
    purchase_category = input(
        "\nEnter the primary category of the spending. Enter in 'S' to see a list of acceptable categories:\n> "
    )

    while purchase_category not in spending_categories:

        if purchase_category == "S":
            print("Supplies"
                  "\nFood"
                  "\nDomestic Travel"
                  "\nGas Expense"
                  "\nMembership Dues"
                  "\nGifts/Prizes/Awards"
                  "\nEquipment Rental"
                  "\nFundraising Expense"
                  "\nStudent Wages"
                  "\nOther Non-Dept Transfers"
                  "\nFacilities Permits & Fees"
                  "\nVehicle Purchase"
                  "\nPeripherals Over $5,000"
                  "\nSoftware Over $5,000"
                  "\nComputers Over $5,000"
                  "\nEquipment Over $5,000"
                  "\nFurniture Over $5,000"
                  "\nMisc Expense-Internal"
                  "\nRental Exp-Internal"
                  "\nDepartment Transfer Out"
                  "\nCost of Goods Sold"
                  "\nMiscellaneous Expenses"
                  "\nSubscriptions & Publications"
                  "\nOn-Line Services"
                  "\nFacility Rental"
                  "\nMarketing & Advertising"
                  "\nOutside Services"
                  "\nProfessional Services"
                  "\nOther Departmental Chgbcks"
                  "\nCustodial Chargeback"
                  "\nMaintenance Chgbcks"
                  "\nRepair & Maint-Equip & Other"
                  "\nRepair & Maint-Facilities"
                  "\nFundraising Expense"
                  "\nEntertainment"
                  "\nRoom Charges"
                  "\nEmployee Relocation"
                  "\nRecruiting Travel"
                  "\nDomestic Travel"
                  "\nAdvances"
                  "\nConference & Seminar Fees"
                  "\nMailing Chargebacks"
                  "\nMail/UPS/Federal Express"
                  "\nPostage Charges"
                  "\nCopy/Printing Chgbacks"
                  "\nPrinting Expense"
                  "\nCopying Expense"
                  "\nTelephone Chargebacks"
                  "\nInstallation-Telephone"
                  "\nTelephone Charges"
                  "\nBenefits"
                  "\nStudent Stipends"
                  "\nStudent - Need Based Aid"
                  "\nMisc Income-Internal"
                  "\nNon-taxable Sales-Internal"
                  "\nDepartment Transfer In"
                  "\nMiscellaneous Income"
                  "\nSponsorship Payments"
                  "\nCommissions"
                  "\nProgram Sales"
                  "\nAdvertising Sales"
                  "\nTicket Sales"
                  "\nDepartment Sales"
                  "\nSales-Nontaxable"
                  "\nSales-Taxable"
                  "\nGifts/Donations (non-devel)"
                  "\nGifts-Cash")

        purchase_category = input(
            "\nEnter the primary category of the spending:\n >")

    return purchase_date, purchase_category, description_of_purchase, spending_categories


def fundsinfo(reimbursement_method, expt_accountingstring, discr_funds,
              club_funds, total_requested, total_spent, reimbursee_address,
              reimbursee_address2, basicinfo):

    rso_code = basicinfo()

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
    sheet3 = client.open("ASG_CSI_Reimbursements").worksheet(
        "ASG_Funding_Tracker")

    total_spent = input("Total Amount Spent on purchase:\n> $")

    print(
        "\nDiscretionary funds are funds that your RSO requested from ASG's discretionary balance. If you were awarded funds from here, you were given a Notice of Legislation (NOL). \n\nIMPORTANT!!!!!!!! ENTER ZERO (0) for Discretionary Funds if you do not have an NOL."
    )
    while True:
        try:
            discr_funds = float(
                input("\nAmount of Discretionary funds spent: \n> $"))
        except ValueError:
            print("Please enter a number: ")

        else:
            break

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

    while True:
        try:
            club_funds = float(input("\nAmount of Club funds spent:\n> $"))
        except ValueError:
            print("Please enter a number: ")

        else:
            break

    total_requested = discr_funds + club_funds

    paymentmethodinputs = [
        "expense transfer", "cash", "direct deposit", "check", "1", "2", "3"
    ]
    paymentmethodinputs2 = ["expense transfer", "cash", "1", "2"]
    if total_requested >= 200.00:
        pymntmethodinput = str(
            input(
                "Should the payment come via:\n[1] Expense Transfer\n[2] Check\n[3] Direct Deposit (I have submitted a direct deposit form, or have one attatched to this packet)\n> "
            ))
        while pymntmethodinput.lower not in paymentmethodinputs and pymntmethodinput not in paymentmethodinputs2:
            pymntmethodinput = str(
                input(
                    "Should the payment come via:\n[1] Expense Transfer\n[2] Check\n[3] Direct Deposit (I have submitted a direct deposit form, or have one attatched to this packet)\n> "
                ))

        if pymntmethodinput == "1" or pymntmethodinput.lower == "expense transfer":
            expt_accountingstring = input(
                "Enter in the Expense Transfer budget string:\n> ")
            #expensetransfer == True
            reimbursement_method = "Expense Transfer"
        elif pymntmethodinput == "2" or pymntmethodinput.lower == "check":
            reimbursee_address = input(
                "Please enter in a physical address (not city, state, and zip) for the reimbursement check to be mailed to: \n>"
            )
            reimbursee_address2 = input(
                "Please enter in 'City, State, Zip Code' in that format: \n>")
            #check==True
            reimbursement_method = "Check"
        elif pymntmethodinput == "3" or pymntmethodinput.lower == "direct deposit":
            reimbursee_address = input(
                "Please enter in a physical address (not city, state, and zip) for the reimbursement check to be mailed to: \n>"
            )
            reimbursee_address2 = input(
                "Please enter in 'City, State, Zip Code' in that format: \n>")
            #directdeposit==True
            reimbursement_method = "Direct Deposit"
    else:
        pymntmethodinput = str(
            input(
                "Should the payment come via:\n[1] Expense Transfer\n[2] Cash\n> "
            ))
        while pymntmethodinput.lower not in paymentmethodinputs2 and pymntmethodinput not in paymentmethodinputs2:
            pymntmethodinput = str(
                input(
                    "Should the payment come via:\n[1] Expense Transfer\n[2] Cash\n> "
                ))
        if pymntmethodinput == "1" or pymntmethodinput.lower == "expense transfer":
            expt_accountingstring = input(
                "Enter in the Expense Transfer budget string:\n> ")
            #expensetransfer == True
            reimbursement_method = "Expense Transfer"
        elif pymntmethodinput == "2" or pymntmethodinput.lower == "cash":
            print(
                "Cash is the standard reimbursement method for requests under $200. You will be contacted via email when your reimbursement is ready to be collected."
            )
            #cash==True
            reimbursement_method = "Cash"

    return reimbursement_method, expt_accountingstring, discr_funds, club_funds, total_requested, total_spent, reimbursee_address, reimbursee_address2


def thecyber(spending_categories, reimbursement_method, form_filler,
             reimbursee, reimbursee_email, phone_number, rso_code, rso_name,
             purchase_date, purchase_category, description_of_purchase,
             expt_accountingstring, expensetransfer, discr_funds, club_funds,
             total_requested, total_spent, cash, check, directdeposit,
             reimbursee_address, reimbursee_address2):
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

    from datetime import date
    today = date.today()

    if discr_funds > 0.00:
        row = [
            purchase_date, reimbursee, reimbursee_email, purchase_category,
            spending_categories[purchase_category], 21148, "SAF", "SS",
            rso_code, "DISCR", discr_funds
        ]

        index = 2

        sheet.insert_row(row, index)

    if club_funds > 0.00:
        row = [
            purchase_date, reimbursee, reimbursee_email, purchase_category,
            spending_categories[purchase_category], 21148, "RSO", "SS",
            rso_code, "DPT02", club_funds
        ]

        index = 2

        sheet.insert_row(row, index)

    return None


def thepaper(spending_categories, reimbursement_method, form_filler,
             reimbursee, reimbursee_email, phone_number, rso_code, rso_name,
             purchase_date, purchase_category, description_of_purchase,
             expt_accountingstring, expensetransfer, discr_funds, club_funds,
             total_requested, total_spent, cash, check, directdeposit,
             reimbursee_address, reimbursee_address2):
    from datetime import date
    today = date.today()
    import os

    filename = "{} {} {} {}.txt".format(today, rso_code, reimbursee,
                                        purchase_date)
    print(filename)

    finalfilename = os.path.join(os.path.expanduser('~'), 'Downloads',
                                 filename)

    printout = open(finalfilename, "w+")

    printout.write("Form Completed by: {: <40.40}")
    printout.write(
        "Date Completed: {}   Budget Year: 2019/2020   1099: Yes_X_   No___\n".
        format(form_filler, today))
    printout.write("\nMake {} Payable to: {: <40.40}".format(
        reimbursement_method, reimbursee))
    if reimbursement_method == "Check" or reimbursement_method == "Direct Deposit":
        printout.write("\nMailing address: {}".format(reimbursee))
        printout.write("\n                 {}".format(reimbursee_address))
        printout.write("\n                 {}".format(reimbursee_address2))
    elif reimbursement_method == "Expense Transfer":
        printout.write("Expense Transfer Budget String:\n    {}\n".format(
            expt_accountingstring))
    else:
        printout.write("")
    printout.write("\nPhone Number: {}".format(phone_number))
    printout.write("\nEmail: {: <33.33}   Activity: {}\n".format(
        reimbursee_email, rso_name))

    printout.write(
        "\nDate of Purchase: {}  Amount Spent: {}  Amount Requested: {}".
        format(purchase_date, total_spent, total_requested))

    printout.write("\nDescription of Purchase: {: <60.60}")
    printout.write(
        "\n____________________________________________________________________________________"
    )
    printout.write("\n")
    printout.write(
        "\nDate of    Desc. of    Account  Fund    DEPT.ID  Program  Activity  Class  Amount"
    )
    printout.write("\nPurchase   Charge\n")

    if discr_funds > 0.00:
        printout.write(
            "{}   {: <11.11} {}     {}   {}      SS       {: <6.6}    {}  ${:.2f}\n"
            .format(purchase_date, purchase_category,
                    spending_categories[purchase_category], 21148, "SAF",
                    rso_code, "DISCR", discr_funds))

    if club_funds > 0.00:
        printout.write(
            "{}   {: <11.11} {}     {}   {}      SS       {: <6.6}    {}  ${:.2f}\n"
            .format(purchase_date, purchase_category,
                    spending_categories[purchase_category], 21279, "RSO",
                    rso_code, "DPT02", club_funds))

    printout.write(
        "\n                                                            TOTAL PAYMENT: ${:.2f}"
        .format(total_requested))
    printout.write(
        "\n____________________________________________________________________________________"
    )
    printout.write(
        "\nPrepared by:             DEPT    EXT     DATE                  ")
    printout.write("\n                                                      ")
    printout.write(
        "\n    Nicholas Niehaus     ASG     5154    {}  ".format(today))
    printout.write("                                                      ")
    printout.write("                                                      ")
    printout.write("\nApproval Signature: _____________________________    ")
    printout.write("")
    printout.write(
        "\n    Tedd Vanadilok       CSL     5154    {}                  ".
        format(today))
    printout.write(
        "\n____________________________________________________________________________________"
    )
    printout.write("\n")
    printout.write(
        "\nAccounting Approval by:    Received by:                Date Received: __/__/____\n"
    )
    printout.write("\n _______________________    _______________________\n")
    printout.write(
        "\n                           Amount Paid Out: $______    \n")
    printout.write(
        "\nDate: __/__/____           Date: __/__/____            \n")
    printout.write(
        "\n####################################################################################"
    )
    printout.write(
        "\nThank you for supporting your Registered Student Organization. ")
    printout.write("\n        ___   _____ ______     ___________ ____")
    printout.write("\n       /   | / ___// ____/    / ____/ ___//  _/")
    printout.write("\n      / /| | \__ \/ / __     / /    \__ \ / /")
    printout.write("\n     / ___ |___/ / /_/ /    / /___ ___/ // /")
    printout.write("\n    /_/  |_/____/\____/     \____//____/___/")
    printout.write(
        "\n####################################################################################"
    )
    printout.write(
        "\n####################################################################################"
    )

    printout.close()

    return filename, finalfilename


def printmenu(user_choice, thecyber, form_filler, reimbursee, reimbursee_email,
              phone_number, rso_name, rso_code, purchaseinfo,
              purchase_category, discr_funds, club_funds, nol_number,
              total_spent, total_requested, reimbursement_method):
    valid_options = ['Continue', '1', '2', '3']

    while user_choice not in valid_options:
        print("[1]\n"
              "President or Treasurer of club:.............{}\n"
              "Person to be reimbursed:.................{}\n"
              "Email of person to be reimbursed:........{}\n"
              "Phone number:....................{}\n"
              "RSO name:................................{}\n"
              "RSO code:................................{}\n"
              "Description of Purchase:\n"
              "{}\n"
              "\n[2]\n"
              "Date on receipt:.........................{}\n"
              "Purchase category:.......................{}\n"
              "Total spent:........................{}\n"
              "\n[3]\n"
              "Discretionary Funds:.....................${:.2f}\n"
              "Club Funds:..............................${:.2f}\n"
              "\nTotal Amount to be Reimbursed:.................${:.2f}\n".
              format(form_filler, reimbursee, reimbursee_email, phone_number,
                     rso_name, rso_code, description_of_purchase,
                     purchase_date, purchase_category, total_spent,
                     discr_funds, club_funds, total_requested))
        if total_requested >= 200.00:
            print("[3]\n"
                  "Address:..............{}\n"
                  "City, State, Zip:.....{}\n"
                  "\nReimbursement Method: {}".format(reimbursee_address,
                                                      reimbursee_address2,
                                                      reimbursement_method))

    user_choice = input("Choose an option: ")
    if user_choice == 'Continue':

        thecyber(spending_categories, reimbursement_method, form_filler,
                 reimbursee, reimbursee_email, phone_number, rso_code,
                 rso_name, purchase_date, purchase_category,
                 description_of_purchase, expt_accountingstring,
                 expensetransfer, discr_funds, club_funds, total_requested,
                 total_spent, cash, check, directdeposit, reimbursee_address,
                 reimbursee_address2)
        thepaper(spending_categories, reimbursement_method, form_filler,
                 reimbursee, reimbursee_email, phone_number, rso_code,
                 rso_name, purchase_date, purchase_category,
                 description_of_purchase, expt_accountingstring,
                 expensetransfer, discr_funds, club_funds, total_requested,
                 total_spent, cash, check, directdeposit, reimbursee_address,
                 reimbursee_address2)

    elif user_choice == "1":
        basicinfo(form_filler, reimbursee, reimbursee_email, phone_number,
                  rso_code, rso_name)
    elif user_choice == "2":
        purchaseinfo(purchase_date, purchase_category, description_of_purchase,
                     expt_accountingstring, expensetransfer)
    elif user_choice == "3":
        fundsinfo(discr_funds, club_funds, total_requested, total_spent, cash,
                  check, directdeposit, rso_code, reimbursee_address,
                  reimbursee_address2)

    return form_filler, reimbursee, reimbursee_email, phone_number, rso_name, rso_code, purchaseinfo, purchase_category, discr_funds, club_funds, nol_number, total_spent, total_requested, cash, check, expensetransfer, directdeposit


if __name__ == "__main__":
    form_filler, reimbursee, reimbursee_email, phone_number, rso_code, rso_name = basicinfo(
        form_filler, reimbursee, reimbursee_email, phone_number, rso_code,
        rso_name)
    purchase_date, purchase_category, description_of_purchase, spending_categories = purchaseinfo(
        spending_categories, purchase_date, purchase_category,
        description_of_purchase)
    reimbursement_method, expt_accountingstring, discr_funds, club_funds, total_requested, total_spent, reimbursee_address, reimbursee_address2 = fundsinfo(
        reimbursement_method, expt_accountingstring, discr_funds, club_funds,
        total_requested, total_spent, reimbursee_address, reimbursee_address2,
        basicinfo)
    printmenu(user_choice, thecyber, form_filler, reimbursee, reimbursee_email,
              phone_number, rso_name, rso_code, purchaseinfo,
              purchase_category, discr_funds, club_funds, total_spent,
              total_requested, reimbursement_method)
