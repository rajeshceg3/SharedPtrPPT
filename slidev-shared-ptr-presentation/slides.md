---\ncolorSchema: dark\ntheme: seriph\nhighlighter: shiki\nlineNumbers: true\nfonts:\n  sans: "Inter"\n  mono: "Fira Code"\ntransition: slide-left\ndrawings:\n  persist: false\n---\n

---
layout: cover
# Possible placeholder for animated background feature:
# background: /path/to/animated-bg.vue or some other mechanism

# ---
# Title Slide
# ---

# Mastering C++ shared\_ptr 🚀

## Smart Pointers for Modern C++ Development

<div class="pt-12">
  <span class="text-xl">Your Name / Organization</span>
  <br>
  <span class="text-sm">Month Day, Year</span>
</div>

<!--
  TODO: Implement animated background with floating code snippets.
  This might require a custom layout or component.
  For example, using a Vue component:
  <FloatingCodeSnippets />
-->


---
layout: default
# TODO: Consider implementing a progress tracker component here later.
# Example: <ProgressTracker :currentSlide=".nav.currentPage" :totalSlides=".nav.total" />

# ---
# Agenda / Overview
# ---

# Agenda

<!--
  The issue mentions a "progress tracker". Slidev has .nav.currentPage and .nav.total.
  A simple way is to show "Slide X of Y" or a more visual one might need a custom component.
  For now, just listing the agenda.
-->

- What are Smart Pointers?
- The Problem with Raw Pointers
- Introduction to shared_ptr
- How shared_ptr Works (Reference Counting)
- Creating and Using shared_ptr
- Best Practices and Pitfalls
- Performance Considerations
- Real-world Examples
- Comparison with other Smart Pointers
- Summary and Q&A

<!-- Removed manual slide counter, replaced by ProgressTracker component -->
<ProgressTracker />


---
layout: default

# ---
# The Hook: Why Smart Pointers?
# ---

# The Cost of Forgetfulness

## "The Million Dollar Bug" & Other Memory Leak Disasters

Remember the Mars Climate Orbiter? Or countless hours spent chasing elusive bugs? Many such issues stem from manual memory management pitfalls.

<br/>

---
<!-- Separate slide for the poll, or could be combined -->
layout: statement

# The Developer's Nightmare

## Ever debugged memory leaks at 3 AM? 😴

<!--
  TODO: Implement an interactive poll.
  Slidev can integrate with tools like Mentimeter or use custom components.
  Example placeholder for a simple poll:
  <Poll question="How many of you have debugged memory leaks at 3 AM?" :options="['Yes, too many times!', 'A few times', 'Thankfully, no!']" />
-->

<div v-if="$slidev.nav.clicks === 1">
  <p class="text-center mt-8">You're not alone!</p>
</div>

---
layout: default

## The Silent Threat: Memory Leaks

<!--
  TODO: Add a visual representation of memory leaks.
  This could be an image, an animated SVG, or a custom Vue component.
  Example: <img src="/images/memory-leak-visualization.svg" alt="Memory Leak Animation" class="mx-auto mt-4 h-60">
  For now, a placeholder text.
-->

Imagine your program's memory as a bucket. With raw pointers, if you forget to empty parts of it, it overflows!

<div class="mt-4 text-center">
  <img src="/images/memory-leak-visualization.gif" alt="Memory Leak Visualization" class="mx-auto mt-4 h-60 rounded-lg shadow-md">
  <p class="text-sm opacity-85">Conceptual visualization of a memory leak.</p>
</div>

<div v-click class="mt-4">
  <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" alt="Leaking Bucket" class="mx-auto h-72 rounded-lg shadow-lg">
  <p class="text-center text-sm opacity-75">And here's a more... dramatic take!</p>
</div>


---
layout: default
# ---
# Raw Pointers - The Old Way
# ---

# The Old Way: Raw Pointers

<div class="grid grid-cols-2 gap-8">
<div>

Consider this "simple" C++ code:

```cpp
#include <iostream>
#include <string>

class Resource {
public:
    std::string name;
    Resource(const std::string& n) : name(n) {
        std::cout << "Resource " << name << " acquired.\n";
    }
    ~Resource() {
        std::cout << "Resource " << name << " released.\n";
    }
    void use() {
        std::cout << "Using resource " << name << ".\n";
    }
};

void process_resource(bool fail) {
    Resource* res = new Resource("Dinosaurs"); // Uh oh, manual allocation
    res->use();
    if (fail) {
        std::cout << "Operation failed! Exiting early.\n";
        // return; // Oops! Forgot to delete res
    }
    // delete res; // If we uncomment the return, this is never reached
    std::cout << "Resource processing finished.\n";
     delete res; // Correct place if no early exit. What if exception?
}

int main() {
    process_resource(false); // Works fine
    std::cout << "----\n";
    process_resource(true);  // Potential leak if not careful!
    return 0;
}
```

</div>
<div>

### Pitfalls of Raw Pointers:

<br/>

