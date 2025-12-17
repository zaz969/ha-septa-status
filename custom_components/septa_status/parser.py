"""Parser for SEPTA alert data."""

import logging
_LOGGER = logging.getLogger(__name__)

def parse_septa_alerts(data: list[dict] | None) -> list[dict] | None:
    """Parse SEPTA alert data and extract relevant bus status information."""
    if data is None:
        return None
    for bus_route in data:
        _LOGGER.debug(f"Bus Route: {bus_route.get('route_id')}")
    return data
