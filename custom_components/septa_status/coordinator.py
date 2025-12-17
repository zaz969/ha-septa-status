from dataclasses import dataclass, field
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, NUM_BUSES

import logging
_LOGGER = logging.getLogger(__name__)

@dataclass
class BusStatus:
    """Class to hold individual bus status data"""

    bus_id: int
    status_message: str = "Unknown"
    is_delayed: bool = False

@dataclass
class SeptaStatusData:
    """Class to hold api data"""

    buses: list[BusStatus] = field(default_factory=lambda: [
        BusStatus(bus_id=i+1) for i in range(NUM_BUSES)
    ])

class SeptaStatusCoordinator(DataUpdateCoordinator):
    data: SeptaStatusData

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:

        self.poll_interval = config_entry.data["interval"]

        # Initialise DataUpdateCoordinator
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN} ({config_entry.unique_id})",
            update_method=self._async_update_data,
            update_interval=timedelta(minutes=self.poll_interval)
        )
        # Initialize with default data
        self.data = SeptaStatusData()

    async def _async_update_data(self) -> SeptaStatusData:
        """Fetch data from the SEPTA API.
        
        This is where you'll call your API to get the actual bus statuses.
        For now, it returns the default data structure.
        """
        # TODO: Replace with actual API call to fetch bus statuses
        # Example:
        # data = await self._fetch_from_api()
        # self.data.buses = parse_api_response(data)
        # return self.data
        
        return self.data
