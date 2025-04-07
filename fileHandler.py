# python
class fileHandler:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @staticmethod
    def _handle_error(e: Exception) -> str:
        return str(e)

    def read_all(self) -> str | list[str]:
        """Return all lines of the file as a list."""
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def read_partially(self, start: int, end: int) -> str:
        """Return concatenated lines in the range [start, end)."""
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            if start < 0 or end > len(lines) or start >= end:
                return "Invalid line range."
            return ''.join(lines[start:end])
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def read_one(self, n: int) -> str:
        """Return the n-th line (0-indexed) from the file."""
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            if n < 0 or n >= len(lines):
                return "Line number out of range."
            return lines[n].strip()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def write_all(self, content: list) -> str:
        """Overwrite the file with the provided content list."""
        try:
            with open(self.file_path, 'w') as file:
                file.writelines(content)
            return "Content written successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def write_partially(self, start: int, end: int, new_content: list) -> str:
        """
        Replace lines in the range [start, end) with new_content.
        new_content must have the same number of elements as the specified range.
        """
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if start < 0 or end > len(lines) or start >= end or len(new_content) != (end - start):
                    return "Invalid line range or content size."
                # Update the specified range.
                lines[start:end] = [line.rstrip('\n') + '\n' for line in new_content]
                file.seek(0)
                file.writelines(lines)
            return "Content written successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def append_all(self, content: list) -> str:
        """Append each string in content to the file."""
        try:
            with open(self.file_path, 'a') as file:
                file.writelines(content)
            return "Content appended successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def append_one(self, n: int, extra: str) -> str:
        """Append extra text to the n-th line (0-indexed)."""
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if n < 0 or n >= len(lines):
                    return "Line number out of range."
                lines[n] = lines[n].rstrip('\n') + extra + '\n'
                file.seek(0)
                file.writelines(lines)
            return "Content appended successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def insert_all(self, n: int, content: list) -> str:
        """Insert new lines starting at position n."""
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if n < 0 or n > len(lines):
                    return "Invalid line number."
                new_lines = [line.rstrip('\n') + '\n' for line in content]
                lines[n:n] = new_lines
                file.seek(0)
                file.writelines(lines)
            return "Content inserted successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def insert_one(self, n: int, line: str) -> str:
        """Insert a single line at position n."""
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if n < 0 or n > len(lines):
                    return "Invalid line number."
                lines.insert(n, line + '\n')
                file.seek(0)
                file.writelines(lines)
            return "Content inserted successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def delete_all(self) -> str:
        """Erase all contents of the file."""
        try:
            with open(self.file_path, 'w') as file:
                file.write("")
            return "File deleted successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def delete_one(self, n: int) -> str:
        """Delete the n-th line (0-indexed) from the file."""
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if n < 0 or n >= len(lines):
                    return "Line number out of range."
                lines.pop(n)
                file.seek(0)
                file.writelines(lines)
            return "Line deleted successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def update_all(self, content: list) -> str:
        """Overwrite the file with new content."""
        try:
            with open(self.file_path, 'w') as file:
                file.writelines(content)
            return "Content updated successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)

    def update_one(self, n: int, content: str) -> str:
        """Replace the n-th line with new content."""
        try:
            with open(self.file_path, 'r+') as file:
                lines = file.readlines()
                if n < 0 or n >= len(lines):
                    return "Line number out of range."
                lines[n] = content + '\n'
                file.seek(0)
                file.writelines(lines)
            return "Content updated successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return self._handle_error(e)