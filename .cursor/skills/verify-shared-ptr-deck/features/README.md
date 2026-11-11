# Feature map: SharedPtrPPT

Slidev deck "Mastering C++ shared_ptr" (slidev-shared-ptr-presentation/, 15 slides, seriph theme, dark).

- Cover, agenda, hook, smart pointer family, deep dives (creation, sharing, reset, custom deleters, best practices, comparison table, migration), Q&A.
- Custom Vue components: ProgressTracker (fixed bottom-right slide counter, reads $slidev.nav), VisualRefCounter, Counter demo.
- C++ code samples via fenced ```cpp blocks with shiki highlighting. Build-repair history: several samples were plain text or indented fences whose <Widget>/<memory> generics broke Vue template parsing; now fenced/escaped.

## Repaired in verification rollout
- Agenda slide: removed leftover broken `<ProgressTracker :currentSlide=".nav.currentPage">` heading (invalid Vue expression; component takes no props and is already mounted).
- `\`<memory>\`` escaped backticks produced a literal raw `<memory>` tag; now properly backticked.
- Interactive-playground `<pre><code>` block with unescaped C++ (raw `<iostream>`, `<Gizmo>` tags, blank lines splitting it into paragraphs) converted to a fenced code block.
- 61 indented (4-space) fence markers dedented so markdown/slidev recognize them.
- Raw C++ generics inside HTML div blocks escaped to entities.
