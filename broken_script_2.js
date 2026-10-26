
        // Global State
        const EXCHANGE_RATE = parseFloat("1380");
        let cart = JSON.parse(localStorage.getItem('fruitfarm_cart_v2') || '[]');
        let currentGuide = JSON.parse(localStorage.getItem('fruitfarm_active_guide') || 'null');

        // Check URL parameter for referral code (?ref=GUIDE_KIM or ?guide=GUIDE_KIM)
        const urlParams = new URLSearchParams(window.location.search);
        const refParam = urlParams.get('ref') || urlParams.get('guide');
        if (refParam) {
            sessionStorage.setItem('referral_guide_code', refParam.toUpperCase());
        }

        function saveCart() {
            localStorage.setItem('fruitfarm_cart_v2', JSON.stringify(cart));
            updateCartUI();
        }

        function addToCart(id, name, priceUsd, priceKrw, imageUrl, qty = 1) {
            const existing = cart.find(item => item.id === id);
            if (existing) {
                existing.qty += qty;
            } else {
                cart.push({
                    id: id,
                    name: name,
                    price_usd: parseFloat(priceUsd),
                    price_krw: parseInt(priceKrw),
                    image_url: imageUrl,
                    qty: qty
                });
            }
            saveCart();
            openCartModal();
        }

        function changeQty(id, delta) {
            const item = cart.find(i => i.id === id);
            if (!item) return;
            item.qty += delta;
            if (item.qty <= 0) {
                cart = cart.filter(i => i.id !== id);
            }
            saveCart();
        }

        function removeFromCart(id) {
            cart = cart.filter(i => i.id !== id);
            saveCart();
        }

        function updateCartUI() {
            const count = cart.reduce((sum, item) => sum + item.qty, 0);
            const subtotalUsd = cart.reduce((sum, item) => sum + (item.price_usd * item.qty), 0);
            
            // Badges
            const navBadge = document.getElementById('nav-cart-badge');
            if (navBadge) navBadge.textContent = count;
            const countBadge = document.getElementById('cart-item-count-badge');
            if (countBadge) countBadge.textContent = `${count}개`;
            const orderCount = document.getElementById('cartOrderCountText');
            if (orderCount) orderCount.textContent = count;

            // Free shipping calculation ($100 threshold)
            const threshold = 100.0;
            const shippingUsd = (subtotalUsd >= threshold || subtotalUsd === 0) ? 0.0 : 15.0;
            const totalUsd = subtotalUsd + shippingUsd;
            const totalKrw = Math.round(totalUsd * EXCHANGE_RATE);

            // Shipping Progress
            const progress = Math.min(100, Math.round((subtotalUsd / threshold) * 100));
            const pBar = document.getElementById('shippingProgressBar');
            const pText = document.getElementById('shippingProgressText');
            const pPercent = document.getElementById('shippingProgressPercent');
            if (pBar) pBar.style.width = `${progress}%`;
            if (pPercent) pPercent.textContent = `${progress}%`;
            if (pText) {
                if (subtotalUsd >= threshold) {
                    pText.innerHTML = '<span class="text-emerald-400 font-bold"><i class="fa-solid fa-circle-check mr-1"></i>한국 자택 무료 직배송 혜택 달성!</span>';
                } else {
                    const remaining = (threshold - subtotalUsd).toFixed(2);
                    pText.textContent = `$${remaining} 추가 주문 시 한국 무료 직배송`;
                }
            }

            // Totals
            if (document.getElementById('cartSubtotalUsd')) document.getElementById('cartSubtotalUsd').textContent = `$${subtotalUsd.toFixed(2)}`;
            if (document.getElementById('cartShippingUsd')) {
                document.getElementById('cartShippingUsd').textContent = shippingUsd === 0 ? (subtotalUsd > 0 ? '무료' : '$0.00') : `$${shippingUsd.toFixed(2)}`;
            }
            if (document.getElementById('cartTotalUsd')) document.getElementById('cartTotalUsd').textContent = `$${totalUsd.toFixed(2)}`;
            if (document.getElementById('cartTotalKrw')) document.getElementById('cartTotalKrw').textContent = `₩${totalKrw.toLocaleString()}원`;

            // Render Items
            const container = document.getElementById('cartItemsList');
            if (!container) return;
            if (cart.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-12 text-slate-500">
                        <i class="fa-solid fa-basket-shopping text-3xl mb-3 text-slate-600"></i>
                        <p class="text-sm">장바구니가 비어 있습니다.</p>
                        <p class="text-xs text-slate-400 mt-1">푸꾸옥 플래그십 인기 $100 세트를 둘러보세요.</p>
                    </div>
                `;
                return;
            }

            container.innerHTML = cart.map(item => `
                <div class="flex items-center space-x-3 p-3 bg-dark-900 rounded-2xl border border-slate-700/60">
                    <img src="${item.image_url}" alt="${item.name}" class="w-14 h-14 object-cover rounded-xl border border-slate-700">
                    <div class="flex-grow min-w-0">
                        <div class="font-bold text-xs text-white truncate">${item.name}</div>
                        <div class="text-gold-300 font-black text-xs mt-0.5">$${item.price_usd.toFixed(2)} <span class="text-slate-400 font-normal text-[10px]">(${Math.round(item.price_usd * EXCHANGE_RATE).toLocaleString()}원)</span></div>
                    </div>
                    <div class="flex items-center space-x-1.5 bg-dark-800 border border-slate-700 rounded-lg p-1">
                        <button onclick="changeQty(${item.id}, -1)" class="w-5 h-5 flex items-center justify-center text-slate-400 hover:text-white text-xs">-</button>
                        <span class="w-5 text-center text-xs font-bold text-white">${item.qty}</span>
                        <button onclick="changeQty(${item.id}, 1)" class="w-5 h-5 flex items-center justify-center text-slate-400 hover:text-white text-xs">+</button>
                    </div>
                    <button onclick="removeFromCart(${item.id})" class="text-slate-500 hover:text-rose-400 p-1">
                        <i class="fa-solid fa-trash-can text-xs"></i>
                    </button>
                </div>
            `).join('');
        }

        // Cart Modals
        function openCartModal() {
            updateCartUI();
            document.getElementById('cartModal').classList.remove('hidden');
        }
        function closeCartModal() {
            document.getElementById('cartModal').classList.add('hidden');
        }

        // Checkout Modals
        function openCheckoutModal() {
            if (cart.length === 0) {
                alert('장바구니에 담긴 상품이 없습니다.');
                return;
            }
            closeCartModal();
            updateOrderGuideDisplay();
            document.getElementById('checkoutModal').classList.remove('hidden');
        }
        function closeCheckoutModal() {
            document.getElementById('checkoutModal').classList.add('hidden');
        }

        function toggleDeliveryType(val) {
            const labelDirect = document.getElementById('labelDirectKorea');
            const labelLocal = document.getElementById('labelLocalPhuquoc');
            const customsContainer = document.getElementById('customsIdContainer');
            const addrLabel = document.getElementById('addressLabel');
            const custAddress = document.getElementById('custAddress');
            const quickResort = document.getElementById('quickResortSelector');

            if (val === 'direct_korea') {
                labelDirect.className = 'cursor-pointer border border-gold-500/50 bg-gold-500/10 p-3 rounded-2xl flex flex-col items-center text-center transition';
                labelLocal.className = 'cursor-pointer border border-slate-700 bg-dark-800 p-3 rounded-2xl flex flex-col items-center text-center transition';
                customsContainer.style.display = 'block';
                if (quickResort) quickResort.classList.add('hidden');
                addrLabel.textContent = '배송 주소 (한국 자택 도로명 주소) *';
                custAddress.placeholder = '도로명 주소 및 상세 동호수를 입력하세요';
            } else {
                labelLocal.className = 'cursor-pointer border border-gold-500/50 bg-gold-500/10 p-3 rounded-2xl flex flex-col items-center text-center transition';
                labelDirect.className = 'cursor-pointer border border-slate-700 bg-dark-800 p-3 rounded-2xl flex flex-col items-center text-center transition';
                customsContainer.style.display = 'none';
                if (quickResort) quickResort.classList.remove('hidden');
                addrLabel.textContent = '푸꾸옥 리조트명 / 호텔 객실 정보 *';
                custAddress.placeholder = '예: 노보텔 리조트 302호 (로비 정문 대면 수령)';
            }
        }

        function selectQuickResort(resortName) {
            const addr = document.getElementById('custAddress');
            if (addr) {
                addr.value = resortName + ' 객실번호: ';
                addr.focus();
            }
        }

        function updateOrderGuideDisplay() {
            const display = document.getElementById('displayGuideCodeInOrder');
            const refCode = sessionStorage.getItem('referral_guide_code') || (currentGuide ? currentGuide.guide_code : null);
            if (refCode) {
                display.textContent = `연계 가이드 [${refCode}] (수수료 자동 적립 대상)`;
                display.className = 'font-mono font-black text-gold-300';
            } else {
                display.textContent = '일반 고객 주문 (가이드 없음)';
                display.className = 'font-mono text-slate-400';
            }
        }

        // Final Order Submit
        function submitFinalOrder(e) {
            e.preventDefault();
            const deliveryType = document.querySelector('input[name="delivery_type"]:checked').value;
            const name = document.getElementById('custName').value.trim();
            const phone = document.getElementById('custPhone').value.trim();
            const kakao = document.getElementById('custKakao').value.trim();
            const address = document.getElementById('custAddress').value.trim();
            const note = document.getElementById('custNote').value.trim();
            const customsId = document.getElementById('custCustomsId').value.trim().toUpperCase();

            if (deliveryType === 'direct_korea') {
                if (!customsId || !/^P[0-9]{12}$/.test(customsId)) {
                    alert('한국 직배송 시 개인통관고유부호(P로 시작하는 13자리)를 정확히 입력해주세요.');
                    document.getElementById('custCustomsId').focus();
                    return;
                }
            }

            const refCode = sessionStorage.getItem('referral_guide_code') || (currentGuide ? currentGuide.guide_code : null);

            const payload = {
                customer_name: name,
                customer_phone: phone,
                customer_kakao: kakao,
                delivery_type: deliveryType,
                delivery_address: address,
                customs_id: customsId,
                delivery_note: note,
                guide_code: refCode || '',
                items: cart.map(i => ({ id: i.id, qty: i.qty }))
            };

            const btn = document.getElementById('btnFinalSubmit');
            btn.disabled = true;
            btn.textContent = '주문 접수 및 재고 검증 중...';

            fetch('/api/order/create', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert(`[주문 접수 완료]\n\n주문번호: ${data.order_number}\n총 결제액: $${data.total_usd.toFixed(2)} (₩${data.total_krw.toLocaleString()}원)\n\n감사합니다! 담당자가 카카오톡/문자로 주문 확인 및 결제 계좌를 안내해드립니다.`);
                    cart = [];
                    saveCart();
                    closeCheckoutModal();
                    window.location.href = `/order/track?q=${data.order_number}`;
                } else {
                    alert('주문 오류: ' + data.message);
                    btn.disabled = false;
                    btn.textContent = '최종 주문 접수하기';
                }
            })
            .catch(err => {
                alert('통신 오류가 발생했습니다: ' + err);
                btn.disabled = false;
                btn.textContent = '최종 주문 접수하기';
            });
        }

            updateCartUI();
            applyGuideModeUI();
        });
    