from typing import Generator
import pytest
import requests
from playwright.sync_api import Playwright, Page, expect, APIRequestContext

GITHUB_API_TOKEN = "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" # 7 days
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set. Please set it to run the tests."

GITHUB_USER = "ThinhNgo1604" # ThinhNgo1604
assert GITHUB_USER, "GITHUB_USER is not set. Please set it to run the tests."

GITHUB_REPO = "Test_API"

# -------------------------
# Option 1
url = f"https://api.github.com/users/{GITHUB_USER}" # Check if the user is valid
headers = {"Authorization": f"token {GITHUB_API_TOKEN}"} # Check if the token is valid

res = requests.get(url, headers=headers)

if res.status_code == 200:
    print("✅ Token hợp lệ, user:", res.json()["login"])
else:
    print("❌ Token không hợp lệ:", res.status_code, res.json())
# ---------------------------

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers,
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session", autouse=True)
def create_test_repo(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # Create a test repository
    new_response = api_request_context.post(
        "/user/repos", data={"name": GITHUB_REPO})
    assert new_response.ok, f"Failed to create repository: {new_response.status} {new_response.text}"

    yield

    delete_response = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert delete_response.ok, f"Failed to delete repository: {delete_response.status}"