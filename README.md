# data-hack
Repository for DATA HACK 2022
---
## Описание папок
- **config** - конфигурационные файлы, необходимые для ETL процесса, а так же шаблон-пример для создания этих конфигов _config_template.yaml_
- **engine** - необходимые для ETL методы: reader, loader, runner
---

## Сборка и запуск PostgreSQl-источника и PostgreSQl для логирования

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

---
## Правила нейминга таблиц
**T0DO**
