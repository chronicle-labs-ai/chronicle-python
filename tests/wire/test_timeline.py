from .conftest import get_client, verify_request_count


def test_timeline_get_timeline() -> None:
    """Test getTimeline endpoint with WireMock"""
    test_id = "timeline.get_timeline.0"
    client = get_client(test_id)
    client.timeline.get_timeline(
        entity_type="entity_type",
        entity_id="entity_id",
    )
    verify_request_count(test_id, "GET", "/v1/timeline/entity_type/entity_id", None, 1)
