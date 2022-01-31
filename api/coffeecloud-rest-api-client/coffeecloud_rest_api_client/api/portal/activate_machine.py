from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    machine_id: int,
    *,
    client: AuthenticatedClient,
    json_body: Any,
) -> Dict[str, Any]:
    url = "{}/machines/activate/{machineId}".format(client.base_url, machineId=machine_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient,
    json_body: Any,
) -> Response[Any]:
    """Sets organisation and location to machine which activates it for use.

    Args:
        machine_id (int):
        json_body (Any):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient,
    json_body: Any,
) -> Response[Any]:
    """Sets organisation and location to machine which activates it for use.

    Args:
        machine_id (int):
        json_body (Any):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)
