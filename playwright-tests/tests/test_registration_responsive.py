"""Responsive design tests for registration page across viewports."""
import pytest
from test_data.registration_data import get_valid_user


class TestMobileViewport:
    """Tests specific to mobile viewport (<767px). Documents BUG-002, BUG-009, BUG-011."""

    @pytest.mark.mobile
    @pytest.mark.xfail(
        reason="BUG-002: CSS hides .error-message with display:none !important on mobile"
    )
    def test_error_messages_visible_on_mobile(self, mobile_registration_page):
        """TC-042: Validation error messages should be visible on mobile."""
        page = mobile_registration_page

        # Trigger a validation error
        user = get_valid_user()
        user["email"] = "notanemail"
        page.fill_form(user)
        page.submit_form()

        # Error message should be in the DOM AND visible
        assert page.email.has_error(), "Error message text should be present"
        assert page.email.error_is_visible(), "Error message should be visible on mobile"

    @pytest.mark.mobile
    @pytest.mark.xfail(
        reason="BUG-009: CSS sets max-height:35px and margin-bottom:-25px on mobile"
    )
    def test_submit_button_fully_visible_on_mobile(self, mobile_registration_page):
        """TC-043: Submit button should not be clipped on mobile."""
        page = mobile_registration_page

        box = page.submit_button.bounding_box()
        assert box is not None, "Submit button should have a bounding box"
        # Standard touch target minimum is 44px height
        assert box["height"] >= 44, (
            f"Button height {box['height']}px is below 44px minimum touch target"
        )

    @pytest.mark.mobile
    @pytest.mark.xfail(
        reason="BUG-011: White SVG overlay covers newsletter checkbox on mobile"
    )
    def test_newsletter_checkbox_visible_on_mobile(self, mobile_registration_page):
        """TC-044: Newsletter checkbox should be visible and not obscured on mobile."""
        page = mobile_registration_page

        assert page.newsletter_checkbox.is_visible(), "Newsletter checkbox should be visible"
        # The overlay should not be displayed
        assert page.newsletter_overlay.is_hidden(), (
            "Newsletter overlay should not be visible on mobile"
        )


class TestTabletViewport:
    """Tests specific to tablet viewport (768-1024px). Documents BUG-010."""

    @pytest.mark.tablet
    @pytest.mark.xfail(
        reason="BUG-010: Advertisement SVG overlay covers Street Address on tablet"
    )
    def test_street_address_not_obscured_on_tablet(self, tablet_registration_page):
        """TC-046: Street Address field should not be covered by ad overlay on tablet."""
        page = tablet_registration_page

        assert page.address.is_visible(), "Street Address field should be visible"
        # The ad overlay should not be displayed
        assert page.address_overlay.is_hidden(), (
            "Advertisement overlay should not cover the Street Address field"
        )
