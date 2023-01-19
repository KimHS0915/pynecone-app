import random

import pynecone as pc


class CountState(pc.State):
    count: int = 0

    def increment(self):
        self.count = self.count + 1 if self.count < 100 else 0

    def decrement(self):
        self.count = self.count - 1 if self.count > 0 else 100

    def randomize(self):
        self.count = random.randint(0, 100)


def index():
    return pc.center(
        pc.vstack(
            pc.heading(CountState.count, font_size='2em'),
            pc.hstack(
                pc.button(
                    'Decrement',
                    color_scheme='red',
                    border_radius='1em',
                    on_click=CountState.decrement,
                ),
                pc.button(
                    'Increment',
                    color_scheme='blue',
                    border_radius='1em',
                    on_click=CountState.increment,
                ),
                pc.button(
                    'Randomize',
                    color_scheme='green',
                    border_radius='1em',
                    on_click=CountState.randomize,
                ),
                padding='2em',
            ),
            padding_y='10em',
            font_size='1em',
            text_align='center',
        )
    )


# Add state and page to the app.
app = pc.App(state=CountState)
app.add_page(index, title='Counter')
app.compile()
