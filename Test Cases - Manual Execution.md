# Test Cases - Manual Execution

**Execution Date**: Feb 12, 2026
**Tester**: Dragana Munitlic
**Environment**: Chrome 133, Windows 10
**Viewports tested**: Desktop (1280px), Tablet (800px), Mobile (375px)

---

## How to Use This Document

- **Actual Result (predicted)**: Pre-filled based on source code analysis — verify each in the browser
- **Status**: Mark as Pass/Fail after manual verification
- **Notes**: Add any additional observations during execution
- For failed tests, reference the corresponding BUG-ID from `Bug Report.md`

---

## Navigation Test Cases

### TC-001: Navigate to Registration Page from Login Page
- **Priority**: High
- **Preconditions**: User is on login page
- **Test Steps**:
  1. Navigate to https://qa-test-web-app.vercel.app/index.html
  2. Verify "Create New Account" link is visible
  3. Click "Create New Account" link
- **Expected Result**:
  - User redirected to registration page
  - Registration form displayed with all fields
  - Page title shows "Create Account"
- **Actual Result**: PASS — "Create New Account" link is present and navigates to `register.html`. Page heading shows "Create Account". All 9 input fields, 2 checkboxes, and submit button are displayed.
- **Status**: Pass
- **Notes**:

---

### TC-002: Navigate Back to Login from Registration Page
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Navigate to registration page
  2. Click "Already have an account? Login" link at bottom
- **Expected Result**:
  - User redirected to login page
  - Login form displayed
- **Actual Result**: PASS — Link present at bottom of form, navigates to `index.html`. Login form displays correctly with "Welcome Back" heading.
- **Status**: Pass
- **Notes**:

---

## Positive Test Cases

### TC-003: Successful Registration with All Valid Data
- **Priority**: High
- **Preconditions**:
  - User is on registration page
  - Email has not been previously registered
- **Test Steps**:
  1. Navigate to registration page
  2. Enter valid first name (e.g., "John")
  3. Enter valid last name (e.g., "Doe")
  4. Enter valid email (e.g., "john.doe.test@example.com")
  5. Enter valid phone number (e.g., "555-123-4567")
  6. Enter valid street address (e.g., "123 Main St")
  7. Enter valid city (e.g., "New York")
  8. Enter valid ZIP code (e.g., "10001")
  9. Enter valid password (e.g., "SecurePass123!")
  10. Confirm password (same as step 9)
  11. Check "I agree to the Terms and Conditions" checkbox
  12. Click "Create Account" button
- **Expected Result**:
  - Registration successful
  - Success message displayed
  - User redirected to login page
- **Actual Result**: PASS — Success message "Registration successful! Redirecting to login..." displayed. User redirected to `index.html?registered=true` after 1.5 seconds.
- **Status**: Pass
- **Notes**: Verify the registered account can also log in (see TC-040)

---

### TC-004: Registration Without Newsletter Subscription
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all required fields with valid data
  2. Check "I agree to Terms and Conditions"
  3. Leave "Subscribe to newsletter" unchecked
  4. Click "Create Account"
- **Expected Result**:
  - Registration successful
  - Newsletter subscription is optional
- **Actual Result**: PASS — Registration succeeds. Newsletter checkbox is not required and does not affect submission.
- **Status**: Pass
- **Notes**:

---

## Required Field Validation

### TC-005: Submit Empty Form
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Navigate to registration page
  2. Leave all fields empty
  3. Click "Create Account" button
- **Expected Result**:
  - Form is NOT submitted
  - Error messages displayed for all required fields
  - User stays on registration page
- **Actual Result**: PARTIAL PASS — Browser's native HTML `required` attribute prevents submission and shows a tooltip on the first empty required field (First Name). However, only one field is highlighted at a time — user must fix each field sequentially to discover the next error.
- **Status**: Pass (with observation)
- **Notes**: No custom error messages shown. Relies entirely on browser-native required field validation. 

---

### TC-006: Submit Without Required Checkbox (Terms & Conditions)
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all form fields with valid data
  2. Leave "I agree to Terms and Conditions" unchecked
  3. Click "Create Account"
- **Expected Result**:
  - Form is NOT submitted
  - Error message: "You must agree to Terms and Conditions" or similar
