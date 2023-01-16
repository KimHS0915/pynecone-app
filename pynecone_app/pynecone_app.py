"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    text: str = 'Hello World'
    color: str = 'red'

    def flip_color(self):
        if self.color == 'red':
            self.color = 'blue'
        else:
            self.color = 'red'


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.badge(
                State.text,
                color_scheme=State.color,
                on_click=State.flip_color,
                font_size='1.5em',
                _hover={
                    'cursor': 'pointer',
                }
            ),
            pc.button(
                'Hello Pynecone',
                border_radius='1em',
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                _hover={
                    "opacity": 0.85,
                },
                on_click=State.flip_color,
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


def about():
    return pc.text('About')


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(about)
app.compile()
