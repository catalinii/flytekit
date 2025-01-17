from flytekit.core.data_persistence import FileAccessProvider


def test_get_random_remote_path():
    fp = FileAccessProvider("/tmp", "s3://my-bucket")
    path = fp.get_random_remote_path()
    assert path.startswith("s3://my-bucket")


def test_is_remote():
    fp = FileAccessProvider("/tmp", "s3://my-bucket")
    assert fp.is_remote("./checkpoint") is False
    assert fp.is_remote("/tmp/foo/bar") is False
    assert fp.is_remote("file://foo/bar") is False
    assert fp.is_remote("s3://my-bucket/foo/bar") is True
