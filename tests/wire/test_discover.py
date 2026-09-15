from .conftest import get_client, verify_request_count


def test_discover_list_sources() -> None:
    """Test listSources endpoint with WireMock"""
    test_id = "discover.list_sources.0"
    client = get_client(test_id)
    client.discover.list_sources()
    verify_request_count(test_id, "GET", "/v1/discover/sources", None, 1)


def test_discover_list_entity_types() -> None:
    """Test listEntityTypes endpoint with WireMock"""
    test_id = "discover.list_entity_types.0"
    client = get_client(test_id)
    client.discover.list_entity_types()
    verify_request_count(test_id, "GET", "/v1/discover/entity-types", None, 1)


def test_discover_list_entities() -> None:
    """Test listEntities endpoint with WireMock"""
    test_id = "discover.list_entities.0"
    client = get_client(test_id)
    client.discover.list_entities(
        entity_type="entity_type",
    )
    verify_request_count(test_id, "GET", "/v1/discover/entities/entity_type", None, 1)


def test_discover_get_event_schema() -> None:
    """Test getEventSchema endpoint with WireMock"""
    test_id = "discover.get_event_schema.0"
    client = get_client(test_id)
    client.discover.get_event_schema(
        source="source",
        event_type="event_type",
    )
    verify_request_count(test_id, "GET", "/v1/discover/schema/source/event_type", None, 1)
