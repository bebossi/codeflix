from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError

@dataclass
class DeleteCategoryRequest:
    id: UUID

class DeleteCategory:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, request: DeleteCategoryRequest) -> None:
        category = self.category_repository.find_by_id(request.id)
        if not category:
            raise CategoryNotFoundError
        self.category_repository.delete(category.id)