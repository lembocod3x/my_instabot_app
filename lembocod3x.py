import requests
import instaloader
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, NumberParseException
from rich.console import Console
from rich.text import Text
from rich import print as rprint
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
import re

# Setup
L = instaloader.Instaloader()
console = Console()

# Optional: Uncomment and replace with your credentials if login is required
# L.login("your_username", "your_password")  # ⚠️ Use securely!

def show_banner():
    banner = """
▖ ▄▖▖  ▖▄ ▄▖  ▄▖▄▖▄ ▄▖▖▖
▌ ▙▖▛▖▞▌▙▘▌▌  ▌ ▌▌▌▌▄▌▚▘
▙▖▙▖▌▝ ▌▙▘▙▌  ▙▖▙▌▙▘▄▌▌▌
"""
    console.print(Align.center(Text(banner, style="bold yellow")))

def command_one():
    rprint("[bold yellow]▄▖▄▖▄▖▖ ▄▖▄▖▖▖[/bold yellow]")
    rprint("[bold yellow]▐ ▙▌▄▌▌ ▌▌▌▌▙▘[/bold yellow]")
    rprint("[bold yellow]▟▖▌ ▙▖▙▖▙▌▙▌▌▌[/bold yellow]")
    rprint("[bold purple]created by LEMBO COD3X[/bold purple]\n")

    ip = input("Enter an IP address to look up: ").strip()

    # Basic IP address validation
    if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
        rprint("[bold red]Invalid IP format.[/bold red]")
        return

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        response.raise_for_status()
        data = response.json()

        table = Table(title="IP Information")
        table.add_column("Key", style="bold green")
        table.add_column("Value", style="white")

        for key, value in data.items():
            table.add_row(key, str(value))

        console.print(table)

    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching IP information: {e}[/bold red]")

def command_two():
    rprint("[bold yellow]▄▖▖ ▖▄▖▄▖▖▖  ▄▖▖ ▖▄▖▄▖[/bold yellow]")
    rprint("[bold yellow]▐ ▛▖▌▚ ▐ ▙▌  ▐ ▛▖▌▙▖▌▌[/bold yellow]")
    rprint("[bold yellow]▟▖▌▝▌▄▌▐  ▌  ▟▖▌▝▌▌ ▙▌[/bold yellow]")
    rprint("[bold purple]created by LEMBO COD3X[/bold purple]\n")

    username = input("Enter the Instagram username to look up: ").strip()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        def print_info(label, value):
            text = Text()
            text.append(f"{label}: ", style="bold red")
            text.append(str(value), style="white")
            console.print(text)

        console.print(f"\n[bold red]--- Instagram Profile Info for @{profile.username} ---[/bold red]")
        print_info("Full Name", profile.full_name)
        print_info("Biography", profile.biography)
        print_info("Followers", profile.followers)
        print_info("Following", profile.followees)
        print_info("Total Posts", profile.mediacount)
        print_info("External URL", profile.external_url)
        print_info("Is Verified", profile.is_verified)
        print_info("Is Private", profile.is_private)
        print_info("Business Account", profile.is_business_account)

    except instaloader.exceptions.ProfileNotExistsException:
        console.print("[bold red]❌ The profile does not exist.[/bold red]")
    except instaloader.exceptions.ConnectionException:
        console.print("[bold red]⚠️ Connection error. Check your internet connection.[/bold red]")
    except instaloader.exceptions.LoginRequiredException:
        console.print("[bold red]⚠️ This profile is private. Login is required to view it.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]⚠️ An unexpected error occurred: {e}[/bold red]")

def command_three():
    rprint("[bold yellow]▖ ▖▖▖▄   ▄▖▖ ▖▄▖▄▖▖▖[/bold yellow]")
    rprint("[bold yellow]▛▖▌▌▌▙▘  ▐ ▛▖▌▙▖▌▌▚▘[/bold yellow]")
    rprint("[bold yellow]▌▝▌▙▌▙▘  ▟▖▌▝▌▌ ▙▌▌▌[/bold yellow]")
    rprint("[bold purple]created by LEMBO COD3X  [/bold purple]\n")

    number_input = input("Enter phone number with country code (e.g., +1234567890) > ").strip()

    try:
        number = phonenumbers.parse(number_input)

        location = geocoder.description_for_number(number, "en") or "Location not found"
        carrier_name = carrier.name_for_number(number, "en") or "Carrier info not found"
        time_zones = timezone.time_zones_for_number(number)
        timezone_info = ', '.join(time_zones) if time_zones else "Timezone info not found"

        details = f"""
[bold red]Valid:[/bold red] {phonenumbers.is_valid_number(number)}
[bold red]Possible:[/bold red] {phonenumbers.is_possible_number(number)}
[bold red]Location:[/bold red] {location}
[bold red]Carrier:[/bold red] {carrier_name}
[bold red]Timezone:[/bold red] {timezone_info}
[bold red]E.164 Format:[/bold red] {phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)}
"""
        rprint(Panel(details.strip(), title="[bold green]Phone Number Details[/bold green]", expand=False))

    except NumberParseException as e:
        rprint("[bold red]Error: Invalid phone number format.[/bold red]")
        rprint(f"[bold yellow]Details: {e}[/bold yellow]")

def main():
    show_banner()
    while True:
        try:
            print("\nChoose a command to run:")
            print("1. IP LOOK 🌐")
            print("2. INST4 INFO ⚡")
            print("3. NUB INFO ⚡")
            print("4. Exit 🛑")

            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == '1':
                command_one()
            elif choice == '2':
                command_two()
            elif choice == '3':
                command_three()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("\n[!] Interrupted by user. Exiting...")
            break

if __name__ == "__main__":
    main()