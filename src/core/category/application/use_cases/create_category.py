from dataclasses import dataclass
from uuid import UUID
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidCategoryData


@dataclass
class CreateCategoryRequest:
    name: str
    description: str
    is_active: bool = True

@dataclass
class CreateCategoryResponse:
    id: UUID


class CreateCategory:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository
    
    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(name=request.name, description=request.description, is_active=request.is_active)
        except ValueError as e:
            raise InvalidCategoryData(e)
        self.category_repository.save(category)
        return CreateCategoryResponse(id=category.id)

        