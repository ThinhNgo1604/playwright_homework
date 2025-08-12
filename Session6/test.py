import pytest

@pytest.fixture
def my_fixture():
    print("🚀 Setup: Mở trình duyệt")
    yield "trang đã mở"
    print("🧹 Teardown: Đóng trình duyệt")

def test_demo(my_fixture):
    print(f"Test đang dùng: {my_fixture}")
