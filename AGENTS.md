# AGENTS.md

Instructions for any AI coding agent (Claude, Copilot, Cursor, OpenCode, etc.) working in this
repository. The checklist below is the canonical set of rules for changes to `README.md`.
CodeRabbit's `path_instructions` for `README.md` in `.coderabbit.yml` point back to this file, so
following it here is what makes generated changes pass review on the first try. The one place that
keeps its own independent copy of these rules is `pre_merge_checks.custom_checks` in
`.coderabbit.yml` — that check runs in a sandbox that can't read repo files, so if you change a
rule here, update that check's `instructions` to match.

## What this repo is

`magictools` is a curated, "awesome-list" style **README.md** of game development resources. There
is effectively no application code to build or test — the primary artifact an agent will touch is
`README.md`, and the main "feature work" in this repo is adding, editing, or reorganizing link
entries in it.

## Rules that apply to any change to `README.md`

These rules apply to **every new or modified list entry** (lines starting with `- ` or `* ` that
contain a `[text](url)` link). Pre-existing, untouched entries should be left alone even if they
would fail one of these checks — don't "fix" unrelated entries as a side effect of your change,
beyond re-sorting required to keep the list alphabetical.

### 1. Scope — only touch what you're asked to change
- Only add/modify the entries relevant to the task.
- Do not reflow, re-emoji, or re-sort entries that are untouched and unrelated to your change.
- If inserting a new entry forces an existing entry to move position, that's fine — but don't alter
  its content.

### 2. Alphabetical ordering
- Every section/subsection (e.g. `#### Assets/Placeholders`, `#### Spritesheet Tools`,
  `### Books`, etc.) is sorted A-Z by link text (the text inside `[]`).
- When adding a new entry, insert it at the correct alphabetical position within its section,
  comparing against both existing and other newly added entries.
- Before finishing, double check the resulting section is still fully sorted A-Z.

### 3. License emoji is required
- Every new entry must start with exactly one of:
  - `:free:` — Free
  - `:tada:` — Open Source
  - `:moneybag:` — Paid
  - `:money_with_wings:` — Partially Free
- Use the literal `:emoji_name:` shortcode text, not a unicode emoji character (e.g. not `🆓`).
- **Exception**: entries added under `### Blogs and Portals`, `### Videos/Podcasts`,
  `### Game Jams`, and `### Communities` do **not** require a license emoji.

### 4. Link validation
- Links must use `https://` only. Never add `http://`, `ftp://`, `file://`, `mailto:`,
  `javascript:`, etc.
- Links must be well-formed and reachable (not a 404/dead domain). Check the URL before adding it
  if at all possible.
- If a link points to a GitHub repo (`https://github.com/<owner>/<repo>`), it must have **at least
  100 stars**. Verify star count before adding; don't add repos below that threshold.

### 5. Game development relevance
- Every new link must be explicitly about game development (engines, game-specific tools, game
  art/audio assets, game tutorials/books, game-dev communities, etc).
- Do not add general-purpose tools/sites that merely *could* be used while making a game but have
  no game-dev-specific focus.

### 6. Format of an entry
Match the existing style exactly:

```
- :free: [Tool Name](https://example.com/) - short description of what it does.
```

- One entry per line.
- Short, factual description after a ` - `.
- No trailing blank line changes inside a list unless adding/removing an entry requires it.

## Other files
- `.github/CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md` contain the human-facing
  version of these same rules — keep them in sync if you change the rules here.
- `.coderabbit.yml` has two relevant parts: `reviews.path_instructions` for `README.md` defers to
  this file plus a few reviewer-behavior directives (comment inline, tag the author, request
  changes on failure); `reviews.pre_merge_checks.custom_checks` keeps a full, independent copy of
  the checklist, since that merge-blocking check can't read `AGENTS.md`. Keep that copy in sync
  with the checklist above.

## Before finishing a change to README.md
1. Re-read the section(s) you edited top to bottom and confirm alphabetical order.
2. Confirm every new entry has a valid license emoji (or is in an exempt section).
3. Confirm every new link is `https://`, well-formed, and (if a GitHub repo) has 100+ stars.
4. Confirm every new link is genuinely game-dev relevant.
5. Confirm you haven't modified unrelated, pre-existing entries.