<div v-click>
#### 💧 Memory Leaks
- Forgetting `delete`.
- Losing pointer before deallocation.
- **Visualization Placeholder:** *Imagine a pipe dripping bits of memory.*
</div>

<br/>

<div v-click>
#### 💥 Exception Safety
- If an exception occurs, `delete` might be skipped.
- Leads to resource leaks in error conditions.
</div>

<br/>

<div v-click>
#### 🤔 Ownership Confusion
- Who is responsible for `delete`?
- Passing raw pointers around makes ownership unclear.
- Can lead to double deletion or no deletion.
- **Diagram Placeholder:** *Tangled web of pointers with unclear ownership.*
</div>

<br/>

<div v-click>
#### 👻 Dangling Pointers
- Accessing memory after it has been `delete`d.
- Leads to crashes or undefined behavior.
</div>

</div>
</div>

<!--
  TODO:
  - Add memory leak visualization (e.g., animated SVG/image).
  - Add animated diagram for memory allocation/deallocation problems & ownership.
-->


---
layout: default
# ---
# Smart Pointers to the Rescue
# ---

# Smart Pointers to the Rescue! 🛡️

<div class="grid grid-cols-2 gap-8 items-center">
<div>

Raw pointers leave memory management entirely up to you. It's like juggling chainsaws – powerful, but one slip and... 😬

**Smart pointers** are C++ objects that wrap raw pointers, automating memory management using a principle called **RAII** (Resource Acquisition Is Initialization).

<br />
<div v-click>
**Key Idea:**
- Resource is acquired in constructor.
- Resource is released in destructor.
- Automatic cleanup, even with exceptions!
</div>

<!-- TODO: Add visual comparison: Raw vs Smart pointers (e.g., a diagram or side-by-side simple code) -->
<div v-click class="mt-4 p-4 border rounded-lg">
  <h4 class="text-lg font-semibold">Raw Pointers:</h4>
  <ul class="list-disc pl-5">
    <li>Manual new/delete</li>
    <li>Prone to leaks & errors</li>
    <li>Ownership unclear</li>
  </ul>
</div>

</div>
<div>

<div v-click class="mt-4 p-4 border rounded-lg bg-green-900 bg-opacity-30">
  <h4 class="text-lg font-semibold text-green-400">Smart Pointers:</h4>
  <ul class="list-disc pl-5">
    <li class="text-green-300">Automatic memory management</li>
    <li class="text-green-300">Safer, less error-prone</li>
    <li class="text-green-300">Clear ownership semantics</li>
  </ul>
</div>

</div>
</div>

---
layout: default

## Meet the Smart Pointer Family

