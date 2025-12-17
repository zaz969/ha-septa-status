from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import SEPTA_ALERT_API_URL

import logging
_LOGGER = logging.getLogger(__name__)

class SEPTAStatusAPI:
    """Class to interact with SEPTA API"""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the API with Home Assistant instance."""
        self.hass = hass

    async def fetch_bus_alerts(self) -> list[dict] | None:
        # Fetch bus alerts from SEPTA API.
        _LOGGER.debug("Fetching bus alerts from SEPTA API")

        session = async_get_clientsession(self.hass)

        try:
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
        

