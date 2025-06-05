from dtos.customer_types import CustomerData

class Customer:
    def __init__(self, id: int, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
    
    @classmethod
    def from_dict(cls, data: CustomerData):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            email = data.get("email", ""),
            phone = data.get("phone", "")
        )
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, email={self.email}, phone={self.phone})" 