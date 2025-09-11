from collections.abc import AsyncGenerator
from typing import Annotated

import httpx
from fastapi import Depends

from pqnstack.app.core.config import settings
from pqnstack.app.core.config import CoordinationState
from pqnstack.network.client import Client
from pqnstack.app.core.config import state


async def get_http_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(timeout=60) as client:
        yield client


ClientDep = Annotated[httpx.AsyncClient, Depends(get_http_client)]


async def get_instrument_client() -> AsyncGenerator[Client, None]:
    async with Client(host=settings.router_address, port=settings.router_port) as client:
        yield client


InstrumentClientDep = Annotated[httpx.AsyncClient, Depends(get_instrument_client)]


async def get_coordination_state() -> AsyncGenerator[CoordinationState, None]:
    yield state.coordination_state


CoordinationStateDep = Annotated[CoordinationState, Depends(get_coordination_state)]

