You have an Apache-style access log at `/app/access.log`. Analyze it and write one JSON object to `/app/report.json`. Treat each non-empty log line as one request. The client IP is the first whitespace-delimited field, and the requested path is the path between the HTTP method and protocol in the quoted request line. Do not modify the input log.

Success criteria:

1. Create `/app/report.json`.
2. The file contains valid JSON with exactly these keys and types: `total_requests` (integer), `unique_ips` (integer), and `top_path` (string).
3. The values are exactly `total_requests = 6`, `unique_ips = 3`, and `top_path = "/index.html"`.
