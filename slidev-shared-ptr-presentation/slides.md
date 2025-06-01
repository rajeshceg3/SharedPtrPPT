---\ncolorSchema: dark\ntheme: seriph\nhighlighter: shiki\nlineNumbers: true\nfonts:\n  sans: "Inter"\n  mono: "Fira Code"\ntransition: slide-left\ndrawings:\n  persist: false\n---\n

<!--
DEV_NOTE: Most TODOs in slides 1-10 have been reviewed.
They primarily relate to visual enhancements or interactive elements
(e.g., animations, diagrams, custom Vue components for polls/visualizations).
These are valuable for the presentation's engagement and will be kept
for future implementation. They are out of scope for initial content generation.
-->
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
  For example,
using a Vue component:
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
<ul class="list-disc pl-5">
  <li v-click>The last remaining `shared_ptr` owning the object is destroyed.</li>
  <li v-click>The last remaining `shared_ptr` owning the object is assigned another pointer via `operator=` or `reset()`.</li>
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

---
layout: default
# ---
# Accessing the Object (Slide 11)
# ---

# Accessing the Managed Object

Once you have a `std::shared_ptr`, you'll want to use the object it manages.
`shared_ptr` provides familiar pointer syntax:

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### How to Access:

1.  **Dereference Operator (`*`)**:
    To get a reference to the managed object.
    ```cpp
    std::shared_ptr<MyClass> ptr = std::make_shared<MyClass>();
    MyClass& obj_ref = *ptr; // Get a reference
    obj_ref.doSomething();
    ```

2.  **Arrow Operator (`->`)**:
    To access members of the managed object directly. This is typically the most common way.
    ```cpp
    std::shared_ptr<Person> ptr_person = std::make_shared<Person>("Ravi");
    std::cout << "Person's name: " << ptr_person->name << std::endl;
    // ptr_person->greet(); // Assuming Person has a greet() method
    ```

3.  **`get()` Method**:
    To get the raw pointer to the managed object. Use with caution!
    - The `shared_ptr` still owns the object.
    - Do not `delete` the pointer returned by `get()`.
    - Useful for interoperability with C-style APIs or functions that expect raw pointers (but don't take ownership).
    ```cpp
    std::shared_ptr<int> s_ptr = std::make_shared<int>(123);
    int* raw_ptr = s_ptr.get();
    if (raw_ptr) {
        std::cout << "Raw pointer value: " << *raw_ptr << std::endl;
    }
    // some_c_api_function(raw_ptr); // If the C API doesn't delete it
    ```
</div>

<div>
<!-- Placeholder for interactive code playground -->
<div class="p-4 border rounded-lg glassmorphic min-h-[300px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Interactive Code Playground</p>
  <img src="https://placehold.co/350x200?text=Code+Editor+Here" alt="Placeholder for interactive code playground" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Embed an interactive C++ code editor (e.g., via a custom component or iframe to an online compiler) where users can try these operations.]</em></p>
  <pre><code class="language-cpp">
// Example for playground:
#include <iostream>
#include <memory>
#include <string>

class Gizmo {
public:
    std::string id = "X42";
    Gizmo(const std::string& id_val) : id(id_val) {
        std::cout << "Gizmo " << id << " created\n";
    }
    ~Gizmo() {
        std::cout << "Gizmo " << id << " destroyed\n";
    }
    void print_id() {
        std::cout << "Gizmo ID: " << id << "\n";
    }
};

int main() {
    auto gizmo_ptr = std::make_shared<Gizmo>("Alpha");

    // Try accessing:
    std::cout << "Accessing id: " << gizmo_ptr->id << std::endl;
    (*gizmo_ptr).print_id(); // Another way to call method

    Gizmo* raw_gizmo_ptr = gizmo_ptr.get();
    std::cout << "Raw ptr points to Gizmo with id: " << raw_gizmo_ptr->id << std::endl;

    return 0;
}
  </code></pre>
</div>
</div>

</div>

**Key Takeaway:** Accessing the object is intuitive, but be careful when using `get()` not to invalidate the `shared_ptr`'s ownership.

---
layout: default
# ---
# Checking and Resetting shared_ptr (Slide 12)
# ---

# Checking Status & Resetting `shared_ptr`

`shared_ptr` provides ways to check its state and to change what object it manages.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### Safety Checks & Information:

1.  **Boolean Context (`if (ptr)`)**:
    A `shared_ptr` is contextually convertible to `bool`. It's `true` if it owns/manages an object, `false` otherwise (i.e., it's an empty `shared_ptr`).
    ```cpp
    #include <iostream>
    #include <memory>
    #include <string>

    class Widget {
    public:
        std::string name;
        Widget(const std::string& n) : name(n) { std::cout << "Widget " << name << " created.\n"; }
        ~Widget() { std::cout << "Widget " << name << " destroyed.\n"; }
    };

    // ... in a function or main ...
    // std::shared_ptr<Widget> ptr_w; // Empty
    // if (ptr_w) {
    //     // This block will not execute
    //     std::cout << "ptr_w manages an object.\n";
    // } else {
    //     std::cout << "ptr_w is empty.\n"; // This will be printed
    // }

    // ptr_w = std::make_shared<Widget>("W1");
    // if (ptr_w) {
    //     std::cout << "Now ptr_w manages an object!\n"; // This executes
    // }
    ```
    <br/>
    Here's a compact, runnable example to demonstrate the boolean context:
    ```cpp
    // Standalone runnable example for boolean context:
    std::shared_ptr<Widget> ptr_w_demo; // Default constructor: empty
    if (ptr_w_demo) {
        // This block will not execute
        std::cout << "ptr_w_demo manages an object (unexpected).\n";
    } else {
        std::cout << "ptr_w_demo is empty initially.\n"; // This will be printed
    }
    ptr_w_demo = std::make_shared<Widget>("W-Demo"); // Now manages a Widget
    if (ptr_w_demo) {
        std::cout << "ptr_w_demo now manages Widget '" << ptr_w_demo->name << "'.\n"; // This executes
    }
    ```

