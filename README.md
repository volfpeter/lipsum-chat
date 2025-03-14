# Lipsum chat

This project is a technology demonstration for server-side rendering with Python, FastAPI, and htmx; in the disguise of an AI chatbot that responds to questions about beer and coffee. More specifically the project showcases the following libraries:

- [FastAPI](https://fastapi.tiangolo.com/): A modern, async, Python web framework.
- [FastHX](https://volfpeter.github.io/fasthx/): Server-side rendering utility with HTMX support for FastAPI.
- [htmy](https://volfpeter.github.io/htmy/): A powerful, async, pure-Python server-side rendering engine.
- [htmx](https://htmx.org/): A JavaScript library for making AJAX requests and DOM updates using HTML attributes.

Importantly, the project **does not** use Jinja or any other traditional templating engine. Instead, it uses `htmy` – in some cases with plain `html` and `markdown` snippets with no custom templating syntax –, so you can enjoy all the benefits of modern IDEs, linters, static code analysis tools, and coding assistants.

Styling is done with [TailwindCSS v4](https://tailwindcss.com/) and [DaisyUI v5](https://daisyui.com/), but the project is not a TailwindCSS or DaisyUI demo, the focus is entirely on server-side rendering.

## Support

Need help kickstarting a new project with this or a similar toolchain? [Get in touch!](https://www.volfp.com/contact)

## Getting started

For a seamless experience, you need `uv` to be installed. If not available, you can find the required dependencies in `pyproject.toml`.

With `uv` in place, all you need to do is run `uv run uvicorn app.main:app --reload` and open http://127.0.0.1:8000/ in your browser.

`uv run` tools:

- Linting: `ruff check .` or `ruff check . --fix`
- Formatting: `ruff format .` or `ruff format . --check` for format check.
- Static type analysis: `uv run mypy .`

## Similar projects

- [fastapi-htmx-tailwind-example](https://github.com/volfpeter/fastapi-htmx-tailwind-example): A similar, but slightly outdated technology demonstration using Jinja and MongDB, with more focus on HTMX.

## License - MIT

The package is open-sourced under the conditions of the [MIT license](https://choosealicense.com/licenses/mit/).
