"""Welcome to Pynecone! This file outlines the steps to create a basic app."""

import pynecone as pc


class TodoState(pc.State):
    items = []
    new_item: str

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = ''

    def finish_item(self, item):
        self.items = [i for i in self.items if i != item]


def render_item(item):
    return pc.list_item(
        pc.hstack(
            pc.checkbox(
                size='lg',
                color_scheme='red'
            ),
            pc.text(item, font_size='1.25em'),
            pc.button(
                'del',
                on_click=lambda: TodoState.finish_item(item),
                height='1.5em',
                background_color='white',
                border='1px solid blue',
            ),
        )
    )


def todo_list():
    return pc.container(
        pc.vstack(
            pc.heading('Todo List'),
            pc.hstack(
                pc.input(
                        on_blur=TodoState.set_new_item,
                        placeholder='Add a todo ...',
                        bg='white',
                ),
                pc.button('Add', on_click=TodoState.add_item, bg='white'),
            ),
            pc.divider(),
            pc.ordered_list(
                pc.foreach(TodoState.items, lambda item: render_item(item)),
            ),
            bg='white',
            margin='5em',
            padding='2em',
            border_radius='0.5em',
            shadow='lg',
        )
    )


# Add state and page to the app.
app = pc.App(state=TodoState)
app.add_page(todo_list, title='Todo List', path='/')
app.compile()
