from PIL import Image

# convert_to_grayscale - преобразует в черно белый формат изображение
def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")  # преобразование в черно-белый формат
    return grayscale_image

# crop_center - обрезает центр изображения по заданным размерам
def crop_center(image, crop_width, crop_height):
    width, height = image.size
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

# image_to_array - Преобразуем черно-белое изображение в массив значений
def image_to_array(image):
    image_array = list(image.getdata())
    width, height = image.size
    image_array = [image_array[i * width:(i + 1) * width] for i in range(height)]
    return image_array

# Преоразуем массив в черно белую фотографию
def array_to_image(image_array):
    width = len(image_array[0])
    height = len(image_array)

    grayscale_image = Image.new("L", (width, height))

    flatten_image = [pixel for row in image_array for pixel in row]

    grayscale_image.putdata(flatten_image)

    return grayscale_image

# Пропускаем изображение через фильтр и получаем массив признаков
def filtr(image_array, filter, step):
    # Создаем пустой массив, который заполним
    x, y = len(image_array), len(image_array)
    array = [[0 for i in range(y)] for j in range(x)]


    for i in range(0,len(image_array)-2, step):
        for j in range(0, len(image_array[i])-2, step):
            # array[i][j] = [[array[i+k][j+m] * filter[k][m] for k in range(3)] for m in range(3)]
            array_pr = 0
            for k in range(len(filter)):
                for m in range(len(filter)):
                    array_pr = array_pr + image_array[i+k][j+m] * filter[k][m]

            array[i][j] = array_pr

    i_max = 0
    i_min = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if i_max < array[i][j]:
                i_max = array[i][j]
            if i_min > array[i][j]:
                i_min = array[i][j]
    print(f'Максимальная сумма: {i_max}')
    print(f'Минимальная сумма:{i_min}')
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = (array[i][j] -i_min) / ((i_max - i_min)/255)
            if array[i][j] > 150:
                array[i][j] = 255
            else:
                array[i][j] = 0

    return array

# Функция для пуллинга массивов
# def pull_maximum(array):
#     for i in range(0,len(image_array)-2, 3):
#         for j in range(0,len(image_array)-2, 3):


# Путь к исходной цветной картинке
input_image_path = "Images/Test.jpg"

# Путь для сохранения черно-белой версии картинки
grayscale_image_path = "Images/grayscale_image.jpg"

# Преобразуем изображение в черно-белое
grayscale_image = convert_to_grayscale(input_image_path)
grayscale_image.save(grayscale_image_path)

# Обрежем центр изображения размером 300 на 300 пикселей
cropped_image = crop_center(grayscale_image, 900, 900)

# Преобразуем кусочек изображения в массив значений
image_array = image_to_array(cropped_image)

fil_1 = [[1, 0, -1],
         [1, 0, -1],
         [1, 0, -1]]

fil_2 = [[-1, -1, -1],
         [0, 0, 0],
         [1, 1, 1]]

fil_3 = [[-1, -1, 0],
         [-1, 0, 1],
         [0, 1, 1]]

# Получаем массивы, которые получились после пропускания картинки через фильтр
# step - страйт, через сколько шагаем
image_fin_ver_pol = filtr(image_array, fil_1, 1)
image_fin_gor_pol = filtr(image_array, fil_2, 1)
image_fin_ugl_pol = filtr(image_array, fil_3, 1)

# Делаем пуллинг массивов и получаем упрощенный массив
# image_fin_ver_pull = pull_maximum(image_fin_ver_pol)
# image_fin_gor_pull = pull_maximum(image_fin_gor_pol)
# image_fin_ugl_pull = pull_maximum(image_fin_ugl_pol)

# Преобразуем массив в черно-белую фотографию
grayscale_image_ver_pol = array_to_image(image_fin_ver_pol)
grayscale_image_gor_pol = array_to_image(image_fin_gor_pol)
grayscale_image_ugl_pol = array_to_image(image_fin_ugl_pol)

# Сохраняем полученную фотографию
grayscale_image_ver_pol.save("Images/vert_lin.jpg")
grayscale_image_gor_pol.save("Images/goriz_lin.jpg")
grayscale_image_ugl_pol.save("Images/uglovoy.jpg")

# grayscale_image_ver_pol.show(title="vert")
# grayscale_image_gor_pol.show(title="goriz")
# grayscale_image_ugl_pol.show(title="ugol")
