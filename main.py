import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SANS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SANSB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f_kick=F(SANSB,11); f_mast=F(SERIF,34); f_sub=F(SERIF,12); f_reg=F(SANSB,10); f_strip=F(SANSB,9); f_num=F(SERIF,20); f_nlab=F(SANS,8); f_hkick=F(SANSB,9); f_hhead=F(SANSB,12); f_hdeck=F(SANS,10); f_ckick=F(SANSB,8); f_chead=F(SANSB,10); f_cdeck=F(SANS,9); f_also=F(SANS,9); f_date=F(SANS,9); f_foot=F(SANS,8); f_pin=F(SANSB,9)
img=Image.new('RGB',(W,H),(250,244,230)); d=ImageDraw.Draw(img)
RED=(178,34,34); NAVY=(18,42,78); TEAL=(16,90,90); GOLD=(176,132,24); GREEN=(22,110,52); GREY=(90,90,90); INK=(20,20,20)
def wrap(t,font,mw):
    lines=[]; cur=''
    for w in t.split():
        s=(cur+' '+w).strip()
        if d.textlength(s,font=font)<=mw: cur=s
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def txt(x,y,t,font,fill=INK,align='l'):
    x-=d.textlength(t,font=font)/2 if align=='c' else d.textlength(t,font=font) if align=='r' else 0
    d.text((x,y),t,font=font,fill=fill)
def chip(x,y,t,fill):
    w=d.textlength(t,font=f_ckick)+8; d.rounded_rectangle([x,y,x+w,y+12],2,fill=fill); d.text((x+4,y+1),t,font=f_ckick,fill=(255,255,255)); return x+w+4
