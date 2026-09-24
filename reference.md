# Reference
## events
<details><summary><code>client.events.<a href="src/chroniclelabs/events/client.py">query_events</a>(...) -> EventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. Results are scoped to the tenant of the API key and ordered newest first by event time and event ID. Pass the opaque `next_cursor` as `cursor` to continue without an offset scan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.events.query_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Values above 200 are clamped to 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Relative time window, for example last_7d.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/chroniclelabs/events/client.py">ingest_event</a>(...) -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
import datetime

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.events.ingest_event(
    source="support-agent",
    topic="conversations",
    event_type="message.sent",
    entities={
        "user": "usr_123"
    },
    payload={"role": "assistant", "content": "Your refund is approved."},
    timestamp=datetime.datetime.fromisoformat("2026-09-24T14:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `IngestRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/chroniclelabs/events/client.py">ingest_event_batch</a>(...) -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:write. Maximum 1000 events per batch; larger batches are rejected with 422. Request bodies over the size limit are rejected with 413. Each request consumes 10 rate-limit units.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle, IngestRequest
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.events.ingest_event_batch(
    request=[
        IngestRequest(
            source="my-agent",
            topic="conversations",
            event_type="message.sent",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.List[IngestRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/chroniclelabs/events/client.py">stream_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. A Server-Sent Events stream of events matching the optional filters, held open indefinitely.

Opening a stream consumes 5 rate-limit units.

Each message has `event: event` and a `data` field carrying one EventResult as JSON. A comment line arrives every 15 seconds so intermediaries do not close an idle connection.

Every message carries an opaque, stream-specific `id` backed by a monotonic per-tenant delivery sequence. It records ingestion order, independently of the source event's `event_time`. Record the last id you processed and do not parse or construct it.

When `Last-Event-ID` is present, the server first establishes the live subscription, replays matching stored events strictly after that position in ascending order, and then continues with live delivery. Events committed at the history-to-live boundary may be delivered more than once, so consumers should deduplicate by `event_id`. This provides at-least-once delivery across a reconnect without leaving a gap.

Replay is limited to 1000 matching events. An older position returns 409 before the stream opens. Slow consumers are disconnected when the bounded live buffer fills and should reconnect with their last processed id. Concurrent streams are limited per tenant and may return 429 with `Retry-After`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.events.stream_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Opaque id from the last SSE message the client processed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## timeline
<details><summary><code>client.timeline.<a href="src/chroniclelabs/timeline/client.py">get_timeline</a>(...) -> EventPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. Cursor paginated, newest first.

Pass `cursor` from `next_cursor` to read the following page, and stop when `has_more` is false. The cursor is opaque: it is a keyset over `(event_time, event_id)`, it is exclusive so a row cannot repeat across pages, and its encoding may change without notice. Do not parse or construct one.

`include_linked=true` selects a different read that also returns causally linked events. That read is not paginated: it returns one page with `has_more` false, and it cannot be combined with `limit` or `cursor`. `since` is only available on that read, because the paginated read has no time filter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.timeline.get_timeline(
    entity_type="entity_type",
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Values above the maximum are reduced to it, not rejected.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a previous response's next_cursor
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Relative time window, for example last_7d.
    
</dd>
</dl>

<dl>
<dd>

**include_linked:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## search
<details><summary><code>client.search.<a href="src/chroniclelabs/search/client.py">events</a>(...) -> EventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. The page size is capped at 200 and a cursor can advance through at most 1,000 relevance-ranked results. Each request consumes 5 rate-limit units.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.search.events(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned by the preceding search page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## discover
<details><summary><code>client.discover.<a href="src/chroniclelabs/discover/client.py">list_sources</a>() -> SourceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. Returns the complete source metadata set without pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.discover.list_sources()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.discover.<a href="src/chroniclelabs/discover/client.py">list_entity_types</a>() -> EntityTypeListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. Returns the complete entity-type metadata set without pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.discover.list_entity_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.discover.<a href="src/chroniclelabs/discover/client.py">list_entities</a>(...) -> EntityListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. Entities are ordered by event count and entity ID. The limit is capped at 200; pass `next_cursor` as `cursor`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.discover.list_entities(
    entity_type="entity_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Values above 200 are clamped to 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.discover.<a href="src/chroniclelabs/discover/client.py">get_event_schema</a>(...) -> SourceSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.discover.get_event_schema(
    source="source",
    event_type="event_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## links
<details><summary><code>client.links.<a href="src/chroniclelabs/links/client.py">add_entity_ref</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.links.add_entity_ref(
    event_id="event_id",
    entity_type="entity_type",
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/chroniclelabs/links/client.py">create_event_link</a>(...) -> CreateLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.links.create_event_link(
    source_event_id="source_event_id",
    target_event_id="target_event_id",
    link_type="link_type",
    confidence=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target_event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**confidence:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/chroniclelabs/links/client.py">link_entities</a>(...) -> LinkEntityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.links.link_entities(
    from_entity_type="from_entity_type",
    from_entity_id="from_entity_id",
    to_entity_type="to_entity_type",
    to_entity_id="to_entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from_entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to_entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to_entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.links.<a href="src/chroniclelabs/links/client.py">traverse_graph</a>(...) -> EventListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope events:read or events:write. The traversal is bounded by `max_depth`, is not cursor-paginated, and consumes 5 rate-limit units.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.links.traverse_graph(
    start_event_id="start_event_id",
    direction="outgoing",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**direction:** `GraphRequestDirection` 
    
</dd>
</dl>

<dl>
<dd>

**link_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**min_confidence:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sdk
<details><summary><code>client.sdk.<a href="src/chroniclelabs/sdk/client.py">identify_user</a>(...) -> AcceptedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope users:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.sdk.identify_user(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**traits:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sdk.<a href="src/chroniclelabs/sdk/client.py">track_signals</a>(...) -> AcceptedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope signals:write. Maximum 1000 signals per request; larger batches are rejected with 422. Each request consumes 10 rate-limit units.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.sdk.track_signals()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**signals:** `typing.Optional[typing.List[SignalRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sdk.<a href="src/chroniclelabs/sdk/client.py">track_traces</a>(...) -> AcceptedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope traces:write. Maximum 1000 traces or total spans per request; larger batches are rejected with 422. Each request consumes 10 rate-limit units.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.sdk.track_traces()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**traces:** `typing.Optional[typing.List[TraceRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## agents
<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">list_agents</a>() -> typing.List[AgentSummary]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.list_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">search_agent_hash_index</a>(...) -> typing.List[HashIndexEntry]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.search_agent_hash_index()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[str]` — Comma-separated hash domains.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">subscribe_to_agent_changes</a>() -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.subscribe_to_agent_changes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">update_agent</a>(...) -> AgentSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.update_agent(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">get_agent_snapshot</a>(...) -> typing.Optional[AgentSnapshot]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.get_agent_snapshot(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">pin_latest_agent_version</a>(...) -> AgentSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.pin_latest_agent_version(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">create_agent_chat_session</a>(...) -> CreateAgentChatSessionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.create_agent_chat_session(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">get_agent_chat_session</a>(...) -> AgentChatSession</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.get_agent_chat_session(
    name="name",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">send_agent_chat_message</a>(...) -> SendAgentChatMessageResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.agents.send_agent_chat_message(
    name="name",
    session_id="session_id",
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">register_agent_artifact</a>(...) -> AgentVersionSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope agents:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.agents import RegisterAgentArtifactRequestArtifact, RegisterAgentArtifactRequestArtifactModel, RegisterAgentArtifactRequestArtifactProvenance, RegisterAgentArtifactRequestArtifactToolsItem
import datetime

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artifact:** `RegisterAgentArtifactRequestArtifact` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[RegisterAgentArtifactRequestMetadata]` — Mutable, human-authored metadata attached to a logical Agent identity. Artifact configuration remains immutable inside `AgentRegistryVersionRecord`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[RegisterAgentArtifactRequestStatus]` — Defaults to `current`. Registering a new current version atomically demotes the previous current version to stable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/chroniclelabs/agents/client.py">record_agent_runs</a>(...) -> RecordAgentRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires scope agents:write.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.agents import RecordAgentRunsRequestRunsItem, RecordAgentRunsRequestRunsItemToolCallsItem
import datetime

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**runs:** `typing.List[RecordAgentRunsRequestRunsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## datasets
<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_datasets</a>(...) -> TaskSuitePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_datasets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">create_dataset</a>(...) -> TaskSuite</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.create_dataset(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[CreateTaskSuitePayloadPurpose]` — Intended use of a dataset — drives the colored badge on the picker and lets apps route additions to the right backend (eval suite, training set, replay corpus, manual review queue).
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">create_dataset_with_trace</a>(...) -> CreateTaskSuiteWithTraceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.datasets import CreateTaskSuiteWithTraceRequestDataset, CreateTaskSuiteWithTraceRequestTrace

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.create_dataset_with_trace(
    dataset=CreateTaskSuiteWithTraceRequestDataset(
        name="name",
    ),
    trace=CreateTaskSuiteWithTraceRequestTrace(
        trace_id="traceId",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset:** `CreateTaskSuiteWithTraceRequestDataset` 
    
</dd>
</dl>

<dl>
<dd>

**trace:** `CreateTaskSuiteWithTraceRequestTrace` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">get_dataset</a>(...) -> TaskSuiteDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.get_dataset(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">archive_dataset</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.archive_dataset(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cascade:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">update_dataset</a>(...) -> TaskSuite</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.update_dataset(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[TaskSuitePatchPurpose]` — Intended use of a dataset — drives the colored badge on the picker and lets apps route additions to the right backend (eval suite, training set, replay corpus, manual review queue).
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">get_dataset_snapshot</a>(...) -> TaskSuiteSnapshot</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.get_dataset_snapshot(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_traces</a>(...) -> TaskPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_traces(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">add_trace_to_dataset</a>(...) -> AddTaskFromTraceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.add_trace_to_dataset(
    dataset_id="dataset_id",
    trace_id="traceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**event_ids:** `typing.Optional[typing.List[str]]` — Accepted for compatibility but never trusted as the authoritative capture. The service re-reads the canonical store by subject.
    
</dd>
</dl>

<dl>
<dd>

**add_task_from_trace_request_idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**split:** `typing.Optional[AddTaskFromTraceRequestSplit]` — Train / validation / test split assignment.
    
</dd>
</dl>

<dl>
<dd>

**task:** `typing.Optional[AddTaskFromTraceRequestTask]` — Optional task fields. Anything left unset is derived from the captured trace (title from the label, instruction from the first message, expected outcome from the events after the cutoff).
    
</dd>
</dl>

<dl>
<dd>

**trace_synthesized:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**verifiers:** `typing.Optional[typing.List[AddTaskFromTraceRequestVerifiersItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">update_dataset_traces</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.datasets import UpdateTracesRequestPatch

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.update_dataset_traces(
    dataset_id="dataset_id",
    patch=UpdateTracesRequestPatch(),
    trace_ids=[
        "traceIds"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**patch:** `UpdateTracesRequestPatch` — Patch to apply to one or more memberships. Nullable annotations preserve the same three states as [`PatchField`]: explicit JSON `null` clears while omission is a no-op.
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">remove_trace_from_dataset</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.remove_trace_from_dataset(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">refresh_dataset_trace</a>(...) -> TaskMembership</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.refresh_dataset_trace(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RefreshMembershipRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_trace_events</a>(...) -> TaskEventPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_trace_events(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_trace_dataset_memberships</a>(...) -> typing.List[TaskMembership]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_trace_dataset_memberships(
    trace_id="trace_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_tasks</a>(...) -> TaskPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_tasks(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">create_dataset_task</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.create_dataset_task(
    dataset_id="dataset_id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateTaskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">get_dataset_task</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.get_dataset_task(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">delete_dataset_task</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.delete_dataset_task(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">update_dataset_task</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.update_dataset_task(
    dataset_id="dataset_id",
    membership_id="membership_id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateTaskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">set_dataset_task_verifiers</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.datasets import SetTaskVerifiersRequestVerifiersItem

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.set_dataset_task_verifiers(
    dataset_id="dataset_id",
    membership_id="membership_id",
    verifiers=[
        SetTaskVerifiersRequestVerifiersItem(
            scorer_id="scorerId",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**verifiers:** `typing.List[SetTaskVerifiersRequestVerifiersItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_task_events</a>(...) -> TaskEventPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_task_events(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">refresh_dataset_task</a>(...) -> TaskMembership</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.refresh_dataset_task(
    dataset_id="dataset_id",
    membership_id="membership_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RefreshMembershipRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_clusters</a>(...) -> typing.List[DatasetCluster]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_clusters(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">create_dataset_cluster</a>(...) -> DatasetCluster</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.create_dataset_cluster(
    dataset_id="dataset_id",
    color="color",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**create_cluster_request_idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**similarity_center:** `typing.Optional[typing.List[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">delete_dataset_cluster</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.delete_dataset_cluster(
    dataset_id="dataset_id",
    cluster_id="cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">update_dataset_cluster</a>(...) -> DatasetCluster</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.update_dataset_cluster(
    dataset_id="dataset_id",
    cluster_id="cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**similarity_center:** `typing.Optional[typing.List[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_saved_views</a>(...) -> typing.List[DatasetSavedView]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_saved_views(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">create_dataset_saved_view</a>(...) -> DatasetSavedView</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.datasets import CreateSavedViewRequestState

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.create_dataset_saved_view(
    dataset_id="dataset_id",
    name="name",
    scope="personal",
    state=CreateSavedViewRequestState(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `CreateSavedViewRequestScope` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `CreateSavedViewRequestState` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**create_saved_view_request_idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schema_version:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**shortcut:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">delete_dataset_saved_view</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.delete_dataset_saved_view(
    dataset_id="dataset_id",
    view_id="view_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**view_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">update_dataset_saved_view</a>(...) -> DatasetSavedView</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.update_dataset_saved_view(
    dataset_id="dataset_id",
    view_id="view_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**view_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[DatasetSavedViewPatchScope]` 
    
</dd>
</dl>

<dl>
<dd>

**shortcut:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[DatasetSavedViewPatchState]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_versions</a>(...) -> typing.List[TaskSuiteVersion]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_versions(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">publish_dataset_version</a>(...) -> TaskSuiteVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.publish_dataset_version(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**publish_version_request_idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">get_dataset_version</a>(...) -> TaskSuiteSnapshot</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.get_dataset_version(
    dataset_id="dataset_id",
    version_id="version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/chroniclelabs/datasets/client.py">list_dataset_evaluation_runs</a>(...) -> typing.List[TaskSuiteEvalRun]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.datasets.list_dataset_evaluation_runs(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## environments
<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">list_environments</a>() -> ListEnvironmentsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.list_environments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">create_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.create_environment(
    slug="support-sandbox",
    label="Support sandbox",
    description="Isolated environment for support-agent backtests.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">get_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.get_environment(
    environment_id="environment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — Environment ID or slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">list_environment_versions</a>(...) -> typing.List[EnvironmentVersionRecord]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.list_environment_versions(
    environment_id="environment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — Environment ID or slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">create_environment_version</a>(...) -> EnvironmentVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.create_environment_version(
    environment_id="environment_id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — Environment ID or slug.
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**spec:** `typing.Optional[EnvironmentSpec]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[EnvironmentVersionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">get_environment_version</a>(...) -> EnvironmentVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.get_environment_version(
    environment_id="environment_id",
    version_selector="version_selector",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — Environment ID or slug.
    
</dd>
</dl>

<dl>
<dd>

**version_selector:** `str` — Environment-version ID or version label.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/chroniclelabs/environments/client.py">compile_environment_version</a>(...) -> CompileEnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.environments.compile_environment_version(
    environment_id="environment_id",
    version_selector="version_selector",
    dataset_snapshot_id="datasetSnapshotId",
    scenario_id="scenarioId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — Environment ID or slug.
    
</dd>
</dl>

<dl>
<dd>

**version_selector:** `str` — Environment-version ID or version label.
    
</dd>
</dl>

<dl>
<dd>

**dataset_snapshot_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scenario_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## backtests
<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">get_backtests_availability</a>() -> BacktestsAvailability</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.get_backtests_availability()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">list_backtest_jobs</a>(...) -> ListBacktestJobsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.list_backtest_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Deprecated compatibility input. Pass the opaque `cursor` instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">create_backtest_job</a>(...) -> CreateBacktestJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns 202 after the durable job and its trials have been admitted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment
from chroniclelabs.backtests import CreateBacktestJobRequestRecipe, CreateBacktestJobRequestRecipeAgentsItem, CreateBacktestJobRequestRecipeData, CreateBacktestJobRequestRecipeDataScenariosItem, CreateBacktestJobRequestRecipeDataSourcesItem, CreateBacktestJobRequestRecipeGradersItem

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.create_backtest_job(
    name="name",
    recipe=CreateBacktestJobRequestRecipe(
        agents=[
            CreateBacktestJobRequestRecipeAgentsItem(
                hue="hue",
                id="id",
                label="label",
                notes="notes",
            )
        ],
        data=CreateBacktestJobRequestRecipeData(
            kind="composed",
            scenarios=[
                CreateBacktestJobRequestRecipeDataScenariosItem(
                    count=1,
                    id="id",
                    kind="adversarial",
                    label="label",
                )
            ],
            sources=[
                CreateBacktestJobRequestRecipeDataSourcesItem(
                    count=1,
                    id="id",
                    kind="prod",
                    label="label",
                )
            ],
        ),
        graders=[
            CreateBacktestJobRequestRecipeGradersItem(
                id="id",
                kind="rubric",
                label="label",
                source="proposed",
                weight="low",
            )
        ],
        mode="replay",
        name="name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recipe:** `CreateBacktestJobRequestRecipe` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Optional caller-generated key for safely retrying a mutation after an ambiguous network failure. Keys are scoped to the authenticated tenant and operation. Reusing a key with the same payload returns the original successful result; reusing it with a different payload returns 409.
    
</dd>
</dl>

<dl>
<dd>

**cases:** `typing.Optional[typing.List[CreateBacktestJobRequestCasesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**evaluator_profile_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**n_concurrent:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">get_backtest_job</a>(...) -> BacktestJobDetailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.get_backtest_job(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">list_backtest_job_trials</a>(...) -> ListBacktestJobTrialsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.list_backtest_job_trials(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque position returned as `next_cursor` by the preceding page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Deprecated compatibility input. Pass the opaque `cursor` instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">get_backtest_trial</a>(...) -> BacktestTrialDetailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.get_backtest_trial(
    job_id="job_id",
    trial_id="trial_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trial_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">cancel_backtest_job</a>(...) -> CancelBacktestJobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.cancel_backtest_job(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.backtests.<a href="src/chroniclelabs/backtests/client.py">stream_backtest_job_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.backtests.stream_backtest_job_events(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## credentials
<details><summary><code>client.credentials.<a href="src/chroniclelabs/credentials/client.py">list_sdk_keys</a>() -> SdkKeyListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.credentials.list_sdk_keys()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/chroniclelabs/credentials/client.py">create_sdk_key</a>(...) -> CreatedSdkKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The bearer secret is returned once and is not stored in plaintext.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.credentials.create_sdk_key(
    name="name",
    scopes=[
        "traces:write"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.List[CreateSdkKeyRequestScopesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/chroniclelabs/credentials/client.py">revoke_sdk_key</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from chroniclelabs import Chronicle
from chroniclelabs.environment import ChronicleEnvironment

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.credentials.revoke_sdk_key(
    key_id="key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

