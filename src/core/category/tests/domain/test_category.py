import unittest
import pytest
import uuid
from src.core.category.domain.category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="Name must be less than 255 characters"):
            Category(name="a" * 256)

    def test_name_is_not_none(self):
        with pytest.raises(ValueError, match="Name is required"):
            Category(name='')

    def test_category_id_is_uuid(self):
        category = Category(name="Test Category")
        assert isinstance(category.id, uuid.UUID)
    
    def test_category_is_active_by_default(self):
        category = Category(name="Test Category")
        assert category.is_active

    def test_category_id_is_not_none(self):
        category = Category(name="Test Category")
        assert category.id is not None


if __name__ == "__main__":
    unittest.main()


class TestUpdateCategory(unittest.TestCase):
    def test_update_category(self):
        category = Category(name="Test Category")
        category.update(name="Updated Category", description="Updated Description", is_active=True)
        assert category.name == "Updated Category"
        assert category.description == "Updated Description"

    def test_update_category_with_invalid_name(self):
        category = Category(name="Test Category")
        with pytest.raises(ValueError, match="Name must be less than 255 characters"):  
            category.update(name="a" * 256, description="Updated Description", is_active=True)

    def test_update_category_with_invalid_name_and_description(self):
        category = Category(name="Test Category")


class TestActivateCategory(unittest.TestCase):
    def test_activate_category(self):
        category = Category(name="Test Category", is_active=False)
        category.activate()
        assert category.is_active is True

    def test_deactivate_category(self):
        category = Category(name="Test Category")
        category.deactivate()
        assert category.is_active is False

class TestDeactivateCategory(unittest.TestCase):
    def test_deactivate_category(self):
        category = Category(name="Test Category")
        category.deactivate()
        assert category.is_active is False


class TestEquality:
    def test_when_categories_have_different_ids_they_should_not_be_equal(self):
        category1 = Category(name="Test Category")
        category2 = Category(name="Test Category")
        assert category1 != category2