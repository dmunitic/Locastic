# Test Cases - User Registration

## Test Case Format

Each test case includes:
- **TC-ID**: Unique identifier
- **Title**: Brief description
- **Priority**: High/Medium/Low
- **Preconditions**: Setup required before test
- **Test Steps**: Numbered steps to execute
- **Expected Result**: What should happen
- **Actual Result**: What actually happened (filled during execution)
- **Status**: Pass/Fail/Blocked/Not Run
- **Notes**: Any additional observations

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

---

### TC-027: Leading/Trailing Spaces in All Fields
- **Priority**: Low
- **Preconditions**: User is on registration page
- **Test Steps**:
  1. Enter data with leading/trailing spaces: "  John  ", "  Doe  ", "  john@example.com  "
  2. Submit form
- **Expected Result**:
  - Application trims spaces OR shows errors
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

---

### TC-048: Forgot Password - Reset with Unregistered Email
- **Priority**: Medium
- **Preconditions**: User is on forgot-password page
- **Test Steps**:
  1. Enter an unregistered email (e.g., "doesnotexist@fake.com")
  2. Click "Send Reset Link"
- **Expected Result**:
  - Should not confirm that a reset was sent for non-existent account
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

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
- **Actual Result**: [To be filled]
- **Status**: Not Run
- **Notes**:

---

## Test Execution Summary

| Status | Count |
|--------|-------|
| Pass   | 0     |
| Fail   | 0     |
| Blocked| 0     |
| Not Run| 49    |
| **Total** | **49** |

**Test Execution Date**: [Date]
**Tester**: [Your Name]
**Environment**: [Browser/OS details]
