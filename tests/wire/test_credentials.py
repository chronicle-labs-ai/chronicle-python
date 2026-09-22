from .conftest import get_client, verify_request_count


def test_credentials_list_sdk_keys() -> None:
    """Test listSdkKeys endpoint with WireMock"""
    test_id = "credentials.list_sdk_keys.0"
    client = get_client(test_id)
    client.credentials.list_sdk_keys()
    verify_request_count(test_id, "GET", "/v1/sdk-keys", None, 1)


def test_credentials_create_sdk_key() -> None:
    """Test createSdkKey endpoint with WireMock"""
    test_id = "credentials.create_sdk_key.0"
    client = get_client(test_id)
    client.credentials.create_sdk_key(
        name="name",
        scopes=["traces:write"],
    )
    verify_request_count(test_id, "POST", "/v1/sdk-keys", None, 1)


def test_credentials_revoke_sdk_key() -> None:
    """Test revokeSdkKey endpoint with WireMock"""
    test_id = "credentials.revoke_sdk_key.0"
    client = get_client(test_id)
    client.credentials.revoke_sdk_key(
        key_id="key_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/sdk-keys/key_id", None, 1)
