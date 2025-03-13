def replace_py_extension(py_file: str, ext: str = "html") -> str:
    """
    Replaces the `py` extension in a file path with the given one,
    keeping the rest of the path the same.
    """
    if not py_file.endswith(".py"):
        raise ValueError("Input file must have a `.py` extension.")

    if ext.startswith("."):
        ext = ext[1:]

    return f"{py_file[:-2]}{ext}"
