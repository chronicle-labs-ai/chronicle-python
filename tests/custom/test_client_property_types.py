from typing_extensions import assert_type

from chroniclelabs import AsyncChronicle, Chronicle
from chroniclelabs.discover.client import AsyncDiscoverClient, DiscoverClient
from chroniclelabs.events.client import AsyncEventsClient, EventsClient
from chroniclelabs.links.client import AsyncLinksClient, LinksClient
from chroniclelabs.sdk.client import AsyncSdkClient, SdkClient
from chroniclelabs.search.client import AsyncSearchClient, SearchClient
from chroniclelabs.timeline.client import AsyncTimelineClient, TimelineClient


def check_sync_client_property_types(client: Chronicle) -> None:
    assert_type(client.events, EventsClient)
    assert_type(client.timeline, TimelineClient)
    assert_type(client.search, SearchClient)
    assert_type(client.discover, DiscoverClient)
    assert_type(client.links, LinksClient)
    assert_type(client.sdk, SdkClient)


def check_async_client_property_types(client: AsyncChronicle) -> None:
    assert_type(client.events, AsyncEventsClient)
    assert_type(client.timeline, AsyncTimelineClient)
    assert_type(client.search, AsyncSearchClient)
    assert_type(client.discover, AsyncDiscoverClient)
    assert_type(client.links, AsyncLinksClient)
    assert_type(client.sdk, AsyncSdkClient)
