import uuid
from dataclasses import dataclass, field

@dataclass
class Category:
    name: str
    description: str = ''
    is_active: bool = True
    id: uuid.UUID = field(default_factory=uuid.uuid4)   

    def __post_init__(self):
        self._validate_name()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description} - {self.is_active}"
    
    def __repr__(self):
        return f"{self.id} - {self.name} - {self.description} - {self.is_active}"
    
    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def _validate_name(self):
        if not self.name:
            raise ValueError("Name is required")
        if len(self.name) > 255:
            raise ValueError("Name must be less than 255 characters")
        
    def update(self, name: str, description: str, is_active: bool):
        self.name = name
        self.description = description
        self.is_active = is_active
        self._validate_name()

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id
