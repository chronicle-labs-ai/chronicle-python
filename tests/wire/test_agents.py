import datetime

from .conftest import get_client, verify_request_count

from chroniclelabs.agents import (
    RecordAgentRunsRequestRunsItem,
    RecordAgentRunsRequestRunsItemToolCallsItem,
    RegisterAgentArtifactRequestArtifact,
    RegisterAgentArtifactRequestArtifactModel,
    RegisterAgentArtifactRequestArtifactProvenance,
    RegisterAgentArtifactRequestArtifactToolsItem,
)


def test_agents_list_agents() -> None:
    """Test listAgents endpoint with WireMock"""
    test_id = "agents.list_agents.0"
    client = get_client(test_id)
    client.agents.list_agents()
    verify_request_count(test_id, "GET", "/v1/agents", None, 1)


def test_agents_search_agent_hash_index() -> None:
    """Test searchAgentHashIndex endpoint with WireMock"""
    test_id = "agents.search_agent_hash_index.0"
    client = get_client(test_id)
    client.agents.search_agent_hash_index()
    verify_request_count(test_id, "GET", "/v1/agents/hash-index", None, 1)


def test_agents_subscribe_to_agent_changes() -> None:
    """Test subscribeToAgentChanges endpoint with WireMock"""
    test_id = "agents.subscribe_to_agent_changes.0"
    client = get_client(test_id)
    for _ in client.agents.subscribe_to_agent_changes():
        pass
    verify_request_count(test_id, "GET", "/v1/agents/subscribe", None, 1)


def test_agents_update_agent() -> None:
    """Test updateAgent endpoint with WireMock"""
    test_id = "agents.update_agent.0"
    client = get_client(test_id)
    client.agents.update_agent(
        name="name",
    )
    verify_request_count(test_id, "PATCH", "/v1/agents/name", None, 1)


def test_agents_get_agent_snapshot() -> None:
    """Test getAgentSnapshot endpoint with WireMock"""
    test_id = "agents.get_agent_snapshot.0"
    client = get_client(test_id)
    client.agents.get_agent_snapshot(
        name="name",
    )
    verify_request_count(test_id, "GET", "/v1/agents/name/snapshot", None, 1)


def test_agents_pin_latest_agent_version() -> None:
    """Test pinLatestAgentVersion endpoint with WireMock"""
    test_id = "agents.pin_latest_agent_version.0"
    client = get_client(test_id)
    client.agents.pin_latest_agent_version(
        name="name",
    )
    verify_request_count(test_id, "POST", "/v1/agents/name/pin-latest", None, 1)


def test_agents_create_agent_chat_session() -> None:
    """Test createAgentChatSession endpoint with WireMock"""
    test_id = "agents.create_agent_chat_session.0"
    client = get_client(test_id)
    client.agents.create_agent_chat_session(
        name="name",
    )
    verify_request_count(test_id, "POST", "/v1/agents/name/chat/sessions", None, 1)


def test_agents_get_agent_chat_session() -> None:
    """Test getAgentChatSession endpoint with WireMock"""
    test_id = "agents.get_agent_chat_session.0"
    client = get_client(test_id)
    client.agents.get_agent_chat_session(
        name="name",
        session_id="session_id",
    )
    verify_request_count(test_id, "GET", "/v1/agents/name/chat/sessions/session_id", None, 1)


def test_agents_send_agent_chat_message() -> None:
    """Test sendAgentChatMessage endpoint with WireMock"""
    test_id = "agents.send_agent_chat_message.0"
    client = get_client(test_id)
    client.agents.send_agent_chat_message(
        name="name",
        session_id="session_id",
        text="text",
    )
    verify_request_count(test_id, "POST", "/v1/agents/name/chat/sessions/session_id/messages", None, 1)


def test_agents_register_agent_artifact() -> None:
    """Test registerAgentArtifact endpoint with WireMock"""
    test_id = "agents.register_agent_artifact.0"
    client = get_client(test_id)
    client.agents.register_agent_artifact(
        artifact=RegisterAgentArtifactRequestArtifact(
            artifact_id="artifactId",
            config_hash="configHash",
            framework="vercel-ai-sdk",
            model=RegisterAgentArtifactRequestArtifactModel(
                label="label",
            ),
            name="name",
            provenance=RegisterAgentArtifactRequestArtifactProvenance(
                created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            ),
            schema_version="schemaVersion",
            tools=[
                RegisterAgentArtifactRequestArtifactToolsItem(
                    name="name",
                )
            ],
            version="version",
        ),
    )
    verify_request_count(test_id, "POST", "/v1/agents/register", None, 1)


def test_agents_record_agent_runs() -> None:
    """Test recordAgentRuns endpoint with WireMock"""
    test_id = "agents.record_agent_runs.0"
    client = get_client(test_id)
    client.agents.record_agent_runs(
        runs=[
            RecordAgentRunsRequestRunsItem(
                artifact_id="artifactId",
                config_hash="configHash",
                operation="generate",
                run_id="runId",
                schema_version="schemaVersion",
                started_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                status="started",
                tool_calls=[
                    RecordAgentRunsRequestRunsItemToolCallsItem(
                        call_id="callId",
                        started_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                        status="started",
                        tool_name="toolName",
                    )
                ],
            )
        ],
    )
    verify_request_count(test_id, "POST", "/v1/agents/runs/batch", None, 1)
