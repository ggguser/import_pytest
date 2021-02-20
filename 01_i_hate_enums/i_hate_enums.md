Класс Enum удобен для хранения строковых констант. Это как дроп-даун в IDE. 
Но чаще всего имя совпадает со значением, поэтому обращение по атрибутам .name и .value не имеет смысла. 
Это только доставляет неудобства. Одно из них в том, что 

вместо  
```assert BRAIN.SMALL == 'small'```

нужно использовать  
```assert BRAIN.SMALL.value == 'small'```

Удобнее всего будет отнаследоваться от str и переопределить `__str__`:
```python
class BRAIN(str, Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    GALAXY = 'galaxy'

    def __str__(self) -> str:
        return str.__str__(self)
```
Это даёт нормальное итерирование и сравнение (см. gist):
```
def test1():
    assert BRAIN.SMALL == "small"

def test4():
    assert [thing for thing in BRAIN] == ["small", "medium", "galaxy"]


def test5():
    assert list(BRAIN) == ["small", "medium", "galaxy"]
```
Подробнее в статье [I hate Enums](https://www.cosmicpython.com/blog/2020-10-27-i-hate-enums.html)