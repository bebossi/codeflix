from unittest.mock import MagicMock
from uuid import UUID
import pytest
from core.category.application.create_category import CreateCategory, CreateCategoryRequest, InvalidCategoryData
from core.category.application.category_repository import CategoryRepository

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_category_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(category_repository=mock_category_repository)
        request = CreateCategoryRequest(name="Category 1", description="Category 1 description")

        category_id = use_case.execute(request)

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_category_repository.save.call_count == 1

    def test_create_category_with_invalid_data(self):
        mock_category_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(category_repository=mock_category_repository)
        with pytest.raises(InvalidCategoryData, match="Name is required") as exc_info:
            use_case.execute(CreateCategoryRequest(name=None, description="Category 1 description"))

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "Name is required"