2.  **Reference Count (`use_count()`)**:
    Returns the number of `shared_ptr` instances (the strong reference count) that share ownership of the managed object. If empty, returns `0`.
    *Primarily for debugging/demonstration; avoid using it in production logic.*
    ```cpp
    // ... continuing with Widget class defined above ...
    // auto sp1 = std::make_shared<Widget>("W-Count");
    // std::cout << "Use count for sp1: " << sp1.use_count() << std::endl; // Output: 1

    // std::shared_ptr<Widget> sp2 = sp1; // Copy sp1
    // std::cout << "Use count for sp1 (after copy): " << sp1.use_count() << std::endl; // Output: 2
    // std::cout << "Use count for sp2: " << sp2.use_count() << std::endl; // Output: 2
    ```
    <br/>
    And here's a compact, runnable example for `use_count()`:
    ```cpp
    // Standalone runnable example for use_count:
    auto sp1_demo = std::make_shared<Widget>("W-CountDemo");
    std::cout << "sp1_demo use_count: " << sp1_demo.use_count() << std::endl; // Expected: 1
    std::shared_ptr<Widget> sp2_demo = sp1_demo;
    std::cout << "sp1_demo use_count after sharing with sp2_demo: " << sp1_demo.use_count() << std::endl; // Expected: 2
    std::cout << "sp2_demo use_count: " << sp2_demo.use_count() << std::endl; // Expected: 2
    ```
</div>

<div>

### Modifying Ownership with `reset()`:

The `reset()` method is versatile:

1.  **`ptr.reset()` (No arguments)**:
    Releases ownership of the object. If this `shared_ptr` was the last owner, the object is destroyed. The `shared_ptr` becomes empty.
    ```cpp
    #include <iostream>
    #include <memory>
    #include <string>

    class Gadget { // Define Gadget class if not already defined on this slide context
    public:
        std::string gadgetName;
        Gadget(const std::string& n) : gadgetName(n) { std::cout << "Gadget " << gadgetName << " created.\n"; }
        ~Gadget() { std::cout << "Gadget " << gadgetName << " destroyed.\n"; }
        std::string id() const { return gadgetName; }
    };

    // ... in a function or main ...
    // auto ptr_gadget = std::make_shared<Gadget>("G-Main");
    // std::cout << "ptr_gadget (" << ptr_gadget->id() << ") use_count before reset: " << ptr_gadget.use_count() << std::endl;
    // ptr_gadget.reset(); // Gadget "G-Main" is destroyed here if ptr_gadget was the last owner
    // std::cout << "ptr_gadget use_count after reset: " << ptr_gadget.use_count() << std::endl; // Output: 0
    // if (!ptr_gadget) {
    //     std::cout << "ptr_gadget is now empty.\n";
    // }
    ```
    <br/>
    Compact, runnable example for `reset()`:
     ```cpp
    // Standalone runnable example for reset():
    auto ptr_grd = std::make_shared<Gadget>("G-ResetDemoStandalone");
    std::cout << "ptr_grd (" << ptr_grd->id() << ") use_count: " << ptr_grd.use_count() << std::endl; // Expected: 1
    ptr_grd.reset(); // "Gadget G-ResetDemoStandalone destroyed." printed
    std::cout << "ptr_grd use_count after reset: " << ptr_grd.use_count() << std::endl; // Expected: 0
    if (!ptr_grd) { std::cout << "ptr_grd is confirmed empty.\n"; }
    ```

2.  **`ptr.reset(new_object_ptr)`**:
    Releases ownership of the current object (if any) and takes ownership of `new_object_ptr`.
    ```cpp
    // ... assuming Gadget class is defined above ...
    // std::shared_ptr<Gadget> ptr_g_replace; // Empty shared_ptr
    // ptr_g_replace.reset(new Gadget("G-Initial")); // Manages G-Initial
    // std::cout << "ptr_g_replace ("<< ptr_g_replace->id() <<") use_count: " << ptr_g_replace.use_count() << std::endl;
    // ptr_g_replace.reset(new Gadget("G-Replaced")); // G-Initial destroyed, now manages G-Replaced
    // std::cout << "ptr_g_replace now manages ("<< ptr_g_replace->id() <<"), count: " << ptr_g_replace.use_count() << std::endl;
    ```
    <br/>
    Compact, runnable example for `reset(new_object_ptr)`:
    ```cpp
    // Standalone runnable example for reset(new):
    std::shared_ptr<Gadget> ptr_grn; // Empty
    ptr_grn.reset(new Gadget("G-ReplaceNewStandalone1")); // Gadget G-ReplaceNewStandalone1 created
    if(ptr_grn) {
        std::cout << "ptr_grn manages ("<< ptr_grn->id() <<"), count: " << ptr_grn.use_count() << std::endl;
    }
    // ptr_grn.reset(new Gadget("G-ReplaceNewStandalone2")); // Gadget G-ReplaceNewStandalone1 destroyed, G-ReplaceNewStandalone2 created
    // The above line using `new` is okay, but make_shared is preferred for new objects.
    // Let's use make_shared for the replacement for better practice demonstration:
    ptr_grn = std::make_shared<Gadget>("G-ReplaceNewStandalone2"); // G-ReplaceNewStandalone1 destroyed (if reset wasn't used prior)
                                                              // or if used, previous object destroyed by reset.
                                                              // Now G-ReplaceNewStandalone2 created and managed.
    if(ptr_grn) {
        std::cout << "ptr_grn now manages ("<< ptr_grn->id() <<"), count: " << ptr_grn.use_count() << std::endl;
    }
    // ptr_grn goes out of scope, G-ReplaceNewStandalone2 destroyed
    ```
    *Note: Prefer `std::make_shared` over `new T(...)` followed by `ptr.reset(new T(...))` when creating and assigning a *new* object. If `reset` is used with a raw pointer from `new`, it takes ownership, but `make_shared` is generally safer and can be more efficient for initial creation.*

