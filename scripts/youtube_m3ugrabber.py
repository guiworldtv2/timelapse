#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",MTV LATINOAMERICA
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/MTV_HD/SA_SAGEMCOM/MTV_HD.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El Trece
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El Trece 2
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v1a1/mono.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV PUBLICA
https://cntlnk-main-edge-access.secure.footprint.net/b16/ngrp:c7_vivo01_dai_source-20001_all/c7_vivo01_dai_source-20001_720p.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV PUBLICA
https://cntlnk-main-edge-access.secure.footprint.net/b16/ngrp:c7_vivo01_dai_source-20001_all/c7_vivo01_dai_source-20001_720p.m3u8
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/assets/moose_na.m3u')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    
banner = r'''


https://gist.githubusercontent.com/guiworldtv/b5db2465556dc55b66e13650bd5f5d37/raw/
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Rosario (720p) [Not 24/7]
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Santa F  (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/canal13santafe_1@751190/master.m3u8?hdnea=st=1645561118~exp=1645737518~acl=/i/canal13santafe_1@751190/*~hmac=5c257cbcbcb2730ac5fedbdd6ee12ad256104b441711d394397744f94a404ad2
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Mar del Plata (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/mdqdistri02_1@829747/master.m3u8?hdnea=st=1645560795~exp=1645737195~acl=/i/mdqdistri02_1@829747/*~hmac=95846b50cc71a3e1a7ca5f4eeec6f4837bf26e61c71ec58e542546b4a2b63a3e
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Tucuman (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/canal8tucuman_1@787002/master.m3u8?hdnea=st=1645561206~exp=1645737606~acl=/i/canal8tucuman_1@787002/*~hmac=0c32d04d2d681e86b55f0dc4afc66b9a7ea33784ebaf36fe1a1e2078b191f94c
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://200.115.193.177/live/26hd-720/.m3u8?CompartilhandoIPTV
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://uni5rtmp.tulix.tv:1935/bettervida/bettervida/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://moiptvhls-i.akamaihd.net/hls/live/652315/secure/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://inliveserver.com:1936/15506/15506/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://azxtv.com/hls/stream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Argentinisima/smil:argentinisima.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://vs-hls-push-uk-live.akamaized.net/x=3/i=urn:bbc:pips:service:bbc_news_channel_hd/mobile_wifi_main_sd_abr_v2.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://103.199.161.254/Content/bbcworld/Live/Channel(BBCworld)/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://45.5.8.78:8000/play/a00i
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://live.canalnueve.tv/canal.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://cdn2.zencast.tv:30443/live/canal10smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8204/8204/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://stmv4.questreaming.com/fenixlarioja/fenixlarioja/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/madryntv/madryntv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://arcast.net:1935/mp/mp/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://200.115.193.177/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.dattalive.com/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/catamarcatelevision/catamarcatelevision/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://s8.stweb.tv/chacra/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://coninfo.net:1935/chacodxdtv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Garage/smil:garage.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://elonceovh.elonce.com/hls/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://v4.tustreaming.cl/enlacebpbtv/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://euronews-euronews-spanish-2-mx.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://f24hls-i.akamaihd.net/hls/live/221147/F24_EN_HI_HLS/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://f24hls-i.akamaihd.net/hls/live/520845/F24_ES_HI_HLS/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://videostreaming.cloudserverlatam.com/8066/8066/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stream.live.novotempo.com/tv/smil:tvnuevotiempo.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://mdstrm.com/live-stream-playlist/5b9076d18ef7b22560354649.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/live-powerTV/power.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://strm.yandex.ru/kal/rt_hd/rt_hd0.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/santa_maria/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.seo.tv.bo:3337/live/franzbalboa2live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://paneltv.online:1936/8116/8116/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tastemade-es8intl-roku.amagi.tv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://videostream.shockmedia.com.ar:1936/telejunin/telejunin/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://cnnsanjuan.com:9999/live/telesol/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/ttv.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://v4.tustreaming.cl/tevexinter/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://cdnh4.iblups.com/hls/irtp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://america-crtvg.flumotion.com/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stratus.stream.cespi.unlp.edu.ar/hls/tvunlp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59a564764e2b6.streamlock.net/vallenato/Vallenato2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/vertv/vertv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Garage/garage.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV  (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV  (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top  (Argentina)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax  HD Argent.
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/chunklist_w950122583_b1828000_sleng.m3u8

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  Argentina (576p) [Not 24/7]
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",24/7 Canal de Noticias
http://59c5c86e10038.streamlock.net:1935/6605140/6605140/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5RTV Santa Fe
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV (Corrientes) (480p)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV Corrientes
http://www.coninfo.net:1935/tvcinco/live1/chunklist_w1546509083.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",CANAL PROVINCIAL SAN MIGUEL
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-180/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-360/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Chacra TV
http://s8.stweb.tv:1935/chacra/live/chunks.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Ciudad TV Chaco
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music TOP
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w1582140541_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/musictop.smil/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w538311571_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar:1935/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/tlxhd-720/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  C rdoba
http://csvl03.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  C rdoba
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Rosario (720p)
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax
http://live-edge01.telecentro.net.ar/live/tlxhd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",1HD Music
http://1hdru-hls-otcnet.cdnvideo.ru/onehdmusic/mono.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Latino Kids TV * | UY
https://videostreaming.cloudserverlatam.com/8066/8066/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="269" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/269_Canal_13_San_Luis.png",tvg-id="269" tvg-name="Canal 13 San Luis" tvg-logo="https://www.m3u.cl/logo/269_Canal_13_San_Luis.png,  Canal 13 San Luis * | AR
https://5975e06a1f292.streamlock.net:4443/sanluistv/ngrp:sanluistv_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="277" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png",tvg-id="277" tvg-name="Canal XFN" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png,  Canal XFN * | AR
https://streamconex.com:1936/canalxfn/canalxfn/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="218" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/218_Senal_Urbana.png",tvg-id="218" tvg-name="Se al Urbana" tvg-logo="https://www.m3u.cl/logo/218_Senal_Urbana.png,  Se al Urbana * | AR
https://stmvideo2.livecastv.com/urbana98/urbana98/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1026" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png",tvg-id="1026" tvg-name="Tele Mix" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png,  Tele Mix * | AR
https://panel.dattalive.com:443/8068/8068/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1010" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1010_UNaM_Transmedia.png",tvg-id="1010" tvg-name="UNaM Transmedia" tvg-logo="https://www.m3u.cl/logo/1010_UNaM_Transmedia.png,  UNaM Transmedia * | AR
http://192.100.186.53:8090/hls/live.stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="488" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png",tvg-id="488" tvg-name="Anime Zone TV" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png,  Anime Zone TV | AR
http://azxtv.com/hls/stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="206" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg",tvg-id="206" tvg-name="Paka Paka" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg,  Paka Paka | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="251" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png",tvg-id="251" tvg-name="13 Max Television" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png,  13 Max Television | AR
http://coninfo.net:1935/13maxhd/live13maxtvnuevo_720p/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="221" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png",tvg-id="221" tvg-name="5R TV Santa Fe" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png,  5R TV Santa Fe | AR
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="249" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/249_5TV.png",tvg-id="249" tvg-name="5TV" tvg-logo="https://www.m3u.cl/logo/249_5TV.png,  5TV | AR
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="250" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/250_9Link.png",tvg-id="250" tvg-name="9Link" tvg-logo="https://www.m3u.cl/logo/250_9Link.png,  9Link | AR
http://www.coninfo.net:1935/9linklive/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="252" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png",tvg-id="252" tvg-name="Aire de Santa Fe" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png,  Aire de Santa Fe | AR
https://sc1.stweb.tv/airedigital/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="253" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/253_Argentinisima_Satelital.png",tvg-id="253" tvg-name="Argentinisima Satelital" tvg-logo="https://www.m3u.cl/logo/253_Argentinisima_Satelital.png,  Argentinisima Satelital | AR
http://186.0.233.76:1935/Argentinisima/smil:argentinisima.smil/chunklist_sleng.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="215" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png",tvg-id="215" tvg-name="Azahares Radio Multimedia" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png,  Azahares Radio Multimedia | AR
http://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="209" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/209_Beat_Digital.png",tvg-id="209" tvg-name="Beat Digital" tvg-logo="https://www.m3u.cl/logo/209_Beat_Digital.png,  Beat Digital | AR
https://5975e06a1f292.streamlock.net:4443/beatvideo/beatvideo/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="224" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png",tvg-id="224" tvg-name="Cadena 103" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png,  Cadena 103 | AR
http://arcast.net:1935/cadena103/cadena103/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="266" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/266_Canal_10.png",tvg-id="266" tvg-name="Canal 10" tvg-logo="https://www.m3u.cl/logo/266_Canal_10.png,  Canal 10 | AR
https://vcp.myplaytv.com:443/canal10cba/smil:canal10cba.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="267" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/267_Canal_10_Mar_del_Plata.png",tvg-id="267" tvg-name="Canal 10 Mar del Plata" tvg-logo="https://www.m3u.cl/logo/267_Canal_10_Mar_del_Plata.png,  Canal 10 Mar del Plata | AR
https://cdn2.zencast.tv:30443/live/canal10smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="799" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg",tvg-id="799" tvg-name="Canal 10 Nortevision" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg,  Canal 10 Nortevision | AR
https://vivo.solumedia.com:19360/nortevision/nortevision.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="299" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png",tvg-id="299" tvg-name="Canal 10 Rio Negro" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png,  Canal 10 Rio Negro | AR
https://panel.dattalive.com:443/8204/8204/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="268" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png",tvg-id="268" tvg-name="Canal 12 Madryn TV" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png,  Canal 12 Madryn TV | AR
https://5f700d5b2c46f.streamlock.net:443/madryntv/madryntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="226" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/226_Canal_13_Jujuy.png",tvg-id="226" tvg-name="Canal 13 Jujuy" tvg-logo="https://www.m3u.cl/logo/226_Canal_13_Jujuy.png,  Canal 13 Jujuy | AR
https://genexservicios.com:19360/canal13jujuy/canal13jujuy.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="227" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg",tvg-id="227" tvg-name="Canal 13 La Rioja" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg,  Canal 13 La Rioja | AR
http://arcast.net:1935/mp/mp/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="228" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png",tvg-id="228" tvg-name="Canal 2 Jujuy" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png,  Canal 2 Jujuy | AR
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="205" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg",tvg-id="205" tvg-name="Canal 2 Sanagasta" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg,  Canal 2 Sanagasta | AR
https://stmvideo1.livecastv.com/canal2/canal2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="229" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png",tvg-id="229" tvg-name="Canal 20 Villamaria" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png,  Canal 20 Villamaria | AR
https://cronos.aldeaglobal.net.ar/hls/canal20.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1057" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png",tvg-id="1057" tvg-name="Canal 21 TV" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png,  Canal 21 TV | AR
https://iptv.ixfo.com.ar:30443/c21tv/hd/c21tv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="230" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg",tvg-id="230" tvg-name="Canal 22 Buenos Aires" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg,  Canal 22 Buenos Aires | AR
https://5f700d5b2c46f.streamlock.net:443/canal22/canal22/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="271" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png",tvg-id="271" tvg-name="Canal 26" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png,  Canal 26 | AR
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 HD (AR)
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist.m3u8?ROGERIOTORRES
#EXTINF:-1  tvg-id="776" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/776_Canal_3_La_Pampa.png",tvg-id="776" tvg-name="Canal 3 La Pampa" tvg-logo="https://www.m3u.cl/logo/776_Canal_3_La_Pampa.png,  Canal 3 La Pampa | AR
https://5975e06a1f292.streamlock.net:4443/c3lapampa/ngrp:c3lapampa_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="256" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png",tvg-id="256" tvg-name="Canal 3 Rosario" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png,  Canal 3 Rosario | AR
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="257" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png",tvg-id="257" tvg-name="Canal 4 Bahia Blanca" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png,  Canal 4 Bahia Blanca | AR
https://vivo.solumedia.com:19360/bvconline/bvconline.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="779" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/779_Canal_4_Eldorado.png",tvg-id="779" tvg-name="Canal 4 Eldorado" tvg-logo="https://www.m3u.cl/logo/779_Canal_4_Eldorado.png,  Canal 4 Eldorado | AR
https://5975e06a1f292.streamlock.net:4443/canal4eldorado/canal4eldorado/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="258" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png",tvg-id="258" tvg-name="Canal 4 Jujuy" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png,  Canal 4 Jujuy | AR
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="259" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png",tvg-id="259" tvg-name="Canal 4 Posadas" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png,  Canal 4 Posadas | AR
http://iptv.ixfo.com.ar:8081/live/C4POS/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="773" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/773_Canal_5_Santa_Fe.png",tvg-id="773" tvg-name="Canal 5 Santa Fe" tvg-logo="https://www.m3u.cl/logo/773_Canal_5_Santa_Fe.png,  Canal 5 Santa Fe | AR
https://5975e06a1f292.streamlock.net:4443/c5sf/c5sf/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="232" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/232_Canal_50_Morteros.png",tvg-id="232" tvg-name="Canal 50 Morteros" tvg-logo="https://www.m3u.cl/logo/232_Canal_50_Morteros.png,  Canal 50 Morteros | AR
http://168.196.255.130:8080/canal50/vivo.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="233" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg",tvg-id="233" tvg-name="CANAL 5TV" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg,  CANAL 5TV | AR
https://srv3.zcast.com.br/carlosr/carlosr/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="307" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png",tvg-id="307" tvg-name="Canal 6 Entre Rios" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png,  Canal 6 Entre Rios | AR
https://stmvideo1.livecastv.com/canal6er/canal6er/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="261" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/261_Canal_6_Moreno.png",tvg-id="261" tvg-name="Canal 6 Moreno" tvg-logo="https://www.m3u.cl/logo/261_Canal_6_Moreno.png,  Canal 6 Moreno | AR
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="262" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png",tvg-id="262" tvg-name="Canal 6 Posadas" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png,  Canal 6 Posadas | AR
https://iptv.ixfo.com.ar:30443/live/c6digital/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="264" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png",tvg-id="264" tvg-name="Canal 7 Jujuy" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png,  Canal 7 Jujuy | AR
https://stream.arcast.live/canal7jujuy/ngrp:canal7jujuy_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="234" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/234_Canal_7_Santiago_del_Estero.jpg",tvg-id="234" tvg-name="Canal 7 Santiago del Estero" tvg-logo="https://www.m3u.cl/logo/234_Canal_7_Santiago_del_Estero.jpg,  Canal 7 Santiago del Estero | AR
https://5975e06a1f292.streamlock.net:4443/envivo/castv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="236" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png",tvg-id="236" tvg-name="Canal 9 Litoral" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png,  Canal 9 Litoral | AR
https://stream.arcast.live/ahora/ahora/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="309" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/309_Canal_9_Televida.png",tvg-id="309" tvg-name="Canal 9 Televida" tvg-logo="https://www.m3u.cl/logo/309_Canal_9_Televida.png,  Canal 9 Televida | AR
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="273" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png",tvg-id="273" tvg-name="Canal 907 FM Comunicar" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png,  Canal 907 FM Comunicar | AR
https://panel.dattalive.com/canal907/canal907/chunklist_w1205944599.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="274" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png",tvg-id="274" tvg-name="Canal Cinco Tigre" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png,  Canal Cinco Tigre | AR
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="275" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png",tvg-id="275" tvg-name="Canal Coop" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png,  Canal Coop | AR
https://panel.dattalive.com:443/8138/8138/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="302" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png",tvg-id="302" tvg-name="Canal Nueve TV" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png,  Canal Nueve TV | AR
https://live.canalnueve.tv/canal.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="801" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg",tvg-id="801" tvg-name="Canal Provincial" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg,  Canal Provincial | AR
https://streaming.telered.com.ar/provincial/streaming/mystream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="203" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/203_Catamarca_TV.png",tvg-id="203" tvg-name="Catamarca TV" tvg-logo="https://www.m3u.cl/logo/203_Catamarca_TV.png,  Catamarca TV | AR
https://5f700d5b2c46f.streamlock.net/catamarcatelevision/catamarcatelevision/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="278" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png",tvg-id="278" tvg-name="Chacra TV" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png,  Chacra TV | AR
https://s8.stweb.tv/chacra/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="237" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg",tvg-id="237" tvg-name="Ciudad TV" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg,  Ciudad TV | AR
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="280" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png",tvg-id="280" tvg-name="CL3 Cablevision" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png,  CL3 Cablevision | AR
http://videostream.shockmedia.com.ar:1935/cl3cable/cl3cable/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="270" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png",tvg-id="270" tvg-name="CN 24/7 Neuquen" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png,  CN 24/7 Neuquen | AR
https://panel.dattalive.com:443/6605140/smil:6605140.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="893" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png",tvg-id="893" tvg-name="Complejo Dance" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png,  Complejo Dance | AR
https://mediacp.hostradios.com.ar:19360/complejodance/complejodance.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="238" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg",tvg-id="238" tvg-name="CPE TV" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg,  CPE TV | AR
https://stream.arcast.live/cpe/ngrp:cpe_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="239" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg",tvg-id="239" tvg-name="Fenix" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg,  Fenix | AR
https://stmvideo1.livecastv.com/fenixlarioja/fenixlarioja/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="803" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png",tvg-id="803" tvg-name="FM Metropolitana 100.5 MHZ" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png,  FM Metropolitana 100.5 MHZ | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="216" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg",tvg-id="216" tvg-name="Informacion Periodistica" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg,  Informacion Periodistica | AR
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="217" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png",tvg-id="217" tvg-name="La Voz de Tucuman" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png,  La Voz de Tucuman | AR
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="212" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png",tvg-id="212" tvg-name="Link TV" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png,  Link TV | AR
https://panel.dattalive.com:443/8128_1/8128_1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="241" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/241_Litus_TV.png",tvg-id="241" tvg-name="Litus TV" tvg-logo="https://www.m3u.cl/logo/241_Litus_TV.png,  Litus TV | AR
https://5975e06a1f292.streamlock.net:4443/litustv/ngrp:litustv_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="283" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png",tvg-id="283" tvg-name="Metro TV Canal 12 Tucuman" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png,  Metro TV Canal 12 Tucuman | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?token=null&PlaylistM3UCL
#EXTINF:-1  tvg-id="795" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png",tvg-id="795" tvg-name="Metropolitana FM" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png,  Metropolitana FM | AR
https://panel.dattalive.com/MetropolitanaFM/MetropolitanaFM/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="793" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/793_Milenium_TV.png",tvg-id="793" tvg-name="Milenium TV" tvg-logo="https://www.m3u.cl/logo/793_Milenium_TV.png,  Milenium TV | AR
https://tuvideoonline.com.ar:3994/live/mileniumtvlive.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="284" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png",tvg-id="284" tvg-name="Multivisi n" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png,  Multivisi n | AR
https://panel.dattalive.com:443/8250/8250/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="285" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png",tvg-id="285" tvg-name="Net TV" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png,  Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="243" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/243_Power.png",tvg-id="243" tvg-name="Power" tvg-logo="https://www.m3u.cl/logo/243_Power.png,  Power | AR
https://live2.tensila.com/1-1-1.power-tv/hls/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="912" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png",tvg-id="912" tvg-name="Radio Blu" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png,  Radio Blu | AR
https://59537faa0729a.streamlock.net:443/radioblu/radioblu/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="210" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png",tvg-id="210" tvg-name="Radiocanal San Francisco" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png,  Radiocanal San Francisco | AR
http://204.199.3.2/.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="287" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/287_RTN.png",tvg-id="287" tvg-name="RTN" tvg-logo="https://www.m3u.cl/logo/287_RTN.png,  RTN | AR
http://media.neuquen.gov.ar/rtn/television/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="202" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/202_San_Pedro_TV.png",tvg-id="202" tvg-name="San Pedro TV" tvg-logo="https://www.m3u.cl/logo/202_San_Pedro_TV.png,  San Pedro TV | AR
https://srv6.zcast.com.br/sptv/sptv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="288" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png",tvg-id="288" tvg-name="Sicardi TV" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png,  Sicardi TV | AR
https://vivo.solumedia.com:19360/sicarditv/sicarditv.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1072" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1072_Somos_La_Pampa.png",tvg-id="1072" tvg-name="Somos La Pampa" tvg-logo="https://www.m3u.cl/logo/1072_Somos_La_Pampa.png,  Somos La Pampa | AR
https://5975e06a1f292.streamlock.net:4443/somosnoticias/somosnoticias/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="289" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png",tvg-id="289" tvg-name="TDC TV Santa Fe" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png,  TDC TV Santa Fe | AR
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="308" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png",tvg-id="308" tvg-name="Tele Estrella" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png,  Tele Estrella | AR
https://stmvideo2.livecastv.com/telestrella/telestrella/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="290" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png",tvg-id="290" tvg-name="Telecreativa" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png,  Telecreativa | AR
https://panel.dattalive.com:443/8012/8012/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="291" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png",tvg-id="291" tvg-name="Telediario Televisi n" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png,  Telediario Televisi n | AR
https://mediacp.hostradios.com.ar:19360/telediario/telediario.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="245" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg",tvg-id="245" tvg-name="Telediez" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg,  Telediez | AR
https://videohd.live:19360/8020/8020.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="246" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/246_Telefe_Rosario.jpg",tvg-id="246" tvg-name="Telefe Rosario" tvg-logo="https://www.m3u.cl/logo/246_Telefe_Rosario.jpg,  Telefe Rosario | AR
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="292" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png",tvg-id="292" tvg-name="Telemax" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png,  Telemax | AR
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="814" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg",tvg-id="814" tvg-name="TeleNord" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg,  TeleNord | AR
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="295" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/295_Telesol_San_Juan.png",tvg-id="295" tvg-name="Telesol San Juan" tvg-logo="https://www.m3u.cl/logo/295_Telesol_San_Juan.png,  Telesol San Juan | AR
https://cnnsanjuan.com:9999/live/telesol/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="293" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png",tvg-id="293" tvg-name="Telpin Canal 2" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png,  Telpin Canal 2 | AR
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="294" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png",tvg-id="294" tvg-name="Terramia TV" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png,  Terramia TV | AR
https://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="777" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/777_Tribu_TV.jpg",tvg-id="777" tvg-name="Tribu TV" tvg-logo="https://www.m3u.cl/logo/777_Tribu_TV.jpg,  Tribu TV | AR
https://5975e06a1f292.streamlock.net:4443/tributv/tributv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="296" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png",tvg-id="296" tvg-name="TSN Necochea" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png,  TSN Necochea | AR
https://panel.dattalive.com:443/tsnnecochea/tsnnecochea/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="788" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg",tvg-id="788" tvg-name="TV Dos Salta" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg,  TV Dos Salta | AR
https://vivo.solumedia.com:19360/tv2salta/tv2salta.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="297" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/297_TV_Mana.png",tvg-id="297" tvg-name="TV Mana" tvg-logo="https://www.m3u.cl/logo/297_TV_Mana.png,  TV Mana | AR
http://csvl03.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="248" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png",tvg-id="248" tvg-name="Uni Teve" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png,  Uni Teve | AR
https://vivo.solumedia.com:19360/uniteve/uniteve.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="304" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/304_UTN_TV.png",tvg-id="304" tvg-name="UTN TV" tvg-logo="https://www.m3u.cl/logo/304_UTN_TV.png,  UTN TV | AR
https://5975e06a1f292.streamlock.net:4443/utntv/utntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1100" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1100_DEPORTV.png",tvg-id="1100" tvg-name="DEPORTV" tvg-logo="https://www.m3u.cl/logo/1100_DEPORTV.png,  DEPORTV | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="282" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/282_Garage_TV.png",tvg-id="282" tvg-name="Garage TV" tvg-logo="https://www.m3u.cl/logo/282_Garage_TV.png,  Garage TV | AR
http://186.0.233.76:1935/Garage/smil:garage.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="493" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png",tvg-id="493" tvg-name="Net TV" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png,  Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="492" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/492_TV_Publica.png",tvg-id="492" tvg-name="TV Publica" tvg-logo="https://www.m3u.cl/logo/492_TV_Publica.png,  TV Publica | AR
https://g1.vxral-hor.transport.edge-access.net/b16/ngrp:c7_vivo01_dai_source-20001_all/c7_vivo01_dai_source-20001.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="24" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png",tvg-id="24" tvg-name="Music Top" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png,  Music Top | AR
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="208" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png",tvg-id="208" tvg-name="CINE.AR" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png,  CINE.AR | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="207" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg",tvg-id="207" tvg-name="Orbe 21" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg,  Orbe 21 | AR
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1003" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png",tvg-id="1003" tvg-name="Sublime Gracia TV" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png,  Sublime Gracia TV | AR
https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El nueve
https://rbmn-live.akamaized.net/hls/live/590971/201212BatallaWorldFinalPri/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El nueve
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/b00d164f-be51-473e-a47c-b33aa1f44186.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Aire de Santa Fe TV
https://sc1.stweb.tv/airedigital/live/chunklist_w1407250980.m3u8

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",DEPORTV
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/chunklist.m3u8
'''
