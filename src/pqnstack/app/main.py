import logging
from typing import Generator, Annotated

import httpx
from fastapi import Depends
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = FastAPI()



async def get_http_client() -> Generator[httpx.AsyncClient]:
    async with httpx.AsyncClient() as client:
        yield client


ClientDep = Annotated[httpx.AsyncClient, Depends(get_http_client)]


class NodeState(BaseModel):
    waveplates_available: bool = False
    chsh_basis: list[float] = [0.0, 45.0]

state = NodeState()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/chsh")
async def chsh(basis: tuple[float, float],
               other_node_address: str,
               http_client: ClientDep):

    logger.debug("Starting CHSH")
    expectations = []
    for angle in basis:
        # measure ab, a'b, ab', a'b' for one expectation value
        counts = []
        for a in [angle, angle + 90]:
            # local_instruments.hwp.move_to(a)
            logger.info("moving waveplate", extra={"angle": a})

            for i in range(2):
                for perp in [False, True]:
                    r = await http_client.get(f"http://{other_node_address}/chsh/set_basis?i={i}&perp={perp}")
                    if r.status_code != 200:
                        logger.error(f"Failed to request follower: {r.text}")
                        return {"error": "Failed to request follower"}
                    # count = local_instruments.measure(measurement_config)
                    count = 1
                    logger.info(f"measuring counts, {count}")
                    counts.append(count)

        # expectation = compute_expectation(counts)
        expectation = sum(counts)
        expectations.append(expectation)

    # chsh_result = compute_chsh(expectations)
    chsh_result = sum(expectations)

    return chsh_result



@app.get("/chsh/set_basis")  # type: ignore[misc]
async def request_basis(i: int, perp: bool) -> bool:
    angle = state.chsh_basis[i] + 90 * perp
    logger.info("moving waveplate", extra={"angle": angle})
    return True







