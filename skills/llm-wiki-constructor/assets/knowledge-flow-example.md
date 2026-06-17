# Knowledge Flow Example

Illustrative walkthrough showing how materials flow through the llm-wiki layers.

**Topic: Renaissance Art**

| Stage | Output |
|---|---|
| 1. Raw intake: Wikipedia on da Vinci, sfumato excerpt, Mona Lisa catalog | Three `/raw` files |
| 2. Source synthesis: Combine all three, flag date disagreement | `source/leonardo-da-vinci.md` |
| 3. Keyword scoring: entities = [da Vinci, Mona Lisa], concepts = [sfumato, chiaroscuro] | Scored lists for confirmation |
| 4. Entity pages: After confirmation | `entity/leonardo-da-vinci.md`, `entity/mona-lisa.md` |
| 5. Concept pages: Bridge entities | `concept/sfumato.md` |
| 6. Wiki navigation: Route page comparing techniques | `wiki/renaissance-painting-techniques.md` |
