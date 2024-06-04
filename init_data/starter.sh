cd /init

# create amazon_products db
psql -c "create database amazon_products"

# create products and categories tables
pipenv run alembic revision --autogenerate -m "Add Product model"
pipenv run alembic upgrade head

# load data
psql -c "\COPY categories (id, category_name) FROM '/code/init_data/categories.csv' DELIMITER ',' CSV"
psql -c "\COPY products (id, title, imgUrl, stars, reviews, price, category_id, isBestSeller) FROM '/code/init_data/products2.csv' DELIMITER ',' CSV"
