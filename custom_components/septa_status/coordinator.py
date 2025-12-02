from dataclasses import dataclass
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN

import logging
_LOGGER = logging.getLogger(__name__)

@dataclass
class SeptaStatusData:
    """Class to hold api data"""

    test: str | None = None

class SeptaStatusCoordinator(DataUpdateCoordinator):
    data: SeptaStatusData

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:

        self.poll_interval = config_entry.data["interval"]

        # Initialise DataUpdateCoordinator
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN} ({config_entry.unique_id})",
            # Set update method to get devices on first load.
            update_method=self._async_update_data,
            # Do not set a polling interval as data will be pushed.
            # You can remove this line but left here for explanatory purposes.
            update_interval=timedelta(minutes=self.poll_interval)
        )

    async def _async_update_data(self):
        return "{\"test\": \"blah\"}"
