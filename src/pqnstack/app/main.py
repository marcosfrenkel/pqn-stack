import logging
from typing import Generator, Annotated

import httpx
from fastapi import Depends
from fastapi import FastAPI
from fastapi import status

logger = logging.getLogger(__name__)

app = FastAPI()



async def get_http_client() -> Generator[httpx.AsyncClient]:
    async with httpx.AsyncClient() as client:
        yield client


ClientDep = Annotated[httpx.AsyncClient, Depends(get_http_client)]


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/chsh")
async def chsh(basis: tuple[float, float],
               other_node_address: str,
               http_client: ClientDep):

    logger.debug("Starting CHSH")

    r = await http_client.get(f"{other_node_address}/chsh/request_follower")
    if r.status_code != 200:
        logger.error(f"Failed to request follower: {r.text}")
        return {"error": "Failed to request follower"}

    logger.debug(f"seem to be working yippee")




# TODO: Remove hardcoded basis
@app.get("/chsh/request_follower")
async def requesting_follower(status_code=status.HTTP_200_OK):
    logger.debug("request follower received.")

    logger.debug(f"setting basis locally to 25")









