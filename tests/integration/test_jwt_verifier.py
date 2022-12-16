import os
import pytest

import cachecontrol
import cachecontrol.cache

from okta_jwt_verifier import BaseJWTVerifier
from okta_jwt_verifier.request_executor import RequestExecutor

from tests.conftest import is_env_set


@pytest.mark.skipif(not is_env_set(),
                    reason='Set env variables for integration tests')
@pytest.mark.asyncio
def test_verify_access_token():
    issuer = os.environ.get('ISSUER')
    client_id = os.environ.get('CLIENT_ID')
    token = os.environ.get('OKTA_ACCESS_TOKEN')
    jwt_verifier = BaseJWTVerifier(issuer, client_id)
    jwt_verifier.verify_access_token(token)


@pytest.mark.skipif(not is_env_set(),
                    reason='Set env variables for integration tests')
@pytest.mark.asyncio
def test_verify_id_token():
    issuer = os.environ.get('ISSUER')
    client_id = os.environ.get('CLIENT_ID')
    token = os.environ.get('OKTA_ID_TOKEN')
    nonce = os.environ.get('NONCE')
    jwt_verifier = BaseJWTVerifier(issuer, client_id)
    jwt_verifier.verify_id_token(token, nonce=nonce)


@pytest.mark.skipif(not is_env_set(),
                    reason='Set env variables for integration tests')
@pytest.mark.asyncio
def test_clear_requests_cache():
    cache_controller = cachecontrol.cache.DictCache()

    class MockRequestExecutor(RequestExecutor):
        def __init__(self, *args, **kwargs):
            super(MockRequestExecutor, self).__init__(*args, cache_controller=cache_controller, **kwargs)

    issuer = os.environ.get('ISSUER')
    client_id = os.environ.get('CLIENT_ID')
    jwt_verifier = BaseJWTVerifier(issuer, client_id,
                               request_executor=MockRequestExecutor)
    jwt_verifier.get_jwks()

    # verify cache_data is not empty
    assert cache_controller.data

    jwt_verifier._clear_requests_cache()

    # verify cache_data is empty
    assert not cache_controller.data
