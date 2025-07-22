import uuid

import pytest
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError

class TestDeleteCategoryIntegration:
    def test_delete_category(self):
        category = Category(name="Category 1", description="Category 1 description")
        category_2 = Category(name="Category 2", description="Category 2 description")
        repository = InMemoryCategoryRepository(categories=[category, category_2])
        use_case = DeleteCategory(category_repository=repository)
        request = DeleteCategoryRequest(id=category.id)
        response = use_case.execute(request)
        assert response is None
        assert repository.find_by_id(category.id) is None