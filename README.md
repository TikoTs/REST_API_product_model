This is a Django REST Framework Product App. This repository houses a Django application designed to streamline product-category management using the Django Rest Framework.

## Usage

### Running Migrations

Before diving into the application, ensure to migrate the database:

```bash
python manage.py migrate
```

### Creating the Product App

Execute the following command to create the product app:

```bash
 python manage.py runserver  
```

### URL Configuration

1. **Admin Interface**: `/admin/`
   - Provides access to the Django admin interface for managing various aspects of the application.

2. **Product Endpoints**:
   - List View: `/products/`
   - Create View: `/products/create/`
   - Detail View: `/products/<int:pk>/`
   - Delete View: `/products/<int:pk>/delete/`
   - Update View: `/products/<int:pk>/update/`

These URLs define the endpoints for various operations related to product management within the application.