- **Actual Result**: FAIL — Form submits successfully without checking the Terms checkbox. No error message displayed. Registration completes and user is redirected to login page. The terms validation code is commented out in the JavaScript.
- **Status**: Fail
- **Notes**: See BUG-007. The checkbox also lacks the HTML `required` attribute.

---

### TC-007: Submit With Only Some Required Fields Filled
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill only First Name and Email
  2. Leave other fields empty
  3. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error messages shown for each empty required field
- **Actual Result**: PARTIAL PASS — Browser stops submission due to `required` attribute on Last Name (the next empty field after First Name). However, it only indicates one missing field at a time, not all empty fields simultaneously.
- **Status**: Pass (with observation)
- **Notes**: Previously entered data IS preserved when browser blocks submission.

---

## Email Validation

### TC-008: Invalid Email Format - No @ Symbol
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter invalid email: "notanemail.com"
  3. Check required checkbox
  4. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message: "Please enter a valid email address"
- **Actual Result**: PASS — JavaScript validation catches this (regex `/\S+@\S/` requires `@`). Error message "Invalid email address" displayed below the email field.
- **Status**: Pass
- **Notes**: This is one of the few cases the weak regex correctly catches, though the check should be performed in real time, not after the form is submitted. On mobile, the error message is not visible (see BUG-002).

---

### TC-009: Invalid Email Format - Missing Domain
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter invalid email: "user@"
  3. Check required checkbox
  4. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message for invalid email
- **Actual Result**: PASS — The regex `/\S+@\S/` requires at least one non-whitespace character after `@`. Error message "Invalid email address" displayed below the email field.
- **Status**: Pass
- **Notes**: See notes for TC-008. 

---

### TC-010: Invalid Email Format - Incomplete Domain (Single Character)
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter invalid email: "user@x"
  3. Check required checkbox
  4. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message for invalid email
- **Actual Result**: FAIL — The regex `/\S+@\S/` only requires one non-whitespace character after `@`, so "user@x" passes validation. Registration succeeds with an invalid email address.
- **Status**: Fail
- **Notes**: See BUG-001. This demonstrates the regex is too permissive — it accepts any single character as a valid domain.

---

### TC-011: Invalid Email Format - Spaces
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter email with spaces: "user name@email.com"
  3. Check required checkbox
  4. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message for invalid email format
- **Actual Result**: Fails. It creates and account with "user name@email.com" that can be logged into.
- **Status**: Fail
- **Notes**: See BUG-001

---

### TC-012: Duplicate Email Registration
- **Priority**: High
- **Preconditions**:
  - Email "existing.user@example.com" already registered
- **Test Steps**:
  1. Register an account with a valid email
  2. Try to register again with the same email
  3. Click "Create Account"
- **Expected Result**:
  - Error message: "User with this email already exists" or similar
- **Actual Result**: Message "User with this email already exists" displays.
- **Status**: Pass
- **Notes**: 

---

## Phone Number Validation

### TC-013: Phone Number - Various Valid Formats
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill form with valid data
  2. Test different phone formats:
     - "555-123-4567"
     - "(555) 123-4567"
     - "5551234567"
     - "+1 555 123 4567"
  3. Submit each
- **Expected Result**:
  - Valid phone formats accepted
- **Actual Result**: PASS (all formats) — Phone validation only checks `phone.length > 0`, so all non-empty strings pass. Any format is accepted.
- **Status**: Pass (but see BUG-004 — accepts literally anything)
- **Notes**: See BUG-004. Passes for the wrong reason — there's no format validation at all.

---

### TC-014: Phone Number - Invalid Format (Letters)
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill form with valid data
  2. Enter phone: "abcd-efg-hijk"
  3. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message: "Please enter a valid phone number"
- **Actual Result**: FAIL — Phone "abcd-efg-hijk" is accepted. Registration succeeds. No error message. Validation only checks `phone.length > 0`.
- **Status**: Fail
- **Notes**: See BUG-004

---

### TC-015: Phone Number - Too Short
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill form with valid data
  2. Enter phone: "123"
  3. Click "Create Account"
- **Expected Result**:
  - Error message about phone number length/format
- **Actual Result**: FAIL — Phone "123" is accepted (length > 0). No minimum length enforcement beyond being non-empty.
- **Status**: Fail
- **Notes**: See BUG-004

