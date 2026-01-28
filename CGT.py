from bitcoinaddress import Wallet
import requests, random, sys, time, os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import track
from rich.table import Table
from rich import box

_1 = 'C'

from fake_useragent import UserAgent

console = Console()
console.clear()

_2 = 'R'

filename = "found.txt"
batch_size = 50

_3 = 'Y'

try:
    ua = UserAgent()
except:
    ua = None

_4 = 'P'

def get_random_ua():
    if ua:
        try:
            return ua.random
        except:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    else:
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

_5 = 'T'

def get_session():
    session = requests.session()
    agent = get_random_ua()
    headers = {'User-Agent': agent}
    session.headers.update(headers)
    return session

_6 = 'O'

def system_boot_animation(c_name, a_name):
    console.print("\n")
    steps = [
        f"Initializing {c_name} Core...",
        "Loading Encryption Modules...",
        "Bypassing Security Nodes...",
        "Connecting to Blockchain Network...",
        f"Authorizing User: {a_name}...",
        "Access Granted."
    ]
    for step in track(steps, description=f"[bold cyan]BOOTING SYSTEM...[/bold cyan]"):
        time.sleep(0.3)
    console.clear()

_7 = 'G'

def check_internet():
    sites = ["https://www.google.com", "https://www.bing.com", "https://blockchain.info"]
    while True:
        try:
            site = random.choice(sites)
            requests.get(site, timeout=10)
            return True
        except:
            console.print(Align.center("[bold red]Connection Lost...[/bold red]"))
            time.sleep(10)

_8 = 'A'

def get_balance_batch_safe(addresses_list, c_name):
    addr_str = '|'.join(addresses_list)
    url = f"https://blockchain.info/multiaddr?active={addr_str}"
    
    while True:
        try:
            session = get_session()
            req = session.get(url, timeout=20)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 429:
                console.print(Align.center(f"[bold yellow]⚠️ {c_name} ALERT: API Limit Reached. Cooldown 10s...[/bold yellow]"))
                time.sleep(10)
                continue
            elif req.status_code == 403:
                console.print(Align.center(f"[bold red]⛔ {c_name} SECURITY: Access Denied. Changing Identity...[/bold red]"))
                time.sleep(2)
                continue
            else:
                time.sleep(5)
                continue

        except requests.exceptions.ConnectionError:
            check_internet()
            console.print(Align.center("[bold green]✅ CONNECTION RESTORED[/bold green]"))
        except requests.exceptions.Timeout:
            time.sleep(2)
        except Exception:
            time.sleep(5)

_9 = 'H'
_0 = 'U'

def parse_input(val_str):
    val_str = val_str.strip().lower()
    if val_str.startswith("0x"):
        return int(val_str, 16)
    try:
        return int(val_str)
    except ValueError:
        return int(val_str, 16)

_x = 'B'
_y = 'E'

