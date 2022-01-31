from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    organisation_id: int,
    location_id: int,
    machine_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/organisations/details/{organisationId}/location/{locationId}/machine/{machineId}".format(
        client.base_url, organisationId=organisation_id, locationId=location_id, machineId=machine_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    organisation_id: int,
    location_id: int,
    machine_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get machine details.

    Args:
        organisation_id (int):
        location_id (int):
        machine_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organisation_id=organisation_id,
        location_id=location_id,
        machine_id=machine_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    organisation_id: int,
    location_id: int,
    machine_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get machine details.

    Args:
        organisation_id (int):
        location_id (int):
        machine_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organisation_id=organisation_id,
        location_id=location_id,
        machine_id=machine_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
