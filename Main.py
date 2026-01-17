import flet as ft
import csv
import os

def main(page: ft.Page):
    page.title = "Kiln Machine Search"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.scroll = "auto"

    def search_machine(e):
        search_val = search_input.value.strip().lower()
        if not search_val:
            res_text.value = "FN 03"
            page.update()
            return

        found_data = None
        try:
            # data.csv ဖိုင်
            with open('data.csv', mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # 'Name' column မှာ ရှာခြင်း
                    if row.get('Name', '').strip().lower() == search_val:
                        found_data = row
                        break
            
            if found_data:
                # အချက်အလက်များကို စာရင်းလိုက် ပြပေးခြင်း
                res_text.value = (
                    f"✅ စက်အမည်: {found_data.get('Name')}\n"
                    f"⚙️ Bearing: {found_data.get('Bearing', '-')}\n"
                    f"🛢️ Oil: {found_data.get('Oil', '-')}\n"
                    f"🔧 Wrench: {found_data.get('Wrench', '-')}\n"
                    f"🛠️ Spanner: {found_data.get('Spanner', '-')}\n"
                    f"🏗️ Grease: {found_data.get('Grease', '-')}"
                )
                res_text.color = ft.colors.BLUE_800
            else:
                res_text.value = "❌ ရှာမတွေ့ပါ။ စာလုံးပေါင်း ပြန်စစ်ပါ။"
                res_text.color = ft.colors.RED_600

        except Exception as err:
            res_text.value = f"Error: {err}"
        
        page.update()

    # UI Design
    search_input = ft.TextField(label="စက်အမည် (ဥပမာ- FN03)", width=350)
    res_text = ft.Text(size=16, weight="bold")

    page.add(
        ft.Container(height=20),
        ft.Text("Kiln Machine Inventory", size=24, weight="bold", color="green"),
        search_input,
        ft.ElevatedButton("ဒေတာရှာပါ", icon=ft.icons.SEARCH, on_click=search_machine),
        ft.Divider(),
        ft.Container(content=res_text, padding=20, bgcolor=ft.colors.GREY_100, border_radius=10, width=350)
    )

if __name__ == "__main__":
    # Koyeb/Render အတွက် Port သတ်မှတ်ချက်
    port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port)