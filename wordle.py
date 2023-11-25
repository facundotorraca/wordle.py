"""
Here is the implementation of a wordle, a 100% in python
CLI oriented.

Why I'm doing this? I dont fucking know. 
Maybe to find purpose in life? Is a very good answer for such
an insignificant thing. 

This wordle will change humanity? Probably not (but we never know).
It will probably be destroyed in some millions of years when the sun
grow in such a big size that will burn the earth or be destroyed in the
next war with nuclear weapons, or also with when python7 is out ansd this 
library wont be compatible anymore...

Who knows the future, we only know the wordle word for today :) Enjoy it

Facundo Torraca
"""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static
from textual.widgets import Placeholder


WORDLE_APP_NAME = "wordle.py"

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

GRID_SIZE = 5

class WordleApp(App):
    """A working 'desktop' calculator."""

    CSS_PATH = "wordle.tcss"

    def compose(self) -> ComposeResult:
        """Add our buttons."""
        yield Header()

        with Container(id="wordle-grid"):
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    yield Static(f"{(i*GRID_SIZE) + j + 1}", classes="box")

        yield Footer()
    

if __name__ == "__main__":
    WordleApp().run()