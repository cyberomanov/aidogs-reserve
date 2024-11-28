import json

import requests
from loguru import logger

from datatypes.airdrop import AidogsAllocationResponse
from datatypes.reserve import AidogsReserveAirdropResponse
from tools.change_ip import execute_change_ip
from user_data.config import change_ip_url


def get_aidogs_airdrop(
        index: int,
        address: str,
        ref_code: str,
        session: requests.Session()
) -> AidogsAllocationResponse:
    change_ip = execute_change_ip(change_ip_url=change_ip_url)
    if change_ip:
        logger.info(f"{index} | {address} | ip has been changed.")

    url = f"https://kasongo.dawgsai.xyz/allocation?address={address}&referred_by={ref_code}"
    response = session.get(url=url)
    return AidogsAllocationResponse.parse_obj(json.loads(response.content))


def post_reserve_aidogs(
        index: int,
        address: str,
        session: requests.Session()
) -> AidogsReserveAirdropResponse:
    change_ip = execute_change_ip(change_ip_url=change_ip_url)
    if change_ip:
        logger.info(f"{index} | {address} | ip has been changed.")

    url = f"https://kasongo.dawgsai.xyz/allocation"
    data = {
        "address": address,
    }
    response = session.post(url=url, data=data)
    return AidogsReserveAirdropResponse.parse_obj(json.loads(response.content))
