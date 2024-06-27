from fastapi import HTTPException, status

post_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post not found",
)