---

## Password Validation

### TC-016: Password and Confirm Password Mismatch
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter password: "SecurePass123!"
  3. Enter confirm password: "DifferentPass456!"
  4. Check required checkbox
  5. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error message: "Passwords do not match"
- **Actual Result**: FAIL — Registration succeeds with mismatched passwords. No error message displayed. The password from the "Password" field is the one stored.
- **Status**: Fail
- **Notes**: See BUG-006

---

### TC-017: Weak Password - Too Short
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter password: "123"
  3. Confirm password: "123"
  4. Check required checkbox
  5. Click "Create Account"
- **Expected Result**:
  - Error message indicating password requirements
  - Form NOT submitted
- **Actual Result**: PARTIAL PASS — "123" (3 chars) is rejected with message "Password must be at least 4 characters". However, "1234" (4 chars) is accepted, which is still far too weak by industry standards (should be 8+ chars minimum).
- **Status**: Fail
- **Notes**: See BUG-003. Minimum is 4 chars instead of industry-standard 8+. No complexity requirements.

---

### TC-018: Weak Password - No Special Characters
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill form with valid data
  2. Enter password: "simplepassword123"
  3. Confirm same password
  4. Submit form
- **Expected Result**:
  - Either accepts (if no special char requirement) OR shows error about password strength
- **Actual Result**: PASS (accepts) — No special character requirement exists. Password validation only checks `length >= 4`. "simplepassword123" passes.
- **Status**: Pass (but no complexity enforcement — see BUG-003)
- **Notes**: No password strength indicator exists.

---

### TC-019: Password Visibility Toggle
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Click into password field
  2. Enter some text
  3. Look for show/hide password toggle icon
- **Expected Result**:
  - Password visibility can be toggled
- **Actual Result**: FAIL — No password visibility toggle exists. Password and Confirm Password fields are standard `type="password"` with no show/hide button.
- **Status**: Fail
- **Notes**: Minor UX improvement. Not a bug per se, but a missing feature.

---

## Address Field Validation

### TC-020: ZIP Code - Invalid Format (Letters)
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter ZIP code: "ABCDE"
  3. Submit form
- **Expected Result**:
  - Error message for invalid ZIP code format
- **Actual Result**: FAIL — "ABCDE" is accepted (length >= 3). No format validation. Registration succeeds.
- **Status**: Fail
- **Notes**: See BUG-008

---

### TC-021: ZIP Code - Too Short/Long
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Test ZIP codes:
     - "12" (too short)
     - "123456789" (too long)
  2. Submit each
- **Expected Result**:
  - Error for invalid length
- **Actual Result**: PARTIAL — "12" (2 chars) is rejected with "Invalid ZIP code" (length < 3). "123456789" (9 chars) is accepted (length >= 3, no max check).
- **Status**: Fail (no upper bound)
- **Notes**: See BUG-008. Only lower bound of 3 chars enforced, which is too short for any real postal code format.

---

## Boundary and Edge Cases

### TC-022: Maximum Length Input - All Text Fields
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter very long strings (255+ characters) in First Name, Last Name, Street Address, City
  2. Fill other fields with valid data
  3. Submit form
- **Expected Result**:
  - Either accepted within limits OR max length error
  - No crash or unexpected behavior
- **Actual Result**: String of 300 characters passed for all the fields, even the Password field.  
- **Status**: Fail
- **Notes**: The Dashboard page displays the entire string that breaks out of the screen.

---

### TC-023: Minimum Length Input - Names
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter single character first name: "A"
  2. Enter single character last name: "B"
  3. Fill other fields with valid data
  4. Submit form
- **Expected Result**:
  - Either accepted OR minimum length error
- **Actual Result**: Single character first name, last name, city, passed. The name on the Dashboard page displays the one character name
- **Status**: Pass
- **Notes**: Consider whether single character names should be allowed. 

---

### TC-024: Special Characters in Name Fields (Valid)
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter names: First Name "Mary-Jane", Last Name "O'Brien"
  2. Fill other fields with valid data
  3. Submit form
- **Expected Result**:
  - Hyphens and apostrophes accepted
