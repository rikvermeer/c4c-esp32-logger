from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    x_api_key: str,
) -> Dict[str, Any]:
    url = "{}/machine-tokens".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-api-key"] = x_api_key

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
    *,
    client: Client,
    x_api_key: str,
) -> Response[Any]:
    """Home call to let the server know that the device exists and wants to connect. Requires the secret
    key.

    Args:
        x_api_key (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        x_api_key=x_api_key,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    x_api_key: str,
) -> Response[Any]:
    """Home call to let the server know that the device exists and wants to connect. Requires the secret
    key.

    Args:
        x_api_key (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        x_api_key=x_api_key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
