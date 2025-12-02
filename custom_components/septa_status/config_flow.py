from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult


from .const import DOMAIN

class SeptaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1
    def __init__(self):
        self._errors = {}


    async def async_step_init(self) -> FlowResult:

        return self.async_show_form(step_id='init', data_schema=vol.Schema({
            vol.Required("interval", default=30): int
        }))

    async def async_step_finalize(self, user_input: dict[str, Any] | None = None):
        self._abort_if_unique_id_configured()
        await self.async_set_unique_id()

        if user_input is not None:
            return self.async_create_entry(title=DOMAIN, data={
                "interval": user_input["interval"]
            })
