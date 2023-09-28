from Entities.SpreadSheets.FinanceSheet import load_finance_sheet
from Services.ClosingFinanceSheet import closing_finance


def main():
    finance_sheet = load_finance_sheet()
    closing_finance(finance_sheet['values'])


if __name__ == '__main__':
    main()
