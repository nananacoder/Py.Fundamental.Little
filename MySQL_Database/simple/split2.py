#!/usr/bin/python

files = "sqlfile.sql"

class SplitFileSql():

    lines_reads = []
    max_row = 1000
    max_row_insert = 10000

    file_output = "splitter.sql"
    current_file_output = 0

    def __init__(self, fullFilePath):
        self.fp = open(fullFilePath, "r+")

    def getLines(self):
        if len(self.lines_reads) == 0:
            self.lines_reads = self.fp.readlines()
            self.fp.close()
        return self.lines_reads

    def create_file(self, lines):
        self.current_file_output += 1
        file = str(self.current_file_output) + "_" + self.file_output
        writer = open(file, "w+")
        writer.writelines(lines)
        writer.close()

    def process(self):
        lines = self.getLines()

        groups = []
        group = []
        c = 0
        for line in lines:
            # quando trova una string INSERT taglia
            if c > self.max_row_insert:
                if "INSERT INTO" in str(line).strip().upper():
                    c = 0
                    groups.append(group)
                    group = []

            group.append(line)
            c += 1
            # quando trova una riga vuota taglia
            if c >= self.max_row:
                if str(line).strip() == "":
                    c = 0
                    groups.append(group)
                    group = []

        if len(group) > 0:
            groups.append(group)
            group = []

        for group in groups:
            self.create_file(group)



cc = SplitFileSql(files)
cc.process()