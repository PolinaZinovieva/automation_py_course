from Homework31.reqs import TestRequests
from Homework31.storage import Storage

class Adapter(TestRequests):

    def to_db(self):

      req = TestRequests()

      req.test_post()
      Storage().insert_into_db(id= self.id_var,name=self.name_var, year=self.year_var,cpu_model=self.cpu_var,hard_disk=self.hard_var)





