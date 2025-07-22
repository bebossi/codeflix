import uuid

import pytest
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError

class TestGetCategoryIntegration:
    def test_get_category(self):
        category = Category(name="Category 1", description="Category 1 description")
        category_2 = Category(name="Category 2", description="Category 2 description")
        repository = InMemoryCategoryRepository(categories=[category, category_2])
        use_case = GetCategory(category_repository=repository)
        request = GetCategoryRequest(id=category.id)
        response = use_case.execute(request)
        assert response == GetCategoryResponse(id=category.id, name=category.name, description=category.description, is_active=category.is_active)

    def test_get_category_not_found(self):
        category = Category(name="Category 1", description="Category 1 description")
        category_2 = Category(name="Category 2", description="Category 2 description")
        repository = InMemoryCategoryRepository(categories=[category, category_2])         
        use_case = GetCategory(category_repository=repository)
        request = GetCategoryRequest(id=uuid.uuid4())
        with pytest.raises(CategoryNotFoundError):
            use_case.execute(request)