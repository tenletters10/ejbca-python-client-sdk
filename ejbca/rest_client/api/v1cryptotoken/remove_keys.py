# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    cryptotoken_name: str,
    key_pair_alias: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/cryptotoken/{cryptotoken_name}/{key_pair_alias}/removekeys".format(
        client.base_url, cryptotoken_name=cryptotoken_name, key_pair_alias=key_pair_alias
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
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
        parsed=EmptyResponse(),
    )


class EmptyResponse:
  def to_dict(self):
    return None
def sync(
    cryptotoken_name: str,
    key_pair_alias: str,
    *,
    client: Client,
) -> Response[Any]:
    """Remove keys

     Remove a key pair given crypto token name and key pair alias to be removed.

    Args:
        cryptotoken_name (str):
        key_pair_alias (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cryptotoken_name=cryptotoken_name,
        key_pair_alias=key_pair_alias,
        client=client,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio_detailed(
    cryptotoken_name: str,
    key_pair_alias: str,
    *,
    client: Client,
) -> Response[Any]:
    """Remove keys

     Remove a key pair given crypto token name and key pair alias to be removed.

    Args:
        cryptotoken_name (str):
        key_pair_alias (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cryptotoken_name=cryptotoken_name,
        key_pair_alias=key_pair_alias,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response).parsed
