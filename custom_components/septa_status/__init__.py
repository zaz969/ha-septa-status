from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.const import CONF_ADDRESS

from .const import DOMAIN

PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up Integration from a config entry."""

    hass.data.setdefault(DOMAIN, {})




async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # This is called when you remove your integration or shutdown HA.
    # If you have created any custom services, they need to be removed here too.

    # Remove the config options update listener
    hass.data[DOMAIN][config_entry.entry_id].cancel_update_listener()

    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(
        config_entry, PLATFORMS
    )

    # Remove the config entry from the hass data object.
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)

    # Return that unloading was successful.
    return unload_ok