<!-- TODO: Add placeholders for live demonstrations with visual feedback -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Live Demo Zone</p>
  <img src="https://placehold.co/300x100?text=Visual+Feedback+Here" alt="Placeholder for live demo" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Visual elements showing `use_count` changes and object status (e.g., "Managed", "Empty") as operations are performed.]</em></p>
</div>

</div>
</div>

**Important:** `use_count()` can be misleading in multi-threaded scenarios or during object construction/destruction. Use primarily for educational or debugging purposes.

---
layout: default
# ---
# The Pitfall: Circular References (Slide 13)
# ---

# The Pitfall: Circular References 🔄

While `shared_ptr` is powerful, it's not immune to all memory management problems.
A common issue is **circular references**.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### What's a Circular Reference?

A circular reference occurs when two or more objects hold `shared_ptr`s to each other, forming a cycle.

- Object A has a `shared_ptr` to Object B.
- Object B has a `shared_ptr` to Object A.

Even if all external `shared_ptr`s to A and B are destroyed, the reference counts within the cycle (A to B, B to A) remain non-zero.
As a result, neither object's reference count ever drops to zero, and their destructors are never called, leading to a **memory leak**.

<!-- TODO: Animated diagram showing circular reference problem -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Circular Reference Diagram</p>
  <img src="https://placehold.co/300x150?text=A+<-->+B+Cycle" alt="Placeholder for circular reference diagram" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Animated diagram showing two objects, A and B, each holding a shared_ptr to the other, and their reference counts never reaching zero.]</em></p>
</div>