- **Actual Result**: First Name "Mary-Jane" displays on the Dashboard page.
- **Status**: Pass
- **Notes**:

---

### TC-025: Special Characters in Name Fields - Symbols
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter first name: "John@#$"
  2. Enter last name: "Doe%^&"
  3. Fill other fields validly
  4. Submit
- **Expected Result**:
  - Error message: invalid characters in name
- **Actual Result**: Passes registration. First Name John@#$ displayed on the Dashboard page.
- **Status**: Fail
- **Notes**: 

---

### TC-026: Numeric Values in Name Fields
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter first name: "John123"
  2. Enter last name: "456Doe"
  3. Submit form
- **Expected Result**:
  - Either rejected or accepted (depending on business rules)
- **Actual Result**: Names with numbers accepted. Name John123 displayed on the Dashboard page.
- **Status**: Pass (with observation)
- **Notes**: No character validation on name fields. Acceptable if no business rule requires alphabetic-only names, but worth flagging for product team review.

---

### TC-027: Leading/Trailing Spaces in All Fields
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter data with leading/trailing spaces: "  John  ", "  Doe  ", "  john@example.com  "
  2. Submit form
- **Expected Result**:
  - Application trims spaces OR shows errors
- **Actual Result**: Spaces before and after permitted. Even in the email field, and the login page DOES NOT accept the email without the spaces, but with the spaces before the email.
- **Status**: Fail
- **Notes**: No extra spaces in the name on the Dashboard page except a single white space after the name.

---

## UI/UX Test Cases

### TC-028: Form Field Labels and Placeholders
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Navigate to registration page
  2. Verify all fields have clear labels
  3. Verify placeholder text is helpful
- **Expected Result**:
  - Descriptive labels and helpful placeholders
  - No spelling/grammar errors
- **Actual Result**: PASS — All fields have descriptive labels (First Name, Last Name, Email Address, Phone Number, Street Address, City, ZIP Code, Password, Confirm Password). Placeholders present: "Enter your first name", "Enter your last name", "Enter your email", "Enter your phone number", "Enter your street address", "Enter your city", "Enter your ZIP code", "Create a password", "Confirm your password". No spelling errors found.
- **Status**: Pass
- **Notes**:

---

### TC-029: Form Field Tab Order
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Click in First Name field
  2. Press Tab key repeatedly
  3. Observe focus progression
- **Expected Result**:
  - Tab order follows visual layout (top to bottom)
  - Focus indicator clearly visible
- **Actual Result**: As expected
- **Status**: Pass
- **Notes**: 

---

### TC-030: Required Field Indicators
- **Priority**: Medium
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. View registration form
  2. Look for asterisks (*) or other indicators
- **Expected Result**:
  - Required fields clearly marked
- **Actual Result**: FAIL — No visual indicators (asterisks, "required" text, different styling) for required fields. All fields look identical. Users cannot distinguish required from optional (Terms checkbox, Newsletter checkbox) without attempting submission.
- **Status**: Fail
- **Notes**: See BUG-005

---

### TC-031: Responsive Design - Mobile View
- **Priority**: Medium
- **Preconditions**: Browser resized to mobile width (~375px)
- **Test Steps**:
  1. Open registration page at mobile width
  2. Verify form layout
  3. Attempt to fill and submit form
- **Expected Result**:
  - Form fully usable on mobile
  - All fields accessible
  - No overlapping elements
- **Actual Result**: FAIL — Multiple issues on mobile:
  1. Error messages are hidden (`display: none !important`) — See BUG-002
  2. Submit button is partially cut off (max-height: 35px, negative margin) — See BUG-009
  3. Newsletter checkbox is covered by white overlay — See BUG-011
  Form is NOT fully usable on mobile.
- **Status**: Fail
- **Notes**: See BUG-002, BUG-009, BUG-011. 

---

### TC-032: Responsive Design - Tablet View
- **Priority**: Low
- **Preconditions**: Browser resized to tablet width (~800px)
- **Test Steps**:
  1. Resize browser to tablet width
  2. Verify layout
  3. Complete registration
- **Expected Result**:
  - Form displays properly
  - All functionality works
- **Actual Result**: FAIL — Street Address field is obscured by an "Advertisement" SVG overlay banner. The overlay has `pointer-events: none` so clicking through may work, but the field is visually blocked.
- **Status**: Fail
- **Notes**: See BUG-010

