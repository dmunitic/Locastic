import pytest
from pathlib import Path
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.dashboard_page import DashboardPage


RESULTS_DIR = Path(__file__).parent / "test-results"


def _context_options(request, viewport):
    """Build context options with video recording and viewport."""
    # Create a folder per test for video/screenshots
    test_name = request.node.name.replace("[", "_").replace("]", "")
    output_dir = RESULTS_DIR / test_name
    output_dir.mkdir(parents=True, exist_ok=True)

    return {
        "viewport": viewport,
        "record_video_dir": str(output_dir),
        "record_video_size": {"width": viewport["width"], "height": viewport["height"]},
    }


def _take_screenshot(context, request):
    """Take a screenshot for each page in the context before closing."""
    test_name = request.node.name.replace("[", "_").replace("]", "")
    output_dir = RESULTS_DIR / test_name
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, page in enumerate(context.pages):
        page.screenshot(path=str(output_dir / f"screenshot_{i}.png"))


# ── Viewport fixtures ──────────────────────────────────────────────


@pytest.fixture
def desktop_context(browser, request):
    options = _context_options(request, {"width": 1280, "height": 720})
    context = browser.new_context(**options)
    yield context
    _take_screenshot(context, request)
    context.close()


@pytest.fixture
def tablet_context(browser, request):
    options = _context_options(request, {"width": 800, "height": 1024})
    context = browser.new_context(**options)
    yield context
    _take_screenshot(context, request)
    context.close()


@pytest.fixture
def mobile_context(browser, request):
    options = _context_options(request, {"width": 375, "height": 667})
    context = browser.new_context(**options)
    yield context
    _take_screenshot(context, request)
    context.close()


# ── Desktop page object fixtures ───────────────────────────────────


@pytest.fixture
def registration_page(desktop_context, base_url):
    page = desktop_context.new_page()
    reg_page = RegistrationPage(page)
    reg_page.URL = base_url + reg_page.URL
    reg_page.navigate()
    return reg_page


@pytest.fixture
def login_page(desktop_context, base_url):
    page = desktop_context.new_page()
    lp = LoginPage(page)
    lp.URL = base_url + lp.URL
    lp.navigate()
    return lp


@pytest.fixture
def forgot_password_page(desktop_context, base_url):
    page = desktop_context.new_page()
    fp = ForgotPasswordPage(page)
    fp.URL = base_url + fp.URL
    fp.navigate()
    return fp


# ── Mobile page object fixtures ───────────────────────────────────


@pytest.fixture
def mobile_registration_page(mobile_context, base_url):
    page = mobile_context.new_page()
    reg_page = RegistrationPage(page)
    reg_page.URL = base_url + reg_page.URL
    reg_page.navigate()
    return reg_page


# ── Tablet page object fixtures ───────────────────────────────────


@pytest.fixture
def tablet_registration_page(tablet_context, base_url):
    page = tablet_context.new_page()
    reg_page = RegistrationPage(page)
    reg_page.URL = base_url + reg_page.URL
    reg_page.navigate()
    return reg_page
