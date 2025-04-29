import markdown2
import os

# Словарь с соответствием секций и Markdown-файлов
content = {
    "Documentation": "test_task/logger.md",
    "Test_task": "test_task/gala_dinner.md",
    "Dev_doc_proc": "test_task/work_process_ru.md"
}

html_template_path = "test_task/index_template.html"
output_html_file = "test_task/index.html"

# Чтение HTML-шаблона
with open(html_template_path, 'r', encoding='utf-8') as template_file:
    template = template_file.read()

# Копируем шаблон для модификации
output_html = template

# Обработка каждого Markdown-файла
for section_id, md_file in content.items():
    # Проверка существования файла
    if not os.path.exists(md_file):
        print(f"Файл {md_file} не найден!")
        continue
    
    # Чтение Markdown-файла
    with open(md_file, 'r', encoding='utf-8') as md:
        md_content = md.read()
    
    # Конвертация Markdown в HTML
    html_content = markdown2.markdown(md_content, extras=["tables"])
    
    # Поиск секции в шаблоне и замена её содержимого
    section_tag = f'<section id="{section_id}"></section>'
    section_with_content = f'<section id="{section_id}">{html_content}</section>'
    output_html = output_html.replace(section_tag, section_with_content)

# Сохранение результата в index.html
with open(output_html_file, 'w', encoding='utf-8') as output_file:
    output_file.write(output_html)

print(f"Файл {output_html_file} успешно создан!")