import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from product.models import Product, Brand
import random

def seed_brand(n):
     fake = Faker()
     images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
     for _ in range(n):
         Brand.objects.create(
             name=fake.name(),
             image=f'brands/{images[random.randint(0, len(images)-1)]}'
         )
     print(f'Seed {n} Brands Successfully')
def seed_product(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flags = ['New','Sale','Feature']

    for _ in range(n):
        Product.objects.create(
            name = fake.name() , 
            image = f'brands/{images[random.randint(0,12)]}' , 
            flag = flags[random.randint(0,2)] ,
            price = round(random.uniform(20.99,99.99),2),
            sku = random.randint(1000,10000000) , 
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=2000) , 
            quantity = random.randint(0,30) ,
            brand = Brand.objects.get(id=random.randint(1,111))
        )

    print(f'Seed {n} Product Successfully')
