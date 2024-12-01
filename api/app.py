from contextvars import ContextVar
from datetime import date
from contextlib import asynccontextmanager

from fastapi import FastAPI
from verselect import HeaderRoutingFastAPI
from fastapi.middleware.cors import CORSMiddleware

from .v2024_11_19.products.routes import router as product_router
from .v2024_11_19.auth.routes import router as auth_router


# api_version_var: ContextVar[date] = ContextVar("api_version")


@asynccontextmanager
async def lifespan(_: FastAPI):

    yield


# app = HeaderRoutingFastAPI(
#    lifespan=lifespan,
#    api_version_header_name="X-API-Version",
#    api_version_var=api_version_var,
# )


# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
# )

# app.add_header_versioned_routers(
#    product_router,
#    header_value="2024-11-19",
# )

# app.add_unversioned_routers(
#    product_router,
# )
app = FastAPI(lifespan=lifespan)


app.include_router(
    product_router,
)
