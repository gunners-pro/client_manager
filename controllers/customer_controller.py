from models.customer_model import Customer
from services.database_service import DatabaseService
from dtos.customer_types import CustomerData

class CustomerController:
    def __init__(self):
        self.db = DatabaseService()

    def add(self, data: CustomerData) -> bool:
        customer = Customer.from_dict(data)
        return self.db.add_customer(customer)
    
    def list_all(self) -> list[Customer]:
        return self.db.list_customers()
    
    def search_by_name(self, name: str) -> list[Customer]:
        return self.db.search_customer_by_name(name)
    
    def update(self, customer: Customer) -> bool:
        return self.db.edit_customer(customer)
    
    def delete(self, id: int) -> bool:
        return self.db.delete_customer(id)