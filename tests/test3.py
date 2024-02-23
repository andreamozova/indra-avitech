from support.functions import (Email)
from config import (GMAIL_EMAIL, GMAIL_PASSWORD)


def test_log_in_log_out(page):
    Email.log_in(page, GMAIL_EMAIL, GMAIL_PASSWORD)
    page.wait_for_selector('[role="navigation"]:first-child')
    assert "#inbox" in page.url

    Email.add_contact_sidebar(page)
    file_input = page.query_selector('[command="Files"]')
    file_input.set_input_files(file_path)

    Email.log_out(page)
    assert "#inbox" not in page.url