---

### TC-033: Form Data Persistence on Validation Error
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with data
  2. Enter an invalid email (e.g., "notanemail")
  3. Submit form
  4. Observe if data is preserved
- **Expected Result**:
  - Error message displayed
  - Previously entered data remains in fields
- **Actual Result**: PASS — When client-side validation fails (e.g., invalid email), `handleRegister()` returns `false` and the page does not reload. All previously entered field values are preserved. User can correct the error without re-entering everything.
- **Status**: Pass
- **Notes**: This works correctly on desktop. On mobile, the error message itself is hidden (BUG-002), but the form data is still preserved.

---

## Security Test Cases

### TC-034: SQL Injection in Text Fields
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter SQL injection strings:
     - First Name: `'; DROP TABLE users; --`
     - Email: `admin'--@test.com`
  2. Fill other fields with valid data
  3. Submit form
- **Expected Result**:
  - Input sanitized or escaped
  - No SQL errors displayed
- **Actual Result**: PASS — Registration succeeds with SQL injection strings in name/address fields. No SQL errors exposed. Server handles the input safely (input is escaped or parameterized). Verified via automated test.
- **Status**: Pass
- **Notes**: 

---

### TC-035: XSS (Cross-Site Scripting) in Text Fields
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter: First Name `<script>alert('XSS')</script>`
  2. Fill other fields with valid data
  3. Submit form
  4. Check if script executes on dashboard or any page
- **Expected Result**:
  - Scripts NOT executed
  - Input escaped or sanitized
- **Actual Result**: PASS — Registration succeeds with `<script>alert('XSS')</script>` as first name. After login, dashboard displays the literal string as text — no script execution. Dashboard uses `textContent` (not `innerHTML`), which is safe against XSS. 
- **Status**: Pass
- **Notes**: Dashboard rendering is safe, but input should ideally be sanitized at registration to prevent stored XSS in other contexts.

---

### TC-036: Password Field Masking
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Click into Password field
  2. Type a password
  3. Observe characters displayed
- **Expected Result**:
  - Characters masked (dots or asterisks)
- **Actual Result**: PASS — Both Password and Confirm Password fields use `type="password"`, which masks input as dots/bullets by default in all browsers.
- **Status**: Pass
- **Notes**:

---

### TC-037: Terms and Conditions Link
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Look for clickable "Terms and Conditions" text
  2. Click it if it's a link
- **Expected Result**:
  - Link opens Terms and Conditions document
- **Actual Result**: FAIL — "I agree to the Terms and Conditions" is plain text inside a `<label>` element, not a hyperlink. There is no way to view the actual Terms and Conditions before agreeing.
- **Status**: Fail
- **Notes**: Minor UX issue. Users should be able to review terms before agreeing.

---

## Browser Compatibility (Optional)

### TC-038: Registration on Different Browsers
- **Priority**: Medium
- **Preconditions**: Access to multiple browsers
- **Test Steps**:
  1. Test successful registration on Chrome, Firefox, Edge
  2. Test validation on each
- **Expected Result**:
  - Form works identically across browsers
- **Actual Result**: Looks consistent on all three browsers.
- **Status**: Pass
- **Notes**: 

---

## Password Match Validation

### TC-039: Empty Confirm Password Field
- **Priority**: High
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Fill all fields with valid data
  2. Enter password: "SecurePass123!"
  3. Leave Confirm Password field empty
  4. Click "Create Account"
- **Expected Result**:
  - Form NOT submitted
  - Error for empty confirm password
- **Actual Result**: PARTIAL — Browser's `required` attribute on Confirm Password field prevents submission with an empty value. However, if the user enters ANY value (even one character), the password match check won't catch the mismatch.
- **Status**: Pass (HTML required catches empty, but mismatch still bypassed — see BUG-006)
- **Notes**:

---

## Post-Registration Flow

### TC-040: Login with Newly Registered Credentials
- **Priority**: High
- **Preconditions**: Successfully registered a new account
- **Test Steps**:
  1. Register a new account with valid data
  2. After redirect to login page, enter the same email
  3. Enter the same password
  4. Click "Login"
- **Expected Result**:
  - Login successful
  - Redirected to dashboard
  - Dashboard shows registered first name
