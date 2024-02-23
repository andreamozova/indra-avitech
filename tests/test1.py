from support.functions import (Email)
from config import (GMAIL_EMAIL, GMAIL_PASSWORD)


def test_log_in_log_out(page):
    Email.log_in(page, GMAIL_EMAIL, GMAIL_PASSWORD)
    page.wait_for_selector('[role="navigation"]:first-child')
    assert "#inbox" in page.url

    Email.log_out(page)
    assert "#inbox" not in page.url


