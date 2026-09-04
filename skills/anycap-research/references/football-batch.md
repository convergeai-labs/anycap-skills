# Batch / Squad Mode

Turn a list of player names (or a whole World Cup squad) into a structured table or JSON array.

## Principle

One structured grounding call per player. Do **not** crawl every search result;
prune first and retrieve only claim-bearing profiles.

## Step 1 -- Get the squad list

If you already have the names, skip to Step 2. To fetch a national-team squad:

```bash
anycap search --prompt 'List the full <COUNTRY> 2026 World Cup squad as a JSON array of player names. Only the JSON.' \
  | jq -r '.data.content'
```

Verify roster completeness against Wikipedia if the squad must be exact (see [football-verify.md](football-verify.md)) -- squads change due to injuries.

## Step 2 -- Loop one profile per player

Save names to a file (one per line), then loop:

```bash
# players.txt: one player name per line
while IFS= read -r name; do
  [ -z "$name" ] && continue
  profile=$(anycap search --prompt "Basic profile of footballer $name as JSON with fields: full_name, date_of_birth, nationality, height, position, current_club, shirt_number, national_team. Only the JSON." \
    | jq -r '.data.content' \
    | sed -e 's/^```json//' -e 's/^```//' -e '/^$/d')
  echo "$profile" | jq -c --arg q "$name" '. + {query_name:$q}'
done < players.txt | jq -s '.' > squad.json
```

Notes:

- The `sed` strips ``` ```json ``` fences so the inner object is valid for `jq`.
- `jq -s '.'` at the end slurps all per-player objects into a single array.
- Add `--arg q "$name"` to keep the original query name for traceability.

## Step 3 -- Render a table

From `squad.json`, produce a Markdown table:

```bash
jq -r '["Name","DOB","Nat","Pos","Club","No."], (.[] | [.full_name, .date_of_birth, .nationality, .position, .current_club, (.shirt_number|tostring)]) | @tsv' squad.json \
  | column -t -s $'\t'
```

## Performance

- If your runtime supports concurrency, run several grounding calls in parallel (background jobs) and collect outputs, rather than strictly sequential. Respect rate limits -- back off on `RATE_LIMITED`.
- For large lists, consider `--query --no-crawl` first to confirm each name resolves to a real player before running full retrieval.

## Robustness

- Skip and log any player whose profile fails to parse as JSON; do not abort the whole batch.
- Record `_retrieved_at` once per run; club/number are point-in-time.
