# Lesson 10 — UI Tests with Selene + Allure + GitHub Actions

![Tests & Allure Report](https://github.com/goncharrov-a/lesson_10/actions/workflows/test.yml/badge.svg)

---

## 📊 Allure Report

Последний Allure отчёт:

![Tests & Allure Report](https://github.com/goncharrov-a/lesson_10/actions/workflows/test.yml/badge.svg)

---

## 📌 Что реализовано

Проект UI авто тестов и публикуемыми Allure отчётами.

---

## 1. UI-тесты (Selene)

Реализованы 4 вида тестов:

- **Чистый Selene**
- **Тест с лямбда-шагами (`with allure.step`)**
- **Тест со степ-декораторами (`@allure.step`)**
- **Полный тест с аннотациями Allure**:  
  epic, feature, story, title, description, labels, issue, testcase — всё корректно отображается в отчёте.

Логика тестов одинаковая

---

## 2. Allure Report

Генерация отчёта через `allure-pytest`  
Публикация на GitHub Pages  
Поддержка **истории**:  
trend, retries, timeline  
Автоматические вложения при падениях:

- скриншот
- HTML страницы
- console logs
- JSON (метаданные)

---

## 3. GitHub Actions

Полностью рабочий pipeline:

- Запуск тестов при:
  - `push` в `main`
  - `pull_request`
  - `ручном запуске` (`workflow_dispatch`)
- Публикация Allure отчёта в ветку **gh-pages**
- Автоматическое обновление истории отчётов
- Доступный отчёт:  
  **https://goncharrov-a.github.io/lesson_10**

---
## 🚀 Используемые технологии

- Python 3.x
- Pytest
- Selene --pre
- Selenium (headless=new)
- Allure
- GitHub Actions
- GitHub Pages

---

## 📝 Требования

Файл `requirements.txt`:
- allure-pytest==2.15.2
- pytest==9.0.1
- selene==2.0.0rc9
