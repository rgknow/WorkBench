# API Reference (stub)

## GET /health
Returns `{ status: "ok" }`.

## GET /assessment/items
Returns list of assessment items (MCQ/short answer).

## POST /assessment/submit
Body: `{ user_id, item_id, answer }`. Returns `{ ok, score }`.

## GET /progress/{user_id}
Returns progress card metrics: creativity_index and skills radar.
