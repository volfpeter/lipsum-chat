# What is this?

This project is a technology demonstration for server-side rendering with Python, FastAPI, and htmx; in the disguise of an AI chatbot that responds to questions about beer and coffee. More specifically the project showcases the following libraries:

- [FastAPI](https://fastapi.tiangolo.com/): A modern, async, Python web framework.
- [FastHX](https://volfpeter.github.io/fasthx/): Server-side rendering utility with HTMX support for FastAPI.
- [htmy](https://volfpeter.github.io/htmy/): A powerful, async, pure-Python server-side rendering engine.
- [htmx](https://htmx.org/): A JavaScript library for making AJAX requests and DOM updates using HTML attributes.

Importantly, the project **does not** use Jinja or any other traditional templating engine. Instead, it uses `htmy` – in some cases with plain `html` and `markdown` snippets with no custom templating syntax –, so you can enjoy all the benefits of modern IDEs, linters, static code analysis tools, and coding assistants.

Styling is done with [TailwindCSS v4](https://tailwindcss.com/) and [DaisyUI v5](https://daisyui.com/), but the project is not a TailwindCSS or DaisyUI demo, the focus is entirely on server-side rendering.

# Is it open source?

This project is fully open source, you can find the code on [GitHub](https://github.com/volfpeter/lipsum-chat).

# Is my data secure?

The backend **does not** store or process any data, so yes, your data is fully secure. 😌
