# Follow real kinds of work through the system

These are explanatory walkthroughs of the documented interfaces, not claims that the exact example jobs were executed. Each ends with the evidence you would need to establish success.

## 1. “Analyze this CSV and make a chart”

**Main pieces:** client → root agent/harness → file/shell tools → generated artifact → client.

1. The user supplies a file and asks a question.
2. The runtime prepares an inference turn with the request and available tool definitions.
3. The model requests a file inspection or a shell command.
4. A process in the cell reads the file and runs code. It can use an installed library, subject to the cell's resources and filesystem/network rules.
5. Tool output returns to the runtime. Further inference can identify problems, revise code or explain the result.
6. The finished chart is stored/delivered through the applicable artifact or file surface.

**What this teaches:** cell CPU runs the data-processing code; remote inference generates decisions and responses. Installing a plotting library changes the tool environment, not model weights.

**Verify:** correct input rows/units, process completion, actual output file and rendered chart. A command that starts is not proof a chart is correct.

## 2. “Check this website using my existing login”

**Main pieces:** conversation owner → browser task → browser broker/session → website → handoff.

1. The owner creates a self-contained browsing brief.
2. The runtime accepts a browser task and returns a handle.
3. The browser service performs permitted interactions in its browser/session context.
4. If user input or approval is required, the task can wait.
5. A continuation steers the existing task.
6. The task returns a result to its owner.

**What this teaches:** browser task state, owning-agent context and authentication state are different objects. A fresh task is not guaranteed to have either a fresh cookie jar or the desired login.

**Verify:** task ownership, current state, observed page/action result and returned handoff. Do not repeat a consequential action merely because the final report is missing.

See [browser lifecycle](06-browser.md).

## 3. “Build a small research app”

**Main pieces:** artifact/Space → SDK → managed search/inference → application state → UI.

A possible design using the inspected SDK:

1. The app requests sources through `ctx.tool.web_search`.
2. It sends selected source content to `ctx.inference.complete` with a result schema.
3. It stores useful structured fields in its application data.
4. It emits progress or invalidates a query so the UI refreshes.
5. For a longer task, it delegates through `ctx.agent.spawnTask` and handles completion.

**What this teaches:** app inference, background agent work and user chat are related but distinct paths. The inspected public inference options did not expose a model/effort selector.

**Verify:** schema validation, saved data, refresh behavior, error handling and eventual completion. An accepted background task does not mean the app's requested state already exists.

See [Spaces interfaces](capabilities.md#apps-spaces-and-artifacts).

## 4. “Use a connected service or a paired device”

**Main pieces:** tool/skill → permission/capability interface → service or device → result.

1. The runtime identifies the appropriate tool and its instructions.
2. It checks whether the connection/device and necessary action are available.
3. The operation follows the applicable permission or approval path.
4. A service or reachable device performs the action.
5. The result returns, and the requested effect is verified where possible.

**What this teaches:** installed documentation is only the first prerequisite. A connected account may have restricted actions; a paired device may be offline; a web tab can be hidden while another device surface works.

**Verify:** permission scope, target identity, response and actual effect. Keep “request sent” separate from “device changed.”

## 5. “Remember this preference, then correct it later”

**Main pieces:** conversation → standing/structured memory → retrieval → provenance/correction.

1. The user gives a durable preference.
2. Installed guidance instructs the agent to capture useful information.
3. Later retrieval can surface the stored claim.
4. A correction should reconcile relevant records and derived uses.
5. Provenance can explain the source and relationship to older claims.

**What this teaches:** editing a Markdown note is one possible change. It does not prove all structured records, indexes or dependent automations were updated.

**Verify:** the relevant stored source, retrieval result and affected workflow. For deletion, use the installed forget procedure and its confirmation requirements.

See [memory](12-memory.md).

## A reusable way to trace anything

Write down this chain:

```text
User intent
→ owning session/task
→ selected tool or interface
→ execution/service boundary
→ returned result
→ persisted state or external effect
→ user-visible delivery
```

At every arrow ask: **what evidence shows this step happened?** That question is more useful than assuming that a successful first step proves the rest.
