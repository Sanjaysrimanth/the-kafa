import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<button class="add-btn">\s*<span class="tick">.*?</span>\s*<span class="add-text">Add</span>\s*</button>'

replacement = '''<div class="cart-action">
                                <button class="add-btn">
                                    <span class="tick">✓</span>
                                    <span class="add-text">Add</span>
                                </button>
                                <div class="qty-group hidden">
                                    <span class="qty-count">1</span>
                                    <button class="qty-plus">+</button>
                                </div>
                            </div>'''

new_html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Added quantity selectors")
