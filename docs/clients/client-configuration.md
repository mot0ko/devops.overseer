# Reste client Configuration

This file defines how **DevOps Overseer** connects to a REST API using its configuration.
If mostly contains the usual REST API client settings in addition of some internal commodities (like the `include` field).
The authentication settings are defined in there own documentation due to multiple features of redirection and reusability for local users that are clearly out of scope for this configuration documentation.

---

## General fields

### `include`
```yaml
include:
  - "~/.devops-overseer/confluence-cloud.yml"
  - "./.devops-overseer/confluence-cloud.yml"
  - "~/.config/devops-overseer/confluence-cloud.yml"
  - "~/.config/devops-overseer/configs/clients/confluence-cloud.yml"
```
- **Purpose:** additional configuration files to merge or override values from.
- **Typical usage:**
  - Global config in `$HOME/.devops-overseer/`
  - Project-specific config in `./.devops-overseer/`
  - Centralized config in `$HOME/.config/devops-overseer/`

---

### `logger`
```yaml
logger:
  name: confluence-cloud
```
- **Fields:**
  - `name`: name for the logger instance. Used for filtering, formatting, or sending logs to specific outputs.

---

### `user-agent`
```yaml
user-agent: devops-overseer-RestClient/1.0
```
- **Purpose:** the `User-Agent` header attached to all requests.
- **Default/Example:** `"devops-overseer-RestClient/1.0"`

---

### `timeout`
```yaml
timeout: 15.0
```
- **Purpose:** maximum time to wait for an HTTP request before failing.

---

### `max-retries`
```yaml
max-retries: 3
```
- **Purpose:** number of times to retry failed HTTP requests before giving up.

---

### `backoff-factor`
```yaml
backoff-factor: 0.5
```
- **Purpose:** delay multiplier for retries (exponential backoff).
  - Example: with `backoff-factor: 0.5`, retries will wait `0.5s`, `1s`, `2s`, etc.

---

### `extra-headers`
```yaml
extra-headers:
```
- **Purpose:** additional HTTP headers to include in every request.
- **Default:** empty (no extra headers).

---

### `endpoints`
```yaml
endpoints:
  myself:
    path: /rest/api/3/myself
```
- **Purpose:** defines API endpoints with their relative paths, to be called with their identifiers in the code (calling `myself` directly)..
- **Example:**
  - `myself`: the `myself` example is often present in REST APIs giving access to your own profile (like Atlassian for example).
  - `path`: relative URL path (`/rest/api/3/myself`).

---
