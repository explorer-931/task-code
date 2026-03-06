from task_manager import load_tasks,save_tasks,add_task,list_tasks


tasks_list = []

add_task(tasks_list,"reading")
add_task(tasks_list,"reading")

save_tasks(tasks_list)
list_tasks(tasks_list)