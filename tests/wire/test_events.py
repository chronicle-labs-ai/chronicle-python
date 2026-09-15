from .conftest import get_client, verify_request_count

from chroniclelabs import IngestRequest


def test_events_query_events() -> None:
    """Test queryEvents endpoint with WireMock"""
    test_id = "events.query_events.0"
    client = get_client(test_id)
    client.events.query_events()
    verify_request_count(test_id, "GET", "/v1/events", None, 1)


def test_events_ingest_event() -> None:
    """Test ingestEvent endpoint with WireMock"""
    test_id = "events.ingest_event.0"
    client = get_client(test_id)
    client.events.ingest_event(
        source="my-agent",
        topic="conversations",
        event_type="message.sent",
    )
    verify_request_count(test_id, "POST", "/v1/events", None, 1)


def test_events_ingest_event_batch() -> None:
    """Test ingestEventBatch endpoint with WireMock"""
    test_id = "events.ingest_event_batch.0"
    client = get_client(test_id)
    client.events.ingest_event_batch(
        request=[
            IngestRequest(
                source="my-agent",
                topic="conversations",
                event_type="message.sent",
            )
        ],
    )
    verify_request_count(test_id, "POST", "/v1/events/batch", None, 1)


def test_events_stream_events() -> None:
    """Test streamEvents endpoint with WireMock"""
    test_id = "events.stream_events.0"
    client = get_client(test_id)
    for _ in client.events.stream_events():
        pass
    verify_request_count(test_id, "GET", "/v1/events/stream", None, 1)
