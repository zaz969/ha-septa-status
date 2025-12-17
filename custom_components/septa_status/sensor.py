"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SeptaStatusCoordinator

import logging
_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform from a config entry."""
    coordinator: SeptaStatusCoordinator = hass.data[DOMAIN][config_entry.entry_id].coordinator

    # Create 5 bus status entities and 5 delayed status entities
    entities = []
    for bus in coordinator.data.buses:
        entities.append(BusStatusSensor(coordinator, bus.bus_id))
        entities.append(BusDelayedSensor(coordinator, bus.bus_id))

    async_add_entities(entities)


class BusStatusSensor(CoordinatorEntity, SensorEntity):
    """Sensor for displaying bus status message."""

    def __init__(self, coordinator: SeptaStatusCoordinator, bus_id: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.bus_id = bus_id
        self._attr_unique_id = f"septa_bus_{bus_id}_status"
        self._attr_name = f"Bus {bus_id} Status"

    @property
    def native_value(self) -> str:
        """Return the current bus status message."""
        for bus in self.coordinator.data.buses:
            if bus.bus_id == self.bus_id:
                return bus.status_message
        return "Unknown"


class BusDelayedSensor(CoordinatorEntity, SensorEntity):
    """Sensor for displaying bus delayed status."""

    def __init__(self, coordinator: SeptaStatusCoordinator, bus_id: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.bus_id = bus_id
        self._attr_unique_id = f"septa_bus_{bus_id}_delayed"
        self._attr_name = f"Bus {bus_id} Delayed"

    @property
    def native_value(self) -> str:
        """Return the bus delayed status (Yes/No)."""
        for bus in self.coordinator.data.buses:
            if bus.bus_id == self.bus_id:
                return "Yes" if bus.is_delayed else "No"
        return "Unknown"
