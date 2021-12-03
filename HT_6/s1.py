"""
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір 
   автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - 
   відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......

"""
import time


def trafficLightGen():
    red = 'Red   '
    yel = 'Yellow'
    green = 'Green '
    colorsForLoop = 6
    yellForLoop = 2
    carCollors = [[[color] * (colorsForLoop-yellForLoop), [yel] * yellForLoop] for color in [red, green]]
    pedestrianCollors = [[[green] * colorsForLoop, [red] * colorsForLoop]]
    carCollors = [l for k in carCollors for d in k for l in d]
    pedestrianCollors = [l for k in pedestrianCollors for e in k for l in e]
    while True:
        for i, j in zip(carCollors, pedestrianCollors):
            time.sleep(1)
            yield print(f"{i:>}    {j:<}")


trafficLightIter = trafficLightGen()
for i in trafficLightIter:
    pass
