from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.get_paginated_machines_response_200 import GetPaginatedMachinesResponse200
from ...types import Response


def _get_kwargs(
    page: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/machines/paginated/{page}".format(client.base_url, page=page)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetPaginatedMachinesResponse200]:
    if response.status_code == 200:
        response_200 = GetPaginatedMachinesResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetPaginatedMachinesResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    page: int,
    *,
    client: AuthenticatedClient,
) -> Response[GetPaginatedMachinesResponse200]:
    """Get all machines paginated of which the user has access to.

    Args:
        page (int):

    Returns:
        Response[GetPaginatedMachinesResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    page: int,
    *,
    client: AuthenticatedClient,
) -> Optional[GetPaginatedMachinesResponse200]:
    """Get all machines paginated of which the user has access to.

    Args:
        page (int):

    Returns:
        Response[GetPaginatedMachinesResponse200]
    """

    return sync_detailed(
        page=page,
        client=client,
    ).parsed


async def asyncio_detailed(
    page: int,
    *,
    client: AuthenticatedClient,
) -> Response[GetPaginatedMachinesResponse200]:
    """Get all machines paginated of which the user has access to.

    Args:
        page (int):

    Returns:
        Response[GetPaginatedMachinesResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    page: int,
    *,
    client: AuthenticatedClient,
) -> Optional[GetPaginatedMachinesResponse200]:
    """Get all machines paginated of which the user has access to.

    Args:
        page (int):

    Returns:
        Response[GetPaginatedMachinesResponse200]
    """

    return (
        await asyncio_detailed(
            page=page,
            client=client,
        )
    ).parsed
