# Blog Platform API

A minimal FastAPI service exposing read-only blog post endpoints. This is a trimmed-down version of a larger blog platform API, keeping just the two endpoints for viewing posts.

## Features

- List all blog posts
- Get details of a single blog post by ID
- In-memory data store, pre-seeded with sample posts for easy testing

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
pip install -r blog_requirements.txt
```

## Running the API

```bash
uvicorn blog_api_stripped:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API docs (Swagger UI) are available at `http://127.0.0.1:8000/docs`.

## Endpoints

### `GET /`
Root endpoint. Returns basic API info and a list of available endpoints.

### `GET /posts`
Returns a list of all blog posts.

**Example:**
```bash
curl "http://127.0.0.1:8000/posts"
```

**Example response:**
```json
[
  {
    "post_id": 1,
    "title": "First post",
    "content": "Content of first post",
    "author_id": 123,
    "likes": 5
  },
  {
    "post_id": 2,
    "title": "FastAPI tutorial",
    "content": "Learn FastAPI",
    "author_id": 123,
    "likes": 2
  }
]
```

### `GET /posts/{post_id}`
Returns details for a single blog post.

**Path parameter:**
| Parameter  | Type | Description       |
|------------|------|--------------------|
| `post_id`  | int  | ID of the post     |

**Example:**
```bash
curl "http://127.0.0.1:8000/posts/1"
```

**Example response:**
```json
{
  "post_id": 1,
  "title": "First post",
  "content": "Content of first post",
  "author_id": 123,
  "likes": 5
}
```

**Errors:**
- `404 Not Found` — if no post exists with the given `post_id`.

## Sample Data

The app seeds the following posts on startup:

| ID | Title              | Author ID | Likes |
|----|--------------------|-----------|-------|
| 1  | First post          | 123       | 5     |
| 2  | FastAPI tutorial     | 123       | 2     |

## Notes

This is a stripped-down version of a larger API. Post creation/updating, likes, comments, tags, users, search, and authentication have been removed.
