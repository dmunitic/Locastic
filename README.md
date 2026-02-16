# QA Test Assignment - User Registration

QA testing of the [QA Test Web Application](https://qa-test-web-app.vercel.app/) registration flow, covering manual testing, bug reporting, and automated testing with Playwright.

## Deliverables

| Document | Description |
|----------|-------------|
| [Test Plan](Test%20Plan.md) | Testing strategy, scope, objectives, and schedule |
| [Test Cases - Manual Execution](Test%20Cases%20-%20Manual%20Execution.md) | 49 test cases with execution results (23 pass, 26 fail) |
| [Test Cases Template](Test%20Cases%20Template.md) | Clean reusable test plan (all cases pre-filled, no execution data) |
| [Bug Report](Bug%20Report.md) | 16 bugs documented with steps to reproduce, screenshots, and recommendations |
| [Automation Suite](playwright-tests/) | Playwright + Python test suite (32 tests) with setup instructions |
| [Test Execution Report](playwright-tests/report.html) | HTML report from the latest automation run |

## Summary

### Test Execution

- **49 test cases** across 16 categories (navigation, validation, security, responsive design, etc.)
- **23 passed**, **26 failed** — all failures traced to documented bugs

### Bugs Found

| Severity | Count |
|----------|-------|
| Critical | 4 |
| High | 4 |
| Medium | 8 |
| **Total** | **16** |

Key findings: broken password match validation, terms checkbox not enforced, error messages hidden on mobile, weak email regex, forgot password page entirely non-functional.

### Automation

- **32 automated tests** using Python, Playwright, and pytest
- Element-centric Page Object Model architecture
- 13 tests pass, 19 xfail (documenting known bugs — auto-alert if a bug gets fixed)
- Covers desktop, mobile, and tablet viewports

See [playwright-tests/README.md](playwright-tests/README.md) for setup and run instructions.

## Environment

- **Application**: https://qa-test-web-app.vercel.app/
- **Browser**: Chrome 133 (primary), Firefox, Edge
- **OS**: Windows 10
- **Viewports**: Desktop (1280px), Tablet (800px), Mobile (375px)
