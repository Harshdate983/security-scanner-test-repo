# These are deliberately fake values used to test scanner false-positive handling.
TEST_PASSWORD = "fake-test-password"
TEST_TOKEN = "fake-test-token"


def test_fake_values_are_nonempty():
    assert TEST_PASSWORD
    assert TEST_TOKEN