C++ offers a few types of smart pointers in the \`<memory>\` header:

<div class="grid grid-cols-3 gap-4 mt-8 text-center">

  <div v-click class="p-4 rounded-lg glassmorphic">
    <h3 class="text-xl font-semibold">`std::unique_ptr`</h3>
    <p class="text-sm">Exclusive ownership. Only one `unique_ptr` can own an object. Lightweight.</p>
    <p class="text-2xl mt-2">☝️</p>
  </div>

  <div v-click class="p-4 rounded-lg glassmorphic border-2 border-cyan-500 shadow-cyan-500/50">
    <h3 class="text-xl font-semibold">`std::shared_ptr` ✨</h3>
    <p class="text-sm">Shared ownership. Multiple `shared_ptr`s can own the same object. Uses reference counting.</p>
    <p class="text-2xl mt-2">🤝</p>
    <!-- TODO: Add spotlight effect here -->
  </div>

  <div v-click class="p-4 rounded-lg glassmorphic">
    <h3 class="text-xl font-semibold">`std::weak_ptr`</h3>
    <p class="text-sm">Non-owning. Observes an object managed by a `shared_ptr`. Breaks circular references.</p>
    <p class="text-2xl mt-2">👀</p>
  </div>

</div>

<div v-click class="mt-12 text-center">
  <p class="text-2xl">Our focus today: The versatile <code class="text-cyan-400 text-3xl">std::shared_ptr</code>!</p>
  <!-- TODO: Add spotlight effect transition to shared_ptr focus -->
</div>

---
layout: default
# ---
# shared_ptr Deep Dive - What Is It?
# ---

# Deep Dive: `std::shared_ptr`

<div class="grid grid-cols-2 gap-8 items-center">

<div>

<div v-click>
## What is `std::shared_ptr`?
</div>

<div v-click class="mt-4">
A `std::shared_ptr` is a smart pointer that retains shared ownership of an object through a pointer. Several `shared_ptr` objects may own the same object.
</div>

<div v-click class="mt-4">
The object is destroyed and its memory deallocated when either of the following happens:
<ul>
  <li v-click>the last remaining `shared_ptr` owning the object is destroyed.</li>
  <li v-click>the last remaining `shared_ptr` owning the object is assigned another pointer via `operator=` or `reset()`.</li>
</ul>
</div>

<div v-click class="mt-6">
To use `shared_ptr`, you need to include the `<memory>` header:
```cpp
#include <memory>
```
</div>

</div>

<div>

<div v-click class="p-6 rounded-lg glassmorphic text-center">
  <!-- TODO: Add visual metaphor: "Shared ownership like a shared Netflix account" -->
  <img src="https://cdn-icons-png.flaticon.com/128/2504/2504821.png" alt="Netflix Icon" class="mx-auto h-20 opacity-80">
  <p class="mt-2">Think of it like a shared Netflix account: multiple users (`shared_ptr`s) can access the same subscription (the object). The account stays active as long as at least one user is interested.</p>
</div>

<br />

<div v-click>
### Key Characteristics:
<ul>
  <li v-click> <span class="text-cyan-400">🤝 [SO_icon] Shared Ownership:</span> Multiple pointers, one object.</li>
  <li v-click> <span class="text-cyan-400">⏱️ [RC_icon] Reference Counting:</span> Keeps track of owners.</li>
  <li v-click> <span class="text-cyan-400">🗑️ [AC_icon] Automatic Cleanup:</span> Deallocates when no owners remain.</li>
  <li v-click> <span class="text-cyan-400">✅ [ES_icon] Exception Safe:</span> Resources are released correctly.</li>
  <!-- TODO: Add icons for each characteristic - Placeholders [icon_name] added. Replace with actual <img> or SVG. -->
</ul>
</div>

</div>

</div>

<!--
  Note: Animated text reveal can be achieved by adding `v-click` to elements or using `v-after` for sequential reveals.
-->


---
layout: default
# ---
# Reference Counting Mechanism
# ---

# How `shared_ptr` Works: Reference Counting 🧠

`std::shared_ptr` uses a technique called **reference counting** to manage the lifetime of the pointed-to object.

<div class="grid grid-cols-2 gap-8 items-start mt-6">

<div>

<div v-click>
### The Control Block
- Besides the raw pointer to the managed object, `shared_ptr` also points to a **control block**.
- This control block is dynamically allocated (usually when the first `shared_ptr` is created).
- It contains:
    - A **strong reference count** (how many `shared_ptr`s own the object).
    - A **weak reference count** (how many `weak_ptr`s observe the object).
    - Optionally, a custom deleter, allocator, etc.
</div>

<br v-click />

<div v-click>
### The Lifecycle:
1.  <span v-click class="font-semibold">Creation:</span> When a new object is managed by a `shared_ptr` (e.g., via `std::make_shared` or `new`):
    - Memory is allocated for the object.
    - The control block is created.
    - The strong reference count is initialized to **1**.
</div>
<div v-click class="mt-2">
2.  <span v-click class="font-semibold">Copying:</span> When a `shared_ptr` is copied (copy constructor or copy assignment):
    - The new `shared_ptr` points to the same object and control block.
    - The strong reference count is **incremented**.
</div>
<div v-click class="mt-2">
3.  <span v-click class="font-semibold">Destruction/Reset:</span> When a `shared_ptr` is destroyed or reset:
    - The strong reference count is **decremented**.
</div>
<div v-click class="mt-2">
4.  <span v-click class="font-semibold">Cleanup:</span> If the strong reference count becomes **0**:
    - The managed object is **deleted** (using `delete` or a custom deleter).
    - The control block itself is then deallocated once the weak reference count also becomes 0.
</div>

</div>

<div class="text-center">

<div v-click>
<!-- TODO: Interactive diagram showing reference count changes -->
<div class="p-4 border rounded-lg glassmorphic min-h-[200px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Object & Ref Count</p>
  <img src="https://placehold.co/300x150?text=Interactive+Diagram
(Object+Lifecycle)" alt="Placeholder for interactive diagram" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[Placeholder for interactive diagram showing an object, shared_ptrs pointing to it, and the reference count changing dynamically.]</em></p>
</div>
</div>

<br v-click />

<div v-click>
<!-- TODO: Visual counter showing ref count increments/decrements -->
<div class="p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center mt-4">
  <p class="text-lg font-semibold mb-2">Visual Ref Count</p>
  <VisualRefCounter :count="3" />
  <p class="mt-2 text-sm"><em>This counter demonstrates the display. Full interactivity to come!</em></p>
</div>
</div>

<br v-click />

<div v-click>
<!-- TODO: Automatic cleanup demonstration -->
<div class="p-4 border rounded-lg glassmorphic min-h-[100px] flex flex-col items-center justify-center mt-4">
  <p class="text-lg font-semibold mb-2">Automatic Cleanup</p>
  <img src="https://media.giphy.com/media/UevalU9pGBJRoZ/giphy.gif" alt="Cleaning" class="rounded opacity-80 h-20">
  <p class="mt-2 text-sm"><em>[Placeholder for animation showing object being automatically deleted when ref count hits 0.]</em></p>
</div>
</div>

</div>

</div>

<!--
  This slide would greatly benefit from custom Vue components for interactivity.
  - Diagram of shared_ptr, control block, and object.
  - Animation of ref count changing with shared_ptr copies and destructions.
-->