- **Actual Result**: PASS — Registration succeeds, redirect to login page, login with same credentials succeeds, dashboard displays the registered first name correctly. Full end-to-end flow verified via automated test.
- **Status**: Pass
- **Notes**: Verified via `test_login_with_registered_credentials` automation test.

---

### TC-041: Login with Mismatched Password After Registration
- **Priority**: High
- **Preconditions**: Registered with password "SecurePass123!" and confirm password "DifferentPass456!"
- **Test Steps**:
  1. Register with mismatched passwords (see TC-016)
  2. Try to login with "SecurePass123!"
  3. Then try with "DifferentPass456!"
- **Expected Result**:
  - Determine which password was actually stored
- **Actual Result**: FAIL — Registration succeeds with mismatched passwords (BUG-006). The "Password" field value is the one stored — login works with that value, not the "Confirm Password" value. While storing the primary password is the lesser evil, the mismatch should have been caught before registration.
- **Status**: Fail
- **Notes**: Demonstrates real-world impact of BUG-006. See also TC-016.

---

## Responsive Design - Mobile Specific

### TC-042: Mobile - Error Messages Visibility
- **Priority**: High
- **Preconditions**: Browser at mobile width (<767px)
- **Test Steps**:
  1. Open registration page at 375px width
  2. Enter invalid email (e.g., "notanemail")
  3. Enter short password (e.g., "12")
  4. Click "Create Account"
- **Expected Result**:
  - Error messages visible below fields
- **Actual Result**: FAIL — Error messages are hidden via CSS: `.error-message { display: none !important; visibility: hidden; }`. The form stays on the page (validation fails), but the user sees NO feedback about what's wrong.
- **Status**: Fail
- **Notes**: See BUG-002. The `!important` flag means this cannot be overridden by any other CSS rule.

---

### TC-043: Mobile - Submit Button Fully Visible and Clickable
- **Priority**: High
- **Preconditions**: Browser at mobile width (<767px)
- **Test Steps**:
  1. Open registration page at mobile viewport
  2. Scroll to "Create Account" button
  3. Verify button is fully visible and clickable
- **Expected Result**:
  - Button fully visible with complete text
- **Actual Result**: FAIL — Button has `max-height: 35px`, `margin-bottom: -25px`, and `overflow: hidden` on mobile. Text is clipped and the button area is visually distorted.
- **Status**: Fail
- **Notes**: See BUG-009

---

### TC-044: Mobile - Newsletter Checkbox Accessible
- **Priority**: Medium
- **Preconditions**: Browser at mobile width (<767px)
- **Test Steps**:
  1. Open registration page at mobile viewport
  2. Locate newsletter checkbox
  3. Verify it is visible and clickable
- **Expected Result**:
  - Checkbox visible and interactive
- **Actual Result**: FAIL — White SVG overlay (opacity 0.9) covers the checkbox. It is nearly invisible. The overlay has `pointer-events: none`, so clicking the area does toggle the checkbox, but users can't see it.
- **Status**: Fail
- **Notes**: See BUG-011

---

### TC-045: Mobile - Login "Remember Me" Checkbox Accessible
- **Priority**: Medium
- **Preconditions**: Browser at mobile width (<767px), on LOGIN page
- **Test Steps**:
  1. Open login page at mobile viewport
  2. Locate "Remember Me" checkbox
  3. Verify visible and clickable
- **Expected Result**:
  - Checkbox visible and interactive
- **Actual Result**: FAIL — Similar overlay issue as newsletter checkbox. The `mobile-hidden` class activates an overlay covering the "Remember Me" checkbox on mobile viewport.
- **Status**: Fail
- **Notes**: This is on the login page, not registration, but part of the user journey.

---

## Responsive Design - Tablet Specific

### TC-046: Tablet - Street Address Field Not Obscured
- **Priority**: High
- **Preconditions**: Browser at tablet width (768-1024px)
- **Test Steps**:
  1. Open registration page at ~800px width
  2. Locate Street Address field
  3. Verify no overlay blocking it
  4. Try typing in the field
- **Expected Result**:
  - Field fully visible and usable
