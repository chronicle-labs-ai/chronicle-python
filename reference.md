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

client = Chronicle(
    token="<token>",
    environment=ChronicleEnvironment.PRODUCTION,
)

client.events.ingest_event(
    source="my-agent",
    topic="conversations",
    event_type="message.sent",
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

