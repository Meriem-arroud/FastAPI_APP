# FastAPI Application

Products management application to hundle CRUD endpoints for creation, reading, updating, and deletion of products.

# Prerequisites
```
postgresql
redis : brew install redis
pipenv : pip install pipenv
```

# Database Initial Setup

- **Create amazon_products database in postgres**
- **Create user**
- **Grant the created user use access on the amazon_products database**
  

# set environment variables
Before running the app, you will need to set the database credentials (user and password) as environment variables.
Below is the syntax for setting the database credentials in macos/linux environment
```
   export POSTGRES_HOST=localhost
   export POSTGRES_USER=<postgres_user_name>
   export POSTGRES_PASSWORD=<postgres_password>
   export REDIS_HOST=localhost

```

# Create pipenv environment
```
cd FASTAPI_APP
pipenv install --dev
```

# Create model tables in postgres database
```
pipenv run alembic init -t async alembic ----> initializes a new Alembic environment for database migrations
pipenv run alembic revision --autogenerate -m "Add Product model"
pipenv run alembic upgrade head
```

# Start redis server
```
redis-server
```

# To run the app 
```
pipenv run uvicorn main:app -reload
```




