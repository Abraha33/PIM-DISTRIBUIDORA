# GitHub CLI Setup Commands — PIM Envax

Este documento contiene comandos sugeridos para crear labels e Issues iniciales cuando GitHub CLI esté autenticado.

## Reautenticar GitHub CLI

```bash
gh auth login -h github.com
gh auth status
```

## Crear labels

```bash
gh label create "module:products_contract" --color "5319e7" --description "products contract module"
gh label create "module:inventory_flow" --color "5319e7" --description "inventory flow module"
gh label create "module:marketing" --color "5319e7" --description "marketing module"
gh label create "module:media" --color "5319e7" --description "media module"
gh label create "module:scraper" --color "5319e7" --description "scraper module"
gh label create "module:commercial" --color "5319e7" --description "commercial module"

gh label create "type:idea" --color "cfd3d7" --description "rough idea or icebox item"
gh label create "type:epic" --color "a2eeef" --description "large body of work"
gh label create "type:ticket" --color "0e8a16" --description "concrete actionable work"
gh label create "type:sensor" --color "1d76db" --description "inventory flow sensor"
gh label create "type:use_case" --color "fbca04" --description "real business use case"
gh label create "type:decision" --color "d4c5f9" --description "architectural or business decision"
gh label create "type:bug" --color "d73a4a" --description "bug or broken behavior"
gh label create "type:validation" --color "006b75" --description "validation or protective check"

gh label create "layer:empresarial" --color "bfdadc" --description "business layer"
gh label create "layer:matematica" --color "bfdadc" --description "mathematical layer"
gh label create "layer:operativa" --color "bfdadc" --description "operational layer"
gh label create "layer:json" --color "bfdadc" --description "JSON layer"
gh label create "layer:documentacion" --color "bfdadc" --description "documentation layer"
gh label create "layer:tecnica" --color "bfdadc" --description "technical layer"

gh label create "status:icebox" --color "eeeeee" --description "not ready yet"
gh label create "status:backlog" --color "eeeeee" --description "backlog item"
gh label create "status:ready" --color "0e8a16" --description "ready to work"
gh label create "status:in_progress" --color "fbca04" --description "work in progress"
gh label create "status:review" --color "1d76db" --description "in review"
gh label create "status:done" --color "0e8a16" --description "done"
gh label create "status:blocked" --color "d73a4a" --description "blocked"

gh label create "maturity:m1" --color "fef2c0" --description "M1 methodology"
gh label create "maturity:m2" --color "fef2c0" --description "M2 validation"
gh label create "maturity:m3" --color "fef2c0" --description "M3 integration"

gh label create "priority:high" --color "b60205" --description "high priority"
gh label create "priority:medium" --color "fbca04" --description "medium priority"
gh label create "priority:low" --color "0e8a16" --description "low priority"
```

## Crear Issues iniciales

```bash
gh issue create \
  --title "EPIC-001 — inventory_flow M1" \
  --label "type:epic,module:inventory_flow,maturity:m1" \
  --body "Define the methodology, sensors, rules, tickets and JSON structure for inventory_flow M1."

gh issue create \
  --title "TICKET-001 — Documentar metodología de trabajo de inventory_flow" \
  --label "type:ticket,module:inventory_flow,status:done,layer:documentacion" \
  --body "Documentar la metodología de trabajo de inventory_flow. Estado: done/draft."

gh issue create \
  --title "TICKET-002 — Diseñar rotation_sensor con base matemática" \
  --label "type:sensor,module:inventory_flow,status:ready,layer:matematica,maturity:m1" \
  --body "Diseñar rotation_sensor con propósito empresarial, variables, fórmula, umbrales, regla M1 y JSON base."

gh issue create \
  --title "TICKET-003 — Diseñar cashflow_sensor" \
  --label "type:sensor,module:inventory_flow,status:backlog,maturity:m1" \
  --body "Diseñar cashflow_sensor para detectar inventario que presiona caja."

gh issue create \
  --title "TICKET-004 — Diseñar space_sensor" \
  --label "type:sensor,module:inventory_flow,status:backlog,maturity:m1" \
  --body "Diseñar space_sensor para detectar inventario que ocupa espacio crítico."

gh issue create \
  --title "TICKET-005 — Diseñar strategic_stock_sensor" \
  --label "type:sensor,module:inventory_flow,status:backlog,maturity:m1" \
  --body "Diseñar strategic_stock_sensor para proteger inventario básico o estratégico."

gh issue create \
  --title "TICKET-006 — Diseñar season_opportunity_sensor" \
  --label "type:sensor,module:inventory_flow,status:backlog,maturity:m1" \
  --body "Diseñar season_opportunity_sensor para detectar oportunidades o riesgos por temporada cercana."
```

## Crear PR después de push

```bash
gh pr create \
  --base main \
  --head codex/backlog-assisted-purchase-invoice-pim-scraper \
  --title "docs: add GitHub issue and project workflow docs" \
  --body "Adds GitHub Issue templates, backlog/project workflow documentation, label taxonomy and initial issue list."
```

## Nota

Estos comandos son operativos, pero deben ejecutarse solo después de que `gh auth status` confirme autenticación válida.
