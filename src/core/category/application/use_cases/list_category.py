from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category

@dataclass
class ListCategoryRequest:
    pass

@dataclass
class CategoryOutput:
    id: UUID
    name: str
    description: str
    is_active: bool

@dataclass
class ListCategoryResponse:
    data: list[CategoryOutput]


class ListCategory:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, request: ListCategoryRequest) -> ListCategoryResponse:
        categories = self.category_repository.list()
        return ListCategoryResponse(data=[CategoryOutput(id=category.id, name=category.name, description=category.description, is_active=category.is_active) for category in categories])