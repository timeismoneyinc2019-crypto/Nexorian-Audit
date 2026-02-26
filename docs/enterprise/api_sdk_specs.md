# Nexorian Enterprise Platform: API & SDK Specifications (Deliverable 3)

## 1. REST API Standards
The Nexorian API follows a **Deterministic REST** pattern.
- **Base URL**: `https://api.nexorian.org/v1/`
- **Authentication**: `X-Nexus-Auth: <JWT>` + `X-Nexus-Signature: <SHA256(payload + key)>`
- **Rate Limiting**: Tier-based headers (`X-Epoch-Limit`, `X-Epoch-Remaining`).

### 1.1 Core Endpoints
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/kernel/execute` | POST | Submits a command for deterministic execution. |
| `/governance/rules` | GET/POST | Manages the active Law Envelopes. |
| `/audit/ledger` | GET | Retrieves verifiable execution proofs. |
| `/sim/replay` | POST | Replays a state transition in the Sandbox. |

## 2. SDK Architecture
The SDKs provide a high-level "Governance Interface" that abstracts the cryptographic signing layer.
- **Languages Supported**: Python, JavaScript/TS, Java, Go, C#.
- **Deterministic Validation**: Every SDK includes an offline validation engine that checks "Law Envelope" compliance before sending the payload to the wire.

## 3. Event Interface (Webhooks vs gRPC)
- **Webhooks**: For async notification of audit completions.
- **gRPC**: For high-throughput, low-latency node-to-node deterministic communication.

---
*Signed: Principal Platform Engineer, Nexorian Corporation*
