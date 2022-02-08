from unicodedata import category
from django.test import TestCase
from store.models import Category , Product
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(
            name='django',slug='django'
        )
    
    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        
        data = self.data1
        # checking datatype return in self.data1
        self.assertTrue(isinstance(data , Category))
        # checking data returned by Category table.
        self.assertEqual(str(data) , 'django')
        
    # def test_category_url(self):
    #     """
    #     Test Category model slug and URL reverse
    #     """
    #     pass
        
class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(
            name='django',slug='django'
        )
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1,
            title='django beginners',
            created_by_id=1,
            slug='django beginners',
            price='20.00',
            image='django'
        )
    
    def test_products_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        
        data = self.data1
        self.assertTrue(isinstance(data , Product))
        self.assertEqual(str(data) , 'django beginners')
    
    
    
        