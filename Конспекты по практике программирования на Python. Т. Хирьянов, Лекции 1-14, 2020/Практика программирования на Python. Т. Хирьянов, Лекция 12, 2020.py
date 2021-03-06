"""
Документация проекта

Документация - это способ вывести коммуникацию между программистами на новый уровень.
Если программой будут пользоваться другие люди требуется обязательное создание документации.

Виды документации:
 - Пользовательский мануал (типа WIKI)
 - Внутренняя документация (в исходном коде, либо размещать отдельно)

 Раздельное хранение внутренней документации от исходного кода приводит
 к неминуемому устареванию и неполноте документации. При изменении кода программист может полениться внести
 изменения в документацию, расположенную где-то в другом месте от исходного кода и так же может лениться ее там
 искать и изучать.

Документация часто страдает от неполноты информации, т.к. в процессе коммуникации программисту проще сказать
коллеге словами, чем подробно описывать в документации. Но слова прозвучали и исчезли, или забылись со временем,
а новые люди уже не смогут получить полноценной информации о коде, т.к. эта информация хранилась в памяти других
программистов, и со временем могла быть забыта, искажена, или может быть утеряна связь с тем человеком, который
обладал нужной инфрмацией.
Письменный текст был, есть и будет самым удобным способом долгосрочной документации.

Устаревание документации хуже чем ее неполнота. Неактуальные комментарии хуже, чем отсутствие комментариев.

При отсутствии документации программист будет вынужден изучать реальное содержание программного кода, с целью
понять как он, работает. На это может потребоваться много дополнительного времени.

При наличии документации программист ее изучает и понимает как работает некоторый код, программа или функция и ему
не нужно самостоятельно разбираться как этот код устроен изнутри, он может сразу его применять.
Если документация соответствует программному коду, то все замечательно, а если документация устарела, то программист,
не зная об этом, начинает использовать программный код, по назначению как описано в документации, что может стать
причиной явных или скрытых проблем, потому что программный код уже может работать не так как было описано.

Внутреннюю документацию можно хранить отдельно от кода, при строгом соблюдения правил сохранения ее актуальности.
Но чаще всего эффективным местом хранения внутренней документации является сам исходный код.
Есть нескольо способ внедрения документации в код:
 0) - самодокументирующийся код (не писать документацию и комментарии совсем), такая документация всегда актуальна
 1) - комментарии  # начинаются с решетки, пишутся на английском языке
 2) - способ сделать автоматическую внутреннюю документацию - документ-строки и аннотации типов используя специальный
      синтаксис разметки reStructuredText (сокращение: ReST, расширение файла: .rst) - облегчённый язык разметки,
      который может быть преобразован в различные форматы — HTML, ePub, PDF и другие.
      Есть и другая разметка MarkDown — это простой язык разметки, используемый для создания форматированного текста
      (например, HTML) с помощью текстового редактора. Он позволяет добавлять к тексту базовое форматирование,
      используя символы, известные и доступные на всех клавиатурах.
 3) - проверяемые утверждения, создаются при помощи assert (специальное слово - утверждение). Правильное восприятие
      assert - реально этому можно верить, потому что если вдруг не так, то это все конец, надо программу переделывать.
      Это влияет минимально на быстродействия. Есть способ при запуске кода игнорировать assert (python -O)
 4) - Контрактное программирование (проектирование). Есть библиотека PyContracts.
      Это метод проектирования программного обеспечения. Он предполагает, что проектировщик должен определить
      формальные, точные и верифицируемые спецификации интерфейсов для компонентов системы. При этом,
      кроме обычного определения абстрактных типов данных, также используются предусловия, постусловия и инварианты.
      Данные спецификации называются «контрактами» в соответствии с концептуальной метафорой условий
      и ответственности в гражданско-правовых договорах.

      Спецификация интерфейса должна быть:
      - формальная
      - точная
      - верифицируемая


Отказоустойчивое программное обеспечение. Концепция fail - fast.
"""


def hypot(x, y):  # допустим мы написали функцию для вычисления гипотенузы треугольника
    return (x * x + y * y) ** 0.5  # такой код нельзя назвать самодокументирующимся, в нем абстрактные имена переменных


def hypotenuse1(leg1, leg2):  # в имена переменных мы заложили четкие понятия на английском языке
    # Square root from sum of squares of triangle legs
    # https://.... link to the Pythagorean theorem
    return (leg1 ** 2 + leg2 ** 2) ** 0.5


def hypotenuse2(leg1: float, leg2: float) -> float:
    """
    Calculates length of hypotenuse of a right triangle.
    # Look https://.... link to the Pythagorean theorem

    :param leg1: length of the first triangle leg.
    :param leg2: length of the other triangle leg.
    :return: length of the hypotenuse of a right triangle

    """
    # Square root from sum of squares of triangle legs
    return (leg1 ** 2 + leg2 ** 2) ** 0.5


def hypotenuse3(leg1: float, leg2: float) -> float:
    """
    Calculates length of hypotenuse of a right triangle.
    # Look https://.... link to the Pythagorean theorem

    :param leg1: length of the first triangle leg.
    :param leg2: length of the other triangle leg.
    :return: length of the hypotenuse of a right triangle

    """
    # Square root from sum of squares of triangle legs
    length = (leg1 ** 2 + leg2 ** 2) ** 0.5
    assert length ** 2 == leg1 ** 2 + leg2 ** 2, "OUCH!!! Pythagorean theorem doesn't work! Stopping program."
    return length


def main():
    x, y = 4, 3  # если ввести 2, 3 то assert выдаст сообщение, в связи с некоторой погрешностью вычислений
    print('Hypotenuse is', hypotenuse3(x, y))


if __name__ == "__main__":
    main()

print(help(hypotenuse2))  # так можно посмотреть документацию по данной функции
