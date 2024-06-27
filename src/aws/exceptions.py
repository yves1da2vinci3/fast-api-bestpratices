from fastapi import HTTPException, status

s3_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="S3 error occurred",
)
