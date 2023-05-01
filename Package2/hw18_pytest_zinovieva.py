import csv
class Files:
    def __init__(self, filename:str, rows):
        self.filename = filename
        self.rows = rows
    def add_row(self):
        with open(
            self.filename,
            "w",
            newline="",
        ) as csv_file:
            writer = csv.writer(csv_file, delimiter=" ")
            writer.writerow(self.rows)

    def delete_row(self):
            reader = open(self.filename, 'r')
            lines = reader.readlines()

            writer = open(self.filename, 'w')
            writer.writelines(lines[:-1])

    def read(self):
        reader = open(self.filename, 'r')
        lines = reader.readlines()
        return lines


executer = Files("../new.csv", ['1', 'Polina', '2', 'Adrianne', '3', 'Elena', '4', 'Bella'])
executer.add_row()
executer.read()
executer.delete_row()




