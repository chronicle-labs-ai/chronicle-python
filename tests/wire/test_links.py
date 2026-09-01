from .conftest import get_client, verify_request_count


def test_links_add_entity_ref() -> None:
    """Test addEntityRef endpoint with WireMock"""
    test_id = "links.add_entity_ref.0"
    client = get_client(test_id)
    client.links.add_entity_ref(
        event_id="event_id",
        entity_type="entity_type",
        entity_id="entity_id",
    )
    verify_request_count(test_id, "POST", "/v1/entity-refs", None, 1)


def test_links_create_event_link() -> None:
    """Test createEventLink endpoint with WireMock"""
    test_id = "links.create_event_link.0"
    client = get_client(test_id)
    client.links.create_event_link(
        source_event_id="source_event_id",
        target_event_id="target_event_id",
        link_type="link_type",
        confidence=1.1,
    )
    verify_request_count(test_id, "POST", "/v1/event-links", None, 1)


def test_links_link_entities() -> None:
    """Test linkEntities endpoint with WireMock"""
    test_id = "links.link_entities.0"
    client = get_client(test_id)
    client.links.link_entities(
        from_entity_type="from_entity_type",
        from_entity_id="from_entity_id",
        to_entity_type="to_entity_type",
        to_entity_id="to_entity_id",
    )
    verify_request_count(test_id, "POST", "/v1/link-entity", None, 1)


def test_links_traverse_graph() -> None:
    """Test traverseGraph endpoint with WireMock"""
    test_id = "links.traverse_graph.0"
    client = get_client(test_id)
    client.links.traverse_graph(
        start_event_id="start_event_id",
        direction="outgoing",
    )
    verify_request_count(test_id, "POST", "/v1/graph", None, 1)
