from todoist_api_python.api import TodoistAPI
import env


def handler():
    api = TodoistAPI(env.API_KEY_TODOIST)
    res = []
    try:
        tasks = api.get_tasks()
        # print(tasks)
        for task in tasks:
            res.append({task.content, task.is_completed})
        print(res)
    except Exception as error:
        print(error)


handler()
