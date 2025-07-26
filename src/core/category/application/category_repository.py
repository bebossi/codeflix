from abc import ABC, abstractmethod
from src.core.category.domain.category import Category

class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category: Category) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Category | None:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def update(self, category: Category) -> None:
        pass