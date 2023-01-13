from datetime import datetime
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


def get_data():
    data = None
    return data

def get_excel():
    wb = Workbook()
    ws: Worksheet = wb.active
    return wb, ws

def add_header(sheet: Worksheet):
    sheet.append(["Name", "IP", "Time", "Value", "_id", "Type"])
    return sheet

def main():
    data = get_data()
    file, sheet = get_excel()
    add_header(sheet=sheet)
    counter = 0

    for d in data.find():
        counter += 1
        d: dict
        row = ["NaN" for _ in ["Name", "IP", "Time", "Value", "createDate", "_id", "Type"]]
        row[0] = d.get("Name")
        row[1] = d.get("IP")
        row[2] = d.get("Time")
        row[3] = d.get("Value")
        row[4] = d.get("createDate").strftime("%Y-%m-%d_%H:%M:%S") if d.get("createDate") else "NAN"
        row[5] = str(d.get("_id"))
        row[6] = d.get("Type")
        sheet.append(row)
        
        if counter % 100000 == 0:
            print(counter)
            file.save(f"mongo_data_{counter}.xlsx")
            file, sheet = get_excel()
            add_header(sheet=sheet)


if __name__ == "__main__":
    main()
