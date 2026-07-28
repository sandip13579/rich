from rich.cells import get_character_cell_size
import unicodedata

character = "…"

print("Character:", character)
print("Unicode codepoint:", ord(character))
print("Hex:", hex(ord(character)))
print("East Asian Width:", unicodedata.east_asian_width(character))
print("Rich width:", get_character_cell_size(character))