<!-- TODO: Memory leak visualization -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[100px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Memory Leak!</p>
  <img src="https://media.giphy.com/media/QRhtS4qWLhD0I/giphy.gif" alt="Leak" class="rounded opacity-80 h-24">
  <p class="mt-2 text-sm"><em>[TODO: Visualization of memory being leaked due to the cycle.]</em></p>
</div>

</div>

<div>

### Code Example:

Let's illustrate with two classes, `Parent` and `Child`:

```cpp
#include <iostream>
#include <memory>
#include <string>

// Forward declaration
class Parent;

class Child {
public:
    std::string name;
    std::shared_ptr<Parent> myParent; // Uh oh, potential cycle

    Child(const std::string& n) : name(n) {
        std::cout << "Child " << name << " created\n";
    }
    ~Child() {
        std::cout << "Child " << name << " destroyed\n";
    }
    void setParent(std::shared_ptr<Parent> p) {
        myParent = p;
    }
};

class Parent {
public:
    std::string name;
    std::shared_ptr<Child> myChild; // Uh oh, potential cycle

    Parent(const std::string& n) : name(n) {
        std::cout << "Parent " << name << " created\n";
    }
    ~Parent() {
        std::cout << "Parent " << name << " destroyed\n";
    }
    void setChild(std::shared_ptr<Child> c) {
        myChild = c;
    }
};

int main() {
    std::cout << "Starting circular reference demo...\n";
    {
        auto parent = std::make_shared<Parent>("Papa");
        auto child = std::make_shared<Child>("Junior");

        parent->setChild(child);
        child->setParent(parent);

        std::cout << "Parent (" << parent->name << ") use_count: " << parent.use_count() << std::endl;
        std::cout << "Child (" << child->name << ") use_count: " << child.use_count() << std::endl;

        // When parent and child go out of scope here,
        // their external shared_ptrs are destroyed.
        // However, parent still holds a shared_ptr to child,
        // and child still holds a shared_ptr to parent.
        // Their reference counts will drop from 2 to 1, but not to 0.
        // DESTRUCTORS WILL NOT BE CALLED! -> Memory Leak!
    } // parent and child shared_ptrs from main() scope are destroyed
      // Internal cycle remains: parent->myChild and child->myParent
      // Ref counts for Parent object: 1 (from child->myParent)
      // Ref counts for Child object: 1 (from parent->myChild)

    std::cout << "Circular reference demo finished.\n";
    // Observe: No destructor messages for Parent 'Papa' or Child 'Junior'!
    return 0;
}

```
**Output will show objects created but not destroyed.** (You'll see "Papa created", "Junior created", use counts, then "Circular reference demo finished.", but no "destroyed" messages).

### The Solution: `std::weak_ptr`

To break such cycles, C++ provides `std::weak_ptr`.
- A `weak_ptr` "observes" an object managed by a `shared_ptr` but **does not affect its strong reference count**.
- To access the object, a `weak_ptr` must be temporarily converted to a `shared_ptr` (using `lock()`). If the object still exists, `lock()` returns a valid `shared_ptr`; otherwise, it returns an empty `shared_ptr`.
- One of the objects in the cycle (e.g., `Child` pointing to `Parent`, or `Parent` to `Child`) should use a `std::weak_ptr` instead of a `std::shared_ptr` for the back-reference.

*(A detailed example of `weak_ptr` usage could be a follow-up slide or topic.)*

</div>
</div>

**Key Lesson:** Be mindful of ownership cycles when using `shared_ptr`. Use `std::weak_ptr` to break them by making one of the links in the cycle non-owning.

---
layout: default
# ---
# Custom Deleters (Slide 14)
# ---

# Custom Deleters: Tailored Cleanup 🛠️

Sometimes, `delete ptr;` isn't the right way to release a resource. `std::shared_ptr` allows you to provide a **custom deleter** for specialized cleanup.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### Why Custom Deleters?

- **Arrays**: `new[]` requires `delete[]`, not `delete`. `shared_ptr`'s default deleter uses `delete` for `T*`. (Prior to C++17, this was the primary way to handle arrays with `shared_ptr`).
- **C-style resources**: Resources like `FILE*` (from `fopen`) need `fclose`, POSIX mutexes might need `pthread_mutex_destroy`, etc.
- **Third-party library objects**: Some libraries provide specific C-style deallocation functions for their opaque types.
- **Logging/Notification**: You might want to perform an action (like logging) when a resource is released.
- **Custom memory allocators**: If an object was allocated with a custom allocator, it might need a custom deallocator.

A custom deleter is a callable object (function pointer, lambda expression, or object with `operator()`) that `shared_ptr` will store and invoke instead of `delete ptr` when the managed object's lifetime ends (i.e., when the last `shared_ptr` owning it is destroyed or reset).

<!-- Placeholder for visual examples of use cases -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Use Case Examples</p>
  <img src="https://placehold.co/300x100?text=File+Handle,+DB+Connection" alt="Placeholder for use cases" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Visuals for file handles needing fclose, DB connections needing disconnect, custom hardware resource release, etc.]</em></p>
</div>

</div>

<div>

### Code Example: Managing `int[]` (Pre-C++17 style)

Before C++17, `std::shared_ptr<T>` would use `delete` by default. For `T` being an array type allocated with `new T[]`, this was incorrect. A custom deleter was essential.

```cpp
#include <iostream>
#include <memory> // For std::shared_ptr
#include <vector> // Just for a different example below

// Custom deleter for an array of integers
void intArrayDeleter(int* p) {
    std::cout << "Custom deleter (intArrayDeleter): Deleting int array at " << p << "\n";
    delete[] p;
}

// Custom deleter for a single int (less common, but shows syntax)
void intDeleter(int* p) {
    std::cout << "Custom deleter (intDeleter): Deleting single int at " << p << "\n";
    delete p;
}

int main() {
    std::cout << "--- Managing dynamic array (pre-C++17 style) ---" << std::endl;
    // Create a shared_ptr to an array of 5 integers
    // The second argument to the shared_ptr constructor is the deleter
    std::shared_ptr<int> intArrayPtr(new int[5], intArrayDeleter);

    // Alternative using a lambda (often preferred for conciseness)
    // std::shared_ptr<int> intArrayPtr(new int[5], [](int* p){
    //     std::cout << "Lambda deleter: Deleting int array at " << p << "\n";
    //     delete[] p;
    // });

    if (intArrayPtr) {
        for (int i = 0; i < 5; ++i) {
            intArrayPtr.get()[i] = i * 100; // Accessing array elements
        }
        std::cout << "intArrayPtr.get()[2] = " << intArrayPtr.get()[2] << std::endl;
    }
    // No need to manually call delete[].
    // intArrayDeleter (or lambda) will be called when intArrayPtr goes out of scope.

    std::cout << "\n--- Managing single int with custom deleter ---" << std::endl;
    std::shared_ptr<int> intPtr(new int(42), intDeleter);
    if (intPtr) {
        std::cout << "Value: " << *intPtr << std::endl;
    }
    // intDeleter will be called for this intPtr.

    std::cout << "\n--- C++17 way for arrays (no custom deleter needed) ---" << std::endl;
    // Since C++17, shared_ptr has an overload for array types T[]
    // This automatically uses delete[]
    std::shared_ptr<int[]> modernArrayPtr(new int[3]);
    if (modernArrayPtr) {
        for (int i = 0; i < 3; ++i) modernArrayPtr[i] = (i + 1) * 7; // Can use operator[] directly
        std::cout << "modernArrayPtr[1] = " << modernArrayPtr[1] << std::endl;
    }
    // (If your compiler is pre-C++17, this line might cause an error or require qualification)

    std::cout << "\n--- Exiting main ---" << std::endl;
    // All shared_ptrs go out of scope, their respective deleters are called.
    return 0;
}

```
**Output will show the custom deleter messages like "Custom deleter (intArrayDeleter): Deleting int array..."**

### Example: `FILE*` Resource
```cpp
#include <cstdio> // For FILE, fopen, fclose, perror, fflush
#include <memory>   // For std::shared_ptr
#include <iostream> // For std::cout

// Example demonstrating managing a FILE* with a custom deleter.
// This code can be run (e.g., in a main function or a dedicated test function).
void manage_file_resource() {
    const char* filename = "example.txt";
    // Attempt to open the file for writing.
    FILE* raw_fp = fopen(filename, "w");

    if (raw_fp) {
        std::cout << "Successfully opened " << filename << " for writing.\n";
        // Create a shared_ptr to manage the FILE*.
        // The custom deleter is a lambda that calls fclose.
        std::shared_ptr<FILE> filePtr(raw_fp, [filename](FILE* fp_to_close) {
            std::cout << "Custom FILE deleter: Closing file '" << filename << "'.\n";
            if (fclose(fp_to_close) == 0) {
                std::cout << "File '" << filename << "' closed successfully.\n";
            } else {
                // perror provides a system error message.
                std::perror(("Error closing file '" + std::string(filename) + "'").c_str());
            }
        });

        // Use the managed FILE resource via the shared_ptr.
        fprintf(filePtr.get(), "Hello from std::shared_ptr with a custom deleter!\n");
        fprintf(filePtr.get(), "The file should be automatically closed when filePtr goes out of scope.\n");

        // It's good practice to flush output to ensure it's written,
        // especially if the program is short-lived or might crash.
        if (fflush(filePtr.get()) != 0) {
            std::perror("Error flushing file content");
        } else {
            std::cout << "Content flushed to " << filename << ".\n";
        }

        std::cout << "filePtr is about to go out of scope (end of manage_file_resource function).\n";
        // When filePtr goes out of scope here, its lambda deleter will be invoked,
        // which in turn calls fclose(raw_fp).
    } else {
        std::perror(("Failed to open file '" + std::string(filename) + "'").c_str());
    }
}
// To test, call manage_file_resource() from main.
// After execution, "example.txt" should exist with the content written.
```
*(This `FILE*` example demonstrates managing non-memory resources. Ensure `example.txt` is writable in the execution directory.)*
</div>
</div>

**Custom deleters make `shared_ptr` incredibly flexible for various resource management tasks beyond basic memory, ensuring RAII principles are upheld.**

---
layout: default
# ---
# Performance Considerations (Slide 15)
# ---

# Performance Considerations ⏱️

While `shared_ptr` offers safety and convenience, it's not "free." There are performance implications to be aware of.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### Memory Overhead

- **Control Block**:
    - `shared_ptr` requires a separate dynamically allocated "control block" to store metadata.
    - This block contains:
        - The **strong reference count** (number of `shared_ptr`s owning the object).
        - The **weak reference count** (number of `weak_ptr`s observing the object).
        - Optionally, a copy of the custom deleter and allocator if provided.
    - This control block is allocated when the first `shared_ptr` takes ownership of a raw pointer, or (often more efficiently) alongside the object itself when using `std::make_shared`.
- **Size of `shared_ptr` Object**:
    - A `std::shared_ptr<T>` object itself typically stores two pointers:
        1.  A raw pointer to the managed object (`T*`).
        2.  A raw pointer to the control block.
    - Thus, `sizeof(std::shared_ptr<T>)` is usually `2 * sizeof(void*)`. This is larger than a raw pointer or `std::unique_ptr` (which is usually the size of one raw pointer).

<div v-click class="mt-4">
**`std::make_shared` Advantage:**
- `std::make_shared<T>(args...)` allocates memory for the `T` object AND its control block in a **single heap allocation**.
- This can be more efficient than `std::shared_ptr<T>(new T(args...))` which typically involves:
    1. Allocation for `T` (by `new T(args...)`).
    2. A separate allocation for the control block (when the `shared_ptr` constructor is called).
- Single allocation reduces memory fragmentation and improves cache locality because the object and its metadata are likely closer in memory.
</div>

<!-- TODO: Memory overhead visualization -->
<div class="mt-6 p-4 border rounded-lg glassmorphic min-h-[120px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Memory Overhead Visual</p>
  <img src="https://placehold.co/300x80?text=shared_ptr+vs+raw_ptr+size" alt="Placeholder for memory overhead viz" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Diagram comparing memory layout/size: raw pointer, unique_ptr, shared_ptr (object + control block).]</em></p>
