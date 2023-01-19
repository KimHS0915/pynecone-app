import pynecone as pc


config = pc.Config(
    app_name="todo_list",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
