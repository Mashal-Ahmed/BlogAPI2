"""
BLOG PLATFORM API
-------------------------------------
Only 2 endpoints kept:
  1. GET /posts          -> list all blog posts
  2. GET /posts/{id}     -> get a single blog post
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Blog Platform API")

# ----- In-memory data storage (simulates a database) -----
posts_db = {
    1: {"title": "First post", "content": "Content of first post", "author_id": 123, "likes": 5},
    2: {"title": "FastAPI tutorial", "content": "Learn FastAPI", "author_id": 123, "likes": 2}
}

# ========== ENDPOINTS ==========

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint - provides basic API information.
    """
    return {
        "message": "Welcome to DocuNode Testing API - Blog Platform (Stripped)",
        "version": "1.0",
        "docs": "/docs",
        "endpoints": [
            "GET /",
            "GET /posts",
            "GET /posts/{post_id}"
        ]
    }

# 1. GET /posts - List all blog posts
@app.get("/posts")
async def list_posts():
    """
    Returns a list of all blog posts.
    Each post contains: post_id, title, content, author_id, likes.
    """
    return [
        {
            "post_id": pid,
            "title": p["title"],
            "content": p["content"],
            "author_id": p["author_id"],
            "likes": p["likes"]
        }
        for pid, p in posts_db.items()
    ]

# 2. GET /posts/{id} - Get a single post by ID
@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    """
    Returns a single blog post including its likes count.
    Returns 404 if post not found.
    """
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    p = posts_db[post_id]
    return {
        "post_id": post_id,
        "title": p["title"],
        "content": p["content"],
        "author_id": p["author_id"],
        "likes": p["likes"]
    }