- **Actual Result**: FAIL — "Advertisement" SVG overlay covers the field. The overlay has `pointer-events: none`, so the field IS technically clickable/typeable, but users cannot see the field label or their input.
- **Status**: Fail
- **Notes**: See BUG-010

---

## Forgot Password Page

### TC-047: Forgot Password - Reset with Valid Email
- **Priority**: Medium
- **Preconditions**: User is on forgot-password page
- **Test Steps**:
  1. Navigate to forgot-password page
  2. Enter a previously registered email
  3. Select a security question and enter an answer
  4. Click "Send Reset Link"
- **Expected Result**:
  - Meaningful confirmation or reset initiated
- **Actual Result**: FAIL — Always shows "Password reset link has been sent to your email!" regardless of whether the email is registered. No API call made. Entirely client-side fake response.
- **Status**: Fail
- **Notes**: See BUG-012

---

### TC-048: Forgot Password - Reset with Unregistered Email
- **Priority**: Medium
- **Preconditions**: User is on forgot-password page
- **Test Steps**:
  1. Enter an unregistered email (e.g., "doesnotexist@fake.com")
  2. Click "Send Reset Link"
- **Expected Result**:
  - Should not confirm that a reset was sent for non-existent account
- **Actual Result**: FAIL — Same success message displayed: "Password reset link has been sent to your email!" No distinction between registered and unregistered emails.
- **Status**: Fail
- **Notes**: See BUG-012

---

### TC-049: Forgot Password - Security Answer Not Validated
- **Priority**: Medium
- **Preconditions**: User is on forgot-password page
- **Test Steps**:
  1. Enter a valid email
  2. Select a security question
  3. Enter a clearly wrong answer
  4. Click "Send Reset Link"
- **Expected Result**:
  - Wrong answer should be rejected
- **Actual Result**: FAIL — Security answer is completely ignored. Success message shown regardless of answer content. The `handleForgotPassword()` function never reads or validates the security answer.
- **Status**: Fail
- **Notes**: See BUG-012

---

## Test Execution Summary

| Status | Count |
|--------|-------|
| Pass   | 23    |
| Fail   | 26    |
| Blocked| 0     |
| Needs Verification | 0 |
| **Total** | **49** |

### Pass/Fail by Category

| Category | Pass | Fail | Needs Verification |
|----------|------|------|--------------------|
| Navigation | 2 | 0 | 0 |
| Positive (happy path) | 2 | 0 | 0 |
| Required Fields | 2 | 1 | 0 |
| Email Validation | 3 | 2 | 0 |
| Phone Validation | 1 | 2 | 0 |
| Password Validation | 1 | 3 | 0 |
| Address/ZIP | 0 | 2 | 0 |
| Boundary/Edge Cases | 3 | 3 | 0 |
| UI/UX | 3 | 3 | 0 |
| Security | 3 | 1 | 0 |
| Browser Compat. | 1 | 0 | 0 |
| Password Match | 1 | 0 | 0 |
| Post-Registration | 1 | 1 | 0 |
| Mobile Responsive | 0 | 4 | 0 |
| Tablet Responsive | 0 | 1 | 0 |
| Forgot Password | 0 | 3 | 0 |

### Bugs Referenced

| Bug ID | Test Cases | Summary |
|--------|------------|---------|
| BUG-001 | TC-009, TC-010, TC-011 | Weak email regex |
| BUG-002 | TC-031, TC-042 | Error messages hidden on mobile |
| BUG-003 | TC-017, TC-018 | Password min length only 4 chars |
| BUG-004 | TC-013, TC-014, TC-015 | Phone accepts any characters |
| BUG-005 | TC-030 | No required field indicators |
| BUG-006 | TC-016, TC-039, TC-041 | Password match always passes |
| BUG-007 | TC-006 | Terms checkbox not enforced |
| BUG-008 | TC-020, TC-021 | ZIP code accepts letters |
| BUG-009 | TC-043 | Mobile submit button cut off |
| BUG-010 | TC-032, TC-046 | Tablet Street Address obscured |
| BUG-011 | TC-044 | Mobile newsletter checkbox obscured |
| BUG-012 | TC-047, TC-048, TC-049 | Forgot password always succeeds |

---

**Execution Date**: Feb 12, 2026
**Tester**: Dragana Munitlic
**Environment**: Chrome 133, Windows 10
