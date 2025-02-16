from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests


class MobileApp(App):
    def profile(self):
        print("function 'profile' success")
        
        response = requests.get("http://127.0.0.1:8000/api/profile/all/")
        
        if response.status_code == 200:
            profiles = response.json()
            for profile in profiles:
                print(profile)
                app.root.add_widget(Button(text=str(profile['user'])))
        else:
            print('Err')
            
    def build(self):
        self.title = "ROSEFLOURISH _app_build_w5_250202"
        
        btn = Button(text="App")
        btn.on_press = self.profile
        
        box = BoxLayout()
        box.add_widget(btn)
        
        return box
    
    
app = MobileApp()

if __name__ == "__main__":
    app.run()