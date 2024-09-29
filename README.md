## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- pip
- Virtualenv (optional but recommended)

## Frontend

You can access the frontend of the application at:

- **Post List**: [{hostname}/posts/]({hostname}/posts/)
- **Post Details**: [{hostname}/posts/{id}]({hostname}/posts/{id})
- **Post Comments**: [{hostname}/posts/{id}/comments]({hostname}/posts/{id}/comments)

This page displays all blog posts along with their details.

## API Endpoints

The following API endpoints are available for retrieving blog posts and comments:

- **Get All Posts**
  - **URL**: [{hostname}/api/posts/](/api/posts/)
  - **Method**: GET
  - **Description**: Retrieves a list of all posts.

- **Get Post Detail**
  - **URL**: [{hostname}/api/posts/{id}/]({hostname}/api/posts/{id}/)
  - **Method**: GET
  - **Description**: Retrieves the details of a specific post by its ID.

- **Get Comments for a Post**
  - **URL**: [{hostname}/api/posts/{id}/comments/]({hostname}/api/posts/{id}/comments/)
  - **Method**: GET
  - **Description**: Retrieves comments related to a specific post by its ID.

## Setup Instructions

1. Clone the repository
```bash
    git clone git@github.com:kristinaNik/Django-app.git
```
2. Copy .env.example and create your local .env file
3. Install the required packages
```bash
pip install -r requirements.txt
```

## Run the the Django server
```bash
python3 manage.py runserver (If you use mac os )
```
```bash
python manage.py runserver (If you use windows os)
```