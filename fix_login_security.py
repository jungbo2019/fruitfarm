login_html = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>관리자 로그인 | FRUIT FARM 푸꾸옥 플래그십</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>body { font-family: 'Pretendard', sans-serif; }</style>
</head>
<body class="bg-stone-950 min-h-screen flex items-center justify-center p-4">

    <div class="max-w-md w-full bg-white rounded-3xl shadow-2xl p-8 space-y-6 border border-stone-200">
        <!-- Logo & Header -->
        <div class="text-center space-y-2">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-amber-500 to-amber-600 mx-auto flex items-center justify-center text-white text-2xl shadow-lg shadow-amber-500/20">
                <i class="fa-solid fa-lemon"></i>
            </div>
            <h2 class="text-2xl font-black text-stone-900 tracking-tight">FRUIT FARM ADMIN</h2>
            <div class="inline-block bg-amber-100 text-amber-900 text-xs font-black px-3.5 py-1 rounded-full border border-amber-300">
                푸꾸옥 플래그십 보안 관제 시스템
            </div>
        </div>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                <div class="p-3 text-xs rounded-xl font-bold flex items-center gap-2 {% if category == 'danger' or category == 'error' %}bg-red-50 text-red-700 border border-red-200{% elif category == 'success' %}bg-emerald-50 text-emerald-700 border border-emerald-200{% else %}bg-stone-100 text-stone-700{% endif %}">
                    <i class="fa-solid fa-circle-exclamation text-sm"></i>
                    <span>{{ message }}</span>
                </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" action="{{ url_for('admin_login') }}" class="space-y-4" autocomplete="off">
            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1.5">관리자 아이디</label>
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-stone-400">
                        <i class="fa-solid fa-user text-sm"></i>
                    </span>
                    <input type="text" name="username" required placeholder="관리자 아이디를 입력하세요"
                           class="w-full pl-10 pr-3.5 py-3 border border-stone-300 rounded-xl text-sm font-medium focus:ring-2 focus:ring-amber-500 focus:border-amber-500 focus:outline-none transition">
                </div>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1.5">비밀번호</label>
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-stone-400">
                        <i class="fa-solid fa-lock text-sm"></i>
                    </span>
                    <input type="password" name="password" id="adminPassword" required placeholder="비밀번호를 입력하세요"
                           class="w-full pl-10 pr-10 py-3 border border-stone-300 rounded-xl text-sm font-medium focus:ring-2 focus:ring-amber-500 focus:border-amber-500 focus:outline-none transition">
                    <button type="button" onclick="togglePasswordVisibility()" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-stone-400 hover:text-stone-700">
                        <i class="fa-solid fa-eye" id="pwdEyeIcon"></i>
                    </button>
                </div>
            </div>

            <button type="submit" class="w-full py-3.5 bg-amber-500 hover:bg-amber-600 text-stone-950 font-black rounded-xl shadow-lg shadow-amber-500/25 transition flex items-center justify-center gap-2">
                <i class="fa-solid fa-right-to-bracket text-sm"></i>
                <span>관리자 시스템 로그인</span>
            </button>
        </form>

        <div class="pt-4 border-t border-stone-100 text-center">
            <a href="{{ url_for('index') }}" class="text-xs text-stone-500 hover:text-stone-900 font-bold transition inline-flex items-center gap-1.5">
                <i class="fa-solid fa-arrow-left"></i>
                <span>고객 쇼핑몰 메인으로 돌아가기</span>
            </a>
        </div>
    </div>

    <script>
    function togglePasswordVisibility() {
        const pwdInput = document.getElementById('adminPassword');
        const eyeIcon = document.getElementById('pwdEyeIcon');
        if (pwdInput.type === 'password') {
            pwdInput.type = 'text';
            eyeIcon.classList.remove('fa-eye');
            eyeIcon.classList.add('fa-eye-slash');
        } else {
            pwdInput.type = 'password';
            eyeIcon.classList.remove('fa-eye-slash');
            eyeIcon.classList.add('fa-eye');
        }
    }
    </script>

</body>
</html>
'''

with open(r'E:\fruitfarm\templates\admin\login.html', 'w', encoding='utf-8') as f:
    f.write(login_html)

print("Updated login.html: hardcoded credentials and hint completely removed.")
