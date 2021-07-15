import pdb
from models.task import Task
from models.user import User

import repositories.task_repositories as task_repository
import repositories.user_repositories as user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_repository.save(user_1)
user_2 = User("Victor", "McDade")
user_repository.save(user_2)


task_1 = Task("Walk dog", user_1, 60)
task_2 = Task("Feed cat", user_2, 5)

task_repository.save(task_1)
task_repository.save(task_2)

pdb.set_trace()



