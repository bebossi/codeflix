from unittest.mock import create_autospec
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.list_category import CategoryOutput, ListCategory, ListCategoryRequest, ListCategoryResponse
from src.core.category.domain.category import Category


class TestListCategory:
    def test_when_no_categories_are_found_should_return_empty_list(self):
        category = Category(name="Category 1", description="Category 1 description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = []

        use_case = ListCategory(category_repository=mock_repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)
        assert response == ListCategoryResponse(data=[])

    def test_when_categories_are_found_should_return_list_of_categories(self):
        category = Category(name="Category 1", description="Category 1 description")
        category_2 = Category(name="Category 2", description="Category 2 description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = [category, category_2]

        use_case = ListCategory(category_repository=mock_repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)
        assert response == ListCategoryResponse(data=[
            CategoryOutput(id=category.id, name=category.name, description=category.description, is_active=category.is_active),
            CategoryOutput(id=category_2.id, name=category_2.name, description=category_2.description, is_active=category_2.is_active)
        ])