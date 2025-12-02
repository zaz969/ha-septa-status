from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class SeptaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self) -> None:
        self._errors = {}

    async def async_step_user(self) -> FlowResult:
        await self.async_set_unique_id("septa_status_listener")
        self._abort_if_unique_id_configured()

        return self.async_show_form(step_id='user', data_schema=vol.Schema({
            vol.Required("interval", default=30): int
        }))