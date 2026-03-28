document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Toggle hamburger animation
            const spans = mobileMenuBtn.querySelectorAll('span');
            if (navLinks.classList.contains('active')) {
                spans[0].style.transform = 'translateY(8px) rotate(45deg)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'translateY(-8px) rotate(-45deg)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                mobileMenuBtn.click();
            }
        });
    });

    // Navbar Scrolled Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Scroll Reveal Animation (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.scroll-reveal').forEach(element => {
        observer.observe(element);
    });

    // Menu Tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    const menuCategories = document.querySelectorAll('.menu-category');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            tabBtns.forEach(b => b.classList.remove('active'));
            menuCategories.forEach(c => {
                c.classList.remove('active');
                c.classList.remove('fade-in-up');
            });

            // Add active class to clicked tab and its content
            btn.classList.add('active');
            const targetId = btn.getAttribute('data-tab');
            const targetContent = document.getElementById(targetId);
            
            // Force reflow to restart animation simply
            void targetContent.offsetWidth;
            
            targetContent.classList.add('active');
            targetContent.classList.add('fade-in-up');
        });
    });

    // --- Global Cart State & UI Logic ---
    const cart = {};
    const floatingCart = document.getElementById('floating-cart');
    const cartBadge = document.getElementById('cart-badge');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCartBtn = document.getElementById('close-cart');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalPrice = document.getElementById('cart-total-price');

    // Sidebar Toggles
    floatingCart.addEventListener('click', () => {
        cartOverlay.classList.add('active');
        cartSidebar.classList.add('open');
    });

    const closeCart = () => {
        cartOverlay.classList.remove('active');
        cartSidebar.classList.remove('open');
    };
    closeCartBtn.addEventListener('click', closeCart);
    cartOverlay.addEventListener('click', closeCart);

    // Global UI Sync
    function updateCartUI() {
        let totalQty = 0;
        let totalPrice = 0;
        let html = '';

        for (const [name, item] of Object.entries(cart)) {
            totalQty += item.qty;
            totalPrice += (item.qty * item.price);
            
            html += `
                <div class="sidebar-item">
                    <img src="${item.img}" alt="${name}" class="sidebar-item-img">
                    <div class="sidebar-item-details">
                        <div class="sidebar-item-name">${name}</div>
                        <div class="sidebar-item-price">₹${item.price}</div>
                        <div class="sidebar-item-qty">
                            <button class="sidebar-qty-btn sidebar-minus" data-name="${name}">-</button>
                            <span class="sidebar-count">${item.qty}</span>
                            <button class="sidebar-qty-btn sidebar-plus" data-name="${name}">+</button>
                        </div>
                    </div>
                </div>
            `;
        }

        if (totalQty === 0) {
            html = '<div class="cart-empty">Your cart is empty.</div>';
            floatingCart.classList.remove('visible');
        } else {
            floatingCart.classList.add('visible');
        }

        cartBadge.textContent = totalQty;
        cartTotalPrice.textContent = '₹' + totalPrice;
        cartItemsContainer.innerHTML = html;
        
        // Bind generated sidebar buttons
        document.querySelectorAll('.sidebar-minus').forEach(btn => {
            btn.addEventListener('click', () => adjustCart(btn.dataset.name, -1));
        });
        document.querySelectorAll('.sidebar-plus').forEach(btn => {
            btn.addEventListener('click', () => adjustCart(btn.dataset.name, 1));
        });
    }

    function adjustCart(name, amount) {
        if (cart[name]) {
            cart[name].qty += amount;
            if (cart[name].qty <= 0) {
                delete cart[name];
            }
            updateCartUI();
            syncMenuButtons(name);
        }
    }

    function syncMenuButtons(name) {
        const cartActions = document.querySelectorAll('.cart-action');
        cartActions.forEach(action => {
            const itemWrapper = action.closest('.menu-item-wrapper');
            const itemName = itemWrapper.querySelector('.item-name').textContent.trim();
            
            if (itemName === name) {
                const addBtn = action.querySelector('.add-btn');
                const qtyGroup = action.querySelector('.qty-group');
                const countSpan = action.querySelector('.qty-count');
                const tick = addBtn.querySelector('.tick');
                
                const itemQty = cart[name] ? cart[name].qty : 0;
                
                if (itemQty === 0) {
                    addBtn.classList.remove('added');
                    tick.textContent = '✓';
                    qtyGroup.classList.add('hidden');
                } else {
                    addBtn.classList.add('added');
                    setTimeout(() => {
                        if (addBtn.classList.contains('added')) {
                            tick.textContent = '-';
                        }
                    }, 300);
                    countSpan.textContent = itemQty;
                    qtyGroup.classList.remove('hidden');
                }
            }
        });
    }

    // Attach local Card listeners to global Cart
    const cartActions = document.querySelectorAll('.cart-action');
    cartActions.forEach(action => {
        const addBtn = action.querySelector('.add-btn');
        const plusBtn = action.querySelector('.qty-plus');
        const itemWrapper = action.closest('.menu-item-wrapper');
        const itemName = itemWrapper.querySelector('.item-name').textContent.trim();
        const itemPriceText = itemWrapper.querySelector('.item-price').textContent;
        const itemPrice = parseInt(itemPriceText.replace('₹', ''), 10);
        // Ensure image SRC works correctly locally
        const itemImgTag = itemWrapper.querySelector('.item-bg');
        const itemImg = itemImgTag ? itemImgTag.src : 'coffee_sample.png';

        addBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (!cart[itemName]) {
                cart[itemName] = { price: itemPrice, qty: 1, img: itemImg };
            } else {
                cart[itemName].qty--;
                if (cart[itemName].qty <= 0) {
                    delete cart[itemName];
                }
            }
            updateCartUI();
            syncMenuButtons(itemName);
        });

        plusBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (cart[itemName]) {
                cart[itemName].qty++;
                updateCartUI();
                syncMenuButtons(itemName);
            }
        });
    });

    // Initial render
    updateCartUI();

});
