from itertools import product

STUDENT_ID = 16

print(
    list(
        product(
            ('python 3.12', 'python 3.11', 'python 3.10', 'python 3.9'),
            ('requirements.txt', 'poetry', 'pipenv'),
        )
    )[(STUDENT_ID - 1) % 12]
)