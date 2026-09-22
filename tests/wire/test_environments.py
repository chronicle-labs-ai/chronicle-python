from .conftest import get_client, verify_request_count


def test_environments_list_environments() -> None:
    """Test listEnvironments endpoint with WireMock"""
    test_id = "environments.list_environments.0"
    client = get_client(test_id)
    client.environments.list_environments()
    verify_request_count(test_id, "GET", "/v1/environments", None, 1)


def test_environments_create_environment() -> None:
    """Test createEnvironment endpoint with WireMock"""
    test_id = "environments.create_environment.0"
    client = get_client(test_id)
    client.environments.create_environment(
        slug="slug",
        label="label",
    )
    verify_request_count(test_id, "POST", "/v1/environments", None, 1)


def test_environments_get_environment() -> None:
    """Test getEnvironment endpoint with WireMock"""
    test_id = "environments.get_environment.0"
    client = get_client(test_id)
    client.environments.get_environment(
        environment_id="environment_id",
    )
    verify_request_count(test_id, "GET", "/v1/environments/environment_id", None, 1)


def test_environments_list_environment_versions() -> None:
    """Test listEnvironmentVersions endpoint with WireMock"""
    test_id = "environments.list_environment_versions.0"
    client = get_client(test_id)
    client.environments.list_environment_versions(
        environment_id="environment_id",
    )
    verify_request_count(test_id, "GET", "/v1/environments/environment_id/versions", None, 1)


def test_environments_create_environment_version() -> None:
    """Test createEnvironmentVersion endpoint with WireMock"""
    test_id = "environments.create_environment_version.0"
    client = get_client(test_id)
    client.environments.create_environment_version(
        environment_id="environment_id",
        version="version",
    )
    verify_request_count(test_id, "POST", "/v1/environments/environment_id/versions", None, 1)


def test_environments_get_environment_version() -> None:
    """Test getEnvironmentVersion endpoint with WireMock"""
    test_id = "environments.get_environment_version.0"
    client = get_client(test_id)
    client.environments.get_environment_version(
        environment_id="environment_id",
        version_selector="version_selector",
    )
    verify_request_count(test_id, "GET", "/v1/environments/environment_id/versions/version_selector", None, 1)


def test_environments_compile_environment_version() -> None:
    """Test compileEnvironmentVersion endpoint with WireMock"""
    test_id = "environments.compile_environment_version.0"
    client = get_client(test_id)
    client.environments.compile_environment_version(
        environment_id="environment_id",
        version_selector="version_selector",
        dataset_snapshot_id="datasetSnapshotId",
        scenario_id="scenarioId",
    )
    verify_request_count(test_id, "POST", "/v1/environments/environment_id/versions/version_selector/compile", None, 1)
