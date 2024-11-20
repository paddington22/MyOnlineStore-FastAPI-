from contextlib import asynccontextmanager

from verselect import HeaderRoutingFastAPI

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan():
    yield


app = HeaderRoutingFastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_header_versioned_routers(
    header_value="2024-11-19",
)
