# Slidev Presentation: A Deep Dive into C++ Shared Pointers

This project is a Slidev presentation designed to provide a comprehensive understanding of C++ shared pointers (`std::shared_ptr`). It covers their usage, benefits, potential pitfalls, and best practices.

## About Slidev

[Slidev](https://sli.dev/) is a powerful, open-source presentation tool built for developers. It leverages web technologies like Vue.js and Markdown to create engaging and interactive slideshows. Key features relevant to this presentation include:

- **Markdown-based content:** Slides are written in Markdown, making them easy to create and edit.
- **Vue.js components:** Allows for custom components and interactive elements within slides.
- **Theming:** Supports various themes to customize the presentation's appearance. This presentation uses `@slidev/theme-seriph`.
- **Code highlighting:** Excellent support for syntax highlighting in code blocks.
- **Export options:** Presentations can be exported to PDF or hosted as static websites.

## Using This Presentation

Here's how you can run, build, and export this presentation:

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js:** (Version 16 or higher recommended) - [Download & Install Node.js](https://nodejs.org/)
- **pnpm:** Slidev uses pnpm as its preferred package manager. If you don't have it, you can install it after installing Node.js:
  ```bash
  npm install -g pnpm
  ```

### 1. Running Locally (for Development/Viewing)

This is the recommended way to view the presentation interactively and see changes live as you edit the slides.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd slidev-shared-ptr-presentation
    ```
2.  **Install dependencies:**
    ```bash
    pnpm install
    ```
3.  **Start the development server:**
    ```bash
    pnpm dev
    ```
4.  **Open in your browser:**
    Navigate to `http://localhost:3030` (or the port shown in your terminal).

Changes made to `slides.md` or any custom components will be reflected live in the browser.

### 2. Building for Static Hosting

You can build the presentation into a static website that can be hosted on platforms like GitHub Pages, Netlify, or Vercel.

1.  **Install dependencies (if you haven't already):**
    ```bash
    pnpm install
    ```
2.  **Build the presentation:**
    ```bash
    pnpm build
    ```
    This command will generate a `dist/` directory containing all the static files for your presentation.
3.  **Deploy the `dist/` directory:**
    Upload the contents of the `dist/` directory to your hosting provider.

### 3. Exporting to PDF

Slidev allows you to export your presentation as a PDF document.

1.  **Install dependencies (if you haven't already):**
    ```bash
    pnpm install
    ```
2.  **Export to PDF:**
    ```bash
    pnpm export
    ```
    This command will generate a PDF file of your presentation (e.g., `slides-export.pdf`) in the project root, or sometimes in a `dist/` or similar folder, depending on Slidev's version and configuration. Check the command output for the exact location.

    **Note:** For the best PDF export results, you might need to install `playwright-chromium`:
    ```bash
    pnpm playwright install chromium
    ```
    Run the `pnpm export` command again after installing Playwright.

## Project Structure

Here's a brief overview of the important files and directories:

-   `slides.md`: The main file containing all the slides written in Markdown. This is where you'll spend most of your time editing content.
-   `components/`: This directory can house custom Vue.js components used within your slides.
-   `layouts/`: Custom layouts for your slides can be defined here.
-   `styles/`: Global styles or overrides can be placed in this directory.
-   `public/`: Static assets (images, fonts, etc.) that are copied to the build output.
-   `package.json`: Project configuration, scripts, and dependencies.
-   `vite.config.ts` (optional): For advanced Vite configuration if needed.
-   `uno.config.ts` (optional): For configuring UnoCSS if you're using it for utility CSS.

## Theme

This presentation uses the `@slidev/theme-seriph` theme, which provides a clean and elegant look. You can explore other themes or customize this one further.

---

Learn more about Slidev at the [official documentation](https://sli.dev/).
