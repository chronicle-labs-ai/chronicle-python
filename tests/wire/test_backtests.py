from .conftest import get_client, verify_request_count

from chroniclelabs.backtests import (
    CreateBacktestJobRequestRecipe,
    CreateBacktestJobRequestRecipeAgentsItem,
    CreateBacktestJobRequestRecipeData,
    CreateBacktestJobRequestRecipeDataScenariosItem,
    CreateBacktestJobRequestRecipeDataSourcesItem,
    CreateBacktestJobRequestRecipeGradersItem,
)


def test_backtests_get_backtests_availability() -> None:
    """Test getBacktestsAvailability endpoint with WireMock"""
    test_id = "backtests.get_backtests_availability.0"
    client = get_client(test_id)
    client.backtests.get_backtests_availability()
    verify_request_count(test_id, "GET", "/v1/backtests/availability", None, 1)


def test_backtests_list_backtest_jobs() -> None:
    """Test listBacktestJobs endpoint with WireMock"""
    test_id = "backtests.list_backtest_jobs.0"
    client = get_client(test_id)
    client.backtests.list_backtest_jobs()
    verify_request_count(test_id, "GET", "/v1/backtests/jobs", None, 1)


def test_backtests_create_backtest_job() -> None:
    """Test createBacktestJob endpoint with WireMock"""
    test_id = "backtests.create_backtest_job.0"
    client = get_client(test_id)
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
    verify_request_count(test_id, "POST", "/v1/backtests/jobs", None, 1)


def test_backtests_get_backtest_job() -> None:
    """Test getBacktestJob endpoint with WireMock"""
    test_id = "backtests.get_backtest_job.0"
    client = get_client(test_id)
    client.backtests.get_backtest_job(
        job_id="job_id",
    )
    verify_request_count(test_id, "GET", "/v1/backtests/jobs/job_id", None, 1)


def test_backtests_list_backtest_job_trials() -> None:
    """Test listBacktestJobTrials endpoint with WireMock"""
    test_id = "backtests.list_backtest_job_trials.0"
    client = get_client(test_id)
    client.backtests.list_backtest_job_trials(
        job_id="job_id",
    )
    verify_request_count(test_id, "GET", "/v1/backtests/jobs/job_id/trials", None, 1)


def test_backtests_get_backtest_trial() -> None:
    """Test getBacktestTrial endpoint with WireMock"""
    test_id = "backtests.get_backtest_trial.0"
    client = get_client(test_id)
    client.backtests.get_backtest_trial(
        job_id="job_id",
        trial_id="trial_id",
    )
    verify_request_count(test_id, "GET", "/v1/backtests/jobs/job_id/trials/trial_id", None, 1)


def test_backtests_cancel_backtest_job() -> None:
    """Test cancelBacktestJob endpoint with WireMock"""
    test_id = "backtests.cancel_backtest_job.0"
    client = get_client(test_id)
    client.backtests.cancel_backtest_job(
        job_id="job_id",
    )
    verify_request_count(test_id, "POST", "/v1/backtests/jobs/job_id/cancel", None, 1)


def test_backtests_stream_backtest_job_events() -> None:
    """Test streamBacktestJobEvents endpoint with WireMock"""
    test_id = "backtests.stream_backtest_job_events.0"
    client = get_client(test_id)
    for _ in client.backtests.stream_backtest_job_events(
        job_id="job_id",
    ):
        pass
    verify_request_count(test_id, "GET", "/v1/backtests/jobs/job_id/stream", None, 1)
