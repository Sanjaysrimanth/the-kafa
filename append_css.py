css = """
/* --- Shopping Cart UI --- */
.floating-cart {
    position: fixed;
    bottom: 30px;
    left: 30px;
    background-color: #000;
    color: #fff;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    cursor: pointer;
    z-index: 100;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.3s ease, visibility 0.3s;
    opacity: 0;
    visibility: hidden;
    transform: scale(0.5) translateY(20px);
}

[data-theme="dark"] .floating-cart {
    background-color: #fff;
    color: #000;
    box-shadow: 0 10px 25px rgba(255,255,255,0.1);
}

.floating-cart.visible {
    opacity: 1;
    visibility: visible;
    transform: scale(1) translateY(0);
}

.floating-cart:hover {
    transform: scale(1.1) translateY(-5px);
}

.cart-badge {
    position: absolute;
    top: -5px;
    right: -5px;
    background-color: #cc0000;
    color: #fff;
    font-size: 0.85rem;
    font-weight: bold;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 3px solid var(--bg-color);
}

.cart-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.6);
    z-index: 999;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s ease;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}

.cart-overlay.active {
    opacity: 1;
    visibility: visible;
}

.cart-sidebar {
    position: fixed;
    top: 0;
    right: 0;
    width: 100%;
    max-width: 400px;
    height: 100vh;
    background-color: var(--bg-color);
    z-index: 1000;
    box-shadow: -10px 0 30px rgba(0,0,0,0.15);
    transform: translateX(100%);
    transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    display: flex;
    flex-direction: column;
}

.cart-sidebar.open {
    transform: translateX(0);
}

[data-theme="dark"] .cart-sidebar {
    background-color: #111;
    box-shadow: -10px 0 30px rgba(0,0,0,0.6);
}

.cart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem;
    border-bottom: 1px solid var(--border-color);
}

.cart-header h2 {
    font-family: var(--font-heading);
    font-size: 1.75rem;
    margin: 0;
}

.close-cart {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--text-color);
    transition: transform 0.3s;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.close-cart:hover {
    background-color: rgba(0,0,0,0.05);
}

[data-theme="dark"] .close-cart:hover {
    background-color: rgba(255,255,255,0.05);
}

.cart-items {
    flex-grow: 1;
    overflow-y: auto;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

/* Empty State */
.cart-empty {
    text-align: center;
    color: var(--text-muted);
    font-style: italic;
    margin-top: 2rem;
}

.sidebar-item {
    display: flex;
    align-items: stretch;
    gap: 1.25rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border-color);
}

.sidebar-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.sidebar-item-img {
    width: 70px;
    height: 90px;
    border-radius: 8px;
    object-fit: cover;
    background-color: #222;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.sidebar-item-details {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.sidebar-item-name {
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
}

.sidebar-item-price {
    color: var(--text-muted);
    font-size: 1rem;
    font-weight: 600;
}

.sidebar-item-qty {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-top: 0.75rem;
}

.sidebar-qty-btn {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: var(--text-color);
    color: var(--bg-color);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    transition: transform 0.2s;
}

.sidebar-qty-btn:active {
    transform: scale(0.9);
}

.sidebar-count {
    font-weight: 700;
    font-size: 1rem;
    min-width: 20px;
    text-align: center;
}

.cart-footer {
    padding: 2rem;
    background-color: var(--bg-color);
    border-top: 1px solid var(--border-color);
    box-shadow: 0 -10px 20px rgba(0,0,0,0.02);
}

[data-theme="dark"] .cart-footer {
    background-color: #111;
}

.cart-total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

.checkout-btn {
    width: 100%;
    padding: 1.25rem;
    background-color: var(--text-color);
    color: var(--bg-color);
    border: none;
    font-weight: 700;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    cursor: pointer;
    transition: transform 0.3s ease;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
}

.checkout-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

[data-theme="dark"] .checkout-btn:hover {
    box-shadow: 0 10px 20px rgba(0,0,0,0.5);
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("CSS appended.")
