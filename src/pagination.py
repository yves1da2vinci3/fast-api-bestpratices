# Pagination module
from pydantic import BaseModel

class PaginationParams(BaseModel):
    skip: int = 0
    limit: int = 10
