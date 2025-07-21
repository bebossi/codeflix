from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository

class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories: list[Category] = None):
        self.categories = categories or []

    def save(self, category: Category):
        self.categories.append(category)

    def find_by_id(self, id: str) -> Category:
        return next((category for category in self.categories if category.id == id), None)