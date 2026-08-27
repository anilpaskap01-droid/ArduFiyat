__version__ = '31.0'
import random
import string
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput

APP_NAME = 'Osmantuş Halayı'

FEATURES = [
    'Keşkek Motoru','Halay Motoru','Mendil RGB','Davul Turbo','Zurna Surround',
    'Uyku Yöneticisi','Enerji Boost','Mutluluk Boost','RAM Temizleyici','Dosya Temizleyici',
    'Sistem Onarımı','Sistem Monitörü','SuperCharge','Aziz Store','Mini Oyun Merkezi',
    'Başarımlar','Sistem Logları','Şifre Üretici','Hesap Makinesi','Bluetooth Tarayıcı',
    'Wi-Fi Testi','Ses Testi','Mikrofon Testi','Telefon Testi','Kamera Testi',
    'Fener Modu','Sıcaklık Monitörü','Aziz AI','Robot Modu','Boss Modu',
    'Turbo Mod','Güvenlik Merkezi','Laboratuvar','Paket Yöneticisi','Dosya Yöneticisi',
    'Bulut Simülasyonu','Yedekleme Merkezi','Geri Yükleme','Tema Merkezi','Bildirim Testi',
    'Alarm Merkezi','Kronometre','Refleks Testi','Şans Modu','AZ Coin',
    'Performans Testi','Uydu Modu','Pusula Simülasyonu','Servis Araçları','Aziz Ultimate',
    'RGB Kontrol','Aziz Terminal','Aziz DNA Lab','Acil Durum Modu','Developer Tools',
    'Kahkaha Motoru','Dans Sensörü','Ayak Vurma Turbo','Omuz Sallama Pro','Düğün Modu',
    'Keşkek Radar','Kaşık Kontrolü','Yastık Sensörü','Horlama Analizi','Mendil Takip',
]

UPDATES = [
    'Osmantuş Halayı Güncellemesi','Keşkek Yeme 5.0','Halay Çekme 8.2',
    'Mendil RGB Driver','Davul Zurna Ultra Pack','Anıl Security Patch','Osmantuş OS 31',
]

class State:
    energy = 100
    happiness = 100
    security = 100
    coins = 500
    xp = 0
    installed = set()
    logs = []
STATE = State()

def log(text):
    STATE.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] {text}")
    STATE.logs = STATE.logs[-80:]

