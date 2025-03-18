from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chamber: str,
    committee_code: str,
    *,
    format_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["format"] = format_

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/committee/{chamber}/{committee_code}/house-communication",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 400:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chamber: str,
    committee_code: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Returns the list of House communications associated with a specified congressional committee.

     GET /committee/:chamber/:committeeCode/house-communication

    **Example Request**

    https://api.congress.gov/v3/committee/house/hspw00/house-communication?api_key=[INSERT_KEY]

    **Example Response**

        {
          \"houseCommunications\": [
                {
                    \"chamber\": \"House\",
                    \"communicationType\": {
                        \"code\": \"EC\",
                        \"name\": \"Executive Communication\"
                    },
                    \"congress\": 114,
                    \"number\": 3262,
                    \"referralDate\": \"2015-10-27\",
                    \"updateDate\": \"2018-02-02\",
                    \"url\": \"https://api.congress.gov/v3/house-communication/114/ec/3262?format=json\"
                },
                {
                    \"chamber\": \"House\",
                    \"communicationType\": {
                        \"code\": \"EC\",
                        \"name\": \"Executive Communication\"
                    },
                    \"congress\": 115,
                    \"number\": 3263,
                    \"referralDate\": \"2015-10-27\",
                    \"updateDate\": \"2018-02-02\",
                    \"url\": \"https://api.congress.gov/v3/house-communication/114/ec/3263?format=json\"
                },
            ]
        }

    Args:
        chamber (str):
        committee_code (str):
        format_ (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chamber=chamber,
        committee_code=committee_code,
        format_=format_,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chamber: str,
    committee_code: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Returns the list of House communications associated with a specified congressional committee.

     GET /committee/:chamber/:committeeCode/house-communication

    **Example Request**

    https://api.congress.gov/v3/committee/house/hspw00/house-communication?api_key=[INSERT_KEY]

    **Example Response**

        {
          \"houseCommunications\": [
                {
                    \"chamber\": \"House\",
                    \"communicationType\": {
                        \"code\": \"EC\",
                        \"name\": \"Executive Communication\"
                    },
                    \"congress\": 114,
                    \"number\": 3262,
                    \"referralDate\": \"2015-10-27\",
                    \"updateDate\": \"2018-02-02\",
                    \"url\": \"https://api.congress.gov/v3/house-communication/114/ec/3262?format=json\"
                },
                {
                    \"chamber\": \"House\",
                    \"communicationType\": {
                        \"code\": \"EC\",
                        \"name\": \"Executive Communication\"
                    },
                    \"congress\": 115,
                    \"number\": 3263,
                    \"referralDate\": \"2015-10-27\",
                    \"updateDate\": \"2018-02-02\",
                    \"url\": \"https://api.congress.gov/v3/house-communication/114/ec/3263?format=json\"
                },
            ]
        }

    Args:
        chamber (str):
        committee_code (str):
        format_ (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chamber=chamber,
        committee_code=committee_code,
        format_=format_,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
