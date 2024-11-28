from loguru import logger

from tools.add_logger import add_logger
from tools.explorer import get_aidogs_airdrop, post_reserve_aidogs
from tools.other_utils import read_file, get_proxied_session
from user_data.config import mobile_proxy, aidogs_ref_code

if __name__ == '__main__':
    add_logger(version='v1.0')
    try:
        addresses = read_file(path='user_data/address.txt')
        session = get_proxied_session(proxy=mobile_proxy)
        for index, address in enumerate(addresses, start=1):
            try:
                airdrop = get_aidogs_airdrop(index=index, address=address, ref_code=aidogs_ref_code, session=session)
                if airdrop.data.eligible:
                    logger.success(f"{index} | {address}: eligible.")
                    if not airdrop.data.reserved:
                        reserve = post_reserve_aidogs(index=index, address=address, session=session)
                        if reserve.data.reserved:
                            logger.success(f"{index} | {address}: reserved {reserve.data.totalAllocated} $AIDOGS.")
                    else:
                        logger.success(f"{index} | {address}: reserved {airdrop.data.totalAllocated} $AIDOGS.")
                else:
                    logger.info(f"{index} | {address}: not eligible.")
            except Exception as e:
                logger.exception(e)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        logger.exception(e)
