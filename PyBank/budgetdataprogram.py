import os
import csv

def read_csv_file(file_path):
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        return [x for x in csvreader]

def calculate_financials(data):
    total_months = len(data)
    net_total = sum(int(x[1]) for x in data)
    changes = []
    months = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    previous_profit = int(data[0][1])
    for x in data[1:]:
        current_profit = int(x[1])
        change = current_profit - previous_profit
        changes.append(change)
        months.append(x[0])

        if change > greatest_increase[1]:
            greatest_increase = [x[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [x[0], change]

        previous_profit = current_profit

    average_change = sum(changes) / len(changes)

    return {
        "total_months": total_months,
        "net_total": net_total,
        "average_change": average_change,
        "greatest_increase": greatest_increase,
        "greatest_decrease": greatest_decrease
    }

def generate_report(financials):
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {financials['total_months']}\n"
        f"Total: ${financials['net_total']}\n"
        f"Average Change: ${financials['average_change']:.2f}\n"
        f"Greatest Increase in Profits: {financials['greatest_increase'][0]} (${financials['greatest_increase'][1]})\n"
        f"Greatest Decrease inProfits: {financials['greatest_decrease'][0]} (${financials['greatest_decrease'][1]})\n"
    )
    return output

def main():
    CSV_PATH = 'budget_data.csv'
    data = read_csv_file(CSV_PATH)
    financials = calculate_financials(data)
    report = generate_report(financials)

    print(report)
    with open("financial_analysis.txt", "w") as file:
        file.write(report)
    print("Financial Analysis ha been saved to 'financial_analysis.txt'.")

main()
