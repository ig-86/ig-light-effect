# İsmet Light Effect Card

Türkçe · **[English](#english)**

Hangi marka olursa olsun, efekt destekleyen bütün ışıkları oda oda yöneten bir Home Assistant kartı. Efektler, beyaz tonlar ve renkler tek ekranda; her şey Home Assistant'ın içindeki kontrol panelinden, kod yazmadan düzenlenir.

**Hızlı kurulum:** Ayarlar → **Marketplace** (eski sürümlerde HACS) → ⋮ → **Özel depolar** → `https://github.com/ig-86/ig-light-effect` (Entegrasyon) → İndir → Home Assistant'ı yeniden başlat → **Ayarlar → Cihazlar ve hizmetler → Entegrasyon ekle → İsmet Light Effect Card**.

## Öne çıkanlar

- **Odalar Home Assistant alanlarından gelir.** YAML'da ışık listesi yazmana gerek yok. Her odada efektlerin hangi ışıklara gideceğini seçersin; seçim evdeki herkes için ortaktır.
- **Farklı markalar aynı odada.** Seçili ışıkların bütün efektleri görünür. Efektin altındaki noktalar onu kaç ışığın desteklediğini gösterir; dokununca efekt yalnız destekleyen ışıklara gider. Aynı anlama gelen efektler tek karoda birleşir (`candle`, `Candle`, `Candlelight` → "Mum Işığı").
- **Her efekte özel simge.** Yüzlerce efektin her biri için aynı stilde çizilmiş simge; bilinmeyen adlarda en uygun simge kendiliğinden seçilir. İstersen kendi simgeni yüklersin.
- **Her odanın kendi sekmeleri, favorileri ve gizlenen efektleri.** Efekte basılı tut (masaüstünde sağ tık): favorile, gizle, simge yükle.
- **Tek Durdur düğmesi.** Efekt çalan her ışığı durdurur, ardından göz yormayan sakin bir beyaza alır (varsayılan 3200 K, %40).
- **Işık sekmesi:** parlaklık çubuğu, beyaz tonlar, renk çemberi ve hazır renkler.
- **Tablet ve telefon düzeni.** Telefonda her şey başparmak altında: üstte oda seçimi, altında çalan efekt ve Durdur, en altta kalın parlaklık çubuğu ve sekmeler. Sağa-sola kaydırınca oda değişir.
- **Kendi efektlerini oluştur.** Işıkları sürükleyip bir efekte kat; desteklemeyen ışık renk ya da beyaz açar, istediğin ışık kendi listesinden başka bir efekt oynatır.
- **Eksik ışıkları tamamla.** Efekti odadaki ışıkların yalnız bir kısmı destekliyorsa ötekilerine renk, beyaz, başka efekt ya da kapat seçilir; efekt bütün odayı kaplar.
- **Önizleme.** Kontrol panelinde efektleri ışıklarda art arda deneyip karşılaştırırsın; çıkınca ışıklar eski haline döner.
- **Dört hazır buton kartı:** telefon, telefonda tam ekran, tam ekran ve boyutu ayarlanabilen pencere. Hiçbiri browser_mod istemez.
- **Sesli komut ve otomasyon.** Assist'e "salonda kuzey ışıkları efektini aç" demen yeter. Her oda için efekt seçimi varlığı ve `ismet_light_effects.play` servisi de var.
- **Gönderim yolu (isteğe bağlı).** Uyumlu bir entegrasyon varsa efektin ışığa yerel ağdan, Bluetooth'tan ya da internetten mi gittiği karonun köşesinde görünür.
- **Gece modu, yedek, sıfırlama.** Belirli saatlerde parlaklık sınırı; bütün düzeni tek dosyaya yedekleyip geri yükleme.
- **İsmet Home ile birlikte.** [İsmet Home](https://github.com/ig-86/ig-home) kuruluysa panonun üst şeridine Efektler düğmesi gelir.
- Türkçe, İngilizce, Almanca, İspanyolca ve Fransızca arayüz.

## Kurulum

Gerekenler: Home Assistant 2024.4 ya da daha yeni. Home Assistant 2026.11 ve sonrasında **Ayarlar → Marketplace**, daha eski sürümlerde [HACS](https://hacs.xyz/docs/use/). Başka kart, tema ya da eklenti gerekmez.

1. **İndir:** Marketplace (ya da HACS) → sağ üstte **⋮** → **Özel depolar** → depo: `https://github.com/ig-86/ig-light-effect`, tür: **Entegrasyon** → **Ekle**. Listeden **İsmet Light Effect Card** → **İndir**.
2. **Yeniden başlat:** Ayarlar → Sistem → ⏻ → Home Assistant'ı yeniden başlat.
3. **Entegrasyonu ekle:** Ayarlar → Cihazlar ve hizmetler → **Entegrasyon ekle** → "İsmet" yaz → **İsmet Light Effect Card** → **Gönder**. Soru sorulmaz, ışıklar kendiliğinden bulunur.
4. **Odalarını düzenle:** Sol menüde **İsmet Işık Efekt Kartı** belirir (yalnız yöneticiler görür). Her oda ışıklarına göre otomatik dolar; dokunmadan da kullanabilirsin. Efektleri sekmeler arasında sürükle, **Favoriler**'e bırakırsan yıldızlanır, **Gizli**'ye bırakırsan kartta görünmez. Hata yaparsan **Geri al** (Ctrl+Z).
5. **Kartı panona ekle:** Pano → ✏️ → **+** → "İsmet" yaz → kartı ya da buton kartlarından birini seç → **Kaydet**. Kart kendini kaydeder; *Kaynaklar* menüsüne bir şey eklemen gerekmez.

```yaml
type: custom:ismet-light-effect-card
```

### Hazır buton kartları

Panoda küçük bir buton olarak durur, dokununca efekt ekranını açar. Telefonun geri tuşu, Esc ve ✕ ile kapanır.

| Kart | Ne açar |
|---|---|
| `custom:ismet-phone-button` | Telefon düzeni; geniş ekranda ortada telefon boyutunda pencere |
| `custom:ismet-phone-fullscreen-button` | Telefon düzeni, telefonda tarayıcının tam ekran modunu da açar |
| `custom:ismet-fullscreen-button` | Bütün ekranı kaplayan efekt ekranı (duvar tableti için) |
| `custom:ismet-window-button` | Boyutu, konumu ve köşeleri ayarlanabilen pencere |

Bütün seçenekler (ad, renk, simge, buton biçimi, pencere boyutu…) görsel düzenleyicide var.

## Otomasyonlar ve sesli komut

Her oda için bir **efekt seçimi** varlığı oluşur (`select.ismet_salon_effect` gibi; Tüm Ev için `select.ismet_home_effect`). Listeden seçince efekt oynar, `—` seçilince durur.

```yaml
action: ismet_light_effects.play
data:
  room: salon            # alan kimliği ya da kartta görünen oda adı; _all = Tüm Ev
  effect: Kuzey Işıkları # ışıktaki adı, kartta görünen adı ya da kendi efektinin adı
  brightness: 60         # isteğe bağlı, %
```

`ismet_light_effects.stop` odadaki efektleri durdurur, `ismet_light_effects.list_effects` odanın oynatabildiği efektleri verir.

**Assist:** "Salonda kuzey ışıkları efektini aç", "Mum ışığı efektini aç" (oda söylenmezse komutu duyan cihazın odası), "Salonda efekti durdur". Cümlede "efekt" kelimesi geçmeli; normal ışık komutların eskisi gibi çalışır.

## Güncelleme

Kontrol panelinde **Ayarlar → Sürüm ve güncelleme → Güncellemeleri denetle**. Yeni sürüm varsa **Güncelle** Marketplace ya da HACS'tan indirir, **Yeniden başlat** Home Assistant'ı yeniden başlatır. Her güncellemeden sonra yeniliklerin özeti bir kez gösterilir. Odaların, sekmelerin, favorilerin ve simgelerin güncellemede silinmez.

## Sorun giderme

- **Kart seçicide kartlar çıkmıyor.** Entegrasyonun eklendiğinden ve Home Assistant'ın yeniden başlatıldığından emin ol, sonra tarayıcıyı Ctrl+F5 ile yenile.
- **Bir ışık efekt listesini daraltıyor.** Kontrol panelinde o ışığa tıkla, **Efektlerde kullan**'ı kapat. Işık renk ve parlaklık için çalışmaya devam eder.
- **Bir ışık görünmüyor.** Işığın bir alana atanmış olması gerekir; alanı olmayanlar panelde **Diğer** odasında toplanır.
- **Hâlâ çözülmedi mi?** Kontrol panelinde **Yardım → Sorun bildir** ya da [GitHub'da sorun aç](https://github.com/ig-86/ig-light-effect/issues).

---

## English

A Home Assistant card that manages every light with effects, room by room, whatever the brand. Effects, white tones and colours in one screen; everything is set up from a control panel inside Home Assistant, no code needed.

**Quick install:** Settings → **Marketplace** (HACS on older versions) → ⋮ → **Custom repositories** → `https://github.com/ig-86/ig-light-effect` (Integration) → Download → restart Home Assistant → **Settings → Devices & services → Add integration → İsmet Light Effect Card**.

### Highlights

- **Rooms come from Home Assistant areas.** No light lists in YAML. Pick which lights each room's effects go to; the choice is shared by everyone in the home.
- **Different brands in one room.** All effects of the selected lights show up. Dots under an effect show how many lights support it; tapping sends it only to those. Effects with the same meaning merge into one tile.
- **A drawn icon for every effect**, picked automatically for unknown names. You can upload your own.
- **Per-room tabs, favourites and hidden effects.** Long-press an effect (right-click on desktop) to favourite, hide or set an icon.
- **One Stop button** that stops every effect and switches the lights to a calm white (3200 K, 40% by default).
- **Light tab:** brightness slider, white tones, colour wheel and preset colours.
- **Tablet and phone layouts.** On phones everything is under your thumb; swipe left or right to change rooms.
- **Create your own effects** by dragging lights into an effect; lights that do not support it show a colour, white or another effect.
- **Fill in missing lights**: when only some lights support an effect, choose what the others do so the effect covers the whole room.
- **Preview** effects on the real lights in the control panel; the lights go back to how they were when you leave.
- **Four ready-made button cards:** phone, phone full screen, full screen and a resizable window. No browser_mod needed.
- **Voice and automations.** Tell Assist "play the aurora effect in the living room". Every room gets an effect select entity and there is an `ismet_light_effects.play` service.
- **Delivery path (optional):** with a compatible integration each tile shows whether the effect goes over the local network, Bluetooth or the cloud.
- **Night mode, backup, reset.** A brightness cap for chosen hours; back up the whole layout to one file and restore it.
- **Works with İsmet Home.** With [İsmet Home](https://github.com/ig-86/ig-home) installed, an Effects button appears in the dashboard's top bar.
- Turkish, English, German, Spanish and French interface.

### Installation

Requires Home Assistant 2024.4 or newer. On Home Assistant 2026.11 and later use **Settings → Marketplace**, on older versions [HACS](https://hacs.xyz/docs/use/).

1. **Download:** Marketplace (or HACS) → **⋮** at the top right → **Custom repositories** → repository `https://github.com/ig-86/ig-light-effect`, type **Integration** → **Add**. Pick **İsmet Light Effect Card** → **Download**.
2. **Restart:** Settings → System → ⏻ → Restart Home Assistant.
3. **Add the integration:** Settings → Devices & services → **Add integration** → type "İsmet" → **İsmet Light Effect Card** → **Submit**. No questions; lights are found automatically.
4. **Arrange your rooms:** **İsmet Işık Efekt Kartı** appears in the sidebar (admins only). Every room fills itself from its lights; drag effects between tabs, onto **Favourites** or **Hidden**. **Undo** (Ctrl+Z) is always there.
5. **Add the card:** dashboard → ✏️ → **+** → type "İsmet" → pick the card or one of the button cards → **Save**. No *Resources* entry needed.

```yaml
type: custom:ismet-light-effect-card
```

Button cards: `custom:ismet-phone-button`, `custom:ismet-phone-fullscreen-button`, `custom:ismet-fullscreen-button`, `custom:ismet-window-button`. All options are in the visual editor.

### Automations and voice

Each room gets an effect select entity (e.g. `select.ismet_salon_effect`, `select.ismet_home_effect` for the whole home). Services: `ismet_light_effects.play` (`room`, `effect`, optional `brightness`, `transition`), `ismet_light_effects.stop` and `ismet_light_effects.list_effects`. Assist understands sentences such as "play the aurora effect in the living room" and "stop the effects in the bedroom".

### Updating

In the control panel: **Settings → Version and updates → Check for updates**. **Update** downloads through Marketplace or HACS and **Restart** restarts Home Assistant. A short what's-new note shows once after each update. Rooms, tabs, favourites and icons are kept.

### Troubleshooting

- **Cards don't show in the card picker:** make sure the integration is added and Home Assistant restarted, then reload the browser with Ctrl+F5.
- **A light narrows the effect list:** click it in the control panel and turn off **Use for effects**.
- **A light is missing:** it needs an area; lights without one are collected in **Other**.
- **Still stuck?** Use **Help → Report a problem** in the control panel or [open an issue](https://github.com/ig-86/ig-light-effect/issues).

---

<sub>Lisans / License: GPL-3.0 ([LICENSE](LICENSE), [NOTICE.md](NOTICE.md)). Bu proje değiştirilmiş bir türevdir / This project is a modified derivative. Based on Lemur Light Effect Card by mendeburlemur — https://github.com/mendebur-lemur/lemur-light-effect-card</sub>
