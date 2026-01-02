<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المهندس معاذ مقداد | MOATH MOQDAD</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #3b82f6;
            --primary-dark: #1d4ed8;
            --secondary: #8b5cf6;
            --dark: #0f172a;
            --darker: #020617;
            --light: #f8fafc;
            --glass: rgba(255, 255, 255, 0.1); /* زيادة العتامة */
            --glass-border: rgba(255, 255, 255, 0.18); /* زيادة العتامة */
            --glass-hover: rgba(255, 255, 255, 0.18); /* زيادة العتامة */
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Tajawal', sans-serif;
            color: var(--light);
            background-color: var(--dark);
            overflow-x: hidden;
            min-height: 100vh;
            line-height: 1.6;
        }
        
        /* خلفية الفيديو - تقليل الشفافية */
        .video-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            overflow: hidden;
        }
        
        .video-bg {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.6); /* زيادة السطوع ليظهر الفيديو أكثر */
        }
        
        /* طبقة التغطية - تقليل الشفافية بشكل كبير */
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                135deg,
                rgba(15, 23, 42, 0.75) 0%, /* تقليل الشفافية */
                rgba(30, 41, 59, 0.65) 100% /* تقليل الشفافية */
            );
            z-index: -2;
        }
        
        /* المحتوى الرئيسي */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            z-index: 1;
        }
        
        /* الصورة الشخصية */
        .profile-section {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .profile-wrapper {
            position: relative;
            width: 220px;
            height: 220px;
            margin: 0 auto 30px;
        }
        
        .profile-circle {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            overflow: hidden;
            border: 4px solid var(--glass-border);
            box-shadow: 
                0 15px 35px rgba(0, 0, 0, 0.4),
                inset 0 0 20px rgba(255, 255, 255, 0.05);
            background: var(--darker);
            transition: all 0.3s ease;
        }
        
        .profile-circle:hover {
            transform: scale(1.05);
            box-shadow: 
                0 20px 40px rgba(0, 0, 0, 0.5),
                0 0 0 1px rgba(59, 130, 246, 0.3);
        }
        
        .profile-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.5s ease;
        }
        
        .profile-circle:hover .profile-img {
            transform: scale(1.1);
        }
        
        /* الاسم والعنوان - ملون */
        .name-section {
            text-align: center;
            margin-bottom: 60px;
            animation: fadeIn 1s ease-out;
        }
        
        .name-arabic {
            font-size: 3.2rem;
            font-weight: 800;
            margin-bottom: 10px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            animation: gradientShift 3s ease infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .name-english {
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: rgba(255, 255, 255, 0.95);
            letter-spacing: 1px;
            animation: fadeInUp 1s ease-out 0.3s both;
        }
        
        .title {
            font-size: 1.4rem;
            color: var(--primary);
            font-weight: 300;
            padding: 10px 30px;
            background: var(--glass);
            border-radius: 50px;
            border: 1px solid var(--glass-border);
            display: inline-block;
            backdrop-filter: blur(15px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
            animation: fadeInUp 1s ease-out 0.6s both;
        }
        
        /* أزرار التواصل - ملونة */
        .contact-section {
            width: 100%;
            max-width: 900px;
            margin-bottom: 40px;
            animation: fadeIn 1s ease-out 0.9s both;
        }
        
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        
        .contact-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 1px solid var(--glass-border);
            padding: 20px;
            display: flex;
            align-items: center;
            text-decoration: none;
            color: inherit;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .contact-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, var(--glass-hover), transparent);
            transition: left 0.6s;
        }
        
        .contact-card:hover::before {
            left: 100%;
        }
        
        .contact-card:hover {
            transform: translateY(-5px);
            background: var(--glass-hover);
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        .contact-icon {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: 15px;
            font-size: 1.5rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            flex-shrink: 0;
            transition: transform 0.3s ease;
            position: relative;
            z-index: 1;
        }
        
        /* تأثير الإنارة للبرامج */
        .contact-icon::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle at center, rgba(255,255,255,0.25) 0%, transparent 70%);
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
            transition: all 0.4s ease;
            pointer-events: none;
            z-index: -1;
        }
        
        .contact-card:hover .contact-icon::after {
            transform: translate(-50%, -50%) scale(1.5);
            opacity: 1;
        }
        
        /* تخصيص ألوان الأيقونات */
        .telegram .contact-icon { 
            background: linear-gradient(135deg, #0088cc, #005580);
        }
        
        .snapchat .contact-icon { 
            background: linear-gradient(135deg, #FFFC00, #FFFC00);
            color: #000;
        }
        
        .facebook .contact-icon { 
            background: linear-gradient(135deg, #1877F2, #0A5BC4);
        }
        
        .discord .contact-icon { 
            background: linear-gradient(135deg, #5865F2, #404EED);
        }
        
        .instagram .contact-icon { 
            background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        }
        
        .tiktok .contact-icon { 
            background: linear-gradient(135deg, #000000, #fe2c55, #25f4ee);
        }
        
        .contact-info {
            flex-grow: 1;
            position: relative;
            z-index: 1;
        }
        
        .contact-label {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 5px;
            font-weight: 300;
        }
        
        .contact-detail {
            font-size: 1.3rem;
            font-weight: 600;
            color: var(--light);
            word-break: break-all;
        }
        
        /* شارات سريعة ملونة */
        .social-badges {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 30px 0 40px;
            animation: fadeIn 1s ease-out 1.2s both;
        }
        
        .social-badge {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            color: var(--light);
            font-size: 1.3rem;
            transition: all 0.3s ease;
            text-decoration: none;
            cursor: pointer;
            position: relative;
        }
        
        .social-badge::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle at center, rgba(255,255,255,0.2) 0%, transparent 70%);
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
            transition: all 0.4s ease;
            pointer-events: none;
            z-index: -1;
        }
        
        .social-badge:hover::after {
            transform: translate(-50%, -50%) scale(1.5);
            opacity: 1;
        }
        
        .social-badge:hover {
            transform: translateY(-5px) scale(1.1);
            background: var(--glass-hover);
            border-color: var(--primary);
        }
        
        .telegram-badge:hover { 
            background: linear-gradient(135deg, #0088cc, #005580);
            color: white;
        }
        .snapchat-badge:hover { 
            background: linear-gradient(135deg, #FFFC00, #FFFC00);
            color: #000;
        }
        .facebook-badge:hover { 
            background: linear-gradient(135deg, #1877F2, #0A5BC4);
            color: white;
        }
        .discord-badge:hover { 
            background: linear-gradient(135deg, #5865F2, #404EED);
            color: white;
        }
        .instagram-badge:hover { 
            background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
            color: white;
        }
        .tiktok-badge:hover { 
            background: linear-gradient(135deg, #000000, #fe2c55, #25f4ee);
            color: white;
        }
        
        /* رسالة النسخ */
        .copy-notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            backdrop-filter: blur(10px);
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4);
            z-index: 1000;
            transform: translateX(120%);
            transition: transform 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .copy-notification.show {
            transform: translateX(0);
        }
        
        /* التذييل */
        footer {
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.9rem;
            padding: 20px;
            width: 100%;
            animation: fadeIn 1s ease-out 1.5s both;
        }
        
        .footer-content {
            background: var(--glass);
            backdrop-filter: blur(15px);
            border-radius: 10px;
            padding: 15px 30px;
            border: 1px solid var(--glass-border);
            display: inline-block;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
        }
        
        /* الرسوم المتحركة */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* تحسين الأداء والسلاسة */
        .main-container * {
            will-change: transform, opacity;
        }
        
        .video-bg {
            will-change: transform;
        }
        
        /* التجاوب مع الأجهزة */
        @media (max-width: 768px) {
            .profile-wrapper {
                width: 180px;
                height: 180px;
            }
            
            .name-arabic {
                font-size: 2.5rem;
            }
            
            .name-english {
                font-size: 1.6rem;
            }
            
            .title {
                font-size: 1.2rem;
                padding: 8px 20px;
            }
            
            .contact-grid {
                grid-template-columns: 1fr;
                max-width: 450px;
                margin: 0 auto;
            }
            
            .contact-card {
                padding: 18px;
            }
            
            .contact-icon {
                width: 55px;
                height: 55px;
                font-size: 1.3rem;
                margin-left: 12px;
            }
            
            .contact-detail {
                font-size: 1.1rem;
            }
            
            .social-badges {
                flex-wrap: wrap;
                gap: 12px;
            }
            
            .copy-notification {
                top: 10px;
                right: 10px;
                left: 10px;
                text-align: center;
            }
        }
        
        @media (max-width: 480px) {
            .main-container {
                padding: 20px 15px;
            }
            
            .profile-wrapper {
                width: 160px;
                height: 160px;
            }
            
            .name-arabic {
                font-size: 2rem;
            }
            
            .name-english {
                font-size: 1.3rem;
            }
            
            .title {
                font-size: 1rem;
                padding: 6px 15px;
            }
            
            .contact-card {
                flex-direction: column;
                text-align: center;
                padding: 15px;
            }
            
            .contact-icon {
                margin: 0 0 10px 0;
                width: 60px;
                height: 60px;
            }
            
            .social-badges {
                gap: 10px;
            }
            
            .social-badge {
                width: 45px;
                height: 45px;
                font-size: 1.1rem;
            }
            
            .footer-content {
                padding: 12px 20px;
            }
        }
    </style>
</head>
<body>
    <!-- رسالة النسخ -->
    <div class="copy-notification" id="copyNotification">
        <i class="fas fa-check-circle"></i>
        <span id="copyMessage">تم النسخ!</span>
    </div>
    
    <!-- خلفية الفيديو -->
    <div class="video-container">
        <video class="video-bg" autoplay muted loop playsinline id="bg-video">
            <source src="https://files.catbox.moe/s82l37.mp4" type="video/mp4">
        </video>
    </div>
    
    <!-- طبقة التغطية -->
    <div class="overlay"></div>
    
    <!-- المحتوى الرئيسي -->
    <div class="main-container">
        <!-- الصورة الشخصية -->
        <div class="profile-section">
            <div class="profile-wrapper">
                <div class="profile-circle">
                    <img src="https://iili.io/fhkfg4f.jpg" 
                         alt="المهندس معاذ مقداد" 
                         class="profile-img" 
                         id="profileImage">
                </div>
            </div>
        </div>
        
        <!-- الاسم والعنوان - ملون -->
        <div class="name-section">
            <h1 class="name-arabic">المهندس معاذ مقداد</h1>
            <h2 class="name-english">MOATH MOQDAD</h2>
            <div class="title">موقع تعريفي عن معاذ مقداد</div>
        </div>
        
        <!-- أزرار التواصل - ملونة -->
        <div class="contact-section">
            <div class="contact-grid">
                <!-- تليجرام -->
                <a href="https://t.me/M2_OG" 
                   target="_blank" 
                   class="contact-card telegram">
                    <div class="contact-icon">
                        <i class="fab fa-telegram-plane"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">تليجرام</div>
                        <div class="contact-detail">@M2_OG</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح تليجرام
                        </div>
                    </div>
                </a>
                
                <!-- سناب شات -->
                <a href="https://www.snapchat.com/add/u966q" 
                   target="_blank" 
                   class="contact-card snapchat">
                    <div class="contact-icon">
                        <i class="fab fa-snapchat-ghost"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">سناب شات</div>
                        <div class="contact-detail">u966q</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح سناب شات
                        </div>
                    </div>
                </a>
                
                <!-- فيس بوك -->
                <a href="https://facebook.com/31rmp" 
                   target="_blank" 
                   class="contact-card facebook">
                    <div class="contact-icon">
                        <i class="fab fa-facebook-f"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">فيس بوك</div>
                        <div class="contact-detail">31rmp</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح فيس بوك
                        </div>
                    </div>
                </a>
                
                <!-- ديسكورد -->
                <a href="https://discord.com/users/_31rm" 
                   target="_blank" 
                   class="contact-card discord">
                    <div class="contact-icon">
                        <i class="fab fa-discord"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">ديسكورد</div>
                        <div class="contact-detail">_31rm</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح ديسكورد
                        </div>
                    </div>
                </a>
                
                <!-- انستغرام -->
                <a href="https://instagram.com/_31rm" 
                   target="_blank" 
                   class="contact-card instagram">
                    <div class="contact-icon">
                        <i class="fab fa-instagram"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">انستغرام</div>
                        <div class="contact-detail">@_31rm</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح انستغرام
                        </div>
                    </div>
                </a>
                
                <!-- تيك توك -->
                <a href="https://www.tiktok.com/@m7t777" 
                   target="_blank" 
                   class="contact-card tiktok">
                    <div class="contact-icon">
                        <i class="fab fa-tiktok"></i>
                    </div>
                    <div class="contact-info">
                        <div class="contact-label">تيك توك</div>
                        <div class="contact-detail">@m7t777</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 5px;">
                            <i class="fas fa-external-link-alt"></i> انقر لفتح تيك توك
                        </div>
                    </div>
                </a>
            </div>
        </div>
        
        <!-- شارات سريعة ملونة -->
        <div class="social-badges">
            <a href="https://t.me/M2_OG" target="_blank" class="social-badge telegram-badge">
                <i class="fab fa-telegram-plane"></i>
            </a>
            <a href="https://www.snapchat.com/add/u966q" target="_blank" class="social-badge snapchat-badge">
                <i class="fab fa-snapchat-ghost"></i>
            </a>
            <a href="https://facebook.com/31rmp" target="_blank" class="social-badge facebook-badge">
                <i class="fab fa-facebook-f"></i>
            </a>
            <a href="https://discord.com/users/_31rm" target="_blank" class="social-badge discord-badge">
                <i class="fab fa-discord"></i>
            </a>
            <a href="https://instagram.com/_31rm" target="_blank" class="social-badge instagram-badge">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="https://www.tiktok.com/@m7t777" target="_blank" class="social-badge tiktok-badge">
                <i class="fab fa-tiktok"></i>
            </a>
        </div>
        
        <!-- التذييل -->
        <footer>
            <div class="footer-content">
                <p>© 2026 المهندس معاذ مقداد | موقع تعريفي</p>
                <p style="margin-top: 5px; font-size: 0.85rem;">المهندس معاذ مقداد</p>
            </div>
        </footer>
    </div>

    <script>
        // دالة نسخ المعلومات
        function copyContact(info, type) {
            // تنظيف النص من المسافات
            const cleanInfo = info.replace(/\s/g, '');
            
            // استخدام API Clipboard الحديث
            navigator.clipboard.writeText(cleanInfo).then(function() {
                // نجاح النسخ
                showCopyNotification(`تم نسخ ${type}: ${cleanInfo}`);
                
                // تأثير النقر
                if (event && event.currentTarget) {
                    const card = event.currentTarget;
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.transform = '';
                    }, 200);
                }
                
            }).catch(function(err) {
                // إذا فشل API الحديث، نستخدم الطريقة القديمة
                const textArea = document.createElement("textarea");
                textArea.value = cleanInfo;
                document.body.appendChild(textArea);
                textArea.select();
                
                try {
                    const successful = document.execCommand('copy');
                    if (successful) {
                        showCopyNotification(`تم نسخ ${type}: ${cleanInfo}`);
                    } else {
                        showCopyNotification('❌ فشل النسخ، حاول مرة أخرى', true);
                    }
                } catch (err) {
                    showCopyNotification('❌ فشل النسخ، حاول يدوياً', true);
                }
                
                document.body.removeChild(textArea);
            });
        }
        
        // عرض إشعار النسخ
        function showCopyNotification(message, isError = false) {
            const notification = document.getElementById('copyNotification');
            const copyMessage = document.getElementById('copyMessage');
            
            // تغيير الرسالة
            copyMessage.textContent = message;
            
            // تغيير اللون إذا كان خطأ
            if (isError) {
                notification.style.background = '#ef4444';
            } else {
                notification.style.background = 'linear-gradient(135deg, #3b82f6, #8b5cf6)';
            }
            
            // إظهار الإشعار
            notification.classList.add('show');
            
            // إخفاء الإشعار بعد 3 ثواني
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        }
        
        // تحسين الأداء
        document.addEventListener('DOMContentLoaded', function() {
            // التأكد من تحميل الصورة
            const profileImg = document.getElementById('profileImage');
            profileImg.onload = function() {
                console.log('✅ تم تحميل الصورة الشخصية بنجاح');
            };
            profileImg.onerror = function() {
                console.log('⚠️ فشل تحميل الصورة');
            };
            
            // تحسين تحميل الفيديو
            const video = document.getElementById('bg-video');
            video.load();
            
            console.log('🚀 موقع المهندس معاذ مقداد - النسخة النهائية');
            console.log('✅ تمت إضافة نصوص: انقر لفتح انستغرام / تيك توك');
            console.log('🎥 تقليل الشفافية: الفيديو الخلفية تظهر أكثر');
            console.log('💫 جميع التصميمات متسقة ومتناسقة');
            console.log('✨ الموقع جاهز ومتكامل!');
        });
    </script>
</body>
</html>
