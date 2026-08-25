from pathlib import Path


def extract_context(
    source_file: str,
    target_line: int,
    context_lines: int = 5
) -> str:
    """
    Extract source-code context around a target line.

    Args:
        source_file: Path to the C/C++ source file.
        target_line: 1-based line number of the violation.
        context_lines: Number of lines before and after the target.

    Returns:
        Source-code context as a formatted string.
    """

    path = Path(source_file)

    if not path.exists():
        raise FileNotFoundError(
            f"Source file not found: {source_file}"
        )

    if target_line < 1:
        raise ValueError(
            "target_line must be greater than or equal to 1"
        )

    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    if target_line > len(lines):
        raise ValueError(
            f"Target line {target_line} exceeds "
            f"file length {len(lines)}"
    )

    start_line = max(1, target_line - context_lines)
    end_line = min(
        len(lines),
        target_line + context_lines
    )

    context = []

    for line_number in range(start_line, end_line + 1):
        line_content = lines[line_number - 1].rstrip("\n")

        marker = ">>" if line_number == target_line else "  "

        context.append(
            f"{marker} {line_number:4} | {line_content}"
        )

    return "\n".join(context)


if __name__ == "__main__":
    result = extract_context(
        "sample_project/src/sensor.c",
        target_line=26,
        context_lines=5
    )

    print(result)

def extract_target_line(
    source_file,
    target_line: int
) -> str:
    """Extract the exact source-code statement at the target line."""

    with open(source_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if target_line < 1 or target_line > len(lines):
        raise ValueError(
            f"Target line {target_line} is outside "
            f"the file range 1-{len(lines)}."
        )

    return lines[target_line - 1].strip()