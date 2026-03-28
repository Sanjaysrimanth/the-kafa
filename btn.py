import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

btn_html = r'''<span class="item-desc">\1</span>
                                <button class="add-btn">
                                    <span class="tick">✓</span>
                                    <span class="add-text">Add</span>
                                </button>'''

new_html = re.sub(r'<span class="item-desc">(.*?)</span>', btn_html, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Injected buttons successfully")
