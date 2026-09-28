# Feature flags and rollout layers

A feature can have shipped documentation, a client toggle, a server gate, an account entitlement, a device requirement, and an action permission. Those are separate conditions.

This page records **September 27, 2026 observations from one authenticated web account**, not product defaults. No flags were changed for this documentation update.

## How the client values were identified

The web bundle defined typed configuration readers over hashed keys. An inline page bootstrap supplied 43 values. Matching reader usage to those values established the meanings below. The browser's consumed bootstrap array was empty, while inline script text still held the initialization data.

This is client evidence. It does not reveal the full backend configuration, mobile flags, or every condition in the feature's implementation.

| Web feature | Hashed key | Observed value |
|---|---|---|
| Voice | `572a7c97` | false |
| Voice design | `7951eeff` | false |
| Home Link | `7402e958` | false |
| Computer tab | `5e1fb489` | false |
| Muse email | `5325d097` | false |
| Confidential VM | `df110356` | false |
| Redteaming | `05344cb9` | false |
| Tool mocking | `83580e32` | false |
| Infinite feed | `d01136f4` | false |
| Surveys | `788be016` | false |
| Dictation | `49572c1a` | true |
| Invites | `2223e52e` | true |
| Invite redemption | `0de9ebf8` | true |
| Mac app download | `8c1233db` | true |
| Subscriptions | `e3507fea` | true; additional eligibility checks existed |
| Telegram channel | `c6e95b18` | false |
| WhatsApp channel | `6fb3f373` | true |
| Messenger channel | `dde7768a` | false |

These keys may change with the web bundle. A true value is not necessarily the only prerequisite; a false UI value does not prove the corresponding capability is absent from every other surface.

For example, paired Mac tools were observed while the web Computer tab was hidden. Muse email documentation was installed while its mailbox endpoint rejected access.

## Local browser preferences

The inspected client also recognized these local-storage preferences; all were unset in that check:

| Key | Observed purpose |
|---|---|
| `hatch:debug:feed-infinite-scroll` | Local opt-in combined with a server flag |
| `hatch:debug:voice-enabled` | Client UI override; not proof of service entitlement |
| `hatch:debug:idea-color-icons` | Presentation preference |

A local UI override does not grant a server capability or permission. Security/attestation controls are not equivalent to cosmetic preferences.

## Backend names found in compiled code

Examples included:

| Area | Compiled names |
|---|---|
| Browser/computer | `hatch_computer_enabled`, `hatch_browser_open_task_recovery_enabled`, `hatch_browser_clipboard_sync_enabled` |
| Conversation UX | `hatch_disable_commentary`, `hatch_model_reactions_enabled`, `hatch_summarization_message_enabled` |
| Memory/summaries | `hatch_memory_use_remote_model`, `hatch_summarization_writeback_enabled` |
| Learning/discovery | `hatch_fleet_learning_consumption_enabled`, `hatch_serendipity_enabled`, `hatch_discovery` |
| Connected sources | `hatch_connector_sync_enabled`, `hatch_flight_email_monitoring_enabled`, `hatch_sync_verification` |
| Messaging | `hatch_channel_imessage_groups_enabled`, `hatch_channel_whatsapp_groups_enabled`, `abra_hatch_agent_to_agent` |
| Apps/sharing/feed | `hatch_spaces_enabled`, `abra_hatch_artifact_sharing_disabled`, `abra_hatch_stateful_artifact_sharing_disabled`, `hatch_feed_generation_disabled` |

**Effective values were not established.** These names are leads for future investigation. They may be unused, retired, conditional, or supplied by services outside the guest.

Compiled service-client paths included `/hatch/check_gatekeepers`, `/hatch/evaluate_configs`, `/hatch/log_exposure`, and `/hatch/config-bundle:latest`. They were not verified as owner-callable endpoints. No supported public getter/setter for the full effective backend gate set was found.

## A useful experiment answers one question

To ask “is this feature available?”, inspect its supported capability surface, prerequisites and one harmless operation. To ask “why is this tab hidden?”, inspect the current client configuration. To ask “does this compiled flag control the feature?”, find a consuming code path and effective state.

Do not substitute one of those answers for another. See [capability atlas](capabilities.md) and [evidence](evidence.md).
