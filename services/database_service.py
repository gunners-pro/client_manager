import sqlite3
from typing import cast
from dtos.customer_types import CustomerData
from models.customer_model import Customer

class DatabaseService:
    def __init__(self, db_name="customers.db"):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT
            )
        """)
        self.connection.commit()

    def add_customer(self, customer: Customer) -> bool:
        try:
            self.cursor.execute("""
                INSERT INTO customers (name, email, phone)
                VALUES (?, ?, ?)
            """, (customer.name, customer.email, customer.phone))
            self.connection.commit()
            return True
                 
        except Exception as e:
            print("Error at add new customer:", e)
            return False
    
    def list_customers(self) -> list:
        self.cursor.execute("SELECT id, name, email, phone FROM customers")
        rows = self.cursor.fetchall()
        return [
            Customer.from_dict(cast(CustomerData, dict(row))) 
            for row in rows
        ]
    
    def search_customer_by_name(self, name: str) -> list:
        self.cursor.execute("""
            SELECT id, name, email, phone FROM customers
            WHERE name LIKE ?
        """, (f"%{name}%"))
        rows = self.cursor.fetchall()
        return [
            Customer.from_dict(cast(CustomerData, dict(row)))
            for row in rows
        ]
    
    def edit_customer(self, customer: Customer) -> bool:
        try:
            self.cursor.execute("""
                UPDATE customers
                SET name = ?, email = ?, phone = ?
                WHERE id = ?
            """, (customer.name, customer.email, customer.phone, customer.id))
            self.connection.commit()
            return True
        
        except Exception as e:
            print("Error at edit customer", e)
            return False
    
    def delete_customer(self, customer_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error at delete customer", e)
            return False
    
    def close_connection(self):
        self.connection.close()