# data-hack
Repository for DATA HACK 2022
---
## Описание папок
- **config** - конфигурационные файлы, необходимые для ETL процесса, а так же шаблон-пример для создания этих конфигов _config_template.yaml_
- **engine** - необходимые для ETL методы: reader, loader, runner
- **src_postgres** - сборка и запуск PostgreSQL, в котором автоматически генерируется тестовый набор данных
- **meta_postgres** - сборка и запуск PostgreSQL, в котором создается таблица для логирования
---
## Включение окружения
```shell
conda create --name datahack python=3.9
conda activate datahack
pip install -r requirements.txt
```
---
## Сборка и запуск PostgreSQL-источника и PostgreSQL для логирования

```shell
cd src_postgres
docker-compose up -d --build
cd ..
cd meta_postgres
docker-compose up -d --build
```

---
## Запуск из консоли

`python run_engine.py --path-to-config path_to_config`
