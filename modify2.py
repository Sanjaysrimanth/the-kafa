import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div class="menu-item">\s*<img src="[^"]*" alt="(.*?)" class="item-bg">\s*<div class="item-overlay">\s*<div class="item-overlay-text">\s*<span class="item-name">.*?</span>\s*<span class="item-desc">(.*?)</span>\s*</div>\s*<span class="item-price">(.*?)</span>\s*</div>\s*</div>'

def replacer(match):
    name = match.group(1).strip()
    desc = match.group(2).strip()
    price = match.group(3).strip()
    
    new_html = f'''<div class="menu-item-wrapper">
                            <div class="menu-item-card">
                                <img src="coffee_sample.png" alt="{name}" class="item-bg">
                            </div>
                            <div class="menu-item-info">
                                <div class="info-top">
                                    <span class="info-category">KAFA</span>
                                    <span class="item-price">{price}</span>
                                </div>
                                <span class="item-name">{name}</span>
                                <span class="item-desc">{desc}</span>
                            </div>
                        </div>'''
    return new_html

new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html to Movie Poster style")
