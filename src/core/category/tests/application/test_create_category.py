from uuid import UUID
import pytest
from core.category.application.create_category import create_category, InvalidCategoryData

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        category_id = create_category(name="Category 1", description="Category 1 description")
        assert category_id is not None
        assert isinstance(category_id, UUID)

    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="Name is required") as exc_info:
            create_category(name=None, description="Category 1 description")

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "Name is required"