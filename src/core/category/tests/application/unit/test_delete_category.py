from unittest.mock import create_autospec
import uuid

import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFoundError
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest

from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestDeleteCategory:
    def test_delete_category(self):
        category = Category(name="Category 1", description="Category 1 description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = category
        use_case = DeleteCategory(mock_repository)

        use_case.execute(DeleteCategoryRequest(id=category.id))

        mock_repository.delete.assert_called_once_with(category.id)

    def test_delete_category_not_found(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = None
        use_case = DeleteCategory(mock_repository)

        with pytest.raises(CategoryNotFoundError):
            use_case.execute(DeleteCategoryRequest(id=uuid.uuid4()))

        mock_repository.delete.assert_not_called()
        assert mock_repository.delete.called is False
