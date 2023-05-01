from Package2.hw18_pytest_zinovieva import Files

class FileTest:
    def __init__(self):
        self.files = Files("new.csv", ['1', 'Polina', '2', 'Adrianne', '3', 'Elena', '4', 'Bella'])

    def setup_class(self):
        print('\nwere in setup class section')


    def check_add_string(self):
        self.files.add_row()
        self.files.read()
        assert self.files.read() == ['1 Polina 2 Adrianne 3 Elena 4 Bella\n']

    def check_pop_string(self):
        self.files.delete_row()
        self.files.read()
        assert self.files.read() == []



ass = FileTest()
ass.check_add_string()