def main():
    _z = ' '
    _s = 's'
    _i = 'i'
    _u = 'u'
    
    chan_name = _1 + _2 + _3 + _4 + _5 + _6 + _7 + _2 + _8 + _4 + _9 + _3 + _5 + _0 + _x + _y
    auth_name = _s + _i + _s + _u
    full_sig = chan_name + _z + "Author:" + _z + auth_name

    system_boot_animation(chan_name, auth_name)

    title_text = f"[bold yellow]💰 {chan_name} 💰[/bold yellow]\n[cyan]Premium Bitcoin Hunter[/cyan]\n[dim]Created By: {auth_name}[/dim]"
    console.print(Align.center(Panel.fit(Align.center(title_text), border_style="green", box=box.DOUBLE)))
    
    try:
        console.print(Align.center("[bold white]👇 ENTER SCAN CONFIGURATION 👇[/bold white]"))
        start_input = input("  🔹 Start Range (Hex/Dec): ")
        end_input   = input("  🔹 End Range   (Hex/Dec): ")
        start_int = parse_input(start_input)
        end_int = parse_input(end_input)
    except ValueError:
        console.print(Align.center("[bold red]❌ CRITICAL ERROR: Invalid Input Format[/bold red]"))
        return

    if start_int > end_int:
        console.print(Align.center("[bold red]❌ LOGIC ERROR: Start Range cannot be greater than End Range[/bold red]"))
        return

    total_keys = end_int - start_int + 1
    
    info_table = Table(show_header=False, box=box.ROUNDED, border_style="cyan")
    info_table.add_row("[bold green]Range Start[/bold green]", str(hex(start_int)))
    info_table.add_row("[bold red]Range End[/bold red]", str(hex(end_int)))
    info_table.add_row("[bold yellow]Total Keys[/bold yellow]", str(total_keys))
    info_table.add_row("[bold magenta]Engine[/bold magenta]", chan_name)
    console.print(Align.center(info_table))
    
    console.print(Align.center("\n[bold green]🚀 LAUNCHING SCANNER...[/bold green]\n"))

    use_shuffle_list = False
    target_list = []
    visited_set = set()

    if total_keys <= 2000000:
        target_list = list(range(start_int, end_int + 1))
        random.shuffle(target_list)
        use_shuffle_list = True

    total_scanned = 0
    found_count = 0

    while True:
        if total_scanned >= total_keys:
            console.print(Align.center(Panel(f"[bold green]🎉 MISSION COMPLETE! Checked {total_keys} Keys.[/bold green]", border_style="green")))
            break

        batch_keys = []
        addr_list = []
        
        while len(batch_keys) < batch_size:
            if total_scanned + len(batch_keys) >= total_keys:
                break

            current_dec = 0
            if use_shuffle_list:
                if not target_list: break
                current_dec = target_list.pop()
            else:
                while True:
                    current_dec = random.randint(start_int, end_int)
                    if current_dec not in visited_set:
                        visited_set.add(current_dec)
                        break
            
            try:
                hex_key = "%064x" % current_dec
                wallet = Wallet(hex_key)
                batch_keys.append(wallet)
                addr_list.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])
                addr_list.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'])
            except:
                continue

        if not batch_keys:
            break

        status_msg = f"[bold cyan]SCANNING...[/bold cyan] [white]({total_scanned}/{total_keys})[/white] | [bold green]FOUND: {found_count}[/bold green] | [dim]{chan_name}[/dim]"
        console.print(status_msg)
        
        data = get_balance_batch_safe(addr_list, chan_name)
        
        if data and 'addresses' in data:
            api_map = {item['address']: item for item in data['addresses']}
            
            for wallet in batch_keys:
                wif = wallet.key.__dict__['mainnet'].__dict__['wif']
                hex_k = wallet.key.hex
                uaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
                caddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
                
                u_bal = 0; u_rec = 0; u_sent = 0
                c_bal = 0; c_rec = 0; c_sent = 0
                
                if uaddr in api_map:
                    u_bal = api_map[uaddr].get('final_balance', 0)
                    u_rec = api_map[uaddr].get('total_received', 0)
                    u_sent = api_map[uaddr].get('total_sent', 0)

                if caddr in api_map:
                    c_bal = api_map[caddr].get('final_balance', 0)
                    c_rec = api_map[caddr].get('total_received', 0)
                    c_sent = api_map[caddr].get('total_sent', 0)
                
                found_u = u_bal > 0 or u_rec > 0 or u_sent > 0
                found_c = c_bal > 0 or c_rec > 0 or c_sent > 0

                if found_u:
                    found_count += 1
                    console.print(Panel(f"[bold green]💰 JACKPOT FOUND BY {chan_name}![/bold green]\n[yellow]Addr:[/yellow] {uaddr}\n[green]Bal:[/green] {u_bal}\n[cyan]Rec:[/cyan] {u_rec}\n[magenta]Key :[/magenta] {hex_k}", border_style="red", box=box.HEAVY))
                    with open(filename, "a") as f:
                        f.write(f"FOUND BY {full_sig}\nAddr: {uaddr} | Bal: {u_bal} | Rec: {u_rec} | Sent: {u_sent} | HEX: {hex_k} | WIF: {wif}\n")

                if found_c:
                    found_count += 1
                    console.print(Panel(f"[bold green]💰 JACKPOT FOUND BY {chan_name}![/bold green]\n[yellow]Addr:[/yellow] {caddr}\n[green]Bal:[/green] {c_bal}\n[cyan]Rec:[/cyan] {c_rec}\n[magenta]Key :[/magenta] {hex_k}", border_style="red", box=box.HEAVY))
                    with open(filename, "a") as f:
                        f.write(f"FOUND BY {full_sig}\nAddr: {caddr} | Bal: {c_bal} | Rec: {c_rec} | Sent: {c_sent} | HEX: {hex_k} | WIF: {wif}\n")

                pk_color = "[dim white]"
                if found_u or found_c:
                    pk_color = "[bold green]"
                
                c1 = "[dim white]"
                if found_u: c1 = "[bold green]"
                    
                c2 = "[dim white]"
                if found_c: c2 = "[bold green]"
                
                console.print(f"{pk_color}KEY: {hex_k}[/] | {c1}1: {uaddr} B:{u_bal} R:{u_rec} S:{u_sent}[/] | {c2}3: {caddr} B:{c_bal} R:{c_rec} S:{c_sent}[/]")

        total_scanned += len(batch_keys)
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.print(Align.center("\n\n[bold yellow]Good Bye![/bold yellow]"))
        console.print(Align.center("[bold cyan]Luck can strike at any moment, so keep working hard![/bold cyan]"))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)