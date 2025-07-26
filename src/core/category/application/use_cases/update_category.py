from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError
from src.core.category.application.exceptions import InvalidCategoryData

@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None

@dataclass
class UpdateCategoryResponse:
    id: UUID
    name: str
    description: str
    is_active: bool

class UpdateCategory:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, request: UpdateCategoryRequest) -> UpdateCategoryResponse:
        category = self.category_repository.find_by_id(request.id)
        if not category:
            raise CategoryNotFoundError
        current_name = category.name
        current_description = category.description
        current_is_active = category.is_active
        if request.name is not None:
            current_name = request.name
        if request.description is not None:
            current_description = request.description
        if request.is_active is not None:
            current_is_active = request.is_active
        try:
            category.update(name=current_name, description=current_description, is_active=current_is_active)
        except ValueError as e:
            raise InvalidCategoryData(e)
        
        self.category_repository.update(category)
        return UpdateCategoryResponse(id=category.id, name=current_name, description=current_description, is_active=current_is_active)
