import uuid
from unittest.mock import create_autospec
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest, UpdateCategoryResponse
from src.core.category.domain.category import Category

class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(id=uuid.uuid4(), name="Category 1", description="Category 1 description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = category
        use_case = UpdateCategory(category_repository=mock_repository)

        response = use_case.execute(UpdateCategoryRequest(id=category.id, name="Category 2"))

        mock_repository.update.assert_called_once_with(category)
        assert response == UpdateCategoryResponse(id=category.id, name="Category 2", description=category.description, is_active=category.is_active)
        assert category.name == "Category 2"

    def test_update_category_description(self):
        category = Category(id=uuid.uuid4(), name="Category 1", description="Category 1 description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = category
        use_case = UpdateCategory(category_repository=mock_repository)

        use_case.execute(UpdateCategoryRequest(id=category.id, description="Category 2 description"))

        mock_repository.update.assert_called_once_with(category)
        assert category.description == "Category 2 description"

    def test_can_deactivate_category(self):
        category = Category(id=uuid.uuid4(), name="Category 1", description="Category 1 description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = category
        use_case = UpdateCategory(category_repository=mock_repository)

        use_case.execute(UpdateCategoryRequest(id=category.id, is_active=False))

        mock_repository.update.assert_called_once_with(category)
        assert category.is_active is False

    def test_can_activate_category(self):
        category = Category(id=uuid.uuid4(), name="Category 1", description="Category 1 description", is_active=False)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.find_by_id.return_value = category
        use_case = UpdateCategory(category_repository=mock_repository)

        use_case.execute(UpdateCategoryRequest(id=category.id, is_active=True))

        mock_repository.update.assert_called_once_with(category)
        assert category.is_active is True