</div>

</div>

<div>

### Execution Time Overhead

- **Reference Counting**:
    - Incrementing and decrementing the strong reference count (during `shared_ptr` copy, assignment, destruction) must be **atomic operations**.
    - Atomic operations ensure that these counts are updated correctly even when `shared_ptr` instances are manipulated across multiple threads concurrently.
    - These atomic operations are generally more expensive than simple non-atomic increments/decrements, potentially adding overhead, especially in scenarios with high contention for the same shared object.
- **Allocation/Deallocation**:
    - As mentioned, `std::make_shared` is preferred to reduce allocation overhead.
    - The deallocation of the control block happens when the weak reference count drops to zero (after the strong count is zero and the object is deleted).

### Thread Safety Clarified

- **Control Block Operations (Reference Counts)**: These are **thread-safe**.
    - Multiple threads can safely copy, assign, reset, and destroy `shared_ptr` instances that point to the same managed object (or are copies of each other). The reference counts will be managed correctly without data races on the counts themselves.
    - Example: `std::shared_ptr<MyData> s_ptr_orig = std::make_shared<MyData>(); std::thread t1([s_ptr_orig]{ auto s_ptr_copy1 = s_ptr_orig; /* safe */ }); std::thread t2([s_ptr_orig]{ auto s_ptr_copy2 = s_ptr_orig; /* safe */ });`
