# <Title>

<!--
  Spec writing guide:
  - Goal: one sentence describing what must be true after this change.
  - Scope: explicit in-scope behaviors, modules, or interfaces. Keep it tight.
  - Non-goals: what this change deliberately excludes; prevents scope creep.
  - Current Context: repository facts that constrain the change (existing APIs,
    data formats, dependency versions, deployment model).
  - Requirements: numbered list of observable behaviors or capabilities.
  - Acceptance Criteria: each criterion gets a stable identifier (AC-1, AC-2...).
    Format: "When <precondition>, then <observable result>." Must be pass/fail.
  - Constraints: technical limits (compatibility, security, performance, migration).
  - Open Questions: unresolved decisions that must be answered before planning.
    Remove all open questions before the spec is approved.
-->

## Goal

<!-- One sentence. Example: "Users can reset their password via email without exposing account enumeration." -->

## Scope

<!-- What's included. Example: "POST /auth/forgot-password endpoint, email template, rate limiting at 3 requests per hour per email." -->

## Non-goals

<!-- What's explicitly excluded. Example: "Two-factor authentication, OAuth provider linking, in-app password change UI." -->

## Current Context

<!-- Repository facts only. Example: "Existing User model has email (unique, indexed). Mailer uses SendGrid. No rate limiter installed." -->

## Requirements

<!--
  Numbered list of observable behaviors.
  Example:
  1. A user can request a password reset by providing their email address.
  2. The system sends a single-use, time-limited reset token to that email.
  3. The token expires after 1 hour and cannot be reused.
-->

## Acceptance Criteria

<!--
  Each criterion must be independently verifiable with a pass/fail result.
  Do not hide implementation steps here — those belong in the plan.

  Example:
  - AC-1: When POST /auth/forgot-password is called with a registered email,
    the response is always 200 with a generic confirmation message, regardless
    of whether the email exists.
  - AC-2: When a valid reset token is submitted to POST /auth/reset-password,
    the user's password is updated and the token is invalidated.
  - AC-3: When the same reset token is submitted a second time, the response
    is 400 with an error indicating the token has been used or expired.
-->

- AC-1:

## Constraints

<!--
  Technical limits the implementation must respect.
  Example:
  - Must not expose whether an email is registered (no enumeration).
  - Reset tokens must be cryptographically random, at least 32 bytes.
  - Email delivery must not block the HTTP response (>2s timeout degrades gracefully).
-->

## Open Questions

<!--
  Unresolved decisions. Must be answered before planning.
  Example:
  - Should we reuse the existing mailer queue or send synchronously?
  - What is the minimum password complexity requirement?
-->
