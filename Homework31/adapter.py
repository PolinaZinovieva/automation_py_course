from Homework31.reqs import TestRequests
from Homework31.storage import Storage

class Adapter(TestRequests):


    def execute_post_to_db(self):
        super().test_post()
        TestRequests().test_post()
        Storage().insert_into_db(id= self.id_var,name=self.name_var, year=self.year_var,price=self.price_var,cpu_model=self.cpu_var,hard_disk=self.hard_var)





    def execute_put_to_db(self):
        super().put_update()
        TestRequests().test_post()
        Storage().update_db(name= self.name_var_n,hard_disk=self.hard_var_n,name2=self.name_var)

    def execute_update_to_request(self):
        TestRequests().from_storage()











