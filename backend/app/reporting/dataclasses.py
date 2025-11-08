from dataclasses import dataclass

@dataclass
class ParserConfig:
    #если в конструктор не передали значение дефолтное возьмется
    example_predicate: str = "^[аё]\d{0,1}$"

# Идея в том чтобы создать конфиг при запросе на апи и потом из этого конфига тырить предикаты,
# на эндпоинте создал его один раз и передал дальше. НИКАКИХ ГЛОБАЛЬНЫХ СОСТОЯНИЙ 

@dataclass
class Group:
    name: str = ""

    lession: int = 0
    practice: int = 0
    labs: int = 0
    online_lession: int = 0

    def get_formatted(self):
        #вдруг тебе понадобится как то преобразовать данные или получать их вместе с названием
        pass

#не передавай в конструктор группы ничего, только имя, все остальное пусть с нулями будет