from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Path, Depends, HTTPException, status

from core.database import db_helper, Product
from . import crud


async def get_product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found",
    )
