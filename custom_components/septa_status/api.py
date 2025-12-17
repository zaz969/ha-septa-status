import aiohttp
from .const import SEPTA_ALERT_API_URL

import logging
_LOGGER = logging.getLogger(__name__)

class SEPTAStatusAPI:
    """Class to interact with SEPTA API"""

    async def fetch_bus_alerts(self) -> dict | None:
        # Fetch bus alerts from SEPTA API.
        _LOGGER.debug("Fetching bus alerts from SEPTA API")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(SEPTA_ALERT_API_URL) as response:
                    if response.status == 200:
                        data = await response.json()
                        _LOGGER.debug("Successfully fetched bus alerts")
                        return data
                    else:
                        _LOGGER.error(f"Error fetching bus alerts: {response.status}")
                        return None
        except Exception as e:
            _LOGGER.error(f"Exception during fetching bus alerts: {e}")
            return None
        

