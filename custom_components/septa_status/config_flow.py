from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN, MIN_TIME_BETWEEN_UPDATES, TITLE


class SeptaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self) -> None:
        self._errors = {}

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        await self.async_set_unique_id("septa_status_listener")
        self._abort_if_unique_id_configured()
        self._errors = {}

        if user_input is None:
            return self.async_show_form(step_id='user', data_schema=vol.Schema({
                vol.Required("interval", default=30): int
            }), errors=self._errors)
        else:
            valid = user_input is not None and user_input["interval"] >= MIN_TIME_BETWEEN_UPDATES
            if valid:
                return self.async_create_entry(title=TITLE, data=user_input)
            else: self._errors["base"] = "invalid_input"

            return self.async_show_form(step_id='user', data_schema=vol.Schema({
                vol.Required("interval", default=30): int
            }), errors=self._errors)
