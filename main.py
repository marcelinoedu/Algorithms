from Entities.SpreadSheets.FinanceSheet import load_finance_sheet
from Services.ClosingFinanceSheet import closing_finance


def main():
    finance_sheet = load_finance_sheet()
    # closing_finance(finance_sheet['values'])
    for i, rows in enumerate(finance_sheet['values'][0:], start=1):
        print(f'linha:{i}, dados: {rows}')


if __name__ == '__main__':
    main()
