from .models import Products
class AccountsDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Products):
             # your model name as in settings.py/DATABASES
             return 'product_db'
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Products):
             # your model name as in settings.py/DATABASES
             return 'product_db'
          return None