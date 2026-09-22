from .conftest import get_client, verify_request_count

from chroniclelabs.datasets import (
    CreateSavedViewRequestState,
    CreateTaskSuiteWithTraceRequestDataset,
    CreateTaskSuiteWithTraceRequestTrace,
    SetTaskVerifiersRequestVerifiersItem,
    UpdateTracesRequestPatch,
)


def test_datasets_list_datasets() -> None:
    """Test listDatasets endpoint with WireMock"""
    test_id = "datasets.list_datasets.0"
    client = get_client(test_id)
    client.datasets.list_datasets()
    verify_request_count(test_id, "GET", "/v1/task-suites", None, 1)


def test_datasets_create_dataset() -> None:
    """Test createDataset endpoint with WireMock"""
    test_id = "datasets.create_dataset.0"
    client = get_client(test_id)
    client.datasets.create_dataset(
        name="name",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites", None, 1)


def test_datasets_create_dataset_with_trace() -> None:
    """Test createDatasetWithTrace endpoint with WireMock"""
    test_id = "datasets.create_dataset_with_trace.0"
    client = get_client(test_id)
    client.datasets.create_dataset_with_trace(
        dataset=CreateTaskSuiteWithTraceRequestDataset(
            name="name",
        ),
        trace=CreateTaskSuiteWithTraceRequestTrace(
            trace_id="traceId",
        ),
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/with-trace", None, 1)


def test_datasets_get_dataset() -> None:
    """Test getDataset endpoint with WireMock"""
    test_id = "datasets.get_dataset.0"
    client = get_client(test_id)
    client.datasets.get_dataset(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id", None, 1)


def test_datasets_archive_dataset() -> None:
    """Test archiveDataset endpoint with WireMock"""
    test_id = "datasets.archive_dataset.0"
    client = get_client(test_id)
    client.datasets.archive_dataset(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/task-suites/dataset_id", None, 1)


def test_datasets_update_dataset() -> None:
    """Test updateDataset endpoint with WireMock"""
    test_id = "datasets.update_dataset.0"
    client = get_client(test_id)
    client.datasets.update_dataset(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "PATCH", "/v1/task-suites/dataset_id", None, 1)


def test_datasets_get_dataset_snapshot() -> None:
    """Test getDatasetSnapshot endpoint with WireMock"""
    test_id = "datasets.get_dataset_snapshot.0"
    client = get_client(test_id)
    client.datasets.get_dataset_snapshot(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/snapshot", None, 1)


def test_datasets_list_dataset_traces() -> None:
    """Test listDatasetTraces endpoint with WireMock"""
    test_id = "datasets.list_dataset_traces.0"
    client = get_client(test_id)
    client.datasets.list_dataset_traces(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/traces", None, 1)


def test_datasets_add_trace_to_dataset() -> None:
    """Test addTraceToDataset endpoint with WireMock"""
    test_id = "datasets.add_trace_to_dataset.0"
    client = get_client(test_id)
    client.datasets.add_trace_to_dataset(
        dataset_id="dataset_id",
        trace_id="traceId",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/traces", None, 1)


def test_datasets_update_dataset_traces() -> None:
    """Test updateDatasetTraces endpoint with WireMock"""
    test_id = "datasets.update_dataset_traces.0"
    client = get_client(test_id)
    client.datasets.update_dataset_traces(
        dataset_id="dataset_id",
        patch=UpdateTracesRequestPatch(),
        trace_ids=["traceIds"],
    )
    verify_request_count(test_id, "PATCH", "/v1/task-suites/dataset_id/traces", None, 1)


def test_datasets_remove_trace_from_dataset() -> None:
    """Test removeTraceFromDataset endpoint with WireMock"""
    test_id = "datasets.remove_trace_from_dataset.0"
    client = get_client(test_id)
    client.datasets.remove_trace_from_dataset(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/task-suites/dataset_id/traces/membership_id", None, 1)


def test_datasets_refresh_dataset_trace() -> None:
    """Test refreshDatasetTrace endpoint with WireMock"""
    test_id = "datasets.refresh_dataset_trace.0"
    client = get_client(test_id)
    client.datasets.refresh_dataset_trace(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/traces/membership_id/refresh", None, 1)


def test_datasets_list_dataset_trace_events() -> None:
    """Test listDatasetTraceEvents endpoint with WireMock"""
    test_id = "datasets.list_dataset_trace_events.0"
    client = get_client(test_id)
    client.datasets.list_dataset_trace_events(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/traces/membership_id/events", None, 1)


def test_datasets_list_trace_dataset_memberships() -> None:
    """Test listTraceDatasetMemberships endpoint with WireMock"""
    test_id = "datasets.list_trace_dataset_memberships.0"
    client = get_client(test_id)
    client.datasets.list_trace_dataset_memberships(
        trace_id="trace_id",
    )
    verify_request_count(test_id, "GET", "/v1/traces/trace_id/task-suite-memberships", None, 1)


def test_datasets_list_dataset_tasks() -> None:
    """Test listDatasetTasks endpoint with WireMock"""
    test_id = "datasets.list_dataset_tasks.0"
    client = get_client(test_id)
    client.datasets.list_dataset_tasks(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/tasks", None, 1)


def test_datasets_create_dataset_task() -> None:
    """Test createDatasetTask endpoint with WireMock"""
    test_id = "datasets.create_dataset_task.0"
    client = get_client(test_id)
    client.datasets.create_dataset_task(
        dataset_id="dataset_id",
        request={"key": "value"},
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/tasks", None, 1)


def test_datasets_get_dataset_task() -> None:
    """Test getDatasetTask endpoint with WireMock"""
    test_id = "datasets.get_dataset_task.0"
    client = get_client(test_id)
    client.datasets.get_dataset_task(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/tasks/membership_id", None, 1)


def test_datasets_delete_dataset_task() -> None:
    """Test deleteDatasetTask endpoint with WireMock"""
    test_id = "datasets.delete_dataset_task.0"
    client = get_client(test_id)
    client.datasets.delete_dataset_task(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/task-suites/dataset_id/tasks/membership_id", None, 1)


def test_datasets_update_dataset_task() -> None:
    """Test updateDatasetTask endpoint with WireMock"""
    test_id = "datasets.update_dataset_task.0"
    client = get_client(test_id)
    client.datasets.update_dataset_task(
        dataset_id="dataset_id",
        membership_id="membership_id",
        request={"key": "value"},
    )
    verify_request_count(test_id, "PATCH", "/v1/task-suites/dataset_id/tasks/membership_id", None, 1)


def test_datasets_set_dataset_task_verifiers() -> None:
    """Test setDatasetTaskVerifiers endpoint with WireMock"""
    test_id = "datasets.set_dataset_task_verifiers.0"
    client = get_client(test_id)
    client.datasets.set_dataset_task_verifiers(
        dataset_id="dataset_id",
        membership_id="membership_id",
        verifiers=[
            SetTaskVerifiersRequestVerifiersItem(
                scorer_id="scorerId",
            )
        ],
    )
    verify_request_count(test_id, "PUT", "/v1/task-suites/dataset_id/tasks/membership_id/verifiers", None, 1)


def test_datasets_list_dataset_task_events() -> None:
    """Test listDatasetTaskEvents endpoint with WireMock"""
    test_id = "datasets.list_dataset_task_events.0"
    client = get_client(test_id)
    client.datasets.list_dataset_task_events(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/tasks/membership_id/events", None, 1)


def test_datasets_refresh_dataset_task() -> None:
    """Test refreshDatasetTask endpoint with WireMock"""
    test_id = "datasets.refresh_dataset_task.0"
    client = get_client(test_id)
    client.datasets.refresh_dataset_task(
        dataset_id="dataset_id",
        membership_id="membership_id",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/tasks/membership_id/refresh", None, 1)


def test_datasets_list_dataset_clusters() -> None:
    """Test listDatasetClusters endpoint with WireMock"""
    test_id = "datasets.list_dataset_clusters.0"
    client = get_client(test_id)
    client.datasets.list_dataset_clusters(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/clusters", None, 1)


def test_datasets_create_dataset_cluster() -> None:
    """Test createDatasetCluster endpoint with WireMock"""
    test_id = "datasets.create_dataset_cluster.0"
    client = get_client(test_id)
    client.datasets.create_dataset_cluster(
        dataset_id="dataset_id",
        color="color",
        label="label",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/clusters", None, 1)


def test_datasets_delete_dataset_cluster() -> None:
    """Test deleteDatasetCluster endpoint with WireMock"""
    test_id = "datasets.delete_dataset_cluster.0"
    client = get_client(test_id)
    client.datasets.delete_dataset_cluster(
        dataset_id="dataset_id",
        cluster_id="cluster_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/task-suites/dataset_id/clusters/cluster_id", None, 1)


def test_datasets_update_dataset_cluster() -> None:
    """Test updateDatasetCluster endpoint with WireMock"""
    test_id = "datasets.update_dataset_cluster.0"
    client = get_client(test_id)
    client.datasets.update_dataset_cluster(
        dataset_id="dataset_id",
        cluster_id="cluster_id",
    )
    verify_request_count(test_id, "PATCH", "/v1/task-suites/dataset_id/clusters/cluster_id", None, 1)


def test_datasets_list_dataset_saved_views() -> None:
    """Test listDatasetSavedViews endpoint with WireMock"""
    test_id = "datasets.list_dataset_saved_views.0"
    client = get_client(test_id)
    client.datasets.list_dataset_saved_views(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/saved-views", None, 1)


def test_datasets_create_dataset_saved_view() -> None:
    """Test createDatasetSavedView endpoint with WireMock"""
    test_id = "datasets.create_dataset_saved_view.0"
    client = get_client(test_id)
    client.datasets.create_dataset_saved_view(
        dataset_id="dataset_id",
        name="name",
        scope="personal",
        state=CreateSavedViewRequestState(),
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/saved-views", None, 1)


def test_datasets_delete_dataset_saved_view() -> None:
    """Test deleteDatasetSavedView endpoint with WireMock"""
    test_id = "datasets.delete_dataset_saved_view.0"
    client = get_client(test_id)
    client.datasets.delete_dataset_saved_view(
        dataset_id="dataset_id",
        view_id="view_id",
    )
    verify_request_count(test_id, "DELETE", "/v1/task-suites/dataset_id/saved-views/view_id", None, 1)


def test_datasets_update_dataset_saved_view() -> None:
    """Test updateDatasetSavedView endpoint with WireMock"""
    test_id = "datasets.update_dataset_saved_view.0"
    client = get_client(test_id)
    client.datasets.update_dataset_saved_view(
        dataset_id="dataset_id",
        view_id="view_id",
    )
    verify_request_count(test_id, "PATCH", "/v1/task-suites/dataset_id/saved-views/view_id", None, 1)


def test_datasets_list_dataset_versions() -> None:
    """Test listDatasetVersions endpoint with WireMock"""
    test_id = "datasets.list_dataset_versions.0"
    client = get_client(test_id)
    client.datasets.list_dataset_versions(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/versions", None, 1)


def test_datasets_publish_dataset_version() -> None:
    """Test publishDatasetVersion endpoint with WireMock"""
    test_id = "datasets.publish_dataset_version.0"
    client = get_client(test_id)
    client.datasets.publish_dataset_version(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "POST", "/v1/task-suites/dataset_id/versions", None, 1)


def test_datasets_get_dataset_version() -> None:
    """Test getDatasetVersion endpoint with WireMock"""
    test_id = "datasets.get_dataset_version.0"
    client = get_client(test_id)
    client.datasets.get_dataset_version(
        dataset_id="dataset_id",
        version_id="version_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/versions/version_id", None, 1)


def test_datasets_list_dataset_evaluation_runs() -> None:
    """Test listDatasetEvaluationRuns endpoint with WireMock"""
    test_id = "datasets.list_dataset_evaluation_runs.0"
    client = get_client(test_id)
    client.datasets.list_dataset_evaluation_runs(
        dataset_id="dataset_id",
    )
    verify_request_count(test_id, "GET", "/v1/task-suites/dataset_id/eval-runs", None, 1)
