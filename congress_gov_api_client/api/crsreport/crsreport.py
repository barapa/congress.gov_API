from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/crsreport",
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
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Returns Congressional Research Service (CRS) report data from the API

     GET /crsreport

    **Example Request**

    https://api.congress.gov/v3/crsreport?api_key=[INSERT_KEY]

    **Example Response**

          {
              \"CRSReports\": [
                 {
                      \"contentType\": \"Reports\",
                      \"id\": \"R43083\",
                      \"publishDate\": \"2025-02-05T11:34:25Z\",
                      \"status\": \"Active\",
                      \"title\": \"SBA Assistance to Small Business Startups: Client Experiences and
    Program Impact\",
                      \"updateDate\": \"2025-02-07T01:36:49Z\",
                      \"url\": \"http://api.congress.gov/v3/crsreport/R43083\",
                      \"version\": 145
                  },
                  {
                      \"contentType\": \"Reports\",
                      \"id\": \"98-202\",
                      \"publishDate\": \"2025-02-05T10:41:39Z\",
                      \"status\": \"Archived\",
                      \"title\": \"Appropriations for FY1999: Treasury, Postal Service, Executive Office
    of the President, and General Government\",
                      \"updateDate\": \"2025-02-05T10:41:39Z\",
                      \"url\": \"http://api1.test.congress.gov/v3/crsreport/98-202\",
                      \"version\": 102
                  }
               ]
           }

    Args:
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
        format_=format_,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Returns Congressional Research Service (CRS) report data from the API

     GET /crsreport

    **Example Request**

    https://api.congress.gov/v3/crsreport?api_key=[INSERT_KEY]

    **Example Response**

          {
              \"CRSReports\": [
                 {
                      \"contentType\": \"Reports\",
                      \"id\": \"R43083\",
                      \"publishDate\": \"2025-02-05T11:34:25Z\",
                      \"status\": \"Active\",
                      \"title\": \"SBA Assistance to Small Business Startups: Client Experiences and
    Program Impact\",
                      \"updateDate\": \"2025-02-07T01:36:49Z\",
                      \"url\": \"http://api.congress.gov/v3/crsreport/R43083\",
                      \"version\": 145
                  },
                  {
                      \"contentType\": \"Reports\",
                      \"id\": \"98-202\",
                      \"publishDate\": \"2025-02-05T10:41:39Z\",
                      \"status\": \"Archived\",
                      \"title\": \"Appropriations for FY1999: Treasury, Postal Service, Executive Office
    of the President, and General Government\",
                      \"updateDate\": \"2025-02-05T10:41:39Z\",
                      \"url\": \"http://api1.test.congress.gov/v3/crsreport/98-202\",
                      \"version\": 102
                  }
               ]
           }

    Args:
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
        format_=format_,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
