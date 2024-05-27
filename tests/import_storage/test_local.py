# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import LocalFilesImportStorage
from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = [
        {
            "id": 1,
            "type": "type",
            "synchronizable": True,
            "path": "path",
            "regex_filter": "regex_filter",
            "use_blob_urls": True,
            "last_sync": "2024-01-15T09:30:00Z",
            "last_sync_count": 1,
            "last_sync_job": "last_sync_job",
            "status": "initialized",
            "traceback": "traceback",
            "meta": {"meta": {"key": "value"}},
            "title": "title",
            "description": "description",
            "created_at": "2024-01-15T09:30:00Z",
            "project": 1,
        }
    ]
    expected_types = (
        "list",
        {
            0: {
                "id": "integer",
                "type": None,
                "synchronizable": None,
                "path": None,
                "regex_filter": None,
                "use_blob_urls": None,
                "last_sync": "datetime",
                "last_sync_count": "integer",
                "last_sync_job": None,
                "status": None,
                "traceback": None,
                "meta": ("dict", {0: (None, None)}),
                "title": None,
                "description": None,
                "created_at": "datetime",
                "project": "integer",
            }
        },
    )
    response = client.import_storage.local.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "project": "integer",
    }
    response = client.import_storage.local.create(request=LocalFilesImportStorage(project=1))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.create(request=LocalFilesImportStorage(project=1))
    validate_response(async_response, expected_response, expected_types)


async def test_validate(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "project": "integer",
    }
    response = client.import_storage.local.validate(request=LocalFilesImportStorage(project=1))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.validate(request=LocalFilesImportStorage(project=1))
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "project": "integer",
    }
    response = client.import_storage.local.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.local.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.local.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "project": "integer",
    }
    response = client.import_storage.local.update(id=1, request=LocalFilesImportStorage(project=1))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.update(id=1, request=LocalFilesImportStorage(project=1))
    validate_response(async_response, expected_response, expected_types)


async def test_sync(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "project": 1,
    }
    expected_types = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "project": "integer",
    }
    response = client.import_storage.local.sync(id="id", request=LocalFilesImportStorage(project=1))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.local.sync(id="id", request=LocalFilesImportStorage(project=1))
    validate_response(async_response, expected_response, expected_types)
