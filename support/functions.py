class Email:

        def __init__(self, page):
                self.page = page

        def log_in(self, email, password):
                next_button = self.get_by_role("button", name="Next")
                self.goto("https://mail.google.com/")
                self.wait_for_selector('input[type="email"]').fill(email)
                self.get_by_role("h1", name="Sign in").is_visible()
                self.get_by_role("button", name="Create account").is_visible()
                next_button.click()

                self.wait_for_selector('input[type="password"]').fill(password)
                self.get_by_role("h1", name="Welcome").is_visible()
                self.get_by_text(email).is_visible()
                self.get_by_role("button", name="Forgot password?").is_visible()
                next_button.click()

        def log_out(self):
                # I was trying to use more reasonable locators in this test but I am missing data-tests
                self.locator('.gb_d.gb_Fa.gb_J').click()
                self.locator('[aria-label="Account and settings"]').is_visible()
                frame_account = self.query_selector('iframe[name="account"]')
                frame = frame_account.content_frame()
                sign_out_element = frame.locator('text="Sign out"')
                sign_out_element.click()

        def add_contact_sidebar(self):
                self.wait_for_timeout(1000)
                self.locator('#gsc-gab-9').click()
                self.wait_for_timeout(3000)
                frame_account = self.query_selector('iframe[title="Contacts"]')
                frame = frame_account.content_frame()
                sign_out_element = frame.locator('[data-displayname="Testing Account"]')
                sign_out_element.click()
                self.wait_for_timeout(1000)
                # not sure why the action doesnt happen but I didnt have capacity to investigate it more
                send_email_button = frame.get_by_label("Send email").first
                send_email_button.click()
                self.wait_for_timeout(1000)


