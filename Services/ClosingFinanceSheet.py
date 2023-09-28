from Entities.SpreadSheets.FinanceSheet import update_finance_sheet
from Services.SendEmail import send_email


def closing_finance(rows):
    update_date = ''
    amount = 0
    for i, row in enumerate(rows[1:], start=2):
        dates_column = row[0]
        incomes_column = row[1] if len(row) > 1 else ''
        debit_column = row[2] if len(row) > 2 else ''
        saving_column = row[3] if len(row) > 3 else ''
        if incomes_column != '':
            if incomes_column and debit_column and saving_column == '':
                difference = float(incomes_column.replace(',', '.')) - float(debit_column.replace(',', '.'))
                amount += difference
            else:
                amount += float(saving_column.replace(',', '.'))
                update_date = dates_column
                continue

            cell_to_update = f'D{i}'
            update_finance_sheet([(cell_to_update, difference)])
        else:
            continue

    subject = f"Fechamento Referente ao mês: {update_date}"
    message = f'Até o fechamento do mês: {update_date}, seu saldo é de: {amount}'
    to_email = 'eduardoofficial12@gmail.com'
    send_email(subject, message, to_email)
