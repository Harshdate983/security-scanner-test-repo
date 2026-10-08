# Intentional scanner test finding: fake administrator password.
admin_password = "fake-admin-password"

# Intentional scanner test finding: fake authentication token.
auth_token = "fake-auth-token-123456"


def authenticate(username, provided_password):
    """Demonstration only; this is not real authentication."""
    return bool(username) and bool(provided_password)
