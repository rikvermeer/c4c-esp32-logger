from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.search_paginated_location_machines_response_200 import SearchPaginatedLocationMachinesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organisation_id: int,
    query: str,
    page: int,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/organisations/details/{organisationId}/machines/search/{query}/{page}".format(
        client.base_url, organisationId=organisation_id, query=query, page=page
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "status": status,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SearchPaginatedLocationMachinesResponse200]:
    if response.status_code == 200:
        response_200 = SearchPaginatedLocationMachinesResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SearchPaginatedLocationMachinesResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organisation_id: int,
    query: str,
    page: int,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
) -> Response[SearchPaginatedLocationMachinesResponse200]:
    """Search machines by organisation.

    Args:
        organisation_id (int):
        query (str):
        page (int):
        status (Union[Unset, None, str]):

    Returns:
        Response[SearchPaginatedLocationMachinesResponse200]
    """

    kwargs = _get_kwargs(
        organisation_id=organisation_id,
        query=query,
        page=page,
        client=client,
        status=status,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organisation_id: int,
    query: str,
    page: int,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
) -> Optional[SearchPaginatedLocationMachinesResponse200]:
    """Search machines by organisation.

    Args:
        organisation_id (int):
        query (str):
        page (int):
        status (Union[Unset, None, str]):

    Returns:
        Response[SearchPaginatedLocationMachinesResponse200]
    """

    return sync_detailed(
        organisation_id=organisation_id,
        query=query,
        page=page,
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    organisation_id: int,
    query: str,
    page: int,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
) -> Response[SearchPaginatedLocationMachinesResponse200]:
    """Search machines by organisation.

    Args:
        organisation_id (int):
        query (str):
        page (int):
        status (Union[Unset, None, str]):

    Returns:
        Response[SearchPaginatedLocationMachinesResponse200]
    """

    kwargs = _get_kwargs(
        organisation_id=organisation_id,
        query=query,
        page=page,
        client=client,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organisation_id: int,
    query: str,
    page: int,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
) -> Optional[SearchPaginatedLocationMachinesResponse200]:
    """Search machines by organisation.

    Args:
        organisation_id (int):
        query (str):
        page (int):
        status (Union[Unset, None, str]):

    Returns:
        Response[SearchPaginatedLocationMachinesResponse200]
    """

    return (
        await asyncio_detailed(
            organisation_id=organisation_id,
            query=query,
            page=page,
            client=client,
            status=status,
        )
    ).parsed
