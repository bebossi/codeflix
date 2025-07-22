from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError

@dataclass
class GetCategoryRequest:
    id: UUID

@dataclass
class GetCategoryResponse:
    id: UUID
    name: str
    description: str
    is_active: bool

class GetCategory:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, request: GetCategoryRequest) -> GetCategoryResponse:
        category = self.category_repository.find_by_id(request.id)
        if not category:
            raise CategoryNotFoundError
        return GetCategoryResponse(id=category.id, name=category.name, description=category.description, is_active=category.is_active)