def scene(x,y,w,h,kind):
    if h<40:
        _bg={'ukraine':(20,26,54),'trophy':(18,90,60),'ship':(30,90,140),'market':(235,240,245),'data':(40,10,10),'heli':(150,180,200),'store':(220,200,170),'desert':(255,220,150),'valley':(200,170,120),'space':(10,16,44)}.get(kind,(210,220,235))
        d.rectangle([x,y,x+w,y+h],fill=_bg,outline=NAVY)
        _m={'market':('line',[(x+4,y+h-4),(x+w//2,y+6),(x+w-4,y+4)],GREEN),'ship':('rect',[x+30,y+8,x+w-30,y+h-4],(180,50,40)),'trophy':('ell',[x+w//2-8,y+2,x+w//2+8,y+h-2],GOLD),'space':('poly',[(x+w//2-3,y+2),(x+w//2+3,y+2),(x+w//2+1,y+h-2),(x+w//2-1,y+h-2)],(255,255,255)),'data':('rect',[x+6,y+4,x+w-6,y+10],RED),'ukraine':('ell',[x+w-14,y+3,x+w-4,y+13],(255,220,120)),'heli':('ell',[x+70,y+4,x+120,y+h-4],(60,80,60)),'desert':('ell',[x+w-16,y+2,x+w-4,y+14],(255,180,60))}.get(kind)
        if _m: (d.line(_m[1],fill=_m[2],width=2) if _m[0]=='line' else d.rectangle(_m[1],fill=_m[2]) if _m[0]=='rect' else d.ellipse(_m[1],fill=_m[2]) if _m[0]=='ell' else d.polygon(_m[1],fill=_m[2]))
        return
    d.rectangle([x,y,x+w,y+h],fill=(210,220,235),outline=NAVY)
    if kind=='riyadh':
        d.rectangle([x,y+h-28,x+w,y+h],fill=(60,60,80))
        for i,bx in enumerate([x+8,x+52,x+96,x+140]): d.rectangle([bx,y+h-70-i*6,bx+26,y+h-28],fill=(40,40,60))
        d.rectangle([x+96,y+8,x+122,y+h-28],fill=(30,30,55)); d.polygon([(x+96,y+8),(x+122,y+8),(x+109,y-2)],fill=(255,190,60)); d.ellipse([x+w-30,y+6,x+w-10,y+26],fill=(255,200,80))
        for sx,sy in [(x+30,y+20),(x+150,y+30),(x+170,y+14)]: d.ellipse([sx-3,sy-3,sx+3,sy+3],fill=(255,120,40)); d.ellipse([sx-7,sy-7,sx+7,sy+7],outline=(255,120,40))
        d.text((x+6,y+h-16),'PIF TOWER',font=f_ckick,fill=(255,255,255))
    elif kind=='shanghai':
        d.rectangle([x,y+h-24,x+w,y+h],fill=(120,30,30)); d.rectangle([x+10,y+22,x+w-10,y+h-24],fill=(240,230,210),outline=NAVY); d.polygon([(x+10,y+22),(x+w-10,y+22),(x+w/2,y+4)],fill=RED)
        d.rectangle([x+w/2-14,y+44,x+w/2+14,y+h-24],fill=(60,40,40)); d.rectangle([x+18,y+30,x+52,y+52],fill=(255,255,255),outline=NAVY); d.text((x+20,y+34),'CCDI',font=f_ckick,fill=RED)
        for i in range(3): d.rectangle([x+62+i*36,y+34,x+92+i*36,y+42],fill=(200,200,200),outline=NAVY)
        d.text((x+6,y+h-16),'ZHONGNANHAI GATE',font=f_ckick,fill=(255,255,255))
    elif kind=='court':
        d.rectangle([x,y+h-22,x+w,y+h],fill=(90,90,90)); d.rectangle([x+14,y+26,x+w-14,y+h-22],fill=(235,228,210),outline=NAVY)
        for cx in [x+30,x+w/2,x+w-30]: d.rectangle([cx-5,y+40,cx+5,y+h-22],fill=(255,255,255),outline=NAVY)
        d.polygon([(x+14,y+26),(x+w-14,y+26),(x+w/2,y+8)],fill=NAVY); d.ellipse([x+w/2-18,y+52,x+w/2+18,y+72],fill=GOLD); d.rectangle([x+w/2-3,y+58,x+w/2+3,y+84],fill=(120,80,20)); d.text((x+6,y+h-16),'FEDERAL COURT',font=f_ckick,fill=(255,255,255))
    elif kind=='ukraine':
        d.rectangle([x,y,x+w,y+h],fill=(20,26,54)); d.polygon([(x+8,y+h-20),(x+40,y+h-50),(x+72,y+h-20)],fill=(50,50,70)); d.polygon([(x+120,y+h-20),(x+150,y+h-58),(x+180,y+h-20)],fill=(50,50,70))
        for sx,sy in [(x+20,y+12),(x+90,y+8),(x+160,y+16)]: d.ellipse([sx-2,sy-2,sx+2,sy+2],fill=(255,255,255))
        d.ellipse([x+w-24,y+8,x+w-8,y+24],fill=(255,220,120)); d.text((x+6,y+h-14),'KYIV NIGHT SKY',font=f_ckick,fill=(255,255,255))
    elif kind=='trophy':
        d.rectangle([x,y,x+w,y+h],fill=(18,90,60)); d.ellipse([x+w/2-22,y+8,x+w/2+22,y+44],fill=GOLD); d.rectangle([x+w/2-5,y+42,x+w/2+5,y+62],fill=GOLD); d.rectangle([x+w/2-16,y+60,x+w/2+16,y+66],fill=GOLD); d.rectangle([x+8,y+70,x+52,y+h-6],fill=(220,40,40)); d.rectangle([x+w-52,y+70,x+w-8,y+h-6],fill=(0,120,80)); d.text((x+6,y+h-16),'AFCON',font=f_ckick,fill=(255,255,255))
    elif kind=='ship':
        d.rectangle([x,y,x+w,y+34],fill=(140,180,220)); d.rectangle([x,y+34,x+w,y+h],fill=(30,90,140)); d.rectangle([x+30,y+44,x+w-30,y+62],fill=(180,50,40)); d.rectangle([x+50,y+30,x+80,y+44],fill=(255,255,255)); d.rectangle([x+110,y+22,x+116,y+44],fill=(60,60,60))
        for i in range(4): d.rectangle([x+34+i*38,y+48,x+58+i*38,y+58],fill=(255,220,80))
        d.text((x+6,y+h-14),'STRAIT OF HORMUZ',font=f_ckick,fill=(255,255,255))
    elif kind=='market':
        d.rectangle([x,y,x+w,y+h],fill=(235,240,245)); d.line([(x+6,y+h-14),(x+50,y+44),(x+90,y+52),(x+130,y+26),(x+w-6,y+12)],fill=GREEN,width=3); d.line([(x+6,y+h-14),(x+w-6,y+h-14)],fill=NAVY,width=2)
        d.text((x+6,y+6),'DOW 50,018',font=f_hkick,fill=GREEN); d.text((x+6,y+h-16),'NYSE',font=f_ckick,fill=NAVY)
    elif kind=='data':
        d.rectangle([x,y,x+w,y+h],fill=(40,10,10)); d.rectangle([x+10,y+10,x+w-10,y+26],fill=RED); d.text((x+12,y+12),'CODE RED',font=f_ckick,fill=(255,255,255))
        for i in range(5): d.rectangle([x+12+i*34,y+34,x+38+i*34,y+34+(i%3+1)*10],fill=(80,160,220))
        d.text((x+6,y+h-14),'DATA CENTRE',font=f_ckick,fill=(255,255,255))
    elif kind=='heli':
        d.rectangle([x,y,x+w,y+h],fill=(150,180,200)); d.polygon([(x+8,y+h-8),(x+70,y+30),(x+150,y+h-8)],fill=(90,120,90)); d.ellipse([x+60,y+18,x+130,y+40],fill=(60,80,60)); d.rectangle([x+128,y+26,x+170,y+32],fill=(60,80,60)); d.line([(x+40,y+14),(x+150,y+14)],fill=(40,40,40),width=3)
        d.text((x+6,y+h-14),'ESKISEHIR',font=f_ckick,fill=(255,255,255))
    elif kind=='store':
        d.rectangle([x,y,x+w,y+h],fill=(220,200,170)); d.rectangle([x+10,y+18,x+w-10,y+h-10],fill=(250,245,235),outline=NAVY); d.rectangle([x+10,y+18,x+w-10,y+34],fill=RED); d.text((x+14,y+21),'MARKET',font=f_ckick,fill=(255,255,255))
        for i in range(4): d.rectangle([x+18+i*40,y+44,x+48+i*40,y+60],fill=(180,180,200))
        d.text((x+6,y+h-14),'CARTAGENA',font=f_ckick,fill=(255,255,255))
    elif kind=='desert':
        d.rectangle([x,y,x+w,y+40],fill=(255,220,150)); d.polygon([(x+6,y+h-6),(x+80,y+44),(x+170,y+h-6)],fill=(200,160,90)); d.ellipse([x+w-30,y+6,x+w-10,y+26],fill=(255,180,60)); d.rectangle([x+20,y+52,x+60,y+62],fill=(80,60,40)); d.text((x+6,y+h-14),'ADEN 60 KM',font=f_ckick,fill=(255,255,255))
    elif kind=='valley':
        d.rectangle([x,y,x+w,y+h],fill=(200,170,120)); d.polygon([(x+6,y+h-6),(x+60,y+30),(x+120,y+h-6)],fill=(120,90,60)); d.polygon([(x+100,y+h-6),(x+150,y+36),(x+w-6,y+h-6)],fill=(100,80,55)); d.rectangle([x+40,y+58,x+90,y+70],fill=(60,60,60)); d.text((x+6,y+h-14),'WADI MAABAQ',font=f_ckick,fill=(255,255,255))
    else:
        d.rectangle([x,y,x+w,y+h],fill=(10,16,44)); d.polygon([(x+w/2-6,y+10),(x+w/2+6,y+10),(x+w/2+2,y+52),(x+w/2-2,y+52)],fill=(255,255,255)); d.ellipse([x+20,y+16,x+44,y+40],fill=(200,200,220)); d.ellipse([x+w-44,y+50,x+w-20,y+74],fill=(180,120,60)); d.text((x+6,y+h-14),'LONG MARCH-2F',font=f_ckick,fill=(255,255,255))
# HEADER
d.rectangle([0,0,W,118],fill=(250,244,230)); txt(12,8,'THE WORLD ON ONE PAGE',f_kick,RED); txt(1012,8,'38 STORIES · 6 REGIONS · 13 FIELDS',f_kick,RED,align='r')
txt(512,26,'Tuesday 24 November 2026',f_mast,INK,align='c')
txt(512,66,'Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts.',f_sub,RED,align='c')
regs=[('Europe',9,NAVY),('Middle East',8,RED),('Asia',8,TEAL),('Africa',2,GREEN),('Americas',7,GOLD),('World/Space',4,(90,60,140))]
bx=12
for name,n,c in regs:
    w=164; d.rectangle([bx,88,bx+w,110],fill=c); txt(bx+w/2,93,f'{name} {n}',f_reg,(255,255,255),align='c'); bx+=w+3
# STRIPS
d.rectangle([12,118,1012,148],fill=(255,255,255),outline=NAVY); txt(18,122,'THE DAY IN UTC',f_hkick,RED)
utc=[('00:30','Zelensky urges talks'),('02:15','NATO space defence'),('08:16','Hanoi blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
ux=120
for t,ev in utc: txt(ux,122,t,f_strip,NAVY); txt(ux,133,ev,f_nlab,GREY); ux+=112
d.rectangle([12,150,1012,182],fill=(18,42,78)); txt(18,154,'THE DAY IN NUMBERS',f_hkick,(255,220,80))
nums=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow, first over 50k'),('+8,99%','Taiex record'),('25','killed or missing, Yemen'),('26','Cikande fire toll')]
nx=150
for v,lab in nums: txt(nx,152,v,f_num,(255,255,255)); txt(nx,170,lab,f_nlab,(220,220,220)); nx+=144
# HEROES
heroes=[('1','RIYADH · MIDDLE EAST','CONFIRMED',GREEN,'Houthi drone hits Riyadh\'s tallest tower again, 11 hurt','A Houthi drone hit the PIF tower, Riyadh\'s tallest, for the second time in a week. Eleven were hurt.','riyadh'),('2','SHANGHAI · ASIA','OFFICIAL',(30,80,180),'China probes Shanghai party chief Chen Jining','Chen Jining, 62, is probed for "serious violations" — the fourth Politburo member to fall this year.','shanghai'),('3','NEW YORK · US / TECH','CONFIRMED',GREEN,'Huawei guilty on 10 of 12 counts','A US jury found Huawei guilty on 10 of 12 counts, including trade-secret theft. Sentencing is Sep 2027.','court')]
hx=12
for num,loc,chip_t,chip_c,head,deck,kind in heroes:
    w=324; d.rectangle([hx,188,hx+w,382],fill=(255,255,255),outline=NAVY); scene(hx+4,192,w-8,88,kind); txt(hx+8,284,f'{num}  {loc}',f_hkick,RED); chip(hx+8,298,chip_t,chip_c)
    [txt(hx+8,314+i*14,ln,f_hhead) for i,ln in enumerate(wrap(head,f_hhead,w-16)[:2])]; [txt(hx+8,344+i*11,ln,f_hdeck) for i,ln in enumerate(wrap(deck,f_hdeck,w-16)[:3])]; hx+=w+8
# CARDS 4-13
cards=[('4','ZAPORIZHZHIA · EUROPE','REPORTED',(30,80,180),'Russian attacks kill 9 across Ukraine in a day','Russia fired 96 drones; 73 were downed. Nine died, 81 were hurt.','ukraine'),('5','CAS · AFRICA / SPORT','OFFICIAL',(30,80,180),'CAS hands Senegal back the AFCON title','CAS ruled Morocco forfeited 3-0, so Senegal won 1-0.','trophy'),('6','HORMUZ · MIDDLE EAST','REPORTED',(30,80,180),'IRGC attacks container ship in Hormuz','An IRGC attack hit a ship at 18:58 UTC near Khasab, Oman.','ship'),('7','NEW YORK · MARKETS','CONFIRMED',GREEN,'Dow closes above 50,000 for the first time','The Dow closed at 50,018. The Nasdaq fell 1.5% as Taiex set a record.','market'),('8','REDMOND · TECH','REPORTED',(30,80,180),"Microsoft declares 'Code Red' after historic outage",'After a 24-hour outage, Microsoft set a one-hour recovery target.','data'),('9','ESKISEHIR · EUROPE','REPORTED',(30,80,180),'Turkish military helicopter crash kills 5','An AS-532 helicopter crashed in Eskisehir at 19:52 UTC, killing five.','heli'),('10','CARTAGENA · AMERICAS','REPORTED',(30,80,180),'Supermarket hostages: 25 held in Cartagena','Twenty-five were held hostage; five elderly women were freed.','store'),('11','ADEN · MIDDLE EAST','REPORTED',(30,80,180),'Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden at 16:51 UTC.','desert'),('12','LAHJ · MIDDLE EAST','REPORTED',(30,80,180),'Saudi strikes kill 25, wound 6 in Yemen','Strikes in Wadi Maabaq killed or left missing 25 and wounded six.','valley'),('13','JIUQUAN · SPACE','OFFICIAL',(30,80,180),'China names first foreign astronaut for Tiangong','Muhammad Zeeshan Ali of Pakistan is the first foreigner on Tiangong.','space')]
for r in range(2):
    for c in range(5):
        num,loc,chip_t,chip_c,head,deck,kind=cards[r*5+c]; x=12+c*200; y=388+r*100; w=194
        d.rectangle([x,y,x+w,y+96],fill=(255,255,255),outline=NAVY); scene(x+3,y+3,w-6,24,kind); txt(x+5,y+30,f'{num} {loc}',f_ckick,RED); chip(x+5,y+41,chip_t,chip_c)
        hl=wrap(head,f_chead,w-10)[:2]; [txt(x+5,y+54+i*10,ln,f_chead) for i,ln in enumerate(hl)]; [txt(x+5,y+54+len(hl)*10+i*8,ln,f_cdeck) for i,ln in enumerate(wrap(deck,f_cdeck,w-10)[:2])]
# MAP (equirectangular, real lat/lon)
MX, MY, MW, MH = 12, 594, 1000, 178
d.rectangle([MX,MY,MX+MW,MY+MH],fill=(185,215,235),outline=NAVY); txt(MX+8,MY+4,'THE WORLD · PINS 1–13',f_hkick,NAVY)
def mp(lon,lat): return (MX+(lon+180)/360*MW, MY+(84-lat)/142*MH)
LAND=[[(-168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-85,70),(-75,62),(-60,60),(-55,47),(-70,42),(-75,35),(-80,26),(-85,30),(-95,29),(-97,26),(-105,20),(-95,16),(-85,12),(-80,9),(-95,15),(-110,23),(-125,40),(-125,49),(-140,60),(-155,58)],[(-80,9),(-75,11),(-62,10),(-52,5),(-50,0),(-42,-5),(-35,-8),(-40,-20),(-48,-28),(-58,-35),(-65,-41),(-70,-50),(-73,-55),(-70,-40),(-72,-20),(-78,-10),(-80,0)],[(-17,15),(-10,30),(0,36),(10,37),(20,32),(32,31),(35,28),(40,15),(48,11),(51,12),(44,0),(40,-10),(35,-20),(32,-28),(25,-34),(18,-35),(14,-22),(12,-6),(9,4),(0,5),(-8,5)],[(-10,36),(-9,43),(-2,48),(0,50),(5,58),(10,60),(18,56),(21,55),(24,58),(28,60),(30,70),(40,68),(55,69),(70,72),(90,75),(110,76),(130,72),(150,70),(170,67),(178,65),(162,60),(158,52),(142,50),(140,40),(130,42),(127,35),(122,30),(120,22),(110,20),(105,10),(100,8),(95,15),(90,22),(80,15),(75,8),(72,20),(65,25),(58,25),(52,27),(48,30),(44,30),(40,36),(35,36),(30,36),(26,38),(22,40),(18,40),(12,44),(8,44),(3,43),(-2,37)],[(114,-22),(122,-14),(132,-12),(142,-11),(146,-19),(150,-23),(153,-27),(150,-37),(140,-38),(132,-32),(124,-33),(115,-35)],[(-45,60),(-30,68),(-20,70),(-40,75),(-55,72)]]
for poly in LAND: d.polygon([mp(lo,la) for lo,la in poly],fill=(205,220,185),outline=(90,110,80))
pins=[(1,24.7,46.7,0,0),(2,31.2,121.5,0,0),(3,40.7,-74.0,0,0),(4,47.8,35.2,0,0),(5,14.7,-17.4,0,0),(6,26.5,56.3,0,0),(7,40.7,-74.0,24,12),(8,47.67,-122.12,0,0),(9,39.8,30.5,0,0),(10,10.4,-75.5,0,0),(11,12.8,45.0,0,0),(12,13.0,44.9,18,12),(13,39.7,98.5,0,0)]
for n,la,lo,dx,dy in pins:
    x,y=mp(lo,la); px,py=x+dx,y+dy; d.line([(x,y),(px,py)],fill=RED,width=1) if (dx or dy) else None
    d.ellipse([px-9,py-9,px+9,py+9],fill=RED,outline=(255,255,255)); t=str(n); d.text((px-d.textlength(t,font=f_pin)/2,py-6),t,font=f_pin,fill=(255,255,255))
txt(MX+8,MY+MH-14,'Pins 1–13 = stories 1–13 above. Redmond (8) is on the US west coast; pins 3 and 7 share New York, offset with a leader line.',f_nlab,NAVY)
# ALSO 14-38
txt(12,778,'ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES',f_hkick,RED)
also=['14 Ankara: Haftar visits Turkey for the first time.','15 London: UK sanctions Houthis and four officials.','16 Villavicencio: Car bomb injures 23 people.','17 Gaza: Israel kills Hamas internal security chief.','18 Baghdad: Iraq orders federal control of Kurdish oilfields.','19 Gaza: Meningitis alert; 272 cases in October.','20 DR Congo: Missing Cessna 208; rebels claim shootdown.','21 Hanoi: Hot-pot explosion kills at least six.','22 Gulf of Finland: Ukraine hits ship Sparta II.','23 Kuala Lumpur: Malaysia to return migrants to Myanmar.','24 Ulleungdo: S. Korea shelter order as jets enter ADIZ.','25 Dhaka: Hasina plans return on 16 December.','26 The Hague: 14 nations endorse ICJ Myanmar ruling.','27 Jakarta: Indonesia nominates two VP candidates.','28 Beijing: China sentences official Ma to death for spying.','29 Brussels: NATO vows defence against space threat.','30 Mexico City: US drone aided capture; Mexico to try him.','31 San Salvador: Bukele names three soldiers killed in Haiti.','32 Ottawa: Pentagon rebukes Canada; only 41.9% of air fleet ready.','33 Washington: US adds Megaspeed to trade blacklist.','34 Kyiv: Zelensky urges Ukraine/Russia/US/Europe talks soon.','35 Ras Al Khaimah: UAE bus-truck crash kills 13.','36 London: England record 5,258 heat deaths, summer 2026.','37 Kourou: Ariane 6 lofts 36 Amazon satellites.','38 Cikande: Factory-fire toll rises to 26.']
for i,s in enumerate(also): txt(12+(i//9)*336,794+(i%9)*15,s,f_also)
# DATE CHECK + FOOTER
d.rectangle([12,936,1012,994],fill=(255,235,235),outline=RED); txt(18,940,'DATE CHECK',f_hkick,RED); _y=954
for _s in ['Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.','LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Huang returns as Nvidia CEO (23 Nov) · EU sanctions package 22 (23 Nov) · COP31 ends with no deal (22 Nov) · Merkury sinks (22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande fire starts (Sat 21 Nov) · Trump hush-money appeal ruling (23 Nov).','NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns (16 Dec).']:
    for _ln in wrap(_s,f_date,976): txt(18,_y,_ln,f_date); _y+=11
txt(12,998,'Sources: dailysummaryof.com · Astrova News · Horizon · WSOC/AP · Reuters. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one party claim. Scenes are drawn illustrations, not photographs.',f_foot,GREY)
os.makedirs(os.path.dirname(OUT),exist_ok=True); img.save(OUT)
print('saved',OUT,os.path.getsize(OUT))
