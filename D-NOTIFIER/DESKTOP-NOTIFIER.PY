# import requests
# from bs4 import BeautifulSoup
# import time
# import subprocess

# # Web scraping and price retrieval
# site = requests.get("https://irarz.com/")
# soup = BeautifulSoup(site.content, "html.parser")
# dolor = soup.find("span", id="usdmax")
# coin = soup.find("span", id="sekee")
# bitcoin = soup.find("span", id="crypto-btc")

# # Formatting prices and message
# news = [dolor.text, coin.text, bitcoin.text]
# message = f"DOLOR PRICE: {news[0]} RIAL\nCOIN PRICE: {news[1]} RIAL\nBITCOIN PRICE: {news[2]} DOLOR"

# # Notification function
# def show_notification(title, message):
#     command = f'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -command "Add-Type -TypeDefinition ^"{M} public class NotificationHelper { [System.Runtime.InteropServices.DllImport(\"user32.dll\", CharSet = System.Runtime.InteropServices.CharSet.Auto)] public static extern int MessageBox(IntPtr hWnd, string text, string caption, int options); } ^"; [System.Windows.Forms.MessageBox]::Show(\"{message}\", \"{title}\", 0, 0); " '
#     subprocess.Popen(command, shell=True)

# # Show notification
# show_notification("BREAKING NEWS", message)