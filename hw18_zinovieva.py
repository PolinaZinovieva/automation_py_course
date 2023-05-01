import csv
import json


class JsonToCSV:
    def __init__(self):
        self.__data = []

    def read_json(self, filename: str):
        with open(filename, "r") as json_file:
            lines = json.load(json_file)
            for l in lines:
                self.__data.append(l)
            print(self.__data)

    def write_csv(self, filename: str):
        with open(
            filename,
            "w",
            newline="",
        ) as csv_file:
            writer = csv.writer(csv_file, delimiter=" ")
            writer.writerows(self.__data)
            self.cleanup()

    def cleanup(self):
        self.__lines = []


converter = JsonToCSV()
converter.read_json("example.json")
converter.write_csv("new.csv")
