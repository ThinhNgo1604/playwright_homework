import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
       "viewport": {
            "width": 1000,
            "height": 1000,
        },
        "ignore_https_errors": True,
    }


# def browser_context_args(browser_context_args, playwright):
#     iphont_11 = playwright.devices["iPhone 11"]
#     return{
#         **browser_context_args,
#         **iphont_11,
#     }