from .conftest import get_client, verify_request_count


def test_sdk_identify_user() -> None:
    """Test identifyUser endpoint with WireMock"""
    test_id = "sdk.identify_user.0"
    client = get_client(test_id)
    client.sdk.identify_user(
        user_id="user_id",
    )
    verify_request_count(test_id, "POST", "/v1/users/identify", None, 1)


def test_sdk_track_signals() -> None:
    """Test trackSignals endpoint with WireMock"""
    test_id = "sdk.track_signals.0"
    client = get_client(test_id)
    client.sdk.track_signals()
    verify_request_count(test_id, "POST", "/v1/signals/track", None, 1)


def test_sdk_track_traces() -> None:
    """Test trackTraces endpoint with WireMock"""
    test_id = "sdk.track_traces.0"
    client = get_client(test_id)
    client.sdk.track_traces()
    verify_request_count(test_id, "POST", "/v1/traces/track", None, 1)
