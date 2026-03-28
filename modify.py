import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    name = match.group(1).strip()
    price = match.group(2).strip()
    desc = match.group(3).strip()
    
    new_html = f'''<div class="menu-item">
                            <img src="coffee_sample.png" alt="{name}" class="item-bg">
                            <div class="item-overlay">
                                <div class="item-overlay-text">
                                    <span class="item-name">{name}</span>
                                    <span class="item-desc">{desc}</span>
                                </div>
                                <span class="item-price">{price}</span>
                            </div>
                        </div>'''
    return new_html

pattern = r'<div class="menu-item">\s*<div class="item-header">\s*<span class="item-name">(.*?)</span>\s*<span class="item-dots"></span>\s*<span class="item-price">(.*?)</span>\s*</div>\s*<p class="item-desc">(.*?)</p>\s*</div>'

new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html")
