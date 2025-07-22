from unittest.mock import create_autospec
from uuid import UUID
import pytest
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError
from src.core.category.domain.category import Category

class TestGetCategory:
    def test_get_category_with_valid_data(self):
        category = Category(name="Test Category", description="Test Description")
        mock_category_repository = create_autospec(CategoryRepository)
        mock_category_repository.find_by_id.return_value = category
        use_case = GetCategory(category_repository=mock_category_repository)
        request = GetCategoryRequest(id=category.id)

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )

    # def test_get_category_not_found(self):
    #     mock_category_repository = MagicMock(CategoryRepository)
    #     use_case = GetCategory(category_repository=mock_category_repository)
    #     request = GetCategoryRequest(id=UUID("00000000-0000-0000-0000-000000000000"))
    #     with pytest.raises(CategoryNotFoundError):
    #         use_case.execute(request)