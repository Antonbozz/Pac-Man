import numpy as np

TASK_TYPES = [
        'Углы треугольника',
        'Теорема Пифагора',
        'Площадь квадрата',
        'Доли',
    ]
TASK_TEXT = {
    'Углы треугольника': 'Два угла треугольника равны _var1_ и _var2_ градусов.\nНайдите третий угол',
    'Теорема Пифагора':
        'Найдите квадрат длины гипотенузы\nпрямоугольного треугольника\nс длинами катетов _var1_ и _var2_',
    'Площадь квадрата': "Найдите площадь квадрата со стороной длины _var1_",
    'Доли': "Найдите число, которое составляет _var1_% от числа _var2_",
}

class Task:

    def triangle_angles(self):
        task_text = TASK_TEXT['Углы треугольника']
        var_1 = np.random.randint(1, 180)
        var_2 = np.random.randint(1, 180-var_1)
        self.answer = round(180-var_1 - var_2,2)
        self.text = task_text.replace('_var1_', str(var_1)).replace('_var2_', str(var_2))

    def piphagor(self):
        task_text = TASK_TEXT['Теорема Пифагора']
        var_1 = np.random.randint(1, 25)
        var_2 = np.random.randint(1, 25)
        self.text = task_text.replace('_var1_', str(var_1)).replace('_var2_', str(var_2))
        self.answer = round(var_1**2 + var_2**2,2)

    def square(self):
        task_text = TASK_TEXT['Площадь квадрата']
        var_1 = np.random.randint(1, 25)
        self.text = task_text.replace('_var1_', str(var_1))
        self.answer = round(var_1**2,2)

    def share(self):
        task_text = TASK_TEXT['Доли']
        var_1 = np.random.randint(1, 100)
        var_2 = np.random.randint(1, 100)
        self.text = task_text.replace('_var1_', str(var_1)).replace('_var2_', str(var_2))
        self.answer = round(var_1/100*var_2,2)

    TASK_GENERATION = {
        'Углы треугольника': triangle_angles,
        'Теорема Пифагора': piphagor,
        'Площадь квадрата': square,
        'Доли': share,
    }

    def generate_task(self):
        task_type = TASK_TYPES[np.random.randint( len(TASK_TYPES))]
        self.TASK_GENERATION[task_type](self)

    def __init__(self):
        self.answer = None
        self.text = ''
        self.generate_task()