class OsmantusApp(App):
    def build(self):
        self.title = APP_NAME
        root = BoxLayout(orientation='vertical', padding=dp(7), spacing=dp(6))
        self.status = Label(text=self.status_text(), size_hint_y=None, height=dp(60), font_size='16sp')
        root.add_widget(self.status)
        tabs = TabbedPanel(do_default_tab=False, tab_width=dp(112))
        for title, content in [
            ('Ana', self.home()), ('Update', self.updates()),
            ('60+ Araç', self.tools()), ('Antivirüs', self.antivirus())
        ]:
            tab = TabbedPanelItem(text=title)
            tab.content = content
            tabs.add_widget(tab)
        root.add_widget(tabs)
        log('Osmantuş Halayı açıldı')
        return root

    def status_text(self):
        return f"OSMANTUŞ HALAYI 31.0   ⚡{STATE.energy}%   😄{STATE.happiness}%   🛡️{STATE.security}%   🪙{STATE.coins}   XP:{STATE.xp}"

    def refresh(self):
        self.status.text = self.status_text()

    def scroll_grid(self, cols=1):
        scroll = ScrollView()
        grid = GridLayout(cols=cols, spacing=dp(8), padding=dp(8), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        scroll.add_widget(grid)
        return scroll, grid

    def home(self):
        scroll, grid = self.scroll_grid(2)
        actions = [
            ('Anıl Antivirüs Pro', lambda *_: self.scan('Hızlı Tarama', 1400)),
            ('Osmantuş Halayı Update', lambda *_: self.install('Osmantuş Halayı Güncellemesi')),
            ('SuperCharge', self.charge), ('RAM Temizle', self.ram_clean),
            ('Depolama Temizle', self.storage_clean), ('Sistem Onar', self.repair),
            ('Sistem Durumu', self.system_status), ('Mini Oyun', self.game),
            ('Hesap Makinesi', self.calculator), ('Şifre Üretici', self.password),
            ('Başarımlar', self.achievements), ('Sistem Logları', self.logs),
        ]
        for text, fn in actions:
            b = Button(text=text, size_hint_y=None, height=dp(76), font_size='15sp')
            b.bind(on_release=fn)
            grid.add_widget(b)
        return scroll

    def updates(self):
        scroll, grid = self.scroll_grid(1)
        grid.add_widget(Label(text='Osmantuş Halayı Güncelleme Merkezi', size_hint_y=None, height=dp(55), font_size='20sp'))
        for name in UPDATES:
            b = Button(text='Güncelle: ' + name, size_hint_y=None, height=dp(64), font_size='15sp')
            b.bind(on_release=lambda _, n=name: self.install(n))
            grid.add_widget(b)
        return scroll

    def tools(self):
        scroll, grid = self.scroll_grid(2)
        for name in FEATURES:
            b = Button(text=name, size_hint_y=None, height=dp(70), font_size='13sp')
            b.bind(on_release=lambda _, n=name: self.feature(n))
            grid.add_widget(b)
        return scroll

    def antivirus(self):
        scroll, grid = self.scroll_grid(1)
        grid.add_widget(Label(text='ANIL ANTİVİRÜS PRO\nSecurity Engine 16.0', size_hint_y=None, height=dp(85), font_size='20sp'))
        items = [
            ('Hızlı Tarama', lambda *_: self.scan('Hızlı Tarama', 1400)),
            ('Tam Sistem Taraması', lambda *_: self.scan('Tam Sistem Taraması', 7800)),
            ('AI Akıllı Tarama', lambda *_: self.scan('AI Akıllı Tarama', 4200)),
            ('Tehditleri Temizle', self.clean_threats), ('Karantina', self.quarantine),
            ('Web Koruması', lambda *_: self.info('Anıl Web Shield','Zararlı site koruması: AKTİF\nŞüpheli indirme filtresi: AKTİF\nSafe Browsing: AKTİF')),
            ('Uygulama Koruması', lambda *_: self.info('App Shield','Osmantuş Halayı: GÜVENLİ\nKeşkek Engine: GÜVENLİ\nHalay Driver: GÜVENLİ')),
            ('Güvenlik Raporu', lambda *_: self.info('Güvenlik Raporu',f'Güvenlik puanı: {STATE.security}/100\nReal-Time Protection: AKTİF\nWeb Shield: AKTİF')),
        ]
        for text, fn in items:
            b = Button(text=text, size_hint_y=None, height=dp(66), font_size='16sp')
            b.bind(on_release=fn)
            grid.add_widget(b)
        return scroll

    def info(self, title, text):
        box = BoxLayout(orientation='vertical', padding=dp(14), spacing=dp(8))
        box.add_widget(Label(text=text, font_size='16sp'))
        close = Button(text='Kapat', size_hint_y=None, height=dp(50))
        box.add_widget(close)
        pop = Popup(title=title, content=box, size_hint=(.9,.6))
        close.bind(on_release=pop.dismiss)
        pop.open()

    def progress(self, title, stages, done):
        box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        label = Label(text=stages[0], font_size='17sp')
        bar = ProgressBar(max=100, value=0)
        pct = Label(text='0%', font_size='16sp')
        box.add_widget(label); box.add_widget(bar); box.add_widget(pct)
        pop = Popup(title=title, content=box, size_hint=(.9,.45), auto_dismiss=False)
        value = {'n':0}
        def tick(dt):
            value['n'] = min(100, value['n'] + random.randint(3,8))
            bar.value = value['n']; pct.text = f"{value['n']}%"
            idx = min(len(stages)-1, value['n'] * len(stages) // 101)
            label.text = stages[idx]
            if value['n'] >= 100:
                Clock.unschedule(tick)
                label.text = 'Tamamlandı'
                Clock.schedule_once(lambda *_: (pop.dismiss(), done()), .5)
        pop.open(); Clock.schedule_interval(tick, .08)

    def install(self, name):
        if name in STATE.installed:
            self.info('Güncelleme', name + '\nzaten kurulu.')
            return
        def done():
            STATE.installed.add(name); STATE.xp += 50; STATE.coins += 25; STATE.happiness = min(100, STATE.happiness + 3)
            log('Güncelleme kuruldu: ' + name); self.refresh()
            self.info('Güncelleme Tamamlandı', f'{name}\nbaşarıyla kuruldu.\n+50 XP  +25 AZ Coin')
        self.progress(name, ['Sunucuya bağlanılıyor','Paket indiriliyor','Dosyalar kuruluyor','Ayarlar uygulanıyor','Son kontrol'], done)

    def feature(self, name):
        special = {'RAM Temizleyici':self.ram_clean,'Dosya Temizleyici':self.storage_clean,'Sistem Onarımı':self.repair,'Sistem Monitörü':self.system_status,'SuperCharge':self.charge,'Hesap Makinesi':self.calculator,'Şifre Üretici':self.password,'Mini Oyun Merkezi':self.game,'Sistem Logları':self.logs}
        if name in special:
            special[name](); return
        STATE.xp += 5; log('Araç açıldı: ' + name); self.refresh()
        self.info(name, random.choice(['Modül AKTİF','Test başarılı','Turbo mod etkin','Tüm servisler normal']) + f'\nKod: OH-{random.randint(10000,99999)}\n+5 XP')

    def scan(self, name, count):
        threats = random.randint(0,3)
        def done():
            STATE.security = max(55, 100 - threats*12); self.refresh(); log(f'Antivirüs {name}: {threats} tehdit')
            found = ['inat.exe','uyumamak.sys','halay_kacis.dll'][:threats]
            text = f'Taranan dosya: {count}\nTehdit: {threats}\nGüvenlik: {STATE.security}/100'
            if found: text += '\n\n' + '\n'.join(found)
            self.info('Anıl Antivirüs Pro', text)
        self.progress(name, ['Anıl Engine başlıyor','Bellek taranıyor','Uygulamalar taranıyor','Şüpheli dosyalar analiz ediliyor','Rapor hazırlanıyor'], done)

    def clean_threats(self, *_):
        def done():
            STATE.security = 100; self.refresh(); log('Tehdit temizliği tamamlandı'); self.info('Anıl Antivirüs Pro','Tüm tehditler temizlendi.\nGüvenlik: 100/100')
        self.progress('Tehdit Temizleyici',['Tehditler bulunuyor','Karantinaya alınıyor','Sistem temizleniyor','Kernel doğrulanıyor'],done)

    def quarantine(self, *_):
        self.info('Karantina','inat.exe   İZOLE\nuyumamak.sys   İZOLE\nkeskek_reddetme.apk   İZOLE')

    def charge(self, *_):
        def done(): STATE.__setattr__('energy',100); self.refresh(); self.info('SuperCharge','Enerji %100')
        self.progress('SuperCharge',['Şarj hazırlanıyor','Enerji çekirdeği doluyor','Pil optimize ediliyor'],done)

    def ram_clean(self, *_):
        mb=random.randint(450,2400)
        self.progress('RAM Temizleyici',['Bellek analiz ediliyor','Cache temizleniyor','RAM optimize ediliyor'],lambda: self.info('RAM Temizleyici',f'{mb} MB temizlendi.'))

    def storage_clean(self, *_):
        mb=random.randint(700,5800)
        self.progress('Depolama Temizleyici',['Geçici dosyalar aranıyor','Cache temizleniyor','Depolama optimize ediliyor'],lambda: self.info('Depolama',f'{mb} MB temizlendi.'))

    def repair(self, *_):
        self.progress('Sistem Onarımı',['Kernel kontrol ediliyor','Halay Driver onarılıyor','Keşkek Engine doğrulanıyor','Bütünlük testi'],lambda: self.info('Sistem Onarımı','Sistem bütünlüğü: %100'))

    def system_status(self, *_):
        self.info('Sistem Monitörü',f"CPU: %{random.randint(5,60)}\nRAM: %{random.randint(20,65)}\nSıcaklık: {random.randint(29,44)} C\nEnerji: %{STATE.energy}\nGüvenlik: %{STATE.security}")

    def password(self, *_):
        pwd=''.join(random.choice(string.ascii_letters+string.digits+'!@#$%') for _ in range(16))
        self.info('Şifre Üretici',pwd)

    def calculator(self, *_):
        box=BoxLayout(orientation='vertical',padding=dp(12),spacing=dp(7))
        a=TextInput(hint_text='Birinci sayı',multiline=False,input_filter='float'); b=TextInput(hint_text='İkinci sayı',multiline=False,input_filter='float'); result=Label(text='Sonuç')
        row=GridLayout(cols=4,size_hint_y=None,height=dp(52),spacing=dp(4)); pop=Popup(title='Hesap Makinesi',content=box,size_hint=(.9,.62))
        def calc(_,op):
            try:
                x=float(a.text); y=float(b.text); r={'+':x+y,'-':x-y,'x':x*y,'/':x/y}[op]; result.text=str(r)
            except Exception: result.text='Hata'
        for op in ['+','-','x','/']:
            bt=Button(text=op); bt.bind(on_release=lambda w,o=op:calc(w,o)); row.add_widget(bt)
        close=Button(text='Kapat',size_hint_y=None,height=dp(48)); close.bind(on_release=pop.dismiss)
        for w in [a,b,row,result,close]: box.add_widget(w)
        pop.open()

    def game(self, *_):
        target=random.randint(1,5); box=BoxLayout(orientation='vertical',padding=dp(12),spacing=dp(8)); label=Label(text='1-5 arası sayıyı bul'); row=GridLayout(cols=5,size_hint_y=None,height=dp(58)); pop=Popup(title='Mini Oyun',content=box,size_hint=(.9,.45))
        def choose(_,n):
            if n==target: STATE.coins+=100; STATE.xp+=30; label.text='DOĞRU! +100 Coin +30 XP'; self.refresh()
            else: label.text=f'Olmadı. Sayı {target}'
        for n in range(1,6):
            bt=Button(text=str(n)); bt.bind(on_release=lambda w,x=n:choose(w,x)); row.add_widget(bt)
        close=Button(text='Kapat',size_hint_y=None,height=dp(48)); close.bind(on_release=pop.dismiss); box.add_widget(label); box.add_widget(row); box.add_widget(close); pop.open()

    def achievements(self, *_):
        self.info('Başarımlar',f"{'AÇIK' if STATE.installed else 'KİLİTLİ'} İlk Güncelleme\n{'AÇIK' if STATE.security==100 else 'KİLİTLİ'} Güvenlik Ustası\n{'AÇIK' if STATE.xp>=100 else 'KİLİTLİ'} XP Avcısı")

    def logs(self, *_):
        self.info('Sistem Logları','\n'.join(STATE.logs[-12:]) if STATE.logs else 'Log yok')

if __name__ == '__main__':
    OsmantusApp().run()
