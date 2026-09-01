from .conftest import get_client, verify_request_count


def test_search_events() -> None:
    """Test events endpoint with WireMock"""
    test_id = "search.events.0"
    client = get_client(test_id)
    client.search.events(
        query="query",
    )
    verify_request_count(test_id, "POST", "/v1/search", None, 1)
