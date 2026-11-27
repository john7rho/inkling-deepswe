# Results: full run

113 tasks, 112 graded, 21 solved (18.8% of graded, 18.6% of all tasks).

| language | solved |
|---|---|
| go | 8/33 |
| javascript | 1/5 |
| python | 3/34 |
| rust | 1/5 |
| typescript | 8/35 |

Averaged over graded tasks: 61.6% of target (fail-to-pass) tests pass, 95.6% of existing (pass-to-pass) tests still pass, partial score 0.876.

Agent exit status: Submitted 87, TimeExceeded 14, LimitsExceeded 10, RuntimeError 1, RepeatedFormatError 1.

`job` is the Pier job each trial ran in: `full-v3` (harness b76a805) for 108 tasks, `full-v2` (harness a426ca1) for the 5 that finished there before the harness change and weren't rerun.

| task | lang | reward | f2p | p2p | steps | min | compactions | exit | job |
|---|---|---|---|---|---|---|---|---|---|
| abs-module-cache-flags | go | 1 | 20/20 | 3/3 | 65 | 25 | 1 | Submitted | full-v3 |
| abs-stepped-slices | go | 1 | 6/6 | 6/6 | 129 | 77 | 3 | Submitted | full-v3 |
| actionlint-action-pinning-lint | go | 1 | 55/55 | 145/145 | 93 | 57 | 3 | Submitted | full-v3 |
| adaptix-name-mapping-aliases | python | 0 | 37/44 | 2738/2738 | 170 | 98 | 6 | Submitted | full-v3 |
| aiomonitor-task-snapshots-diff | python | 0 | 47/53 | 8/8 | 59 | 43 | 2 | Submitted | full-v3 |
| anko-default-function-arguments | go | 0 | 0/2 | 114/119 | 149 | 100 | 4 | TimeExceeded | full-v3 |
| anko-typed-variable-bindings | go | 0 | 6/9 | 94/94 | 123 | 42 | 3 | Submitted | full-v3 |
| arcane-drift-detection-baselines | go | 1 | 82/82 | 2/2 | 146 | 75 | 5 | Submitted | full-v2 |
| arktype-json-schema-refs-dependencies | typescript | 0 | 15/25 | 1679/1679 | 199 | 82 | 5 | LimitsExceeded | full-v3 |
| awilix-async-container-initialization | typescript | 1 | 24/24 | 162/162 | 36 | 27 | 0 | Submitted | full-v2 |
| bandit-incremental-cache-control | python | 0 | 69/88 | 275/275 | 147 | 79 | 5 | Submitted | full-v3 |
| bandit-interprocedural-taint-checks | python | 0 | 59/66 | 293/293 | 58 | 48 | 1 | Submitted | full-v3 |
| bandit-structured-nosec-directives | python | 0 | 67/69 | 279/282 | 47 | 61 | 1 | Submitted | full-v3 |
| boa-hierarchical-evaluation-cancellation | rust | 0 | 0/17 | 7/7 | 188 | 83 | 6 | Submitted | full-v3 |
| cattrs-partial-structuring-recovery | python | 0 | 67/69 | 7/7 | 68 | 57 | 2 | Submitted | full-v3 |
| clack-async-autocomplete-options | typescript | 0 | 72/82 | 643/643 | 64 | 38 | 1 | Submitted | full-v3 |
| claude-code-by-agents-recursive-delegation | typescript | 0 | 6/7 | 31/31 | 46 | 35 | 1 | Submitted | full-v3 |
| cliffy-config-file-parsing | typescript | 0 | 32/37 | 451/451 | 173 | 78 | 4 | Submitted | full-v3 |
| csstree-shorthand-expansion-compression | javascript | 0 | 0/79 | 16715/16715 | 70 | 102 | 1 | TimeExceeded | full-v3 |
| dasel-html-document-format | go | 0 | 135/146 | 1012/1012 | 79 | 46 | 2 | Submitted | full-v3 |
| dateutil-rfc5545-timezone-interop | python | 0 | 65/67 | 2035/2035 | 91 | 51 | 2 | Submitted | full-v2 |
| drizzle-orm-window-function-builders | typescript | 1 | 130/130 | 566/566 | 117 | 57 | 3 | Submitted | full-v3 |
| dynamodb-toolbox-conditional-attribute-requirements | typescript | 0 | 0/31 | 1156/1267 | 200 | 95 | 9 | LimitsExceeded | full-v3 |
| dynamodb-toolbox-lazy-recursive-schemas | typescript | 0 | 10/37 | 1267/1267 | 148 | 98 | 8 | Submitted | full-v3 |
| effect-sse-httpapi-streaming | typescript | 0 | 0/47 | 0/70 | 200 | 84 | 9 | LimitsExceeded | full-v3 |
| eicrud-keyset-pagination-cursor | typescript | 0 | 0/14 | 159/168 | 103 | 38 | 1 | Submitted | full-v3 |
| etree-xml-diff-patch | go | 0 | 48/52 | 15/15 | 59 | 35 | 1 | Submitted | full-v3 |
| expr-try-catch-errors | go | 0 | 0/79 | 66265/66265 | 139 | 90 | 4 | Submitted | full-v3 |
| fastapi-deprecation-response-headers | python | 0 | 134/137 | 3134/3134 | 182 | 98 | 5 | Submitted | full-v3 |
| fastapi-implicit-head-options | python | 0 | 31/43 | 3132/3134 | 153 | 98 | 4 | Submitted | full-v3 |
| fd-deterministic-multi-key-sorting | rust | 1 | 43/43 | 109/109 | 75 | 39 | 2 | Submitted | full-v3 |
| geo-shapeindex-serialization | go | 0 | 14/24 | 599/599 | 66 | 30 | 1 | Submitted | full-v3 |
| go-critic-doc-link-checker | go | 0 | 2/3 | 15/16 | 155 | 97 | 4 | Submitted | full-v3 |
| go-genai-streamed-function-args | go | 0 | 5/6 | 62/62 | 69 | 47 | 2 | Submitted | full-v2 |
| go-git-worktree-merge-conflicts | go | 0 | 0/17 | 0/2 | 95 | 101 | 3 | TimeExceeded | full-v3 |
| goreleaser-retry-publish-auditing | go | 1 | 29/29 | 29/29 | 64 | 39 | 2 | Submitted | full-v3 |
| gql-incremental-graphql-delivery | python | 0 | 16/17 | 811/811 | 200 | 98 | 9 | LimitsExceeded | full-v3 |
| happy-dom-abort-pending-body-reads | typescript | 1 | 14/14 | 165/165 | 115 | 71 | 5 | Submitted | full-v3 |
| happy-dom-deterministic-intersectionobserver | typescript | 0 | 12/14 | 9/9 | 43 | 19 | 0 | Submitted | full-v3 |
| helm-array-merge-strategies | go | 0 | 20/47 | 12/12 | 160 | 86 | 4 | Submitted | full-v3 |
| helm-unified-manifest-stream | go | 1 | 5/5 | 2/2 | 168 | 86 | 4 | Submitted | full-v3 |
| httpx-deterministic-cookie-store | typescript | 0 | 112/115 | 1280/1281 | 38 | 25 | 0 | Submitted | full-v3 |
| httpx-multipart-response-parsing | python | 1 | 122/122 | 1272/1272 | 40 | 29 | 0 | Submitted | full-v3 |
| httpx-streaming-json-iteration | python | 0 | 94/108 | 1404/1404 | 41 | 16 | 0 | Submitted | full-v3 |
| igel-persist-feature-schema | python | 0 | 6/24 | 2/2 | 55 | 30 | 1 | Submitted | full-v3 |
| ink-grid-box-layout | typescript | 0 | 0/25 | 49/49 | 86 | 98 | 2 | Submitted | full-v3 |
| ipython-session-bundle-replay | python | 0 | 7/17 | 29/29 | 55 | 36 | 1 | Submitted | full-v3 |
| katex-multicolumn-array-spans | javascript | 0 | 0/94 | 599/599 | 200 | 90 | 5 | LimitsExceeded | full-v3 |
| kcp-go-multiplexed-kcp-streams | go |  |  |  |  |  |  | RuntimeError | full-v3 |
| kea-atomic-signal-selectors | typescript | 0 | 0/12 | 139/139 | 16 | 32 | 0 | RepeatedFormatError | full-v3 |
| kgateway-consistent-hash-policy | go | 1 | 2/2 | 214/214 | 103 | 42 | 3 | Submitted | full-v3 |
| kombu-single-active-consumer-priority | python | 0 | 83/85 | 1421/1421 | 83 | 58 | 2 | Submitted | full-v3 |
| kombu-virtual-queue-dead-lettering | python | 0 | 68/76 | 1412/1412 | 104 | 50 | 3 | Submitted | full-v3 |
| koota-composite-trait-aspects | typescript | 0 | 0/51 | 172/172 | 100 | 100 | 5 | TimeExceeded | full-v3 |
| koota-deferred-mutation-buffer | typescript | 0 | 0/71 | 128/128 | 78 | 101 | 3 | Submitted | full-v3 |
| koota-entity-snapshot-rollback | python | 0 | 83/84 | 47/47 | 96 | 80 | 3 | Submitted | full-v3 |
| koota-pair-relation-tracking | typescript | 0 | 0/38 | 172/172 | 113 | 91 | 6 | Submitted | full-v3 |
| koota-query-predicates | typescript | 0 | 0/43 | 159/172 | 147 | 100 | 7 | TimeExceeded | full-v3 |
| kysely-window-grouping-helpers | typescript | 0 | 0/254 | 0/22 | 157 | 96 | 5 | Submitted | full-v3 |
| langchain-request-coalescing | python | 0 | 48/50 | 232/232 | 52 | 40 | 1 | Submitted | full-v3 |
| mashumaro-flattened-dataclass-fields | python | 0 | 38/66 | 30013/30014 | 174 | 86 | 5 | Submitted | full-v3 |
| meriyah-explicit-resource-declarations | typescript | 0 | 46/49 | 51462/51469 | 177 | 84 | 5 | Submitted | full-v3 |
| mnamer-daemon-watch-lifecycle | python | 1 | 51/51 | 319/319 | 46 | 37 | 1 | Submitted | full-v3 |
| mobly-grouped-test-barriers | python | 0 | 72/79 | 808/808 | 106 | 89 | 3 | Submitted | full-v3 |
| narwhals-rolling-window-suite | python | 0 | 80/103 | 10093/10093 | 198 | 84 | 7 | Submitted | full-v3 |
| numba-stencil-boundary-modes | python | 0 | 1/29 | 729/827 | 115 | 100 | 3 | TimeExceeded | full-v3 |
| obsidian-linter-auto-table-of-contents | typescript | 0 | 0/41 | 1131/1131 | 47 | 32 | 1 | Submitted | full-v3 |
| obsidian-linter-link-format-conversion | typescript | 1 | 60/60 | 1131/1131 | 38 | 27 | 1 | Submitted | full-v3 |
| obsidian-linter-scoped-ignore-markers | typescript | 0 | 33/33 | 1128/1133 | 76 | 78 | 3 | Submitted | full-v3 |
| ofetch-per-origin-circuit-breaker | typescript | 1 | 47/47 | 13/13 | 41 | 36 | 1 | Submitted | full-v3 |
| onedump-dump-encryption-pipeline | go | 0 | 77/82 | 6/6 | 44 | 34 | 1 | Submitted | full-v3 |
| opa-rego-rule-profiling | go | 0 | 22/25 | 6/6 | 82 | 35 | 1 | Submitted | full-v3 |
| opa-template-string-reconstruction | go | 0 | 0/5 | 4/4 | 200 | 49 | 4 | LimitsExceeded | full-v3 |
| optique-conditional-option-dependencies | typescript | 0 | 21/36 | 2034/2034 | 164 | 83 | 5 | Submitted | full-v3 |
| oxvg-structural-selector-preservation | rust | 0 | 0/6 | 62/62 | 172 | 100 | 6 | TimeExceeded | full-v3 |
| participle-grammar-conflict-analysis | go | 0 | 14/91 | 153/153 | 74 | 71 | 2 | Submitted | full-v3 |
| pebble-durability-wait-apis | go | 0 | 0/59 | 44/44 | 144 | 98 | 5 | Submitted | full-v3 |
| pest-character-class-coalescing | rust | 0 | 74/104 | 249/250 | 78 | 50 | 1 | Submitted | full-v3 |
| prometheus-transactional-reload-status | typescript | 1 | 15/15 | 82/82 | 147 | 49 | 2 | Submitted | full-v3 |
| prometheus-typed-label-sorting | go | 1 | 17/17 | 28/28 | 98 | 61 | 2 | Submitted | full-v2 |
| psd-tools-blend-range-api | python | 0 | 43/45 | 979/979 | 40 | 12 | 0 | Submitted | full-v3 |
| pwntools-tube-multiplexing | python | 0 | 24/73 | 1/1 | 31 | 35 | 0 | Submitted | full-v3 |
| python-statemachine-state-data-scoping | python | 0 | 45/72 | 1286/1286 | 134 | 62 | 4 | Submitted | full-v3 |
| query-persist-restored-query-state | typescript | 1 | 8/8 | 42/42 | 98 | 41 | 3 | Submitted | full-v3 |
| quill-shared-toolbar-focus | typescript | 0 | 10/13 | 22/22 | 171 | 92 | 5 | Submitted | full-v3 |
| returns-validated-error-accumulation | python | 1 | 159/159 | 61/61 | 56 | 49 | 2 | Submitted | full-v3 |
| scc-bounded-memory-spilling | go | 0 | 16/31 | 286/286 | 74 | 39 | 2 | Submitted | full-v3 |
| scriggo-method-declarations | go | 0 | 0/48 | 599/1049 | 200 | 98 | 8 | LimitsExceeded | full-v3 |
| skrub-duration-encoding | python | 0 | 115/130 | 2784/2784 | 123 | 62 | 4 | Submitted | full-v3 |
| sql-formatter-bigquery-pipe-formatting | typescript | 0 | 0/26 | 5709/5709 | 116 | 101 | 4 | TimeExceeded | full-v3 |
| sqlfmt-create-table-ddl-formatting | python | 0 | 25/32 | 1268/1273 | 128 | 96 | 3 | Submitted | full-v3 |
| sqlite-utils-safe-import-checkpoints | python | 0 | 59/60 | 1038/1038 | 107 | 50 | 2 | Submitted | full-v3 |
| superjson-error-stack-serialization | typescript | 0 | 79/80 | 116/116 | 30 | 37 | 0 | Submitted | full-v3 |
| task-task-graph-export | go | 0 | 19/20 | 17/17 | 111 | 73 | 4 | Submitted | full-v3 |
| tengo-callable-instance-isolation | go | 0 | 2/23 | 122/122 | 136 | 100 | 5 | TimeExceeded | full-v3 |
| tengo-destructuring-bindings | go | 0 | 0/91 | 132/132 | 126 | 101 | 4 | TimeExceeded | full-v3 |
| termenv-preserve-ansi-resets | go | 0 | 31/35 | 87/87 | 39 | 32 | 0 | Submitted | full-v3 |
| testem-bail-on-test-failure | javascript | 0 | 1/90 | 489/489 | 142 | 100 | 10 | TimeExceeded | full-v3 |
| testem-per-launcher-reports | javascript | 0 | 64/65 | 469/469 | 55 | 35 | 1 | Submitted | full-v3 |
| textual-kitty-key-phases | python | 0 | 6/23 | 57/57 | 136 | 100 | 3 | TimeExceeded | full-v3 |
| textual-richlog-follow-state | python | 0 | 14/20 | 6/6 | 200 | 78 | 4 | LimitsExceeded | full-v3 |
| tomlkit-toml-table-converters | python | 0 | 25/60 | 964/964 | 117 | 102 | 3 | TimeExceeded | full-v3 |
| true-myth-iterable-collection-combinators | typescript | 0 | 74/96 | 561/561 | 97 | 83 | 4 | Submitted | full-v3 |
| ts-pattern-match-each | typescript | 1 | 85/85 | 6/6 | 28 | 21 | 0 | Submitted | full-v3 |
| updo-policy-alerting | go | 0 | 14/17 | 123/123 | 42 | 30 | 1 | Submitted | full-v3 |
| valibot-recursive-schema-composition | typescript | 0 | 2/10 | 208/209 | 116 | 100 | 3 | TimeExceeded | full-v3 |
| vitest-duration-sharding | typescript | 0 | 51/56 | 24/24 | 200 | 53 | 3 | LimitsExceeded | full-v3 |
| vulture-persistent-analysis-cache | python | 0 | 23/24 | 295/295 | 81 | 36 | 1 | Submitted | full-v3 |
| wasmi-trap-coredumps | rust | 0 | 0/22 | 58/58 | 172 | 92 | 9 | Submitted | full-v3 |
| wazero-multi-module-snapshots | go | 0 | 73/78 | 2/2 | 76 | 37 | 1 | Submitted | full-v3 |
| yaegi-go-embed-directives | go | 0 | 0/38 | 58/58 | 200 | 83 | 6 | LimitsExceeded | full-v3 |
| yjs-map-conflict-detection | javascript | 1 | 9/9 | 231/231 | 115 | 67 | 3 | Submitted | full-v3 |
| ytt-jsonpath-query-api | go | 0 | 11/103 | 0/1 | 53 | 55 | 1 | Submitted | full-v3 |
