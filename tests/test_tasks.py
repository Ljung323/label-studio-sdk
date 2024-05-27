# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import BaseTask, TaskSimple
from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_create_many(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "task_count": 1,
        "annotation_count": 1,
        "predictions_count": 1,
        "duration": 1.1,
        "file_upload_ids": [1],
        "could_be_tasks_list": True,
        "found_formats": ["found_formats"],
        "data_columns": ["data_columns"],
    }
    expected_types = {
        "task_count": "integer",
        "annotation_count": "integer",
        "predictions_count": "integer",
        "duration": None,
        "file_upload_ids": ("list", {0: "integer"}),
        "could_be_tasks_list": None,
        "found_formats": ("list", {0: None}),
        "data_columns": ("list", {0: None}),
    }
    response = client.tasks.create_many(id=1, data={})
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.create_many(id=1, data={})
    validate_response(async_response, expected_response, expected_types)


async def test_create_many_status(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "preannotated_from_fields": {"preannotated_from_fields": {"key": "value"}},
        "commit_to_project": True,
        "return_task_ids": True,
        "status": "created",
        "url": "url",
        "traceback": "traceback",
        "error": "error",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "finished_at": "2024-01-15T09:30:00Z",
        "task_count": 1,
        "annotation_count": 1,
        "prediction_count": 1,
        "duration": 1,
        "file_upload_ids": {"file_upload_ids": {"key": "value"}},
        "could_be_tasks_list": True,
        "found_formats": {"found_formats": {"key": "value"}},
        "data_columns": {"data_columns": {"key": "value"}},
        "tasks": {"tasks": {"key": "value"}},
        "task_ids": {"task_ids": {"key": "value"}},
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "preannotated_from_fields": ("dict", {0: (None, None)}),
        "commit_to_project": None,
        "return_task_ids": None,
        "status": None,
        "url": None,
        "traceback": None,
        "error": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "finished_at": "datetime",
        "task_count": "integer",
        "annotation_count": "integer",
        "prediction_count": "integer",
        "duration": "integer",
        "file_upload_ids": ("dict", {0: (None, None)}),
        "could_be_tasks_list": None,
        "found_formats": ("dict", {0: (None, None)}),
        "data_columns": ("dict", {0: (None, None)}),
        "tasks": ("dict", {0: (None, None)}),
        "task_ids": ("dict", {0: (None, None)}),
        "project": "integer",
    }
    response = client.tasks.create_many_status(id=1, import_pk="import_pk")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.create_many_status(id=1, import_pk="import_pk")
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "data": {"data": {"key": "value"}},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": True,
        "overlap": 1,
        "inner_id": 1,
        "total_annotations": 1,
        "cancelled_annotations": 1,
        "total_predictions": 1,
        "comment_count": 1,
        "unresolved_comment_count": 1,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "updated_by": 1,
        "file_upload": 1,
        "comment_authors": [1],
    }
    expected_types = {
        "id": "integer",
        "data": ("dict", {0: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "inner_id": "integer",
        "total_annotations": "integer",
        "cancelled_annotations": "integer",
        "total_predictions": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "updated_by": "integer",
        "file_upload": "integer",
        "comment_authors": ("list", {0: "integer"}),
    }
    response = client.tasks.create(request=BaseTask(data={}))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.create(request=BaseTask(data={}))
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "predictions": "predictions",
        "annotations": [
            {
                "id": 1,
                "created_username": "created_username",
                "created_ago": "created_ago",
                "completed_by": 1,
                "unique_id": "unique_id",
                "was_cancelled": True,
                "ground_truth": True,
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "draft_created_at": "2024-01-15T09:30:00Z",
                "lead_time": 1.1,
                "import_id": 1,
                "last_action": "prediction",
                "task": 1,
                "project": 1,
                "updated_by": 1,
                "parent_prediction": 1,
                "parent_annotation": 1,
                "last_created_by": 1,
            }
        ],
        "drafts": "drafts",
        "annotators": "annotators",
        "inner_id": 1,
        "cancelled_annotations": 1,
        "total_annotations": 1,
        "total_predictions": 1,
        "completed_at": "2024-01-15T09:30:00Z",
        "annotations_results": "annotations_results",
        "predictions_results": "predictions_results",
        "predictions_score": 1.1,
        "file_upload": "file_upload",
        "storage_filename": "storage_filename",
        "annotations_ids": "annotations_ids",
        "predictions_model_versions": "predictions_model_versions",
        "avg_lead_time": 1.1,
        "draft_exists": True,
        "updated_by": "updated_by",
        "data": {"data": {"key": "value"}},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": True,
        "overlap": 1,
        "comment_count": 1,
        "unresolved_comment_count": 1,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "comment_authors": [1],
    }
    expected_types = {
        "id": "integer",
        "predictions": None,
        "annotations": (
            "list",
            {
                0: {
                    "id": "integer",
                    "created_username": None,
                    "created_ago": None,
                    "completed_by": "integer",
                    "unique_id": None,
                    "was_cancelled": None,
                    "ground_truth": None,
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "draft_created_at": "datetime",
                    "lead_time": None,
                    "import_id": "integer",
                    "last_action": None,
                    "task": "integer",
                    "project": "integer",
                    "updated_by": "integer",
                    "parent_prediction": "integer",
                    "parent_annotation": "integer",
                    "last_created_by": "integer",
                }
            },
        ),
        "drafts": None,
        "annotators": None,
        "inner_id": "integer",
        "cancelled_annotations": "integer",
        "total_annotations": "integer",
        "total_predictions": "integer",
        "completed_at": "datetime",
        "annotations_results": None,
        "predictions_results": None,
        "predictions_score": None,
        "file_upload": None,
        "storage_filename": None,
        "annotations_ids": None,
        "predictions_model_versions": None,
        "avg_lead_time": None,
        "draft_exists": None,
        "updated_by": None,
        "data": ("dict", {0: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "comment_authors": ("list", {0: "integer"}),
    }
    response = client.tasks.get(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.get(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.tasks.delete(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.tasks.delete(id="id") is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "data": {"data": {"key": "value"}},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": True,
        "overlap": 1,
        "inner_id": 1,
        "total_annotations": 1,
        "cancelled_annotations": 1,
        "total_predictions": 1,
        "comment_count": 1,
        "unresolved_comment_count": 1,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "updated_by": 1,
        "file_upload": 1,
        "comment_authors": [1],
        "annotations": [
            {
                "id": 1,
                "created_username": "created_username",
                "created_ago": "created_ago",
                "completed_by": 1,
                "unique_id": "unique_id",
                "was_cancelled": True,
                "ground_truth": True,
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "draft_created_at": "2024-01-15T09:30:00Z",
                "lead_time": 1.1,
                "import_id": 1,
                "last_action": "prediction",
                "task": 1,
                "project": 1,
                "updated_by": 1,
                "parent_prediction": 1,
                "parent_annotation": 1,
                "last_created_by": 1,
            }
        ],
        "predictions": [
            {
                "id": 1,
                "model_version": "model_version",
                "created_ago": "created_ago",
                "score": 1.1,
                "cluster": 1,
                "mislabeling": 1.1,
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "model": 1,
                "model_run": 1,
                "task": 1,
                "project": 1,
            }
        ],
    }
    expected_types = {
        "id": "integer",
        "data": ("dict", {0: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "inner_id": "integer",
        "total_annotations": "integer",
        "cancelled_annotations": "integer",
        "total_predictions": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "updated_by": "integer",
        "file_upload": "integer",
        "comment_authors": ("list", {0: "integer"}),
        "annotations": (
            "list",
            {
                0: {
                    "id": "integer",
                    "created_username": None,
                    "created_ago": None,
                    "completed_by": "integer",
                    "unique_id": None,
                    "was_cancelled": None,
                    "ground_truth": None,
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "draft_created_at": "datetime",
                    "lead_time": None,
                    "import_id": "integer",
                    "last_action": None,
                    "task": "integer",
                    "project": "integer",
                    "updated_by": "integer",
                    "parent_prediction": "integer",
                    "parent_annotation": "integer",
                    "last_created_by": "integer",
                }
            },
        ),
        "predictions": (
            "list",
            {
                0: {
                    "id": "integer",
                    "model_version": None,
                    "created_ago": None,
                    "score": None,
                    "cluster": "integer",
                    "mislabeling": None,
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "model": "integer",
                    "model_run": "integer",
                    "task": "integer",
                    "project": "integer",
                }
            },
        ),
    }
    response = client.tasks.update(id="id", request=TaskSimple(data={}))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.update(id="id", request=TaskSimple(data={}))
    validate_response(async_response, expected_response, expected_types)
