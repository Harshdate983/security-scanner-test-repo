# Intentional scanner test finding with an unusual variable name.
service_value = "sk-test-api-987654321"

# Documentation-safe URL; no real network request is made.
API_URL = "https://example.com/api"


def build_endpoint(path):
    return f"{API_URL}/{path.lstrip('/')}"
