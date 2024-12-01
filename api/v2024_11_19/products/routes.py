from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from . import crud
from .dependencies import get_product_by_id
from .schemas import ProductResponse, ProductCreate, ProductUpdate, ProductUpdatePartial
from core.database import db_helper, Product

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", response_model=list[ProductResponse])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):  # -> ProductResponse:
    return await crud.get_products(session=session)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    payload: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        product = await crud.create_product(session=session, payload=payload)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Product {payload.title} already exists",
        )
    return product


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product: Product = Depends(get_product_by_id),
):
    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    payload: ProductUpdate,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.get_scoped_session),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=payload,
    )


@router.patch("/{product_id}", response_model=ProductResponse)
async def update_product_partial(
    payload: ProductUpdatePartial,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.get_scoped_session),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=payload,
        partial=True,
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.get_scoped_session),
) -> None:
    await crud.delete_product(product=product, session=session)