- **Managed Object Access**: `shared_ptr` itself does **NOT** provide thread safety for operations on the *managed object* (`*s_ptr` or `s_ptr->member`).
    - If multiple threads can access the *same managed object*, and at least one of these accesses is a write (modifies the object's state), then you **must** synchronize access to that object using mutexes, atomics (for members), or other concurrency control mechanisms.
    - `shared_ptr` only protects its own internal state (the reference counts).
    ```cpp
    // std::shared_ptr<std::vector<int>> list_ptr = std::make_shared<std::vector<int>>();
    // Thread A:
    //   list_ptr->push_back(1); // Needs external lock if Thread B also modifies/reads
    // Thread B:
    //   if (!list_ptr->empty()) { int val = list_ptr->at(0); } // Needs external lock
    ```

<!-- TODO: Benchmark charts & thread safety diagrams -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[120px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Visual Aids</p>
  <img src="https://placehold.co/300x100?text=Benchmarks+&+Thread+Safety+Diagrams" alt="Placeholder for charts" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Benchmark charts (e.g., raw_ptr vs unique_ptr vs shared_ptr creation/access/destruction). Diagrams illustrating thread-safe ref counting vs. non-thread-safe object access.]</em></p>
</div>

</div>
</div>

**Key Considerations:**
- The overhead of `shared_ptr` is often acceptable for the safety and convenience it provides, especially for managing objects with non-trivial lifetimes or complex ownership.
- **When to be most mindful:**
    - In highly performance-sensitive code sections.
    - When managing a very large number of very small, short-lived objects where overhead could accumulate.
- Always prefer `std::make_shared` for creating objects managed by `shared_ptr`.
- If shared ownership is not required, `std::unique_ptr` is a more lightweight smart pointer with less overhead.

---
layout:default
# ---
# Best Practices - The Golden Rules (Slide 16)
# ---

# Best Practices: The Golden Rules 📜

Using `std::shared_ptr` effectively involves following some key guidelines to maximize benefits and avoid pitfalls.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### Do This 👍

<div v-click class="prose prose-sm max-w-none">

- **Prefer `std::make_shared<T>(...)` for creating shared objects.**
  ```cpp
  // Good: Efficient and exception-safe
  auto ptr = std::make_shared<MyClass>(arg1, arg2);
  ```
  - **Why?**
    - **Efficiency:** Often performs a single heap allocation for both the object and its control block. This reduces allocation overhead and improves cache locality.
    - **Exception Safety:** Prevents memory leaks if an exception occurs during the construction of the `shared_ptr` itself after the raw pointer has been allocated but before the `shared_ptr` takes ownership. (e.g. `f(std::shared_ptr<T>(new T()), std::shared_ptr<U>(new U()))` - if `new U()` throws, `new T()` could leak. `make_shared` avoids this).

- **Pass `shared_ptr` by value if a function needs to take (shared) ownership or store/extend the lifetime of the object.**
  ```cpp
  void processWidget(std::shared_ptr<Widget> sp_w) {
      // sp_w is now another co-owner.
      // Safe to store sp_w or pass it further.
  }
  ```
  This correctly increments the reference count, ensuring the object lives as long as `sp_w` (and other owners) exist.

- **Pass `shared_ptr` by `const&` (or `&`) if a function only needs to observe/access the object and *not* affect its lifetime or ownership.**
  ```cpp
  void displayWidget(const std::shared_ptr<Widget>& sp_w) {
      if (sp_w) sp_w->display(); // Just using, not owning.
  }
  ```
  This avoids unnecessary reference count increments/decrements (atomic operations).

- **Consider passing a raw pointer (`T*`) or reference (`T&`) if a function only needs to *use* the object for the duration of the call and doesn't care about its ownership or lifetime management at all.**
  ```cpp
  void useWidgetRaw(Widget* w) { if(w) w->doSomething(); }
  // Call: useWidgetRaw(sp_w.get());

  void useWidgetRef(const Widget& w) { w.printInfo(); }
  // Call: if(sp_w) useWidgetRef(*sp_w);
  ```
  **Caveat:** Ensure the `shared_ptr` (and thus the object) outlives the raw pointer/reference. This is safe if the raw pointer/reference doesn't escape the function's scope in a way that outlives the `shared_ptr`.

- **Use `std::static_pointer_cast`, `std::dynamic_pointer_cast`, `std::const_pointer_cast` for safe casting between `shared_ptr` types that manage objects in an inheritance hierarchy.** These correctly manage the control block.

- **Break ownership cycles with `std::weak_ptr`.** If object A holds a `shared_ptr` to B, and B needs a pointer back to A (e.g., parent-child, observer patterns), B's pointer to A should typically be a `std::weak_ptr<A>`.

- **Inherit from `std::enable_shared_from_this<T>` to safely obtain a `shared_ptr<T>` from `this` within a member function of class `T`, but *only if* you know an instance of `T` is already managed by a `shared_ptr`.** Then call `shared_from_this()`.
  ```cpp
  class MyHandler : public std::enable_shared_from_this<MyHandler> {
  public:
      void asyncOperation() {
          // ...
          // Schedule a callback that needs a shared_ptr to this:
          // auto self = shared_from_this();
          // some_async_scheduler([self]() { self->onComplete(); });
      }
      void onComplete() { /* ... */ }
  };
  ```

</div>

<!-- TODO: Visual checklist with animated checkmarks -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[100px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Visual Checklist</p>
  <img src="https://placehold.co/250x80?text=Do's+Checklist+Animation" alt="Placeholder for checklist" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Animated checklist for Do's.]</em></p>
</div>

</div>

<div>

### Avoid This 👎

<div v-click class="prose prose-sm max-w-none">

- **Don't create multiple independent `shared_ptr` instances from the same raw pointer.**
  ```cpp
  Widget* raw_ptr = new Widget();
  std::shared_ptr<Widget> sp1(raw_ptr);
  // std::shared_ptr<Widget> sp2(raw_ptr); // VERY BAD!
  // sp1 and sp2 will have separate control blocks.
  // Both will try to delete raw_ptr, leading to double deletion.
  ```

- **Avoid `std::shared_ptr<T>(new T(...))` if `std::make_shared<T>(...)` can be used.** (See "Do This" for reasons).

- **Don't create a `shared_ptr` by calling `new MyClass(...)` and passing `this` to its constructor or a member function that then tries to create a `shared_ptr` from `this` without `enable_shared_from_this`.**
  ```cpp
  class Node : public std::enable_shared_from_this<Node> { // Note: Inherit from std::enable_shared_from_this
  public:
    Controller* controller_ptr; // Assuming Controller is defined elsewhere

    Node(Controller* ctrl) : controller_ptr(ctrl) {}

    void registerWithController() {
        // Assuming Controller::registerNode expects a std::shared_ptr<Node>
        // And 'this' object is already managed by a std::shared_ptr externally.
        // controller_ptr->registerNode(shared_from_this());
        std::cout << "Node registered using shared_from_this().\n";
    }

    void problematicRegistration(Controller* ctrl) {
        // BAD: Creates an independent shared_ptr from 'this'.
        // If 'this' object is already managed by another shared_ptr,
        // this leads to two separate control blocks and likely double deletion.
        // ctrl->registerNode(std::shared_ptr<Node>(this));
        std::cout << "Problematic registration attempt with std::shared_ptr<Node>(this).\n";
    }

    // Example method to be called to initiate registration
    // AFTER a shared_ptr to this Node object has been created.
    // void someMethodThatCallsRegister() {
    //    if (controller_ptr) {
    //        // Correct way, assuming this Node object is already managed by a shared_ptr
    //        controller_ptr->registerNode(shared_from_this());
    //    }
    // }
  };
  ```
  **Explanation:**
  If an object (like `Node`) needs to give out `shared_ptr`s to itself, and it's already under the ownership of an existing `shared_ptr`, it should inherit from `std::enable_shared_from_this<ClassName>` and use its `shared_from_this()` method.

  Creating a *new* `std::shared_ptr<Node>(this)` from a raw `this` pointer (as shown in `problematicRegistration` or the commented-out constructor line) is dangerous because:
  1. If the `Node` instance is *already* managed by a `shared_ptr` (e.g., `auto node_ptr = std::make_shared<Node>(...);`), then `std::shared_ptr<Node>(this)` creates a *second, independent* `shared_ptr` with its own control block. Both `shared_ptr`s will think they uniquely own the memory, leading to a double `delete` when they both go out of scope.
  2. If the `Node` instance was created as a stack variable or with `new` but *not* yet managed by any `shared_ptr`, creating a `shared_ptr` from `this` inside its constructor or a member function can be problematic if not handled carefully (e.g. the object might be deleted prematurely if that `shared_ptr` is the only one and goes out of scope).

  The `shared_from_this()` method, when called on an object already managed by a `std::shared_ptr`, returns a new `shared_ptr` instance that *shares ownership* with the existing `shared_ptr`(s), correctly incrementing the reference count in the *same* control block.

- **Be extremely cautious with `get()`:**
    - **Never `delete` the pointer returned by `get()`.** The `shared_ptr` owns it.
    - **Never create another `shared_ptr` (or any other owning smart pointer) from the pointer returned by `get()` without proper aliasing constructor usage (advanced).**
    ```cpp
    // std::shared_ptr<Widget> sp_owner = std::make_shared<Widget>();
    // Widget* raw_w = sp_owner.get();
    // std::shared_ptr<Widget> sp_another_owner(raw_w); // BAD!
    ```

- **Don't use `shared_ptr` for cyclic strong references without `weak_ptr` to break the cycle.** (This leads to memory leaks, as discussed on Slide 13).

- **Avoid using `shared_ptr` when exclusive ownership (`std::unique_ptr`) or non-owning observation (raw pointer/reference, `std::weak_ptr`) is more appropriate.** `shared_ptr` signals *shared* ownership; using it unnecessarily can obscure design intent and add slight overhead.

- **Don't store `std::shared_ptr<void>` without a custom deleter that knows how to correctly delete the original type.** While `shared_ptr` is type-erasing for the deleter, the default `delete` on `void*` is undefined behavior.

</div>

<!-- TODO: Color-coded examples, quiz -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Interactive Learning</p>
  <img src="https://placehold.co/250x120?text=Don'ts+(Red)+Quiz" alt="Placeholder for quiz" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Color-coded Do/Don't code snippets. Interactive quiz questions about best practices.]</em></p>
</div>

</div>
</div>

**Following these rules helps write safer, more maintainable, and efficient C++ code with `shared_ptr`.**

---
layout: default
# ---
# Real-world Example: Resource Manager (Slide 17)
# ---

# Real-world Example: Resource Manager 🏗️

Let's see how `std::shared_ptr` can be used in a more complex scenario, like managing shared resources within an application.

<div class="grid grid-cols-2 gap-8 items-start">

<div>

### Scenario: Shared Application Resources

Many applications require common services or resources that need to be accessed by multiple components or worker threads. Examples include:
- A central database connection pool.
- A global application logger.
- A shared cache or configuration manager.

These resources typically should:
- Be initialized once (or lazily on first use).
- Be safely shared among various parts of the application.
- Be automatically cleaned up (e.g., connections closed, buffers flushed) only when no longer needed by any component.

`std::shared_ptr` is an excellent tool for managing the lifetime of such shared resources.

<!-- TODO: Architecture diagram -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[150px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">System Architecture</p>
  <img src="https://placehold.co/300x150?text=ResourceManager+Architecture" alt="Placeholder for architecture diagram" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Diagram showing ResourceManager holding shared_ptrs to Database/Logger, and multiple Worker instances also holding shared_ptrs to these resources.]</em></p>
</div>

<!-- TODO: Lifetime management visualization -->
<div class="mt-4 p-4 border rounded-lg glassmorphic min-h-[120px] flex flex-col items-center justify-center">
  <p class="text-lg font-semibold mb-2">Resource Lifetimes</p>
  <img src="https://placehold.co/300x100?text=Resource+Lifecycles+Demo" alt="Placeholder for lifetime viz" class="rounded opacity-70">
  <p class="mt-2 text-sm"><em>[TODO: Visualization showing how shared_ptr reference counts for Database/Logger change as Workers are created and destroyed, and how ResourceManager's ownership also plays a role.]</em></p>
</div>

</div>

<div>

### Code Example:

This example simulates a `ResourceManager` that provides shared `Database` and `Logger` instances to multiple `Worker` objects.

```cpp
#include <iostream>
#include <memory> // For std::shared_ptr, std::make_shared
#include <string>
#include <vector> // For std::vector

// --- Dummy Shared Resource Classes ---
class Database {
public:
    Database() { std::cout << "[Resource] Database connection established.\n"; }
    ~Database() { std::cout << "[Resource] Database connection closed.\n"; }
    void query(const std::string& q_str) {
        std::cout << "  DB: Executing query -> " << q_str << "\n";
    }
};

class Logger {
public:
    Logger() { std::cout << "[Resource] Logger initialized.\n"; }
    ~Logger() { std::cout << "[Resource] Logger shut down.\n"; }
    void log(const std::string& msg) {
        std::cout << "  LOG: " << msg << "\n";
    }
};

// --- Worker Class using Shared Resources ---
class Worker {
    std::shared_ptr<Database> db_service;    // Shared DB connection
    std::shared_ptr<Logger> logging_service; // Shared Logger
    std::string id;
public:
    Worker(std::shared_ptr<Database> db,
           std::shared_ptr<Logger> logger,
           const std::string& worker_id)
        : db_service(db), logging_service(logger), id(worker_id) {
        // Both db and logger shared_ptrs have their ref counts incremented
        if(logging_service) logging_service->log("Worker " + id + " created and configured.");
    }

    ~Worker() {
        if(logging_service) logging_service->log("Worker " + id + " being destroyed.");
        // When Worker is destroyed, its shared_ptr members (db_service, logging_service)
        // are destroyed, decrementing the ref counts of the Database and Logger objects.
    }

    void performTask() {
        if (!logging_service || !db_service) return;
        logging_service->log("Worker " + id + " starting task.");
        db_service->query("SELECT data FROM table WHERE owner='" + id + "'");
        // Simulate some work
        for(int i=0; i < 3; ++i) { /* processing */ }
        logging_service->log("Worker " + id + " finished task.");
    }
};

// --- ResourceManager Class ---
class ResourceManager {
    std::shared_ptr<Database> shared_db_instance;
    std::shared_ptr<Logger> shared_logger_instance;
    std::vector<std::shared_ptr<Worker>> worker_pool;

public:
    ResourceManager() {
        // Initialize shared resources
        shared_logger_instance = std::make_shared<Logger>();
        shared_logger_instance->log("ResourceManager initializing shared resources...");
        shared_db_instance = std::make_shared<Database>();
        shared_logger_instance->log("ResourceManager initialized successfully.");
    }

    ~ResourceManager() {
        if(shared_logger_instance) shared_logger_instance->log("ResourceManager shutting down. Clearing workers...");
        worker_pool.clear(); // Destroys all worker shared_ptrs in the vector.
                             // This in turn destroys Worker objects if ref count hits 0.
        if(shared_logger_instance) shared_logger_instance->log("All workers cleared from pool.");
        // shared_db_instance and shared_logger_instance will be destroyed here if ResourceManager
        // was the last owner, leading to Database and Logger objects cleanup.
        std::cout << "[System] ResourceManager itself destroyed.\n";
    }

    void addWorker(const std::string& worker_id) {
        if(shared_logger_instance) shared_logger_instance->log("Attempting to add worker: " + worker_id);
        // Create a new worker, passing shared_ptrs to the common resources.
        // This increments ref counts for Database and Logger.
        auto worker = std::make_shared<Worker>(shared_db_instance, shared_logger_instance, worker_id);
        worker_pool.push_back(worker);
    }

    void processAllWorkerTasks() {
        if (!shared_logger_instance) {
            std::cout << "[Error] Logger not available in processAllWorkerTasks!\n"; return;
        }
        shared_logger_instance->log("ResourceManager directing all workers to perform tasks.");
        for (const auto& worker_ptr : worker_pool) {
            if(worker_ptr) worker_ptr->performTask();
        }
        shared_logger_instance->log("All worker tasks initiated.");
    }
};

// --- Main Demonstration ---
int main() {
    std::cout << "--- Real-world Example: Resource Manager --- \n";
    std::cout << "--- Creating ResourceManager (Scope 1) --- \n";
    {
        ResourceManager manager_alpha; // Logger and DB created here
        manager_alpha.addWorker("W-Alpha-001");
        manager_alpha.addWorker("W-Alpha-002");

        manager_alpha.processAllWorkerTasks();

        std::cout << "\n--- ResourceManager 'manager_alpha' is about to go out of scope --- \n";
        // manager_alpha destructor runs:
        // 1. Workers in worker_pool are cleared & destroyed. Their shared_ptrs to DB/Logger are released.
        // 2. ResourceManager's own shared_ptrs to DB/Logger are released.
        // 3. If ref counts for DB/Logger hit 0, they are destroyed.
    }
    std::cout << "\n--- ResourceManager example finished. All resources should be cleaned up. --- \n";
    return 0;
}

```
**The output will clearly show the lifecycle: resources created by `ResourceManager`, shared with `Worker`s, and then automatically cleaned up when `ResourceManager` and all `Worker`s are destroyed.**
</div>
</div>

This example demonstrates how `shared_ptr` facilitates robust management of shared resources, ensuring they are available as long as needed and cleaned up automatically when all references are gone.
