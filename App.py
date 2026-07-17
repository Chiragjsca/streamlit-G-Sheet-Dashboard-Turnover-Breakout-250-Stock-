Kz='#6a1b9a'
Ky='#f3e5f5'
Kx='#2e7d32'
Kw='#3949ab'
Kv='#e8eaf6'
Ku='180 Days'
Kt='90 Days'
Ks='Newest First'
Kr='Today Only'
Kq='Past 7 Days'
Kp='540222'
Ko='532480'
Kn='532209'
Km='513377'
Kl='500420'
Kk='540175'
Kj='502525'
Ki='500260'
Kh='508869'
Kg='532488'
Kf='524715'
Ke='500209'
Kd='DALMIA'
Kc='APOLLOHOSP'
Kb='SUNPHARMA'
Ka='lower limit'
KZ='upper limit'
KY='title_raw'
KX="\n            function(params) {\n                let v = String(params.value).toLowerCase();\n                if (v.includes('strong uptrend') || v.includes('bullish') || v.includes('strong buy')) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (v.includes('uptrend') || v.includes('buy') || v.includes('high') || v.includes('yes')) return { 'backgroundColor': '#a5d6a733', 'color': '#000' };\n                if (v.includes('sideways') || v.includes('watch') || v.includes('normal')) return { 'backgroundColor': '#f4b40033', 'color': '#000' };\n                if (v.includes('bearish') || v.includes('avoid') || v.includes('low') || v.includes('downtrend')) return { 'backgroundColor': '#ea433533', 'color': '#000' };\n                return null;\n            }\n            "
KW="\n            function(params) {\n                let val = parseFloat(params.value);\n                if (val >= 75) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 55) return { 'backgroundColor': '#f4b40033', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 35) return { 'backgroundColor': '#ff990033', 'color': '#000' };\n                return { 'backgroundColor': '#ea433533', 'color': '#000' };\n            }\n            "
KV='Automatically adjust column widths based on text length of the selected row.'
KU=' (100%)'
KT='Other Assets (unspecified)'
KS='Cash & Equivalents'
KR='#00897b'
KQ='Trade Receivables'
KP='Inventory'
KO='#5e35b1'
KN='Fixed Assets / Net PPE'
KM='#5c6bc0'
KL='#8d6e63'
KK='Trade Payables'
KJ='Total Debt'
KI='Reserves'
KH='Equity Capital'
KG='gauge+number'
KF='institutional'
KE='institutional %'
KD='delivery %'
KC='% delivery'
KB='Last Close'
KA='rgba(0,0,0,0.08)'
K9='RSI(14)'
K8='system-ui, sans-serif'
K7='rgba(0,0,0,0.06)'
K6='#31333F'
K5='tonexty'
K4='circle'
K3='#EF6C00'
K2='top right'
K1='#7C3AED'
K0='#FFD600'
J_='Candle'
Jz='%d %b %Y %H:%M'
Jy='⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.'
Jx='stock name'
Jw='company name'
Jv='Type symbol name...'
Ju='Search symbol:'
Jt='Stocks'
Js='%{customdata}: %{y:.2f}%<extra></extra>'
Jr='displaylogo'
Jq='#e3f2fd'
Jp='close price'
Jo='%Y%m%d_%H%M'
Jn='52w low date'
Jm='52w high date'
Jl='Market Cap'
Jk='RONW %'
Jj='Face Value'
Ji='Institutional %'
Jh='Promoters %'
Jg='50 DMA < 200 DMA'
Jf='50 DMA > 200 DMA'
Je='50 DMA > 100 DMA > 200 DMA'
Jd='50 DMA < 100 DMA < 200 DMA'
Jc='All (No Filter)'
Jb='macd crossover'
Ja='start gtt order'
JZ='output'
JY='🎨 Custom Hex: '
JX='#ff9900'
JW='#f4b400'
JV='bf_search'
JU='perf_matrix_search'
JT='main_matrix_search'
JS='search_query'
JR='50 dma'
JQ='d/e ratio'
JP='52w low'
JO='turn_val'
JN='turnover_actual'
JM='most_active'
JL='official nse'
JK='market smith'
JJ='chartlink'
JI='zerodha'
JH='screener'
JG='history data'
JF='trading view'
JE='1OvX7BdWiqejOmOsSiMogC2ni-b7irWch4TC2HqR_93c'
JD='https://www.googleapis.com/auth/drive'
JC='https://spreadsheets.google.com/feeds'
JB="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
JA='Output'
J9='Price %'
J8='GROQ_API_KEY'
J7='GEMINI_API_KEY'
Gn='concalls'
Gm='credit_ratings'
Gl='annual_reports'
Gk='announcements'
Gj='1 Year'
Gi='30 Days'
Gh='total assets'
Gg='net ppe'
Gf='fixed assets'
Ge='trade payables'
Gd='trade receivables'
Gc='cash equivalent'
Gb='cash and equiv'
Ga='cash & equiv'
GZ='inventory'
GY='total debt'
GX='reserves'
GW='total equity capital'
GV='Sector'
GU='rgba(0,0,0,0.3)'
GT='#FF5252'
GS='#00E676'
GR='type'
GQ='#D50000'
GP='#00C853'
GO='🚨 **[ALERT]** '
GN='Recent'
GM='Grade'
GL='Strategy'
GK='% Gain'
GJ='Target'
GI='last_pine_result'
GH='last_ai_result'
GG='100%'
GF='streamlit'
GE='Default'
GD='📏 Column Width Adjustment:'
GC='Difference from 200 DMA column not detected for this sheet.'
GB='#fff8e1'
GA='#1b5e20'
G9='market cap'
G8='volume'
G7='buy signal'
G6='trend'
G5='breakout signal'
G4='volume trend'
G3='industry'
G2='52w_low'
G1='52w_high'
G0='Watchlist'
F_='pledged'
Fz='pledged %'
Fy='promoter'
Fx='promoters %'
Fw='200 dma'
Fv='#ef5350'
Fu='Error'
Ft='Loading...'
Fs='⚡ Groq (Fast)'
Fr=getattr
Fq=TypeError
ET='ppt'
ES='#9e9e9e'
ER='#FFFFFF'
EQ='system-ui, -apple-system, sans-serif'
EP='skip'
EO='lines'
EN='Low'
EM='High'
EL='locked in circuit'
EK='hits circuit'
EJ='lower circuit'
EI='upper circuit'
EH='52-week low'
EG='52-week high'
EF='%d %b %Y'
EE='Use Case'
ED='% Risk'
EC='Type'
EB='model'
EA='markers'
E9='dash'
E8='52'
E7='sector'
E6='atr_approx'
E5='Added On'
E4='BF Grade'
E3='delivery'
E2='net sales'
E1='net profit'
E0='Turnover_Actual'
D_='Pct_Change'
Dz='value'
Dy='stock'
Dx='stock symbol'
Dw='ticker'
Dv='<[^>]*>'
Du='gcp_service_account'
Dt='No Data'
Ds=range
Dr=enumerate
DG='#c62828'
DF='dot'
DE='Volume'
DD='.//item'
DC='result'
DB='sym'
DA='left'
D9='% Diff from 200 DMA'
D8='N/A'
D7='#b71c1c'
D6='openpyxl'
D5='trail_sl_50dma'
D4='52 week high'
D3='added'
D2='BF Score'
D1='Note'
D0='price %'
C_='id'
Cz='nse code'
Cy='#ffffff'
Cx='</div>'
Cw='#66bb6a'
Ca='#37474f'
CZ='Mozilla/5.0'
CY='User-Agent'
CX='✅✅ Fit to Row 2'
CW='✅ Fit to Row 1'
CV='<br>'
CU='#e8f5e9'
CT='bf_score'
CS='52 week low'
CR='Value'
CQ='%Y-%m-%d %H:%M:%S'
CP='-%'
CO='+%'
CN='Diff @ 200 DMA'
CM='Final List 2'
CL='Final List'
Bw='rgba(0,0,0,0.2)'
Bv='Arial Black, Arial, sans-serif'
Bu='snap'
Bt='Buy Signal'
Bs='MACD Crossover'
Br='Trend'
Bq='Breakout Signal'
Bp='Volume Trend'
Bo='_'
Bn='📱 If frame is blank on mobile, tap the link above to open directly.'
Bm='#ffebee'
Bl='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
Bk='%Y%m%d'
Bj='bf_grade'
BM='UTC'
BL='RSI (14)'
BK='Price (₹)'
BJ='date'
BI='note'
BH='[%,]'
BG='Close'
BF='NSE Fundamentals'
BE='Top 250 Stocks'
B2='Diff. from 200 DMA'
B1='gray'
B0='#f9a825'
A_='price'
Az=isinstance
As='#0a1758'
Ar='pubDate'
Aq=1.
Ap='turnover'
Ao='52W Low'
An='52W High'
Am='% Delivery'
Ag='sec'
Af='hour'
Ae='min'
Ad='#16e37f'
Ac='symbol'
Ab='_txt_'
Aa='_bg_'
AZ=any
AY=ValueError
AR='bold'
AQ='normal'
AP='#ea4335'
AO='None'
AN='coerce'
AM='CMP'
AL=list
AI='timestamp'
AH='Just now'
AE='#1565C0'
AD='display_title'
AC='%'
AB=','
AA=max
A5='title'
A4='cmp'
A3='nan'
A2='Turnover'
x='change'
w='#0f9d58'
q='plotly_white'
n='_raw_symbol_'
k='-'
j='Symbol'
i=.0
g=Exception
f='link'
c='---'
b=round
U=int
S=next
Q=len
M=float
L='time_ago'
J=False
G=str
E=dict
D=None
C=''
B=True
import streamlit as A,pandas as H,numpy as A6,gspread as EU
from google.oauth2.service_account import Credentials as Go
from google.auth.transport.requests import AuthorizedSession as K_
import json as EV,urllib.parse
from datetime import datetime as l
from st_aggrid import AgGrid as EW,GridOptionsBuilder as EX,JsCode as B3
from st_aggrid.shared import GridUpdateMode as L0
import streamlit.components.v1 as O,re,io,google.generativeai as Gp,plotly.graph_objects as P
from plotly.subplots import make_subplots as L1
A.set_page_config(page_title='Top 250 NSE Stock-Turnover Breakout Dashboard',layout='wide',page_icon='📊')
if hasattr(A,'fragment'):DH=A.fragment
elif hasattr(A,'experimental_fragment'):DH=A.experimental_fragment
else:
	def DH(func=D,**B):
		if func is not D:return func
		def A(f):return f
		return A
A.markdown('\n<style>\n    /* Force EVERY tab-bar container to wrap onto multiple lines instead of\n       staying on one scrollable line. Multiple selector variants are used\n       (data-baseweb, role, and Streamlit\'s own class) because Streamlit\'s\n       internal DOM/class names have changed across versions. */\n    div[data-testid="stTabs"],\n    div[data-testid="stTabs"] > div,\n    .stTabs,\n    .stTabs > div {\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        max-width: 100% !important;\n    }\n\n    div[data-baseweb="tab-list"],\n    div[role="tablist"] {\n        display: flex !important;\n        flex-wrap: wrap !important;\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        white-space: normal !important;\n        row-gap: 4px !important;\n        column-gap: 6px !important;\n        height: auto !important;\n        max-width: 100% !important;\n        width: 100% !important;\n        scrollbar-width: none !important;\n    }\n    div[data-baseweb="tab-list"]::-webkit-scrollbar {\n        display: none !important;\n    }\n\n    /* Each tab button: allow shrinking/wrapping instead of forcing one line */\n    button[data-baseweb="tab"],\n    div[role="tablist"] > button,\n    div[role="tablist"] [role="tab"] {\n        flex: 0 0 auto !important;\n        white-space: normal !important;\n        margin-top: 1px !important;\n        margin-bottom: 1px !important;\n        padding-top: 6px !important;\n        padding-bottom: 6px !important;\n        height: auto !important;\n    }\n\n    /* Hide the "‹ ›" scroll-arrow buttons Streamlit shows when a tab bar overflows */\n    button[data-testid="stTabsScrollButton"],\n    div[data-baseweb="tab-list"] ~ button,\n    div[data-baseweb="tab-list"] + button,\n    button[kind="tabScroll"],\n    button[aria-label*="scroll" i] {\n        display: none !important;\n    }\n\n    div[data-baseweb="tab-highlight"] {\n        display: none !important;\n    }\n    div[data-baseweb="tab"][aria-selected="true"],\n    [role="tab"][aria-selected="true"] {\n        background-color: rgba(31, 119, 180, 0.1) !important;\n        border-radius: 5px !important;\n        border-bottom: 2px solid #1f77b4 !important;\n    }\n</style>\n',unsafe_allow_html=B)
Cb=J
BN=J
if J7 in A.secrets:Gp.configure(api_key=A.secrets[J7]);Cb=B
if J8 in A.secrets:
	try:from groq import Groq as L2;L3=L2(api_key=A.secrets[J8]);BN=B
	except ImportError:BN=J
EY=Cb or BN
def EZ(prompt,model_choice):
	A=prompt
	if model_choice==Fs and BN:B=L3.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{'role':'user','content':A}],max_tokens=2048);return B.choices[0].message.content
	elif Cb:C=Gp.GenerativeModel('gemini-2.5-flash');return C.generate_content(A).text
	else:raise RuntimeError('No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.')
def Ea(key_suffix=C):
	D='🧠 Gemini';C,E=[],0
	if BN:C.append(Fs)
	if Cb:C.append(D)
	if not C:C=[Fs,D]
	return A.radio('🤖 AI Model:',C,index=0,horizontal=B,key=f"ai_model_sel_{key_suffix}")
L4=['Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.','Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.','Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.','Using the turnover data for {sym}, identify if there is unusual turnover activity. Does the current turnover indicate institutional buying, selling, or accumulation? What does it signal?','Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?','What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?',"Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",'Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.','Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?',"Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?"]
L5="Strategy 1 — Turnover Breakout with Dynamic Stop Loss\n  Rule 1: Enter long when today's turnover > 2× the 20-day average turnover AND price closes above the prior day's high; set stop loss at 1.5× ATR below entry price.\n  Rule 2: Add a false breakout filter — price must hold above the breakout level for 2 consecutive candles before confirming entry; trail stop at the lowest low of the last 3 bars.\n  Rule 3: Set profit target at 2:1 risk-reward ratio; plot a turnover histogram overlay to identify surge bars visually; include an alert condition for live breakout detection.\n\nStrategy 2 — Moving Average Crossover (50/100/200 DMA)\n  Rule 4: Buy when 50 DMA crosses above 100 DMA with price trading above the 200 DMA; exit when 50 DMA crosses back below 100 DMA; use 200 DMA as the hard stop-loss floor.\n  Rule 5: Add RSI confirmation — only enter when RSI is between 50–70 at the crossover candle; plot all three DMAs on the chart with distinct colours for visual clarity.\n  Rule 6: Allow a re-entry if 50 DMA pulls back to 100 DMA without breaking below 200 DMA; set stop loss 2% below the 50 DMA value at the time of entry.\n\nStrategy 3 — Trend Following with Trailing Stop\n  Rule 7: Enter long when price breaks a 20-day high with above-average turnover and ADX > 25; apply a Chandelier Exit trailing stop set at 3× ATR from the highest close after entry.\n  Rule 8: Use 200 DMA direction as the trend filter — only take long trades when price is above 200 DMA; tighten trailing stop to 2× ATR once profit exceeds 10% from entry.\n  Rule 9: Add a re-entry condition: if stopped out but price remains above 200 DMA, re-enter on the next pullback to the 50 DMA; limit to a maximum of 2 re-entries per trend leg.\n\nStrategy 4 — Mean Reversion from 52W High/Low\n  Rule 10: Buy when price is within 15% of the 52-week low AND RSI < 35; set profit target at the 52-week midpoint; place hard stop loss 5% below the 52-week low level.\n  Rule 11: Exit/short signal when price is within 5% of the 52-week high with RSI > 70; use Bollinger Band upper band touch as secondary confirmation; target the middle Bollinger Band as exit.\n  Rule 12: Apply a turnover reversal filter — only enter when the reversal candle's turnover is ≥ 1.5× the 20-day average; plot the 52-week high and low as horizontal reference lines on the chart."
L6='\n### 💡 Core Rules\n- **Sheet Convention:** Always use **NSE Code** instead of *Symbol* in the Google Sheet — this keeps NSE chart links working correctly.\n- **No Compromise:** Follow the Rules. Never compromise on Rules — Rules are better than any single Buy/Sell decision.\n- **Timing Edge:** Take advantage of time — buy when a stock is at its lower end (near 52W Low) and sell at a higher price when momentum kicks in (e.g. an Upper Circuit move).\n\n---\n\n### 🟢 Rule 1 — Near 52 Week High\nCMP / Close Price is highlighted **Green** when it is near the 52-Week High (within ~8%).\n\n### 🟠 Rule 2 — Near 52 Week Low (Buy Zone)\nCMP / Close Price is highlighted **Orange** when it is near the 52-Week Low (within ~8%) — **this is the type of stock to look at buying.**\n\n**52W Low / High Date column — color meaning:**\n| Signal | Meaning |\n|---|---|\n| 🟢 Green in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 18 days** |\n| 🟢 Green in *52 Week High Date* | Stock touched its 52-Week High within the **last 18 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 30 days** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High within the **last 30 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low **about 1 year ago** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High **about 1 year ago** |\n\n### 🔵 Rule 3 — Diff @ 200 DMA Strategy\nOnly buy **52-Week Low** stocks, ranked by the **Difference from 200 DMA** column on the **Diff @ 200 DMA** tab — biggest fall first.\n\n**Path:**\n1. Open the **Diff @ 200 DMA** tab (Main sheet).\n2. Refer to the **Difference from 200 DMA** column.\n3. Sort results **−40% → −30% → −20% → −10%** (most negative first).\n\n**Mind Map:**\n```\nRule 3 → Buy Only 52-Week Low Stocks\n│\n├── Main Sheet → Open Tab "Diff @ 200 DMA"\n├── Check Column → "Difference from 200 DMA"\n├── Sort Logic → Biggest Fall First (-40% → -30% → -20% → -10%)\n├── Meaning → Stock is trading below its 200 DMA\n├── Priority → More negative % = higher priority\n├── Selection Criteria\n│     ├── Only 52-Week Low stocks\n│     ├── Negative Difference from 200 DMA\n│     └── Deep-discount stocks preferred\n└── Final Action → Analyze & buy quality stocks\n```\n\n---\n\n### 🔗 Useful NSE Reference Links\n- **All Reports (Bhavcopy / Market Activity):** Bhavcopy (PR)(zip), Market Activity Report (csv), Full Bhavcopy & security delivery data, MCAP, PD, PR, SME → https://www.nseindia.com/all-reports/\n- **Securities Available for Trading** (ETF, Close-Ended MF Schemes, SME) → https://www.nseindia.com/static/market-data/securities-available-for-trading\n- **52-Week Low — Equity Market** → https://www.nseindia.com/market-data/52-week-low-equity-market#capital_market_link\n\n---\n\n### 🛑 Risk Management — No Compromise\n- **Stop Loss (Max 1–2%), no compromise.** બીજો chance મળશે કમાવાનો — પૈસા 10% ઓછા થયા તો 15% કમાવા પડશે.\n- **Risk-Reward Ratio:** max 5 trades, max 10% loss — never lose all your money in a single trade.\n- **Target / Profit Booking:** Max 10–20%.\n- Don\'t trade emotionally — the share market is a mind game.\n- Know everything related to a share before moving ahead.\n- Stay calm, serious, and stick to the decision you\'ve made.\n- **Clear Vision, no compromise:** Focus → Stop Loss → Risk-Reward Ratio → Target/Profit → 52-Week Low Buy.\n- **Priority order:** IPO → F&O → 52-Week Low Shares.\n'
L7={BE:['50 DMA','100 DMA','200 DMA','NSE 1','Trading View 1','History Data 1','Screener 1','Zerodha 1','Chartlink 1','Market smith india 1','Official NSE URL 1'],BF:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
L8={BE:['E','F','G','AA','AB','AC','AD','AE','AF','AG','AH'],BF:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
def Gq(letter):
	A=letter;A=G(A).strip().upper()
	if not A or not A.isalpha():return-1
	B=0
	for C in A:B=B*26+(ord(C)-ord('A')+1)
	return B-1
def L9(sheet_name,ordered_columns):
	C=sheet_name;A=ordered_columns;A=AL(A);B=set()
	for D in L7.get(C,[]):
		if D in A:B.add(D)
	for F in L8.get(C,[]):
		E=Gq(F)
		if 0<=E<Q(A):B.add(A[E])
	return B
LA={BE:D,BF:D,CL:D,CM:D,CN:D,CO:D,CP:D}
LB={BE:[A2,Am,'Close Price',AM,J9,An,Ao,JA,'Differance from 200 DMA','Cumulative Average Rule (CAR) Rating'],BF:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
LC={BE:['B','C','D','L'],BF:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
def LD(sheet_name,ordered_columns):
	D=sheet_name;A=ordered_columns;A=AL(A);B=[]
	for G in LC.get(D,[]):
		E=Gq(G)
		if 0<=E<Q(A):
			F=A[E]
			if F not in B:B.append(F)
	for C in LB.get(D,[]):
		if C in A and C not in B:B.append(C)
	return B
import streamlit as A
LE='\n<style>\n    #MainMenu {visibility: show;}\n    header {visibility: show;}\n    [data-testid="stToolbar"] {visibility: show;}\n    footer {visibility: show;}\n</style>\n'
A.markdown(LE,unsafe_allow_html=B)
import streamlit as A
LF='\n<style>\n    [data-testid="stToolbar"] {\n        right: 2rem;\n    }\n    [data-testid="stToolbar"]::before {\n        content: "";\n    }\n    button[kind="header"] {display: none;}\n</style>\n'
A.markdown(LF,unsafe_allow_html=B)
LG='romo'
if'logged_in'not in A.session_state:A.session_state.logged_in=J
if'watchlist'not in A.session_state:A.session_state.watchlist={}
if'ai_history'not in A.session_state:A.session_state.ai_history=[]
if'grid_reset_token'not in A.session_state:A.session_state.grid_reset_token=0
if not A.session_state.logged_in:
	A.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>250-T Dashboard</p>",unsafe_allow_html=B);A.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>",unsafe_allow_html=B);Os,LH,Ot=A.columns([1,1,1])
	with LH:
		with A.form('login_form'):
			LI=A.text_input('Enter Password',type='password');LJ=A.form_submit_button('Login',use_container_width=B)
			if LJ:
				if LI==LG:A.session_state.logged_in=B;A.rerun()
				else:import random;LK=['Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!','❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!','❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!','❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!','❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!'];A.error(random.choice(LK))
	LL=l.now().strftime(CQ);A.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {LL}</p>",unsafe_allow_html=B);A.stop()
A.markdown('\n<style>\n    /* Reduce ALL headings to 90% smaller size */\n    h1, h2, h3, h4, h5, h6, .stSubheader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {\n        font-size: 0.85rem !important;\n        font-weight: bold !important;\n        margin-top: 0.5rem !important;\n        margin-bottom: 0.5rem !important;\n    }\n</style>\n',unsafe_allow_html=B)
import yfinance as Gr,streamlit as A
from datetime import datetime as l
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Turnover Breakout Dashboard</p>",unsafe_allow_html=B)
A.caption(f"Data refreshed: {l.now().strftime(CQ)}")
@A.cache_data(ttl=60)
def LM():
	A='UNSUPPORTED';H={'NIFTY 50':'^NSEI','NIFTY NEXT 50':'^NN50','NIFTY MIDCAP 50':'^NSEMDCP50','NIFTY MIDCAP 100':'^CRSLMID','NIFTY MIDCAP 150':A,'NIFTY SMLCAP 50':A,'NIFTY SMLCAP 100':A,'NIFTY SMLCAP 250':A,'NIFTY MIDSML 400':A,'NIFTY 100':'^CNX100','NIFTY 200':'^CNX200','NIFTY500 MULTI...':A,'NIFTY LARGEMID...':A,'NIFTY MID SELE...':A,'NIFTY TOTAL MK...':A,'NIFTY MICROCAP...':A,'NIFTY 500':'^CRSLDX','NIFTY FPI 150':A,'NIFTY500 LMS E...':A,'NIFTY MIDSMALL...':A,'NIFTY SMALLCAP...':A};B={}
	for(C,E)in H.items():
		if E==A:B[C]={A_:Dt,x:i};continue
		try:
			I=Gr.Ticker(E);D=I.history(period='5d')
			if not D.empty and Q(D)>=2:F=M(D[BG].iloc[-1]);G=M(D[BG].iloc[-2]);J=(F-G)/G*100;B[C]={A_:f"{F:,.2f}",x:J}
			else:B[C]={A_:Ft,x:i}
		except g:B[C]={A_:Fu,x:i}
	return B
LN=LM()
At=JB
Gs=0
for(Bx,AS)in LN.items():
	if AS[A_]in[Dt,Ft,Fu]:continue
	Gs+=1;Eb=Cw if AS[x]>=0 else Fv;Ec='+'if AS[x]>=0 else C;LO='https://www.nseindia.com/market-data/live-market-indices';At+=f"<a href='{LO}' target='_blank' style='text-decoration:none;'>";At+=f"<div style='background-color: {Eb}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";At+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bx}</div>";At+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";At+=f"<span style='font-size: 15px; font-weight: 700;'>{AS[A_]}</span>";At+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Ec}{AS[x]:.2f}%</span>";At+=f"</div></div></a>"
At+=Cx
with A.expander('📈 Click to view Live Market Indices',expanded=J):
	if Gs==0:A.info('Market data is currently unavailable. Please check back later.')
	else:A.markdown(At,unsafe_allow_html=B)
A.write(c)
def Gt(color_dict):
	A=color_dict
	if not A:return Cy
	B,C,D=U(A.get('red',0)*255),U(A.get('green',0)*255),U(A.get('blue',0)*255);return f"#{B:02x}{C:02x}{D:02x}"
@A.cache_data(ttl=300,show_spinner=J)
def LP(nse_symbol,period='1y'):
	try:
		C=G(nse_symbol).strip().upper()
		if not C:return H.DataFrame()
		E=C if C.endswith('.NS')else f"{C}.NS";A=Gr.download(E,period=period,interval='1d',progress=J,auto_adjust=B)
		if A is D or A.empty:return H.DataFrame()
		if Az(A.columns,H.MultiIndex):A.columns=A.columns.get_level_values(0)
		A.index=H.to_datetime(A.index);return A
	except g:return H.DataFrame()
@A.cache_data(ttl=300)
def DI(sheet_name):
	M='sheets'
	try:
		if Du not in A.secrets:A.error("Missing 'gcp_service_account' in secrets.");return H.DataFrame()
		D=A.secrets[Du]
		if Az(D,G):D=EV.loads(D)
		Y=[JC,JD];N=Go.from_service_account_info(D,scopes=Y);j=EU.authorize(N);Z=JE;a=urllib.parse.quote(sheet_name);b=K_(N);c=f"https://sheets.googleapis.com/v4/spreadsheets/{Z}?includeGridData=true&ranges={a}";d=b.get(c);E=d.json()
		if'error'in E:return H.DataFrame()
		if M not in E or not E[M]:return H.DataFrame()
		e=E[M][0]['data'][0];O=e.get('rowData',[])
		if not O:return H.DataFrame()
		J,P,R=[],[],[]
		for f in O:
			h=f.get('values',[]);S,T,U=[],[],[]
			for V in h:S.append(V.get('formattedValue',C));W=V.get('effectiveFormat',{});T.append(Gt(W.get('backgroundColor',{})));U.append(Gt(W.get('textFormat',{}).get('foregroundColor',{})))
			J.append(S);P.append(T);R.append(U)
		i=J[0];K=[];F={}
		for B in i:
			B=G(B).strip()
			if B==C:B='empty_column'
			if B in F:F[B]+=1;B=f"{B}_{F[B]}"
			else:F[B]=0
			K.append(B)
		L=H.DataFrame(J[1:],columns=K)
		for(I,X)in Dr(K):L[f"_bg_{X}"]=[A[I]if I<Q(A)else Cy for A in P[1:]];L[f"_txt_{X}"]=[A[I]if I<Q(A)else'#000000'for A in R[1:]]
		return L
	except g as k:return H.DataFrame()
def LQ(df,symbol_col):
	K=symbol_col;H='1';F='🔗 Link';I=df.copy();I[n]=I[K]
	for(L,M)in I.iterrows():
		A=G(M[n]).strip()
		if not A or A==A3:continue
		for J in I.columns:
			if J.startswith(Aa)or J.startswith(Ab)or J==n:continue
			B=J.lower();C,E=D,F
			if JF in B:C,E=f"https://www.tradingview.com/symbols/{A}/",f"Tre {A}"if not B.endswith(H)else F
			elif JG in B:C,E=f"https://www.equitypandit.com/historical-data/{A}",f"History {A}"if not B.endswith(H)else F
			elif JH in B:C,E=f"https://www.screener.in/company/{A}",f"Scr {A}"if not B.endswith(H)else F
			elif JI in B:C,E=f"https://zerodha.com/markets/stocks/NSE/{A}",f"🪁 {A}"if not B.endswith(H)else F
			elif JJ in B:C,E=f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={A}",f"CL {A}"if not B.endswith(H)else F
			elif JK in B:C,E=f"https://marketsmithindia.com/mstool/eval/{A}/evaluation.jsp",f"ms {A}"if not B.endswith(H)else F
			elif JL in B:C,E=f"https://www.nseindia.com/get-quotes/equity?symbol={A}",f"nse📰 {A}"if not B.endswith(H)else F
			elif'nse'in B or J==K:C,E=f"https://charting.nseindia.com/?symbol={A}-EQ",A if not B.endswith(H)else F
			if C:I.at[L,J]=f'<a href="{C}" target="_blank" style="text-decoration:none; color:#000000;">{E}</a>'
	return I
def DJ(df,col_name,st_container,display_label=D):
	J=display_label;D=col_name
	if D in df.columns:
		A=df[D].astype(G).str.replace(BH,C,regex=B);A=H.to_numeric(A,errors=AN).replace([A6.inf,-A6.inf],A6.nan);E=A.dropna()
		if not E.empty:
			F,I=b(M(E.min()),2),b(M(E.max()),2)
			if F<I:L=J if J else f"{D} Range:";K=st_container.slider(L,min_value=F,max_value=I,value=(F,I),key=f"filter_num_{D}");return df[(A>=K[0])&(A<=K[1])]
	return df
def Gu(df,col_name,st_container):
	Q='Past 1 Year';P='Past 6 Months';O='Past 2 Months';N='Past 1 Month';M='Past 30 Days';L='Past 25 Days';K='Past 20 Days';J='Past 15 Days';I='Past 10 Days';G='Past 5 Days';F='All Time';E=col_name
	if E in df.columns:
		R=[F,G,I,J,K,L,M,N,O,P,Q];A=st_container.selectbox(f"{E}:",R,key=f"filter_date_{E}")
		if A!=F:
			S=H.to_datetime(df[E],errors=AN,dayfirst=B);C=H.Timestamp.now()
			if A==G:D=C-H.Timedelta(days=5)
			elif A==I:D=C-H.Timedelta(days=10)
			elif A==J:D=C-H.Timedelta(days=15)
			elif A==K:D=C-H.Timedelta(days=20)
			elif A==L:D=C-H.Timedelta(days=25)
			elif A==M:D=C-H.Timedelta(days=30)
			elif A==N:D=C-H.DateOffset(months=1)
			elif A==O:D=C-H.DateOffset(months=2)
			elif A==P:D=C-H.DateOffset(months=6)
			elif A==Q:D=C-H.DateOffset(years=1)
			return df[S>=D]
	return df
def By(val):
	if H.isna(val):return 0
	A=re.sub(Dv,C,G(val));return Q(A)
def Gv(df):
	A=df.copy();D=[A for A in A.columns if A.startswith(Aa)or A.startswith(Ab)or A==n];A=A.drop(columns=D,errors='ignore')
	for B in A.select_dtypes(include=['object']).columns:A[B]=A[B].apply(lambda x:re.sub(Dv,C,G(x))if H.notnull(x)else x)
	return A
import streamlit.components.v1 as O
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>",unsafe_allow_html=B)
A.caption('Live market data covering 2,000+ equities. Powered by TradingView.')
with A.expander('🏆 Click to view Full-Market India Rankings',expanded=J):
	LR,LS,LT,LU,LV,LW=A.tabs(['🚀 Gainers & Losers','📦 Volume & Active','📦 Turnover & Active','⭐ 52W High / Low','🔄 52W Reversals','📊 Top 100 Traded'])
	def AT(screen_type):return f'''
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
          {{
          "width": "100%",
          "height": "500",
          "defaultColumn": "overview",
          "defaultScreen": "{screen_type}",
          "market": "india",
          "showToolbar": true,
          "colorTheme": "light",
          "locale": "en"
        }}
          </script>
        </div>
        '''
	with LR:
		AU,AV=A.columns(2)
		with AU:A.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>",unsafe_allow_html=B);O.html(AT('top_gainers'),height=520)
		with AV:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>",unsafe_allow_html=B);O.html(AT('top_losers'),height=520)
	with LS:
		AU,AV=A.columns(2)
		with AU:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>",unsafe_allow_html=B);O.html(AT('volume_leaders'),height=520)
		with AV:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>",unsafe_allow_html=B);O.html(AT(JM),height=520)
	with LT:
		AU,AV=A.columns(2)
		with AU:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Turnover Leaders</p>",unsafe_allow_html=B);O.html(AT('turnover_leaders'),height=520)
		with AV:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Turnover & Value)</p>",unsafe_allow_html=B);O.html(AT(JM),height=520)
	with LU:
		AU,AV=A.columns(2)
		with AU:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>",unsafe_allow_html=B);O.html(AT('new_52wk_high'),height=520)
		with AV:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>",unsafe_allow_html=B);O.html(AT('new_52wk_low'),height=520)
	with LV:
		AU,AV=A.columns(2)
		with AU:A.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>",unsafe_allow_html=B);O.html(AT('outperforming_52wk_high'),height=520)
		with AV:A.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>",unsafe_allow_html=B);O.html(AT('underperforming_52wk_low'),height=520)
	with LW:A.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>",unsafe_allow_html=B);O.html(AT('general'),height=520)
A.write(c)
@A.cache_data(ttl=300)
def LX():
	B=DI(BE);A={}
	if B.empty:return A
	E=[A for A in B.columns if not A.startswith(Aa)and not A.startswith(Ab)];I=S((A for A in E if A.lower()in[Cz,Ac,Dw,Dx,C_,Dy]),D);J=S((A for A in E if A4 in A.lower()),D);K=S((A for A in E if D0 in A.lower()or x in A.lower()),D)
	if not I or not J:return A
	for(R,F)in B.iterrows():
		H=G(F.get(I,C)).strip()
		if not H or H==A3:continue
		O=G(F.get(J,C)).replace(AB,C).strip();P=G(F.get(K,'0')).replace(AC,C).replace(AB,C).strip()if K else'0'
		try:Q=M(O);L=f"{Q:,.2f}"
		except AY:L=Dt
		try:N=M(P)
		except AY:N=i
		A[H]={A_:L,x:N}
	return A
LY=LX()
Au=JB
Gw=0
for(Bx,AS)in LY.items():
	if AS[A_]in[Dt,Ft,Fu]:continue
	Gw+=1;Eb=Cw if AS[x]>=0 else Fv;Ec='+'if AS[x]>=0 else C;LZ=f"https://www.nseindia.com/get-quotes/equity?symbol={Bx}";Au+=f"<a href='{LZ}' target='_blank' style='text-decoration:none;'>";Au+=f"<div style='background-color: {Eb}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Au+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bx}</div>";Au+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Au+=f"<span style='font-size: 15px; font-weight: 700;'>{AS[A_]}</span>";Au+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Ec}{AS[x]:.2f}%</span>";Au+=f"</div></div></a>"
Au+=Cx
with A.expander('📈 Click to view Top 250 Stocks Matrix',expanded=J):
	if Gw==0:A.info("Stock matrix data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:A.markdown(Au,unsafe_allow_html=B)
A.write(c)
@A.cache_data(ttl=300)
def La():
	P='[a-zA-Z%, ]';E=DI(BE)
	if E.empty:return H.DataFrame()
	F=[A for A in E.columns if not A.startswith(Aa)and not A.startswith(Ab)];I=S((A for A in F if A.lower()in[Cz,Ac,Dw,Dx,C_,Dy]),D);J=S((A for A in F if A4 in A.lower()),D);K=S((A for A in F if D0 in A.lower()or x in A.lower()),D);L=S((A for A in F if Ap in A.lower()),D);M=S((A for A in F if Dz in A.lower()and'face'not in A.lower()and'enterprise'not in A.lower()),D);N=S((A for A in F if Ap in A.lower()),D)
	if not I:return H.DataFrame()
	A=H.DataFrame();A[j]=E[I].astype(G).str.strip();A[AM]=H.to_numeric(E[J].astype(G).str.replace(BH,C,regex=B),errors=AN)if J else i;A[D_]=H.to_numeric(E[K].astype(G).str.replace(BH,C,regex=B),errors=AN)if K else i;A[A2]=H.to_numeric(E[L].astype(G).str.replace(BH,C,regex=B),errors=AN)if L else i;O=A[AM]*A[A2]
	if M:A[CR]=H.to_numeric(E[M].astype(G).str.replace(P,C,regex=B),errors=AN)
	else:A[CR]=O
	if N:A[E0]=H.to_numeric(E[N].astype(G).str.replace(P,C,regex=B),errors=AN)
	else:A[E0]=O
	A=A.dropna(subset=[j,AM]).reset_index(drop=B);A=A[(A[j]!=A3)&(A[j]!=C)];return A
def B4(dataframe,metric_label=x):
	J=dataframe;G=metric_label;A="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
	if J.empty:return"<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
	for(R,B)in J.iterrows():
		K=B[j];L=B[AM];H=B[D_];M=Cw if H>=0 else Fv;N='+'if H>=0 else C
		if G==Ap:D=B.get(A2,0);F=f"Turn: {D/1000000:.1f}M"if D>=1000000 else f"Turn: {D:,.0f}"
		elif G==Dz:E=B.get(CR,0);F=f"Val: ₹{E/10000000:,.1f}Cr"if E>=10000000 else f"Val: ₹{E:,.0f}"
		elif G==JN:I=B.get(E0,0);F=f"T.O: ₹{I/10000000:,.1f}Cr"if I>=10000000 else f"T.O: ₹{I:,.0f}"
		elif G==JO:D=B.get(A2,0);E=B.get(CR,0);O=f"{D/1000000:.1f}M"if D>=1000000 else f"{D/1000:.1f}k";P=f"₹{E/10000000:,.1f}Cr"if E>=10000000 else f"₹{E:,.0f}";F=f"📦 {O} | 💰 {P}"
		else:F=f"{N}{H:.2f}%"
		Q=f"https://www.nseindia.com/get-quotes/equity?symbol={K}";A+=f"<a href='{Q}' target='_blank' style='text-decoration:none;'>";A+=f"<div style='background-color: {M}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";A+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{K}</div>";A+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";A+=f"<span style='font-size: 15px; font-weight: 700;'>{L:,.2f}</span>";A+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{F}</span>";A+=f"</div></div></a>"
	A+=Cx;return A
Ah=La()
with A.expander('🏆 Click to view Advanced Ranking Dashboards (Top 250 Stocks)',expanded=J):
	if Ah.empty:A.info("Ranking data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:
		Lb=Ah.nlargest(20,D_);Lc=Ah.nsmallest(20,D_);Ld=Ah.nlargest(20,A2);Le=Ah[Ah[A2]>0].nsmallest(20,A2);Lf=Ah.nlargest(20,A2);Lg=Ah.nlargest(20,CR);Lh=Ah.nlargest(20,E0);Li=Ah.nlargest(20,CR);Lj,Lk,Ll,Lm,Ln,Lo=A.tabs(['📈 Gainers/Losers','📦 Volume Leaders','🔥 Active (Vol & Val)','💰 Top by Value','💎 Top by Turnover','💰 Most Active'])
		with Lj:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>",unsafe_allow_html=B);A.markdown(B4(Lb,x),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>",unsafe_allow_html=B);A.markdown(B4(Lc,x),unsafe_allow_html=B)
		with Lk:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B4(Ld,Ap),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B4(Le,Ap),unsafe_allow_html=B)
		with Ll:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>",unsafe_allow_html=B);A.markdown(B4(Lf,JO),unsafe_allow_html=B)
		with Lm:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>",unsafe_allow_html=B);A.markdown(B4(Lg,Dz),unsafe_allow_html=B)
		with Ln:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>",unsafe_allow_html=B);A.markdown(B4(Lh,JN),unsafe_allow_html=B)
		with Lo:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>",unsafe_allow_html=B);A.markdown(B4(Li,Dz),unsafe_allow_html=B)
A.write(c)
def DK(row,actual_cols):
	B=0;A=[]
	def E(col_keywords,negate=J):
		for E in col_keywords:
			A=S((A for A in actual_cols if E.lower()in A.lower()),D)
			if A and A in row:
				try:B=M(G(row[A]).replace(AC,C).replace(AB,C).strip());return-B if negate else B
				except:pass
	N=E([A4]);Q=E([JP,CS,'52wlow'])
	if N and Q and Q>0:
		I=(N-Q)/Q*100
		if 8<=I<=15:B+=30;A.append(f"✅ CMP +{I:.1f}% from 52W Low (sweet zone)")
		elif I<8:B+=15;A.append(f"⚠️ CMP +{I:.1f}% from 52W Low (still bottoming)")
		elif I<=25:B+=10;A.append(f"🟡 CMP +{I:.1f}% from 52W Low (extended)")
		else:A.append(f"❌ CMP +{I:.1f}% from 52W Low (too far)")
	O=E([Fw])
	if N and O and O>0:
		if N>O:B+=15;A.append('✅ CMP above 200 DMA (uptrend confirmed)')
		else:
			U=(N-O)/O*100
			if U>-10:B+=7;A.append(f"🟡 CMP {U:.1f}% below 200 DMA (near support)")
			else:A.append(f"❌ CMP {U:.1f}% below 200 DMA (downtrend)")
	K=E([Ap])
	if K and K>0:
		if K>=10000000:B+=10;A.append(f"✅ High turnover: {K:,.0f}")
		elif K>=1000000:B+=6;A.append(f"🟡 Moderate turnover: {K:,.0f}")
		else:B+=2;A.append(f"⚠️ Low turnover: {K:,.0f}")
	F=E([JQ,'debt','d/e'])
	if F is not D:
		if F<=.1:B+=10;A.append(f"✅ Debt-Free / Zero Debt (D/E={F:.2f})")
		elif F<=.5:B+=7;A.append(f"✅ Very Low Debt (D/E={F:.2f})")
		elif F<=Aq:B+=4;A.append(f"🟡 Manageable Debt (D/E={F:.2f})")
		else:A.append(f"❌ High Debt (D/E={F:.2f})")
	R=E([E1])
	if R is not D:
		if R>0:B+=10;A.append(f"✅ Profitable: Net Profit ₹{R:.1f} Cr")
		else:A.append(f"❌ Loss Making: Net Profit ₹{R:.1f} Cr")
	H=E(['ronw'])
	if H is not D:
		if H>=15:B+=10;A.append(f"✅ Strong RONW: {H:.1f}%")
		elif H>=8:B+=6;A.append(f"🟡 Moderate RONW: {H:.1f}%")
		elif H>0:B+=2;A.append(f"⚠️ Low RONW: {H:.1f}%")
		else:A.append(f"❌ Negative RONW: {H:.1f}%")
	L=E([Fx,Fy])
	if L is not D:
		if L>=50:B+=8;A.append(f"✅ Promoter Holding: {L:.1f}%")
		elif L>=35:B+=5;A.append(f"🟡 Promoter Holding: {L:.1f}%")
		else:A.append(f"⚠️ Low Promoter: {L:.1f}%")
	P=E([Fz,F_])
	if P is not D:
		if P==0:B+=7;A.append('✅ Zero Pledged Shares')
		elif P<=5:B+=4;A.append(f"🟡 Low Pledge: {P:.1f}%")
		else:A.append(f"❌ High Pledge: {P:.1f}%")
	V=E([E2,'net sale'])
	if V and V>0:A.append(f"📊 Net Sales: ₹{V:.1f} Cr")
	W=E([E3])
	if W is not D:A.append(f"📦 % Delivery: {W:.1f}%")
	if B>=75:T='🟢 STRONG BUY'
	elif B>=55:T='🟡 WATCHLIST'
	elif B>=35:T='🟠 CAUTION'
	else:T='🔴 AVOID'
	return B,T,A
Gx=G0
def Gy():
	if Du not in A.secrets:return
	B=A.secrets[Du]
	if Az(B,G):B=EV.loads(B)
	C=[JC,JD];D=Go.from_service_account_info(B,scopes=C);return EU.authorize(D)
Lp=JE
def Gz(client):
	try:
		A=client.open_by_key(Lp)
		try:return A.worksheet(Gx)
		except EU.WorksheetNotFound:B=A.add_worksheet(title=Gx,rows=500,cols=6);B.append_row([j,AM,D1,D2,E4,E5]);return B
	except g:return
def Lq():
	D=Gy()
	if not D:return
	E=Gz(D)
	if not E:return
	try:
		I=E.get_all_records();F={}
		for B in I:
			H=G(B.get(j,C)).strip()
			if H:F[H]={BI:G(B.get(D1,C)),A4:G(B.get(AM,C)),CT:G(B.get(D2,C)),Bj:G(B.get(E4,C)),D3:G(B.get(E5,C))}
		A.session_state.watchlist=F
	except g:pass
def Ed():
	F=Gy()
	if not F:A.warning('⚠️ Google Sheet write failed — check secrets.');return J
	E=Gz(F)
	if not E:return J
	try:
		E.clear();E.append_row([j,AM,D1,D2,E4,E5])
		for(G,D)in A.session_state.watchlist.items():E.append_row([G,D.get(A4,C),D.get(BI,C),D.get(CT,C),D.get(Bj,C),D.get(D3,C)])
		return B
	except g as H:A.warning(f"⚠️ Sheet write error: {H}");return J
def Lr(sym,cmp=C,note=C,bf_score=C,bf_grade=C):A.session_state.watchlist[sym]={A4:cmp,BI:note,CT:bf_score,Bj:bf_grade,D3:l.now().strftime('%Y-%m-%d %H:%M')}
def G_(sym):A.session_state.watchlist.pop(sym,D)
if'watchlist_loaded'not in A.session_state:Lq();A.session_state.watchlist_loaded=B
def Ls(row_data,cols):
	N='sl_standard'
	def E(keys):
		for B in keys:
			for A in cols:
				if B in A.lower():
					try:D=G(row_data.get(A,C)).replace(AB,C).replace(AC,C).strip();return M(D)
					except(AY,Fq):pass
	B=E([A4]);I=E(['52w high',D4,'52wk high']);J=E([JP,CS,'52wk low']);K=E([JR,'50dma']);L=E([Fw,'200dma']);A={A4:B,G1:I,G2:J,'dma50':K,'dma200':L}
	if B and I and J:F=(I-J)/52;A[E6]=b(F,2);A['sl_tight']=b(B-Aq*F,2);A[N]=b(B-1.5*F,2);A['sl_wide']=b(B-2.*F,2);O=2.;H=B-A[N];A['target_1r']=b(B+H*Aq,2);A['target_2r']=b(B+H*O,2);A['target_3r']=b(B+H*3.,2);A[D5]=b(K,2)if K else D;A['trail_sl_200dma']=b(L,2)if L else D;A['risk_pct']=b(H/B*100,2)if B else D
	return A
def Ee(history):
	E='AI Analysis';B=history
	if not B:return b''
	F=H.DataFrame(B,columns=[j,'Model','Query','AI Result','Timestamp']);C=io.BytesIO()
	with H.ExcelWriter(C,engine=D6)as D:F.to_excel(D,index=J,sheet_name=E);A=D.sheets[E];A.column_dimensions['A'].width=12;A.column_dimensions['B'].width=14;A.column_dimensions['C'].width=40;A.column_dimensions['D'].width=80;A.column_dimensions['E'].width=20
	return C.getvalue()
if A.sidebar.button('🧹 Clear All Filters',use_container_width=B):
	for Ef in AL(A.session_state.keys()):
		if Ef.startswith('filter_')or Ef in(JS,JT,JU,JV):del A.session_state[Ef]
	A.session_state.grid_reset_token+=1;A.rerun()
A.sidebar.markdown(c)
A.sidebar.header('🔍 Global Search')
H0=A.sidebar.text_input('Search by Symbol, Name, etc...',key=JS)
A.sidebar.markdown(c)
A.sidebar.header('📑 Select a Tab')
Lt=[BE,'Technical Analysis',BF,CL,CM,CN,CO,CP]
y=A.sidebar.selectbox('Choose sheet',Lt,key='filter_sheet')
A.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {y}</p>",unsafe_allow_html=B)
with A.spinner('Downloading data from Google API...'):Eg=DI(y)
if not Eg.empty:
	Eh=0;R=[A for A in Eg.columns if not A.startswith(Aa)and not A.startswith(Ab)];Lu=L9(y,R);Ei=LA.get(y)
	if Ei and Ei in R:Eh=R.index(Ei)
	else:
		for(BO,Lv)in Dr(R):
			if Lv.lower()in[Cz,Ac,Dw,Dx,C_,Dy]:Eh=BO;break
	A.sidebar.markdown(c);A.sidebar.header('⚙️ Settings');Bz=A.sidebar.selectbox('Symbol Column (locked):',R,index=Eh,key='filter_symbol_col',disabled=B,help='Locked for consistency across sheets. To change it, edit LOCKED_SYMBOL_COLUMN near the top of the .py file.');H1=LQ(Eg,Bz);K=H1.copy()
	if H0:Lw=K[R].astype(G).apply(lambda x:x.str.contains(H0,case=J,na=J)).any(axis=1);K=K[Lw]
	A.sidebar.markdown(c);A.sidebar.header('🎨 Color Filters');Ej=A.sidebar.selectbox('Select Column to Filter by Color:',[AO]+R,key='filter_color_col')
	if Ej!=AO:
		Ek=f"_bg_{Ej}"
		if Ek in K.columns:
			Lx=K[Ek].unique();El={Cy:'⚪ White (Default)',w:'🟢 Green',AP:'🔴 Red',JW:'🟡 Yellow','#4285f4':'🔵 Blue',JX:'🟠 Orange','#b6d7a8':'🟩 Light Green','#f4cccc':'🟥 Light Red','#d9d2e9':'🟪 Light Purple'};Em=[]
			for Ly in Lx:
				En=G(Ly).lower()
				if En in El:Em.append(El[En])
				else:Em.append(f"🎨 Custom Hex: {En}")
			H2=A.sidebar.multiselect(f"Select Colors in '{Ej}':",sorted(Em),key='filter_color_selections')
			if H2:
				Eo=[]
				for Ep in H2:
					for(Lz,Bx)in El.items():
						if Bx==Ep:Eo.append(Lz)
					if Ep.startswith(JY):Eo.append(Ep.replace(JY,C))
				K=K[K[Ek].str.lower().isin(Eo)]
	A.sidebar.markdown(c);A.sidebar.header('🎯 Categorical Filters');L_=[A for A in R if AZ(B in A.lower()for B in['cumulative average',G3,E7,JZ,Ja,G4,G5,G6,Jb,G7])]
	for DL in L_:
		M0=sorted([A for A in H1[DL].unique()if G(A).strip()!=C]);H3=A.sidebar.multiselect(f"Filter by {DL}:",options=M0,key=f"filter_cat_{DL}")
		if H3:K=K[K[DL].isin(H3)]
	A.sidebar.markdown(c);A.sidebar.header('📈 DMA Trend Filter');Cc=A.sidebar.selectbox('Select DMA Condition:',[Jc,Jd,Je,Jf,Jg],key='filter_dma_trend')
	if Cc!=Jc:
		H4=S((A for A in R if JR in A.lower()),D);H5=S((A for A in R if'100 dma'in A.lower()),D);H6=S((A for A in R if Fw in A.lower()),D)
		if H4 and H6:
			DM=H.to_numeric(K[H4].astype(G).str.replace(BH,C,regex=B),errors=AN);DN=H.to_numeric(K[H6].astype(G).str.replace(BH,C,regex=B),errors=AN)
			if Cc==Jf:K=K[DM>DN]
			elif Cc==Jg:K=K[DM<DN]
			elif H5:
				DO=H.to_numeric(K[H5].astype(G).str.replace(BH,C,regex=B),errors=AN)
				if Cc==Jd:K=K[(DM<DO)&(DO<DN)]
				elif Cc==Je:K=K[(DM>DO)&(DO>DN)]
	A.sidebar.markdown(c);A.sidebar.header('📊 Numeric Range Filters');Eq=S((A for A in R if'diff'in A.lower()and'200'in A.lower()),D)
	if Eq:K=DJ(K,Eq,A.sidebar,'Diff. from 200 DMA Range:')
	Er=S((A for A in R if E8 in A.lower()and'low'in A.lower()and(AC in A.lower()or'per'in A.lower())),D)
	if Er:K=DJ(K,Er,A.sidebar,'From 52W Low Range:')
	Es=S((A for A in R if E8 in A.lower()and'high'in A.lower()and(AC in A.lower()or'per'in A.lower())),D)
	if Es:K=DJ(K,Es,A.sidebar,'From 52W High Range:')
	M1=[A2,AM,J9,Jh,Ji,Jj,'Net Profit','EPS',Jk,Jl,'Enterprise Value','RSI','Delivery'];H7={Eq,Er,Es}
	for Cd in M1:
		Et=S((A for A in R if Cd.lower()in A.lower()and A not in H7),D)
		if Et:K=DJ(K,Et,A.sidebar);H7.add(Et)
	A.sidebar.markdown(c);A.sidebar.header('📅 Date Filters');H8=S((A for A in R if Jm in A.lower()),D);H9=S((A for A in R if Jn in A.lower()),D)
	if H8:K=Gu(K,H8,A.sidebar)
	if H9:K=Gu(K,H9,A.sidebar)
	A.sidebar.markdown(c);A.sidebar.header('📊 My Watchlist')
	if A.session_state.watchlist:
		HA=Q(A.session_state.watchlist);A.sidebar.caption(f"🔖 {HA} stock{"s"if HA>1 else C} saved")
		for(DP,Eu)in AL(A.session_state.watchlist.items()):
			M2,M3=A.sidebar.columns([3,1]);M2.markdown(f"**{DP}** {"`"+Eu[A4]+"`"if Eu[A4]else C}<br><small style='color:gray'>{Eu.get(BI,C)[:35]}</small>",unsafe_allow_html=B)
			if M3.button('❌',key=f"wl_rm_{DP}",help=f"Remove {DP}"):G_(DP);Ed();A.rerun()
		A.sidebar.markdown(C);M4=H.DataFrame([{j:B,AM:A[A4],D1:A[BI],D2:A.get(CT,C),E4:A.get(Bj,C),E5:A[D3]}for(B,A)in A.session_state.watchlist.items()]);HB=io.BytesIO()
		with H.ExcelWriter(HB,engine=D6)as M5:M4.to_excel(M5,index=J,sheet_name=G0)
		A.sidebar.download_button('📥 Download Watchlist Excel',data=HB.getvalue(),file_name=f"Watchlist_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=B)
	else:A.sidebar.info('No stocks in watchlist yet.\nAdd from the workspace panel below.')
	if A.session_state.ai_history:
		A.sidebar.markdown(c);A.sidebar.header('🤖 AI History Export');A.sidebar.caption(f"{Q(A.session_state.ai_history)} analyses saved this session");M6=Ee(A.session_state.ai_history);A.sidebar.download_button('📥 Download All AI Results (Excel)',data=M6,file_name=f"AI_Analysis_{l.now().strftime(Jo)}.xlsx",mime=Bl,use_container_width=B)
		if A.sidebar.button('🗑️ Clear AI History',use_container_width=B):A.session_state.ai_history=[];A.rerun()
	BP=[]
	if Bz in K.columns:BP.append(Bz)
	HC=S((A for A in R if Ap in A.lower()),D);M7=S((A for A in R if Jp in A.lower()or'prev'in A.lower()),D);A7=S((A for A in R if A4 in A.lower()),D);AJ=S((A for A in R if D0 in A.lower()),D);B5=S((A for A in R if E8 in A.lower()and'high'in A.lower()and BJ not in A.lower()and AC not in A.lower()),D);B6=S((A for A in R if E8 in A.lower()and'low'in A.lower()and BJ not in A.lower()and AC not in A.lower()),D);BQ=S((A for A in R if E3 in A.lower()),D);DQ=S((A for A in R if G8 in A.lower()or A.lower().strip()=='vol'),D);BR=S((A for A in R if'rsi'in A.lower()),D);Ce=S((A for A in R if G4 in A.lower()),D);BS=S((A for A in R if G5 in A.lower()),D);DR=S((A for A in R if G6 in A.lower()and A!=Ce and'dma'not in A.lower()),D);DS=S((A for A in R if'macd'in A.lower()),D);BT=S((A for A in R if G7 in A.lower()),D);BU=S((A for A in R if'diff'in A.lower()and'200'in A.lower()),D);HD=LD(y,R)
	if HD:
		for p in HD:
			if p not in BP:BP.append(p)
	else:
		for Cd in(DQ,M7,A7,AJ,B5,B6):
			if Cd and Cd not in BP:BP.append(Cd)
	M8=[A for A in K.columns if A not in BP and not A.startswith(Aa)and not A.startswith(Ab)and A!=n];M9=[A for A in K.columns if A.startswith(Aa)or A.startswith(Ab)or A==n];MA=BP+M8+M9;K=K[MA];A.markdown(c)
	with A.expander(f"🚀 Executive Dashboard — {y}",expanded=B):
		A.caption('Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.')
		def Ai(series):
			A=series
			if A is D:return H.Series(dtype=M)
			return H.to_numeric(A.astype(G).str.replace('[%,₹\\s]',C,regex=B),errors=AN)
		W=K;MB=Q(W);Aj=Ai(W[AJ])if AJ and AJ in W.columns else H.Series(dtype=M);HE=Ai(W[DQ])if DQ and DQ in W.columns else H.Series(dtype=M);AW=Ai(W[A7])if A7 and A7 in W.columns else H.Series(dtype=M);BV=Ai(W[B5])if B5 and B5 in W.columns else H.Series(dtype=M);Av=Ai(W[B6])if B6 and B6 in W.columns else H.Series(dtype=M);HF=Ai(W[BR])if BR and BR in W.columns else H.Series(dtype=M);HG=Ai(W[BQ])if BQ and BQ in W.columns else H.Series(dtype=M);Ev=S((A for A in R if G9 in A.lower()),D);HH=Ai(W[Ev])if Ev and Ev in W.columns else H.Series(dtype=M);r=Ai(W[BU])if BU and BU in W.columns else H.Series(dtype=M);Ew=S((A for A in R if Ap in A.lower()),D);HI=Ai(W[Ew])if Ew and Ew in W.columns else H.Series(dtype=M);HJ=U((Aj>0).sum())if not Aj.empty else 0;Ex=U((Aj<0).sum())if not Aj.empty else 0;MC=U((Aj==0).sum())if not Aj.empty else 0;Ou=M(Aj.mean())if Aj.notna().any()else i;Ov=HJ/Ex if Ex>0 else D;Ow=M(Aj.median())if Aj.notna().any()else D;Ox=M(HE.sum())if HE.notna().any()else i;Oy=M(HH.sum())if HH.notna().any()else i;Oz=M(HI.sum())if HI.notna().any()else i;O_=M(HF.mean())if HF.notna().any()else D;P0=M(HG.mean())if HG.notna().any()else D;MD=U((r>0).sum())if r.notna().any()else 0;ME=U((r<0).sum())if r.notna().any()else 0;HK=0
		if BS and BS in W.columns:HK=U(W[BS].astype(G).str.contains('breakout|buy|bullish',case=J,na=J).sum())
		HL=0
		if BT and BT in W.columns:HL=U(W[BT].astype(G).str.contains('buy',case=J,na=J).sum())
		HM,HN=0,0;HO=0
		if AW.notna().any()and BV.notna().any():MF=AW/BV.replace(0,A6.nan)*100;HM=U((MF>=95).sum())
		if AW.notna().any()and Av.notna().any():HP=AW/Av.replace(0,A6.nan)*100;HN=U((HP<=105).sum());HO=U((HP<=115).sum())
		def AX(container,label,value,bg='#f5f7fa',fg='#1a1a1a'):container.markdown(f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'><div style='font-size:0.70em; color:#666; font-weight:700; letter-spacing:0.2px;'>{label}</div><div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div></div>",unsafe_allow_html=B)
		BW=A.columns(7);AX(BW[0],'📦 TOTAL STOCKS',f"{MB:,}");AX(BW[1],'🟢 ADVANCES',f"{HJ:,}",bg=CU,fg=GA);AX(BW[2],'🔴 DECLINES',f"{Ex:,}",bg=Bm,fg=D7);AX(BW[3],'⚪ UNCHANGED',f"{MC:,}");AX(BW[4],'🕳️ NEAR 52W LOW (≤15%)',f"{HO:,}"if AW.notna().any()and Av.notna().any()else D8,bg=Bm,fg=D7);AX(BW[5],'🚀 BREAKOUTS',f"{HK:,}",bg=GB,fg='#e65100');AX(BW[6],'✅ BUY SIGNALS',f"{HL:,}",bg=Jq,fg='#0d47a1');A.markdown("<div style='margin-top:8px;'></div>",unsafe_allow_html=B);DT=A.columns(4);AX(DT[0],'🏔️ NEAR 52W HIGH (≥95%)',f"{HM:,}",bg=CU,fg=GA);AX(DT[1],'🕳️ NEAR 52W LOW (≤5%)',f"{HN:,}",bg=Bm,fg=D7);AX(DT[2],'📉 BELOW 200 DMA',f"{ME:,}"if r.notna().any()else D8,bg=Bm,fg=D7);AX(DT[3],'🎯 ABOVE 200 DMA',f"{MD:,}"if r.notna().any()else D8,bg=CU,fg=GA);A.markdown(CV,unsafe_allow_html=B);DU={Jr:J,'modeBarButtons':[['toImage']]}
		def MG(frac):
			B=frac;B=AA(i,min(Aq,B));D=[(i,(234,67,53)),(.5,(249,168,37)),(Aq,(15,157,88))]
			for H in Ds(Q(D)-1):
				C,A=D[H];E,F=D[H+1]
				if C<=B<=E:G=(B-C)/(E-C)if E>C else i;I=U(A[0]+(F[0]-A[0])*G);J=U(A[1]+(F[1]-A[1])*G);K=U(A[2]+(F[2]-A[2])*G);return f"#{I:02x}{J:02x}{K:02x}"
			return'#999999'
		def P1(title_text,points,y_min,y_max,y_label,height=340):
			G=height;F=y_max;E=points;B=y_min
			if not E:A.info('No data available for this chart.');return
			N=Q(E);P=F-B or Aq;H=C
			for(R,(S,I,T))in Dr(E):U=(I-B)/P;K=AA(i,min(Aq,U));V=MG(K);W=R/AA(N-1,1)*100;X=(1-K)*100;H+=f'<a href="{T}" target="_blank" title="{S}: {I:.2f}{y_label}" style="position:absolute; left:{W:.3f}%; top:{X:.3f}%; width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; background:{V}; display:block; border:1px solid rgba(255,255,255,0.75); box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
			L=C
			for(Y,M)in[(0,F),(25,D),(50,(B+F)/2),(75,D),(100,B)]:Z=f"{M:.0f}"if M is not D else C;L+=f'<div style="position:absolute; left:0; right:0; top:{Y}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;"><span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:#9aa0a6;">{Z}</span></div>'
			a=f'<div style="font-family:\'Source Sans Pro\',sans-serif;"><div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div><div style="font-size:11px; color:#9aa0a6; margin-bottom:8px;">Click any dot to open its NSE chart in a new tab</div><div style="position:relative; width:calc(100% - 26px); height:{G}px; margin-left:26px; background:#fff; border:1px solid rgba(0,0,0,0.08); border-radius:6px; overflow:hidden;">{L}{H}</div><div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;"><span style="font-size:10px; color:#ea4335;">● low</span><span style="font-size:10px; color:#f9a825;">● mid</span><span style="font-size:10px; color:#0f9d58;">● high</span></div></div>';O.html(a,height=G+90,scrolling=J)
		if Bz in W.columns:BX=W[Bz].astype(G)
		elif n in W.columns:BX=W[n].astype(G)
		else:BX=W.index.astype(G).to_series(index=W.index)
		if n in W.columns:B_=W[n].astype(G).str.strip()
		else:B_=BX.astype(G).str.replace('<[^>]+>',C,regex=B).str.strip()
		def HQ(fig,chart_key):
			O='customdata';N='points';M='selection';K=chart_key;H=fig;H.update_layout(clickmode='event+select')
			try:I=A.plotly_chart(H,use_container_width=B,key=K,on_select='rerun')
			except Fq:A.plotly_chart(H,use_container_width=B,key=K);A.caption('⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.');return
			C=D;F=I.get(M)if Az(I,E)else Fr(I,M,D)
			if F:
				L=F.get(N)if Az(F,E)else Fr(F,N,D)
				if L:
					J=L[-1];G=J.get(O)if Az(J,E)else Fr(J,O,D)
					if G:C=G[0]if Az(G,(AL,tuple))else G
			if C:
				P=f"https://charting.nseindia.com/?symbol={C}-EQ";Q,R=A.columns([3,1])
				with Q:A.success(f"Selected: **{C}**")
				with R:A.link_button('📈 Open on NSE',P,use_container_width=B)
				A.markdown(f"🔗 **More links for {C}:** [TV (🔗)](https://www.tradingview.com/symbols/{C}/) &nbsp;|&nbsp; [TVC (🔗)](https://www.tradingview.com/chart/?symbol=NSE%3A{C}) &nbsp;|&nbsp; [NSE (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={C}) &nbsp;|&nbsp; [NC (🔗)](https://www.charting.nseindia.com/?symbol={C}-EQ) &nbsp;|&nbsp; [CL (🔗)](https://www.chartink.com/stocks-new?symbol={C}) &nbsp;|&nbsp; [CL2 (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={C}) &nbsp;|&nbsp; [Hist (🔗)](https://www.equitypandit.com/historical-data/{C}) &nbsp;|&nbsp; [Scr (🔗)](https://www.screener.in/company/{C}) &nbsp;|&nbsp; [MS (🔗)](https://marketsmithindia.com/mstool/eval/{C}/evaluation.jsp) &nbsp;|&nbsp; [ZK (🔗)](https://zerodha.com/markets/stocks/NSE/{C}) &nbsp;|&nbsp; [WB (🔗)](https://www.whalesbook.com/company/profile/{C}/) &nbsp;|&nbsp; [S (🔗)](https://www.stockanalysis.com/quote/nse/{C}) &nbsp;|&nbsp; [GFi (🔗)](https://www.google.com/finance/beta/quote/{C}:NSE)")
			else:A.caption('Click any dot above to select a stock — its NSE chart button and quick-links will appear here.')
		def MH(key_prefix):
			W='% Above 52W Low';V='% Below 52W High';C=key_prefix;X,Y=A.columns(2)
			with X:
				if AW.notna().any()and BV.notna().any():G=(BV-AW)/BV.replace(0,A6.nan)*100;I=G.dropna().sort_values(ascending=B).head(30).index;K=H.DataFrame({j:BX.loc[I].values,V:G.loc[I].values}).iloc[::-1];L=P.Figure(P.Bar(x=K[V],y=K[j],orientation='h',marker_color=w));L.update_layout(title='🏔️ Top 30 Nearest 52W High',template=q,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(L,use_container_width=B,key=f"{C}_nearhigh_{y}",config=DU)
				else:A.info('52-Week High column not detected for this sheet.')
			with Y:
				if AW.notna().any()and Av.notna().any():M=(AW-Av)/Av.replace(0,A6.nan)*100;N=M.dropna().sort_values(ascending=B).head(30).index;O=H.DataFrame({j:BX.loc[N].values,W:M.loc[N].values}).iloc[::-1];Q=P.Figure(P.Bar(x=O[W],y=O[j],orientation='h',marker_color=AP));Q.update_layout(title='🕳️ Top 30 Nearest 52W Low',template=q,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(Q,use_container_width=B,key=f"{C}_nearlow_{y}",config=DU)
				else:A.info('52-Week Low column not detected for this sheet.')
			Z,a=A.columns(2)
			with Z:
				if r.notna().any():
					R=r[r<0].dropna().sort_values(ascending=B).head(30).index;D=H.DataFrame({j:BX.loc[R].values,D9:r.loc[R].values}).iloc[::-1]
					if not D.empty:S=P.Figure(P.Bar(x=D[D9],y=D[j],orientation='h',marker_color=AP));S.update_layout(title='📉 Top 30 Below 200 DMA',template=q,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(S,use_container_width=B,key=f"{C}_below200_{y}",config=DU)
					else:A.info('No stocks currently below 200 DMA.')
				else:A.info(GC)
			with a:
				if r.notna().any():
					T=r[r>0].dropna().sort_values(ascending=J).head(30).index;F=H.DataFrame({j:BX.loc[T].values,D9:r.loc[T].values}).iloc[::-1]
					if not F.empty:U=P.Figure(P.Bar(x=F[D9],y=F[j],orientation='h',marker_color=w));U.update_layout(title='🎯 Top 30 Above 200 DMA',template=q,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(U,use_container_width=B,key=f"{C}_above200_{y}",config=DU)
					else:A.info('No stocks currently above 200 DMA.')
				else:A.info(GC)
		MH(E9);MI=A.container();MJ=A.container()
		with MI:
			if AW.notna().any()and BV.notna().any()and Av.notna().any():MK=(BV-Av).replace(0,A6.nan);HR=((AW-Av)/MK*100).clip(0,100);HS=HR.notna()&B_.notna();HT=B_[HS].str.strip().values;HU=HR[HS].values;HV=P.Figure(P.Scatter(x=HT,y=HU,mode=EA,marker=E(size=9,color=HU,colorscale=[[0,AP],[.5,B0],[1,w]],cmin=0,cmax=100,showscale=B,colorbar=E(title='% of Range')),customdata=HT,hovertemplate=Js));HV.update_layout(title='📍 Position within 52-Week Range (0% = Low, 100% = High)',template=q,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jt),yaxis_title='% of 52W Range');HQ(HV,f"dash_range_{y}")
			else:A.info('52-Week High/Low columns not detected for this sheet.')
		with MJ:
			if r.notna().any()and B_ is not D:HW=r.notna()&B_.notna();HX=B_[HW].str.strip().values;DV=r[HW].values;HY=AA(abs(M(A6.nanmin(DV))),abs(M(A6.nanmax(DV))),1e-09);HZ=P.Figure(P.Scatter(x=HX,y=DV,mode=EA,marker=E(size=9,color=DV,colorscale=[[0,AP],[.5,B0],[1,w]],cmin=-HY,cmax=HY,showscale=B,colorbar=E(title='% Diff')),customdata=HX,hovertemplate=Js));HZ.update_layout(title='📐 Difference from 200 DMA (0% = at 200 DMA)',template=q,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jt),yaxis_title=D9);HQ(HZ,f"dash_diff200_{y}")
			else:A.info(GC)
	A.markdown(c);ML,MM,MN=A.columns([3,1,2.2])
	with ML:Ha=A.radio(GD,[GE,CW,CX],horizontal=B,help='Automatically adjust the column widths based on the text length of the selected row.')
	with MN:A.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>",unsafe_allow_html=B);Hb=A.text_input(Ju,placeholder=Jv,key=JT,label_visibility='collapsed')
	if Hb:K=K[K[n].astype(G).str.contains(Hb,case=J,na=J)]
	MO=Gv(K);Hc=io.BytesIO()
	with H.ExcelWriter(Hc,engine=D6)as MP:MQ=y[:31].replace(':',C).replace('/',C);MO.to_excel(MP,index=J,sheet_name=MQ)
	with MM:A.markdown("<div style='margin-top: 28px;'></div>",unsafe_allow_html=B);A.download_button(label='📥 Download as Excel',data=Hc.getvalue(),file_name=f"{y}_Export_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=J)
	MR,MS=A.columns([1,4])
	with MR:A.write(f"**Rows:** {K.shape[0]} | **Columns:** {Q(R)}")
	with MS:MT=A.empty()
	DW=B3("\n    class HtmlRenderer {\n        init(params) {\n            this.eGui = document.createElement('span');\n            this.eGui.innerHTML = params.value ? String(params.value) : '';\n        }\n        getGui() {\n            return this.eGui;\n        }\n    }\n    ");Hd=B3('\n    function(params) {\n        let colName = params.colDef.field;\n        let c_low = colName.toLowerCase();\n\n        let bgCol = "_bg_" + colName;\n        let txtCol = "_txt_" + colName;\n\n        let bgColor = params.data[bgCol];\n        let txtColor = params.data[txtCol];\n\n        let isTargetCol = c_low.includes("cmp") || c_low.includes("close price") || c_low.includes("prev");\n\n        if (isTargetCol) {\n            if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') return null;\n            return {\n                \'backgroundColor\': bgColor,\n                \'color\': txtColor || \'#000000\',\n                \'fontWeight\': (txtColor === \'#ffffff\' || bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n            };\n        }\n\n        if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') {\n            return { \'color\': \'#000000\' };\n        }\n\n        return {\n            \'backgroundColor\': bgColor,\n            \'color\': \'#000000\',\n            \'fontWeight\': (bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n        };\n    }\n    ');B7=EX.from_dataframe(K);B7.configure_selection(selection_mode='single',use_checkbox=B);B7.configure_side_bar(filters_panel=J,columns_panel=B);MU=[Cz,C_,Jw,Jx,Ac,G3,E7];Cf=B
	for p in K.columns:
		if p.startswith(Aa)or p.startswith(Ab)or p==n:B7.configure_column(p,hide=B);continue
		if p in Lu:B7.configure_column(p,hide=B);continue
		if Ha==CW and Q(K)>0:
			Ey=By(K.iloc[0][p]);Ez=Q(G(p));Cg=U(AA(Ey,Ez)*7+22)
			if Cf:Cg+=30
			DX,DY=Cg,40
		elif Ha==CX and Q(K)>1:
			Ey=By(K.iloc[1][p]);Ez=Q(G(p));Cg=U(AA(Ey,Ez)*7+22)
			if Cf:Cg+=30
			DX,DY=Cg,40
		else:DX,DY=(220,150)if p.lower()in MU else(120,80)
		Ch=p==Bz;He=DA if Ch or Cf else D
		if Cf:Cf=J
		MV=p.lower()
		if Ch or AZ(A in MV for A in[JF,JG,JH,JI,JJ,JK,JL,'nse']):B7.configure_column(p,width=DX,minWidth=DY,sortable=B,filter=B,resizable=B,editable=J,pinned=He,lockPinned=Ch,suppressMovable=Ch,checkboxSelection=Ch,cellRenderer=DW,cellStyle=Hd)
		else:B7.configure_column(p,width=DX,minWidth=DY,sortable=B,filter=B,resizable=B,editable=J,pinned=He,cellStyle=Hd)
	B7.configure_grid_options(domLayout=AQ,rowHeight=35,headerHeight=45,enableCellTextSelection=B,ensureDomOrder=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);MW=B7.build();MX=EW(K,gridOptions=MW,theme=GF,update_mode=L0.SELECTION_CHANGED,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,enable_enterprise_modules=J,height=400,width=GG,key=f"primary_stock_table_grid_{A.session_state.grid_reset_token}");BY=MX.get('selected_rows',[])
	if BY is not D and Q(BY)>0 or Q(K)>0:
		if BY is not D and Q(BY)>0:T=BY.iloc[0]if Az(BY,H.DataFrame)else BY[0]
		else:T=K.iloc[0]
		F=G(T.get(n,C)).strip()
		if F:
			with MT.container():A.markdown(f"**⚡ {F} Links:** [TV (🔗)](https://www.tradingview.com/symbols/{F}/) &nbsp;|&nbsp; [TVC (🔗)](https://www.tradingview.com/chart/?symbol=NSE%3A{F}) &nbsp;|&nbsp; [NSE (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={F}) &nbsp;|&nbsp; [NC (🔗)](https://www.charting.nseindia.com/?symbol={F}-EQ) &nbsp;|&nbsp; [% (🔗)](https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern#) &nbsp;|&nbsp; [%K (🔗)](https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern#) &nbsp;|&nbsp; [EQ (🔗)](https://www.nseindia.com/report-detail/eq_security) &nbsp;|&nbsp; [AZ (🔗)](https://https://www.nseindia.com/companies-listing/corporate-filings-application) &nbsp;|&nbsp; [Fin (🔗)](https://https://www.nseindia.com/companies-listing/corporate-filings-financial-results-comparision) &nbsp;|&nbsp; [CL (🔗)](https://www.chartink.com/stocks-new?symbol={F}) &nbsp;|&nbsp; [CL2 (🔗)](https://www.chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={F}) &nbsp;|&nbsp; [History (🔗)](https://www.equitypandit.com/historical-data/{F}) &nbsp;|&nbsp; [Scr(🔗)](https://www.screener.in/company/{F}) &nbsp;|&nbsp; [MS (🔗)](https://marketsmithindia.com/mstool/eval/{F}/evaluation.jsp) &nbsp;|&nbsp; [ZK (🔗)](https://www.zerodha.com/markets/stocks/NSE/{F}) &nbsp;|&nbsp; [WB (🔗)](https://www.whalesbook.com/company/profile/{F}/) &nbsp;|&nbsp; [S (🔗)](https://www.stockanalysis.com/quote/nse/{F}) &nbsp;|&nbsp; [GFi (🔗)](https://www.google.com/finance/beta/quote/{F}:NSE)")
			A.markdown(f"---");A.subheader(f"🛠️ Live Workspace Panel: {F}");A8=A.slider('📏 Adjust Panel Box Height (px):',min_value=300,max_value=1000,value=500,step=50,key='panel_height_slider');A9=A.tabs(['🕯️ Price Chart (EMA + RSI)','📈 Chart & Trade Info (NSE Component)','📋 History Data (EquityPandit)','🎯 Bullish/Bearish Zone','📁 Screener Documents','🪁 Zerodha Portal','📊 MarketSmith India','📉 TradingView Symbol Profile','🤖 AI Stock Analysis','💻 AI Pine Script Builder','🔬 Bottom Fishing Score','🎯 GTT Order Calculator','📊 Watchlist Manager','📰 News Feed'])
			with A9[1]:Hf=f"https://charting.nseindia.com/?symbol={F}-EQ";A.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({Hf})",unsafe_allow_html=J);A.caption(Bn);O.html(f'<iframe src="{Hf}" width="100%" height="{A8}" style="border:none; border-radius:5px;"></iframe>',height=A8+20)
			with A9[2]:Hg=f"https://www.equitypandit.com/historical-data/{F.lower()}";A.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({Hg})");A.caption(Bn);O.html(f'<iframe src="{Hg}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[3]:Hh=f"https://www.equitypandit.com/share-price/{F.lower()}#chart";A.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({Hh})");A.caption(Bn);O.html(f'<iframe src="{Hh}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[4]:Hi=f"https://www.screener.in/company/{F}/consolidated/";A.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({Hi})");A.caption(Bn);O.html(f'<iframe src="{Hi}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[5]:Hj=f"https://zerodha.com/markets/stocks/NSE/{F}/";A.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({Hj})");A.caption(Bn);O.html(f'<iframe src="{Hj}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[6]:Hk=f"https://marketsmithindia.com/mstool/eval/{F.lower()}/evaluation.jsp";A.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({Hk})");A.caption(Bn);O.html(f'<iframe src="{Hk}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[7]:Hl=f"https://www.tradingview.com/symbols/{F}/";A.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({Hl})");A.caption(Bn);O.html(f'<iframe src="{Hl}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[8]:
				A.markdown(f"### 🤖 Ask AI About **{F}**")
				if not EY:A.warning(Jy)
				else:
					DZ=Ea('analysis');A.caption('⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash'if BN and Cb else'⚡ Groq connected'if BN else'🧠 Gemini connected');A.write('Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.');E_=A.text_area('Your Query:',value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {F}.",height=80,key='ai_query_analysis')
					if A.button('✨ Generate AI Analysis',use_container_width=B,key='btn_ai_analysis'):
						with A.spinner(f"Analyzing {F} with {DZ}..."):
							try:F0={A:B for(A,B)in T.items()if not G(A).startswith(Bo)};Ci=f"""
You are a professional stock market analyst evaluating Indian NSE stocks.
The user is asking about the stock: {F}.

Here is the live data extracted directly from the user's dashboard for this stock:
{F0}

User Query: {E_}

Please provide a clear, concise, and professional response.
""";F1=EZ(Ci,DZ);A.session_state[GH]={DB:F,EB:DZ,'query':E_,DC:F1};A.session_state.ai_history.append([F,DZ,E_,F1,l.now().strftime(CQ)]);A.info(F1)
							except g as BZ:A.error(f"AI error: {BZ}")
					if A.session_state.get(GH,{}).get(DB)==F:
						Cj=A.session_state[GH];Da=Cj[DC];A.markdown(c);MY,MZ,Ma=A.columns(3)
						with MY:Mb=Ee([[F,Cj[EB],Cj['query'],Da,l.now().strftime(CQ)]]);A.download_button('📥 Save as Excel',data=Mb,file_name=f"AI_{F}_{l.now().strftime(Jo)}.xlsx",mime=Bl,use_container_width=B,key='dl_ai_excel_analysis')
						with MZ:Mc=urllib.parse.quote(f"📊 *{F} AI Analysis* ({Cj[EB]})\n\n{Da[:800]}"+('\n\n_(truncated)_'if Q(Da)>800 else C));A.markdown(f"<a href='https://wa.me/?text={Mc}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
						with Ma:Md=urllib.parse.quote(f"📊 {F} AI Analysis ({Cj[EB]})\n\n{Da[:800]}");A.markdown(f"<a href='https://t.me/share/url?url=NSEDashboard&text={Md}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
					A.markdown(c);A.markdown('**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:');Me='\n'.join([f"{A+1}. {B.replace("{sym}",F)}"for(A,B)in Dr(L4)]);A.text(Me)
			with A9[9]:
				A.markdown(f"### 💻 AI Pine Script Generator for **{F}**")
				if not EY:A.warning(Jy)
				else:
					Mf=Ea('pine');A.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.");Hm=A.selectbox('Select Strategy Focus:',['Volume Breakout with Dynamic Stop Loss','Moving Average Crossover (50/100/200 DMA)','Trend Following with Trailing Stop','Mean Reversion from 52W High/Low'],key='pine_strategy_focus');Mg=A.text_area('Additional Custom Rules (Optional):',value=f"Include risk management parameters and plot signals on the chart.",height=60,key='pine_query')
					if A.button('⚙️ Generate TradingView Pine Script',use_container_width=B,key='btn_pine'):
						with A.spinner(f"Writing Pine Script v5 code for {F}..."):
							try:F0={A:B for(A,B)in T.items()if not G(A).startswith(Bo)};Ci=f'''
You are an expert quantitative developer specializing in TradingView Pine Script v5.

Write a complete, ready-to-copy Pine Script v5 strategy for the stock: {F}.

Strategy Focus: {Hm}
Custom Rules: {Mg}

Here is the live fundamental and technical data for {F} to incorporate as baseline context or threshold values if relevant:
{F0}

Formatting Requirements:
1. Start with `//@version=5` and `strategy("{F} Custom Script", overlay=true)`
2. Include clear comments explaining the logic.
3. Provide ONLY the Pine Script code inside a markdown code block, no other conversational text.
''';Hn=EZ(Ci,Mf);A.session_state[GI]={DB:F,DC:Hn};A.markdown('### 📋 Your Custom Strategy Code:');A.write('Copy the code below and paste it into the TradingView Pine Editor.');A.markdown(Hn)
							except g as BZ:A.error(f"AI error: {BZ}")
					if A.session_state.get(GI,{}).get(DB)==F:Mh=A.session_state[GI][DC];Mi=Ee([[F,'Pine Script',Hm,Mh,l.now().strftime(CQ)]]);A.download_button('📥 Save Pine Script as Excel',data=Mi,file_name=f"PineScript_{F}_{l.now().strftime(Bk)}.xlsx",mime=Bl,key='dl_pine_excel')
					A.markdown(c);A.markdown('**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:');A.text(L5)
			with A9[10]:
				A.markdown(f"### 🔬 Bottom Fishing Analysis: **{F}**");A.caption('Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.');Ho={A:B for(A,B)in T.items()if not G(A).startswith(Bo)};C0,F2,F3=DK(Ho,R);F4=Ad if C0>=75 else JW if C0>=55 else JX if C0>=35 else AP;A.markdown(f'''
                <div style="background:{F4}22; border-left:6px solid {F4}; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
                    <div style="font-size:2rem; font-weight:bold; color:{F4};">{C0}/100</div>
                    <div style="font-size:1.3rem; font-weight:bold;">{F2}</div>
                    <div style="font-size:0.85rem; color:#555; margin-top:4px;">Bottom Fishing Composite Score for {F}</div>
                </div>
                ''',unsafe_allow_html=B);A.markdown('#### 📋 Detailed Scoring Breakdown')
				for Mj in F3:A.markdown(f"- {Mj}")
				A.markdown(c);A.markdown('#### 📖 Scoring Criteria');Mk='\n| # | Criteria | Max Points | Description |\n|---|----------|-----------|-------------|\n| 1 | **52W Low Proximity** | 30 | CMP is 8–15% above 52W Low (ideal entry zone) |\n| 2 | **Uptrend (200 DMA)** | 15 | CMP above 200 DMA = confirmed uptrend |\n| 3 | **Turnover Activity** | 10 | High trading turnover = institutional interest |\n| 4 | **Low/Zero Debt** | 10 | D/E ratio ≤ 0.1 is ideal (no loan burden) |\n| 5 | **Net Profitability** | 10 | Positive net profit confirms fundamental health |\n| 6 | **RONW %** | 10 | Return on Net Worth ≥ 15% = strong business |\n| 7 | **Promoter Holding** | 8 | ≥ 50% shows management confidence |\n| 8 | **Zero Pledge** | 7 | No pledged shares = no financial stress |\n';A.markdown(Mk);A.info('💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), backed by positive profits, low debt, and high promoter holding. This combination maximizes probability of a bull run from the bottom.')
				if EY:
					A.markdown(c);F5=Ea('bf')
					if A.button('🤖 Get AI Deep Analysis for Bottom Buy',use_container_width=B,key='bf_ai_btn'):
						with A.spinner(f"Running deep bottom-fishing analysis for {F} with {F5}..."):
							try:Ci=f"""
You are an expert Indian stock market analyst specializing in bottom-fishing and value investing.

Stock: {F}
Live Data from Dashboard: {Ho}
Bottom Fishing Score: {C0}/100
Grade: {F2}
Scoring Breakdown: {chr(10).join(F3)}

Please provide a comprehensive bottom-fishing analysis covering:
1. Is this stock in or near the 52-week low zone? What does this mean?
2. Is the stock entering an uptrend? Evidence from DMA data.
3. Turnover analysis — is there accumulation visible?
4. Fundamental health — debt, profitability, revenue growth signals.
5. Bull run potential — sector tailwinds, promoter activity, institutional interest.
6. Specific entry price zone recommendation with stop loss and target.
7. Risk factors that could delay recovery.
8. Overall verdict: Strong Buy / Watchlist / Avoid for bottom-fishing strategy.

Be specific, data-driven, and actionable for a retail investor.
""";F6=EZ(Ci,F5);A.session_state['last_bf_ai_result']={DB:F,DC:F6};A.session_state.ai_history.append([F,F5,'Bottom Fishing Deep Analysis',F6,l.now().strftime(CQ)]);A.success('✅ AI Analysis Complete');A.markdown(F6)
							except g as BZ:A.error(f"AI error: {BZ}")
					A.markdown(c);A.markdown('#### 📤 Share BF Score Card');Hp=f"""🔬 *Bottom Fishing Score: {F}*

📊 Score: *{C0}/100*
📈 Grade: {F2}

"""+'\n'.join(F3[:5])+f"\n\n🕒 {l.now().strftime(Jz)}\n📌 NSE Stock Dashboard";Ml=urllib.parse.quote(Hp);Mm=urllib.parse.quote(Hp);Mn,Mo=A.columns(2)
					with Mn:A.markdown(f"<a href='https://wa.me/?text={Ml}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
					with Mo:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={Mm}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
			with A9[11]:
				A.markdown(f"### 🎯 GTT Order Calculator: **{F}**");A.caption('Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.');Mp={A:B for(A,B)in T.items()if not G(A).startswith(Bo)};AF=Ls(Mp,R)
				if not AF.get(A4):A.warning('⚠️ CMP column not found in sheet data. Cannot compute GTT levels.')
				else:
					V=AF[A4];Mq,Mr,Ms,Mt=A.columns(4);Mq.metric('📍 CMP',f"₹{V:,.2f}")
					if AF.get(G1):Mr.metric('⬆️ 52W High',f"₹{AF[G1]:,.2f}")
					if AF.get(G2):Ms.metric('⬇️ 52W Low',f"₹{AF[G2]:,.2f}")
					if AF.get(E6):Mt.metric('📊 ATR (approx)',f"₹{AF[E6]:,.2f}")
					A.markdown(c);A.markdown('#### ⚙️ Customize ATR Multiplier');Mu,Mv=A.columns(2);Hq=Mu.number_input('Manual ATR Override (₹) — leave 0 to use auto',min_value=i,value=i,step=.5,key='gtt_manual_atr');Db=Mv.selectbox('Risk-Reward Ratio:',['1:1','1:1.5','1:2','1:2.5','1:3'],index=2,key='gtt_rr_ratio');Mw=M(Db.split(':')[1]);C1=Hq if Hq>0 else AF.get(E6,0)
					if C1 and C1>0:
						Hr=b(V-Aq*C1,2);C2=b(V-1.5*C1,2);Hs=b(V-2.*C1,2);Dc=V-C2;Dd=b(V+Dc*Aq,2);De=b(V+Dc*Mw,2);Df=b(V+Dc*3.,2);Mx=b(Dc/V*100,2);A.markdown('#### 🛡️ Stop-Loss Levels');F7=H.DataFrame([{EC:'Tight SL (1× ATR)',BK:Hr,ED:b((V-Hr)/V*100,2),EE:'Intraday / Scalp'},{EC:'Standard SL (1.5× ATR)',BK:C2,ED:b((V-C2)/V*100,2),EE:'Swing / BTST'},{EC:'Wide SL (2× ATR)',BK:Hs,ED:b((V-Hs)/V*100,2),EE:'Positional'}])
						if AF.get(D5):F7=H.concat([F7,H.DataFrame([{EC:'Trail SL @ 50 DMA',BK:AF[D5],ED:b((V-AF[D5])/V*100,2)if AF[D5]<V else 0,EE:'Trailing Stop'}])],ignore_index=B)
						A.dataframe(F7,use_container_width=B,hide_index=B);A.markdown(f"#### 🎯 Target Levels (based on {Db} R:R)");My=H.DataFrame([{GJ:'T1 (1R)',BK:Dd,GK:b((Dd-V)/V*100,2),GL:'Book 30–40%'},{GJ:f"T2 ({Db} R:R)",BK:De,GK:b((De-V)/V*100,2),GL:'Book 40–50%'},{GJ:'T3 (3R — runner)',BK:Df,GK:b((Df-V)/V*100,2),GL:'Hold remainder'}]);A.dataframe(My,use_container_width=B,hide_index=B);A.markdown('#### 💰 Position Sizing Helper');Mz,M_=A.columns(2);N0=Mz.number_input('Capital (₹):',min_value=1000,value=100000,step=5000,key='gtt_capital');Ht=M_.number_input('Max Risk % of Capital:',min_value=.5,max_value=1e1,value=2.,step=.5,key='gtt_risk_pct');Hu=N0*Ht/100;F8=U(Hu/(V-C2))if V-C2>0 else 0;Hv=F8*V;A.success(f"📦 Suggested Qty: **{F8} shares** &nbsp;|&nbsp; Investment: **₹{Hv:,.0f}** &nbsp;|&nbsp; Max Loss: **₹{Hu:,.0f}** ({Ht}%)");A.markdown(c);A.markdown('#### 📋 GTT Order Summary (Copy-Ready)');F9=f"""🎯 *GTT Order: {F}*

📍 Entry CMP: ₹{V:,.2f}
🛡️ Stop-Loss: ₹{C2:,.2f} ({Mx:.1f}% risk)
🎯 Target 1:  ₹{Dd:,.2f} (+{b((Dd-V)/V*100,1)}%)
🎯 Target 2:  ₹{De:,.2f} (+{b((De-V)/V*100,1)}%)
🎯 Target 3:  ₹{Df:,.2f} (+{b((Df-V)/V*100,1)}%)
📦 Qty: {F8} shares | ₹{Hv:,.0f}
📊 ATR: ₹{C1:.2f} | R:R {Db}
🕒 {l.now().strftime(Jz)}""";A.code(F9,language=C);N1=urllib.parse.quote(F9);N2=urllib.parse.quote(F9);N3,N4=A.columns(2)
						with N3:A.markdown(f"<a href='https://wa.me/?text={N1}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share GTT on WhatsApp</button></a>",unsafe_allow_html=B)
						with N4:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={N2}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share GTT on Telegram</button></a>",unsafe_allow_html=B)
					else:A.warning('⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.')
			with A9[12]:
				A.markdown(f"### 📊 Watchlist Manager");Hw={A:B for(A,B)in T.items()if not G(A).startswith(Bo)};N5,N6,_=DK(Hw,R);N7=G(Hw.get(A7,C))if A7 else C;FA=F in A.session_state.watchlist;A.markdown(f"**Current Stock: {F}** {"✅ Already in Watchlist"if FA else C}");N8=A.text_input('📝 Note (optional):',value=A.session_state.watchlist.get(F,{}).get(BI,C),placeholder='e.g. Near 52W low, watching for breakout',key=f"wl_note_{F}");N9,NA=A.columns(2)
				with N9:
					if A.button(f"{"🔄 Update"if FA else"➕ Add"} {F} to Watchlist",use_container_width=B,key='wl_add_btn'):
						Lr(F,cmp=N7,note=N8,bf_score=G(N5),bf_grade=N6);NB=Ed()
						if NB:A.success(f"✅ {F} saved to Watchlist (Google Sheet updated!)")
						else:A.info(f"✅ {F} added to session Watchlist (Sheet write failed — check secrets).")
						A.rerun()
				with NA:
					if FA:
						if A.button(f"❌ Remove {F} from Watchlist",use_container_width=B,key='wl_rm_btn'):G_(F);Ed();A.rerun()
				A.markdown(c);A.markdown('#### 🗂️ Your Full Watchlist')
				if A.session_state.watchlist:
					NC=[{j:B,'CMP (₹)':A[A4],D2:A.get(CT,C),GM:A.get(Bj,C),D1:A.get(BI,C),'Added':A.get(D3,C)}for(B,A)in A.session_state.watchlist.items()];Hx=H.DataFrame(NC);A.dataframe(Hx,use_container_width=B,hide_index=B);Hy=io.BytesIO()
					with H.ExcelWriter(Hy,engine=D6)as ND:Hx.to_excel(ND,index=J,sheet_name=G0)
					A.download_button('📥 Download Watchlist as Excel',data=Hy.getvalue(),file_name=f"Watchlist_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=B,key='dl_wl_excel_tab');NE='\n'.join([f"• {B} — Score:{A.get(CT,C)} {A.get(Bj,C).split()[0]if A.get(Bj)else C} — {A.get(BI,C)[:30]}"for(B,A)in AL(A.session_state.watchlist.items())[:15]]);Hz=f"📊 *My NSE Watchlist*\n\n{NE}\n\n🕒 {l.now().strftime(EF)}";NF=urllib.parse.quote(Hz);NG=urllib.parse.quote(Hz);A.markdown(C);NH,NI=A.columns(2)
					with NH:A.markdown(f"<a href='https://wa.me/?text={NF}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share Watchlist on WhatsApp</button></a>",unsafe_allow_html=B)
					with NI:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NG}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share Watchlist on Telegram</button></a>",unsafe_allow_html=B)
				else:A.info('Your watchlist is empty. Add stocks using the button above!')
			with A9[13]:
				A.markdown(f"### 📰 Latest News & Alerts: **{F}**");import urllib.request,urllib.parse,xml.etree.ElementTree as C3,datetime as l,email.utils
				def NJ(pubdate_str):
					try:
						E=email.utils.parsedate_to_datetime(pubdate_str);F=l.datetime.now(l.timezone.utc);G=F-E;A=G.total_seconds()
						if A<0:return AH
						if A<60:return f"{U(A)} secs ago"
						if A<3600:B=U(A/60);return f"{B} min{"s"if B!=1 else C} ago"
						if A<86400:D=U(A/3600);return f"{D} hour{"s"if D!=1 else C} ago"
						if A<172800:return'Yesterday'
						H=U(A/86400);return f"{H} days ago"
					except g:return GN
				@A.cache_data(ttl=600)
				def NK(target_symbol,limit=10):
					try:
						I=urllib.parse.quote(f'"{target_symbol}" stock share news NSE India');J=f"https://news.google.com/rss/search?q={I}&hl=en-IN&gl=IN&ceid=IN:en";K=urllib.request.Request(J,headers={CY:CZ})
						with urllib.request.urlopen(K)as M:N=M.read()
						O=C3.fromstring(N);P=[D4,EG,CS,EH,EI,EJ,EK,EL];E=[]
						for A in O.findall(DD):
							F=A.find(A5).text;Q=A.find(f).text;G=A.find(Ar).text if A.find(Ar)is not D else C;R=AZ(A in F.lower()for A in P);S=GO if R else C
							try:H=email.utils.parsedate_to_datetime(G)
							except g:H=l.datetime.min.replace(tzinfo=l.timezone.utc)
							E.append({AD:f"{S}{F}",f:Q,L:NJ(G),AI:H})
						E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
					except g:return[]
				with A.spinner(f"Fetching today's latest news for {F}..."):
					H_=NK(F,limit=10)
					if H_:
						for N in H_:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>",unsafe_allow_html=B)
					else:A.info(f"No recent news found for {F}.")
			with A9[0]:
				with A.expander(f"🕯️ Price Chart & Technical Indicators — {F}",expanded=B):
					NL=A.select_slider('History range:',options=['3mo','6mo','1y','2y','5y'],value='1y',key=f"chart_period_{F}")
					with A.spinner(f"Loading price history for {F}..."):m=LP(F,period=NL)
					if m.empty or BG not in m.columns:A.warning(f"⚠️ No historical price data available for **{F}** via Yahoo Finance (tried `{F}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
					else:
						Ak=m[BG].squeeze().dropna();AK=M(Ak.iloc[-1]);Ba=M(Ak.iloc[-2])if Q(Ak)>1 else AK;Dg=(AK-Ba)/Ba*100 if Ba else i;I0=Ak.diff();NM=I0.clip(lower=0).rolling(14).mean();NN=(-I0.clip(upper=0)).rolling(14).mean();FB=100-100/(1+NM/NN.replace(0,M(A3)));Ck=FB.dropna().iloc[-1]if not FB.dropna().empty else D;NO,NP=A.tabs(['Price + EMAs','RSI'])
						with NO:
							NQ=A.radio('Chart type',[J_,'Line'],horizontal=B,key=f"chart_type_{F}");I1=Ak.diff();NR=I1.clip(lower=0).rolling(9).mean();NS=(-I1.clip(upper=0)).rolling(9).mean();Aw=100-100/(1+NR/NS.replace(0,M(A3)));FC=Aw.ewm(span=3,adjust=J).mean();I2=A6.arange(1,22,dtype=M);FD=Aw.rolling(21).apply(lambda x:M(A6.dot(x,I2)/I2.sum()),raw=B);u=AL(m.index);I3=Aw.values;Cl,I4=[],[];FE,I5=[],[]
							for BO in Ds(22,Q(Aw)):
								FF,I6=I3[BO],I3[BO-1]
								if A6.isnan(FF)or A6.isnan(I6):continue
								if FF>=50 and I6<50:
									Dh=Aw.index[BO]
									if Dh in Ak.index:Cl.append(Dh);I4.append(M(Ak.loc[Dh])*.993);FE.append(Dh);I5.append(M(FF))
							if not FC.dropna().empty and not FD.dropna().empty:FG=FC.dropna().iloc[-1];FH=FD.dropna().iloc[-1];FI=GP if FG>FH else GQ;NT='🟢 H-M: POSITIVE (Bullish)'if FG>FH else'🔴 H-M: NEGATIVE (Bearish)';A.markdown(f"<div style='background:{FI}22;border-left:4px solid {FI};padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;font-weight:700;color:{FI}'>{NT} — EMA3: {FG:.1f} | WMA21: {FH:.1f}</div>",unsafe_allow_html=B)
							e=L1(rows=3,cols=1,shared_xaxes=B,row_heights=[.55,.25,.2],vertical_spacing=.03,specs=[[{GR:'xy'}],[{GR:'xy'}],[{GR:'xy'}]])
							if NQ==J_:
								try:e.add_trace(P.Candlestick(x=u,open=m['Open'].squeeze(),high=m[EM].squeeze(),low=m[EN].squeeze(),close=m[BG].squeeze(),name='OHLC',increasing_line_color=GS,decreasing_line_color=GT,increasing_fillcolor=GS,decreasing_fillcolor=GT,line=E(width=1.6),whiskerwidth=.9),row=1,col=1)
								except g:e.add_trace(P.Scatter(x=u,y=Ak,name=BG,line=E(color=AE,width=2)),row=1,col=1)
							else:e.add_trace(P.Scatter(x=u,y=Ak,name=BG,line=E(color=AE,width=2)),row=1,col=1)
							for(NU,NV,NW)in[(20,K0,'EMA20'),(50,'#FF6D00','EMA50'),(200,'#2979FF','EMA200')]:NX=Ak.ewm(span=NU,adjust=J).mean();e.add_trace(P.Scatter(x=u,y=NX,name=NW,line=E(color=NV,width=1.8)),row=1,col=1)
							I7=M(m[EM].max());I8=M(m[EN].min());e.add_hline(y=I7,line_dash=E9,line_color=K1,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W High ₹{I7:,.2f}",annotation_position=K2,annotation_font=E(color=K1,size=13));e.add_hline(y=I8,line_dash=E9,line_color=K3,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W Low ₹{I8:,.2f}",annotation_position='bottom right',annotation_font=E(color=K3,size=13))
							if Cl:e.add_trace(P.Scatter(x=Cl,y=I4,mode=EA,name='H-M Entry (RSI>50)',marker=E(color='lime',size=12,symbol=K4,line=E(color='white',width=1.5))),row=1,col=1)
							try:I9=m[DE].squeeze();NY=m['Open'].squeeze();NZ=m[BG].squeeze();Na=[GS if B>=A else GT for(A,B)in zip(NY.tolist(),NZ.tolist())];e.add_trace(P.Bar(x=u,y=I9.tolist(),name=DE,marker=E(color=Na,line=E(width=0)),opacity=.85,showlegend=J),row=3,col=1);Nb=I9.rolling(20).mean();e.add_trace(P.Scatter(x=u,y=Nb.tolist(),name='Vol Avg(20)',line=E(color='#616161',width=1.2,dash=DF)),row=3,col=1)
							except g:pass
							Di=Aw.reindex(Aw.index);IA=H.Series(5e1,index=Aw.index);Nc=Di.where(Di>=50,5e1);e.add_trace(P.Scatter(x=u,y=IA.tolist(),line=E(width=0),mode=EO,showlegend=J,hoverinfo=EP),row=2,col=1);e.add_trace(P.Scatter(x=u,y=Nc.tolist(),fill=K5,fillcolor='rgba(38,166,154,0.35)',line=E(width=0),mode=EO,showlegend=J,hoverinfo=EP),row=2,col=1);Nd=Di.where(Di<=50,5e1);e.add_trace(P.Scatter(x=u,y=IA.tolist(),line=E(width=0),mode=EO,showlegend=J,hoverinfo=EP),row=2,col=1);e.add_trace(P.Scatter(x=u,y=Nd.tolist(),fill=K5,fillcolor='rgba(239,83,80,0.35)',line=E(width=0),mode=EO,showlegend=J,hoverinfo=EP),row=2,col=1);e.add_trace(P.Scatter(x=u,y=Aw.tolist(),name='RSI(9)',line=E(color='#1976D2',width=1.5)),row=2,col=1);e.add_trace(P.Scatter(x=u,y=FC.tolist(),name='EMA3',line=E(color='#4CAF50',width=1.5)),row=2,col=1);e.add_trace(P.Scatter(x=u,y=FD.tolist(),name='WMA21',line=E(color='#EF5350',width=1.5)),row=2,col=1)
							if FE:e.add_trace(P.Scatter(x=FE,y=I5,mode=EA,name='Entry (RSI panel)',showlegend=J,marker=E(color='lime',size=6,symbol=K4,line=E(color='white',width=1))),row=2,col=1)
							e.add_hline(y=70,line_dash=DF,line_color=GQ,opacity=.5,row=2,col=1);e.add_hline(y=50,line_dash=E9,line_color='#888888',row=2,col=1,annotation_text='50',annotation_position='right');e.add_hline(y=30,line_dash=DF,line_color=K0,opacity=.8,row=2,col=1,annotation_text='30',annotation_position='right');e.update_layout(template=q,height=950,title=E(text=f"{F} — Ultra HD Chart (Price, EMAs, H-M, Volume)",font=E(size=12,color='#0E1117',family=EQ)),margin=E(t=60,b=80,l=20,r=20),xaxis_rangeslider_visible=J,xaxis2_rangeslider_visible=J,xaxis3_rangeslider_visible=J,legend=E(orientation='h',y=-.15,x=.5,xanchor='center',yanchor='top',font=E(size=13,color=K6,family=EQ)),hovermode='x unified',font=E(size=13,color=K6,family=EQ),hoverlabel=E(font_size=14,font_family=EQ,bgcolor='rgba(255,255,255,0.95)'),plot_bgcolor=ER,paper_bgcolor=ER,bargap=.15);e.update_xaxes(showspikes=B,spikemode='across+toaxis',spikesnap='cursor',spikethickness=1.5,spikedash='solid',spikecolor='#808495',gridcolor=K7,linecolor=GU,tickfont=E(size=12,family=K8));e.update_yaxes(gridcolor=K7,zeroline=J,linecolor=GU,tickfont=E(size=12,family=K8));e.update_yaxes(range=[0,100],row=2,col=1);e.update_yaxes(title_text=BK,title_font=E(size=14,weight=AR),row=1,col=1);e.update_yaxes(title_text='RSI / H-M',title_font=E(size=14,weight=AR),row=2,col=1);e.update_yaxes(title_text=DE,title_font=E(size=14,weight=AR),row=3,col=1);Ne={Jr:J,'responsive':B,'toImageButtonOptions':{'format':'png','filename':f"{F}_Ultra_HD_Analysis",'height':1080,'width':1920,'scale':6},'modeBarButtonsToAdd':['drawline','drawopenpath','drawrect','eraseshape']};A.plotly_chart(e,use_container_width=B,key=f"price_ema_chart_{F}",config=Ne)
							if Cl:A.caption(f"🟢 {Q(Cl)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). **H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). For informational purposes only.")
							else:A.caption('**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). 🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only.')
							X={}
							if y!=BF:
								Dj=DI(BF)
								if not Dj.empty:
									Nf=[A for A in Dj.columns if not A.startswith(Aa)and not A.startswith(Ab)];IB=S((A for A in Nf if A.lower()in[Cz,Ac,Dw,Dx,C_,Dy]),D)
									if IB:
										IC=Dj[Dj[IB].astype(G).str.strip()==F]
										if not IC.empty:Ng=IC.iloc[0].to_dict();X={A:B for(A,B)in Ng.items()if not G(A).startswith(Aa)and not G(A).startswith(Ab)and G(A)!=n}
							def Y(row,primary_dict,*K):
								def B(r_data):
									J='n/a';B=r_data
									if B is D or Q(B)==0:return k
									try:H=AL(B.keys())if Az(B,E)else AL(B.index)
									except g:return k
									H=[A for A in H if not G(A).startswith(Aa)and not G(A).startswith(Ab)and G(A)!=n]
									for L in K:
										I=L.lower().strip()
										for F in H:
											if G(F).strip().lower()==I:
												A=B.get(F,C);A=C if A is D else G(A).strip()
												if A not in(C,A3,AO,D8,J,k):return A
										for F in H:
											if I in G(F).strip().lower():
												A=B.get(F,C);A=C if A is D else G(A).strip()
												if A not in(C,A3,AO,D8,J,k):return A
									return k
								A=B(primary_dict)
								if A==k:A=B(row)
								return A
							def ID(label,value):return f"<div style='background:var(--secondary-background-color,#F0F2F6);border:1px solid rgba(128,128,128,0.35);border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'><div style='font-size:11px;color:var(--text-color,#31333F);opacity:0.65;margin-bottom:3px;'>{label}</div><div style='font-size:14px;font-weight:700;color:var(--text-color,#0E1117);word-break:break-word;'>{value}</div></div>"
							def FJ(title,fields):D=C.join(ID(A,Y(T,X,*B))for(A,B)in fields);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
						with NP:Nh=AL(m.index);B8=P.Figure();B8.add_trace(P.Scatter(x=Nh,y=FB,name=K9,line=E(color='#AB47BC',width=2)));B8.add_hline(y=70,line_dash=DF,line_color=GQ,opacity=.6);B8.add_hline(y=30,line_dash=DF,line_color=GP,opacity=.6);B8.add_hrect(y0=45,y1=65,fillcolor=GP,opacity=.06,line_width=0,annotation_text='Ideal entry 45-65',annotation_position=K2);B8.update_layout(template=q,height=280,yaxis=E(range=[0,100]),margin=E(t=30,b=20),plot_bgcolor=ER,paper_bgcolor=ER,font=E(color='#1A1A1A'));B8.update_xaxes(gridcolor=KA);B8.update_yaxes(gridcolor=KA);A.plotly_chart(B8,use_container_width=B,key=f"rsi14_chart_{F}")
				A.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>",unsafe_allow_html=B)
				with A.expander(f"📋 {F} — Google Sheet Data",expanded=B):
					def Ni(title,items):D=C.join(ID(A,B)for(A,B)in items);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
					Nj='▲'if Dg>=0 else'▼';Nk='#00A152'if Dg>=0 else'#D32F2F';Ni('📊 Price Snapshot',[(KB,f"₹{AK:,.2f} <span style='color:{Nk};font-size:12px;'>{Nj} {Dg:+.2f}%</span>"),(An,f"₹{M(m[EM].max()):,.2f}"),(Ao,f"₹{M(m[EN].min()):,.2f}"),(K9,f"{Ck:.1f}"if Ck is not D else'–')])
					with A.expander('📋 Company Price Dashboard',expanded=J):FJ('🏢 Company Info',[('Company Name',[Jw,Jx]),(GV,[E7,G3]),(Am,[KC,KD,E3]),('52W High Date',[Jm,'52 week high date']),('52W Low Date',[Jn,'52 week low date']),(A2,[Ap]),(DE,[G8])]);FJ('📡 Signals & System Output',[(JA,[JZ]),('Difference from 200 DMA',['difference from 200 dma','differance from 200 dma']),('CAR Rating',['cumulative average rule (car) rating','car rating']),('Start GTT Order',[Ja,'gtt order']),(Bp,[G4]),(Bq,[G5]),(Br,[G6]),(Bs,[Jb]),(Bt,[G7])]);FJ('💰 Fundamentals',[(Jj,['face value']),('Total Equity Capital',[GW]),(Jl,[G9]),('EPS',['eps']),(Jk,['ronw']),(Jh,[Fx,Fy]),(Ji,[KE,KF]),('Pledged %',[Fz,F_]),('D/E Ratio',[JQ,'de ratio']),('Net Sales (Cr)',[E2]),('Net Profit (Cr.)',[E1]),('Reserves (Cr)',[GX]),('Total Debt (Cr)',[GY]),('Inventory (Cr)',[GZ]),('Cash & Equiv (Cr)',[Ga,Gb,Gc]),('Operating Cash Flow (Cr)',['operating cash flow']),('Trade Receivables (Cr)',[Gd]),('Trade Payables (Cr)',[Ge]),('Fixed Assets/Net PPE (Cr)',[Gf,Gg]),('Total Assets (Cr)',[Gh]),('Open (₹)',['open price','open (','open']),('High (₹)',['day high','high price','high (']),('Low (₹)',['day low','low price','low (']),('Prev Close (₹)',['prev close','previous close',Jp]),('Price Change (₹)',['price change','change (','change in price']),('% Change',['% change',D0,'change %']),('Shares Outstanding (Cr)',['shares outstanding']),('Book Value (₹/share)',['book value']),('Public %',['public %','public holding']),('FII %',['fii %','fii holding','fii']),('DII %',['dii %','dii holding','dii'])])
					def d(raw):
						if raw in(D,k,C,A3,AO):return
						try:return M(G(raw).replace(AB,C).replace('₹',C).strip())
						except(AY,Fq):return
					def z(h,alpha=.35):return f"rgba({U(h[1:3],16)},{U(h[3:5],16)},{U(h[5:7],16)},{alpha})"
					if Ba and AK is not D:IE=AK-Ba;IF=P.Figure(P.Waterfall(orientation='v',measure=['absolute','relative','total'],x=['Prev Close','Change',KB],y=[Ba,IE,AK],text=[f"₹{Ba:,.2f}",f"{IE:+.2f}",f"₹{AK:,.2f}"],textposition='outside',textfont=E(color=As,size=13),increasing=E(marker=E(color=w)),decreasing=E(marker=E(color=AP)),totals=E(marker=E(color=AE)),connector=E(line=E(color=GU))));IF.update_layout(title=f"📈 Price Change Bridge — {F} ({Dg:+.2f}%)",template=q,height=300,showlegend=J,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IF,use_container_width=B,key=f"waterfall_price_{F}");A.caption("Prev Close → today's Price Change → Last Close. Shown as a Waterfall, not a Sankey, since a price drop can't be a negative flow.")
					else:A.info("Prev Close / Last Close not available for this stock, so the Price Change bridge can't be built.")
					Nl=Y(T,X,G8);Al=d(Y(T,X,KC,KD,E3));C4=d(Nl)
					if C4 is not D and Al is not D and 0<=Al<=100:FK=C4*Al/100;IG=C4-FK;IH=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Volume<br>{C4:,.0f} shares",f"Delivered<br>{FK:,.0f} shares ({Al:.1f}%)",f"Intraday / Non-Delivery<br>{IG:,.0f} shares ({100-Al:.1f}%)"],color=[Ca,w,B0]),link=E(source=[0,0],target=[1,2],value=[FK,IG],color=[z(w),z(B0)])));IH.update_layout(title=f"📦 Volume → Delivery Split — {F}",template=q,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IH,use_container_width=B,key=f"sankey_volume_{F}");A.caption('Total Volume split by % Delivery into shares actually delivered (genuine buying/holding) vs. shares traded intraday and squared off same day.')
					else:A.info("Volume / % Delivery not available for this stock, so the Volume → Delivery split can't be built.")
					if Ck is not D:II=P.Figure(P.Indicator(mode=KG,value=M(Ck),number=E(font=E(color=As,size=28)),title=E(text=f"RSI(14) — {F}",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AE),steps=[E(range=[0,30],color=Jq),E(range=[30,70],color='#f5f5f5'),E(range=[70,100],color=Bm)],threshold=E(line=E(color=DG,width=3),value=M(Ck)))));II.update_layout(template=q,height=260,margin=E(t=50,b=10,l=30,r=30));A.plotly_chart(II,use_container_width=B,key=f"gauge_rsi_{F}");A.caption("Below 30 = oversold, above 70 = overbought. A gauge, not a Sankey — RSI doesn't split into parts.")
					else:A.info('RSI(14) not available for this stock.')
					Dk=M(m[EM].max())if not m.empty else D;Cm=M(m[EN].min())if not m.empty else D
					if Dk and Cm is not D and Dk>Cm and AK is not D:IJ=AA(i,min(1e2,(AK-Cm)/(Dk-Cm)*100));IK=P.Figure(P.Indicator(mode=KG,value=IJ,number=E(suffix=AC,font=E(color=As,size=28)),title=E(text=f"52W Range Position — {F}<br><span style='font-size:11px'>Low ₹{Cm:,.2f} · Last ₹{AK:,.2f} · High ₹{Dk:,.2f}</span>",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AE),steps=[E(range=[0,33],color=Bm),E(range=[33,66],color=GB),E(range=[66,100],color=CU)],threshold=E(line=E(color=DG,width=3),value=IJ))));IK.update_layout(template=q,height=280,margin=E(t=65,b=10,l=30,r=30));A.plotly_chart(IK,use_container_width=B,key=f"gauge_52wrange_{F}");A.caption("0% = at the 52-week low, 100% = at the 52-week high. A gauge, not a Sankey — price levels aren't a splittable quantity.")
					else:A.info('52-week High/Low/Last Close not available for this stock.')
					C5=d(Y(T,X,Ap));FL=J
					if C5 is D and C4 is not D and AK:C5=C4*AK/1e7;FL=B
					if C5 is not D and Al is not D and 0<=Al<=100:FM=C5*Al/100;IL=C5-FM;IM=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"{"Est. "if FL else C}Turnover<br>₹{C5:,.2f} Cr",f"Delivered Value<br>₹{FM:,.2f} Cr ({Al:.1f}%)",f"Intraday Value<br>₹{IL:,.2f} Cr ({100-Al:.1f}%)"],color=[Ca,w,B0]),link=E(source=[0,0],target=[1,2],value=[FM,IL],color=[z(w),z(B0)])));IM.update_layout(title=f"💵 Turnover → Delivery Split — {F}",template=q,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IM,use_container_width=B,key=f"sankey_turnover_{F}");Nm=" Your sheet's Turnover field is blank for this stock, so this uses an estimate (Volume × Last Close) — the same fallback this app already uses elsewhere."if FL else C;A.caption(f"Turnover split by % Delivery, mirroring the Volume split above in ₹ terms.{Nm}")
					else:A.info("Turnover / % Delivery / Volume not available for this stock, so the Turnover → Delivery split can't be built.")
					C6=d(Y(T,X,G9));C7=d(Y(T,X,Fx,Fy));C8=d(Y(T,X,KE,KF));FN=d(Y(T,X,Fz,F_))
					if C6 is not D and C6>0 and(C7 is not D or C8 is not D):
						C7=C7 or i;C8=C8 or i;IN=AA(i,1e2-C7-C8);Cn=C6*C7/100;IO=C6*C8/100;IP=C6*IN/100;IQ=[f"Market Cap<br>₹{C6:,.2f} Cr",f"Promoters<br>₹{Cn:,.2f} Cr ({C7:.1f}%)",f"Institutional<br>₹{IO:,.2f} Cr ({C8:.1f}%)",f"Public / Other<br>₹{IP:,.2f} Cr ({IN:.1f}%)"];IR=[Ca,AE,w,ES];IS=[0,0,0];IT=[1,2,3];IU=[Cn,IO,IP];IV=[z(A)for A in[AE,w,ES]];IW=C
						if FN is not D and Cn>0:FO=Cn*FN/100;IX=Cn-FO;IQ+=[f"Pledged (of Promoters)<br>₹{FO:,.2f} Cr ({FN:.1f}%)",f"Free / Unpledged<br>₹{IX:,.2f} Cr"];IR+=[DG,Cw];IS+=[1,1];IT+=[4,5];IU+=[FO,IX];IV+=[z(DG),z(Cw)];IW=" Promoters' holding is further split into Pledged vs Free based on Pledged %."
						IY=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=IQ,color=IR),link=E(source=IS,target=IT,value=IU,color=IV)));IY.update_layout(title=f"🧾 Shareholding Pattern — Who Owns {F}",template=q,height=380,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(IY,use_container_width=B,key=f"sankey_shareholding_{F}");A.caption(f'Market Cap × holding % from the Fundamentals data above. "Public / Other" absorbs whatever isn\'t reported as Promoters/Institutional (Public %, FII %, DII % show "-" for stocks where your sheet doesn\'t break those out separately).{IW}')
					else:A.info("Market Cap / shareholding % data not available for this stock, so the Shareholding Pattern flow can't be built.")
					Bb=d(Y(T,X,E2));B9=d(Y(T,X,E1))
					if Bb is not D and B9 is not D and 0<B9<Bb:IZ=Bb-B9;FP=B9/Bb*100;Ia=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Net Sales<br>₹{Bb:,.2f} Cr (100%)",f"Net Profit<br>₹{B9:,.2f} Cr ({FP:.1f}%)",f"Total Expenses<br>₹{IZ:,.2f} Cr ({100-FP:.1f}%)"],color=[AE,w,AP]),link=E(source=[0,0],target=[1,2],value=[B9,IZ],color=['rgba(15,157,88,0.35)','rgba(234,67,53,0.35)'])));Ia.update_layout(title=f"💰 Revenue & Expenses Flow — {F} (Net Margin {FP:.1f}%)",template=q,height=320,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ia,use_container_width=B,key=f"sankey_{F}");A.caption('Based on Net Sales / Net Profit from the Fundamentals data above. "Total Expenses" is the remainder (Net Sales − Net Profit) — your sheet doesn\'t carry a Cost-of-Revenue/Opex breakdown, so a multi-stage flow (Gross → Operating → Net) isn\'t available for this stock.')
					elif Bb is not D and B9 is not D:A.info(f"Revenue & Expenses flow needs a normal profitable split (0 < Net Profit < Net Sales). {F} currently shows Net Sales ₹{Bb:,.2f} Cr and Net Profit ₹{B9:,.2f} Cr, which doesn't fit a simple flow diagram (e.g. a net loss).")
					else:A.info("Net Sales / Net Profit not available for this stock, so the Revenue & Expenses flow can't be built.")
					Nn=d(Y(T,X,GW));No=d(Y(T,X,GX));Np=d(Y(T,X,GY));Nq=d(Y(T,X,Ge));Nr=[(KH,Nn,AE),(KI,No,w),(KJ,Np,AP),(KK,Nq,KL)];BA=[(B,A,C)for(B,A,C)in Nr if A is not D and A>0]
					if Q(BA)>=2:Ib=sum(B for(A,B,A)in BA);Ic=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Total Financing<br>₹{Ib:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/Ib*100:.1f}%)"for(B,A,C)in BA],color=[KM]+[B for(A,A,B)in BA]),link=E(source=[0]*Q(BA),target=AL(Ds(1,Q(BA)+1)),value=[B for(A,B,A)in BA],color=[z(B)for(A,A,B)in BA])));Ic.update_layout(title=f"🏗️ Capital Structure — How {F} Is Financed",template=q,height=300,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ic,use_container_width=B,key=f"sankey_capstruct_{F}");A.caption('Equity Capital + Reserves + Total Debt + Trade Payables, from the Fundamentals data above.')
					else:A.info('Not enough of Total Equity Capital / Reserves / Total Debt / Trade Payables available to build a Capital Structure flow.')
					C9=d(Y(T,X,Gh));Ns=[(KN,d(Y(T,X,Gf,Gg)),KO),(KP,d(Y(T,X,GZ)),B0),(KQ,d(Y(T,X,Gd)),KR),(KS,d(Y(T,X,Ga,Gb,Gc)),AE)];FQ=[(B,A,C)for(B,A,C)in Ns if A is not D and A>=0]
					if C9 is not D and C9>0 and FQ:
						Id=sum(B for(A,B,A)in FQ);FR=C9-Id
						if FR>=0:CA=FQ+([(KT,FR,ES)]if FR>0 else[]);Ie=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Total Assets<br>₹{C9:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/C9*100:.1f}%)"for(B,A,C)in CA],color=[Ca]+[B for(A,A,B)in CA]),link=E(source=[0]*Q(CA),target=AL(Ds(1,Q(CA)+1)),value=[B for(A,B,A)in CA],color=[z(B)for(A,A,B)in CA])));Ie.update_layout(title=f"📦 Asset Deployment — Where {F}'s Assets Sit",template=q,height=340,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ie,use_container_width=B,key=f"sankey_assets_{F}");A.caption('Fixed Assets, Inventory, Trade Receivables and Cash & Equivalents from the Fundamentals data above. "Other Assets" is the gap versus reported Total Assets (e.g. intangibles, investments, or other items your sheet doesn\'t itemize).')
						else:A.info(f"{F}'s itemized asset categories (₹{Id:,.2f} Cr) add up to more than the reported Total Assets (₹{C9:,.2f} Cr) — likely a data mismatch between sheet rows, so the Asset Deployment flow isn't shown to avoid a misleading chart.")
					else:A.info("Total Assets / asset-category data not available for this stock, so the Asset Deployment flow can't be built.")
					FS,If,Dl=[],[],[];CB,CC,CD,CE=[],[],[],[]
					def Bc(label,color,col_x):FS.append(label);If.append(color);Dl.append(col_x);return Q(FS)-1
					Nt,Nu,Ig,FT=.001,.24,.5,.999;Nv=[(KH,d(Y(T,X,GW)),AE),(KI,d(Y(T,X,GX)),w),(KJ,d(Y(T,X,GY)),AP),(KK,d(Y(T,X,Ge)),KL)];FU=[(B,A,C)for(B,A,C)in Nv if A is not D and A>0];Ih=Q(FU)>=2;BB=D
					if Ih:
						Dm=sum(B for(A,B,A)in FU);BB=Bc(f"Total Financing<br>₹{Dm:,.2f} Cr (100%)",KM,Nu)
						for(Ax,AG,Co)in FU:u=Bc(f"{Ax}<br>₹{AG:,.2f} Cr ({AG/Dm*100:.1f}%)",Co,Nt);CB.append(u);CC.append(BB);CD.append(AG);CE.append(z(Co))
					Bd=d(Y(T,X,Gh));Nw=[(KN,d(Y(T,X,Gf,Gg)),KO),(KP,d(Y(T,X,GZ)),B0),(KQ,d(Y(T,X,Gd)),KR),(KS,d(Y(T,X,Ga,Gb,Gc)),AE)];FV=[(B,A,C)for(B,A,C)in Nw if A is not D and A>=0];Dn=Bd is not D and Bd>0 and bool(FV)
					if Dn:Nx=sum(B for(A,B,A)in FV);FW=Bd-Nx;Dn=FW>=0
					if Dn:
						Ny=FV+([(KT,FW,ES)]if FW>0 else[]);Nz=f" ({Bd/Dm*100:.1f}%)"if BB is not D else KU;Ii=Bc(f"Total Assets<br>₹{Bd:,.2f} Cr{Nz}",Ca,Ig)
						if BB is not D:CB.append(BB);CC.append(Ii);CD.append(Bd);CE.append(z(Ca))
						for(Ax,AG,Co)in Ny:u=Bc(f"{Ax}<br>₹{AG:,.2f} Cr ({AG/Bd*100:.1f}%)",Co,FT);CB.append(Ii);CC.append(u);CD.append(AG);CE.append(z(Co))
					Be=d(Y(T,X,E2));CF=d(Y(T,X,E1));Ij=Be is not D and CF is not D and 0<CF<Be
					if Ij:
						Ik=Be-CF;N_=f" ({Be/Dm*100:.1f}%)"if BB is not D else KU;FX=Bc(f"Net Sales<br>₹{Be:,.2f} Cr{N_}",AE,Ig)
						if BB is not D:CB.append(BB);CC.append(FX);CD.append(Be);CE.append(z(AE))
						Il=CF/Be*100;O0=Bc(f"Net Profit<br>₹{CF:,.2f} Cr ({Il:.1f}%)",w,FT);O1=Bc(f"Total Expenses<br>₹{Ik:,.2f} Cr ({100-Il:.1f}%)",AP,FT);CB+=[FX,FX];CC+=[O0,O1];CD+=[CF,Ik];CE+=[z(w),z(AP)]
					O2=sum([Ih,Dn,Ij])
					if O2>0:
						from collections import defaultdict as Im;In=Im(U)
						for Cp in Dl:In[Cp]+=1
						Io=Im(U);Ip=[]
						for Cp in Dl:Ax=In[Cp];BO=Io[Cp];Io[Cp]+=1;Ip.append(b((BO+.5)/Ax,4)if Ax>1 else .5)
						Iq=P.Figure(P.Sankey(arrangement=Bu,textfont=E(color=As,size=13,family=Bv),node=E(pad=22,thickness=18,line=E(color=Bw,width=.5),label=FS,color=If,x=Dl,y=Ip),link=E(source=CB,target=CC,value=CD,color=CE)));Iq.update_layout(title=f"💎 Combined Money Flow — {F} (Financing → Assets / Revenue, merged)",template=q,height=560,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Iq,use_container_width=B,key=f"sankey_merged_{F}");A.caption("All money-related flows merged into one chart: financing sources (Equity + Reserves + Debt + Trade Payables) feed Total Financing, which splits into two parallel paths — Total Assets (incl. Trade Receivables) and Net Sales → Net Profit / Total Expenses. It's drawn as two branches off one hub, rather than one long chain, because Total Assets and Net Sales are different kinds of totals (balance sheet vs. P&L) that don't feed into each other. Trade Payables now also appears in the 🏗️ Capital Structure chart above.")
					else:A.info('Not enough financing / assets / revenue data available for this stock to build the Combined Money Flow chart.')
	A.markdown(c);A.subheader('📊 National Live Market Analytics Portal Framework');Z=A.tabs(['🔥 Most Active','🚀 Volume Gainers','🏆 Top Gainers/Losers','⭐ 52W Boundaries','📦 Stocks Traded','⚖️ Advances/Declines','🕒 Pre-Open Market','⚡ Price Band Hitters','🗺️ Index Ticker Heatmap','🎫 IPO Tracker','⚠️ Volume Shockers','📂 Document Reports','🖋️ TV Script Engine','🔮 MunafaSutra Tickers','🎯 Dhan Asset Registry','💎 Weekly Activity Metrics','🔧 ScanX Core Screener','🚦 ScanX Live Engine','🎨 Screener Exploration','📈 IPO Chittorgarh','🏷️ IPO Watch Panel','💓 NSE Pulse','📊 Chartink Screeners','📋 Chartink Dashboard','🗾 Chartink Atlas','📚 Mahesh Kaushik','💰 EFTI Wealth','✅ Securities Available','🏛️ Corporate Filings','📉 52W Low Market'])
	def a(url,label='Open in Browser'):return f"<div style='margin-bottom:8px;'><a href='{url}' target='_blank' style='display:inline-block; background:#1976d2; color:#fff; font-size:14px; font-weight:600;padding:8px 18px; border-radius:6px; text-decoration:none;'>🌐 {label}</a><span style='font-size:12px; color:#888; margin-left:12px;'>📱 Mobile: tap button if frame is blank</span></div>"
	with Z[0]:I='https://www.nseindia.com/market-data/most-active-equities';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[1]:I='https://www.nseindia.com/market-data/volume-gainers-spurts';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[2]:I='https://www.nseindia.com/market-data/top-gainers-losers';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[3]:I='https://www.nseindia.com/market-data/52-week-high-equity-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[4]:I='https://www.nseindia.com/market-data/stocks-traded';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[5]:I='https://www.nseindia.com/market-data/advance';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[6]:I='https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[7]:I='https://www.nseindia.com/market-data/upper-band-hitters';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[8]:I='https://www.nseindia.com/index-tracker/NIFTY%2050';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[9]:I='https://www.nseindia.com/market-data/all-upcoming-issues-ipo';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[10]:I='https://www.moneycontrol.com/stocks/market-stats/volume-shockers-nse/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[11]:I='https://www.nseindia.com/all-reports/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[12]:I='https://www.tradingview.com/scripts/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[13]:I='https://munafasutra.com/nse/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[14]:I='https://dhan.co/all-stocks-list/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[15]:I='https://dhan.co/stocks/market/most-active-stocks-this-week/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[16]:I='https://scanx.trade/create-custom-screener';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[17]:I='https://scanx.trade/stock-screener/live-market-screener';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[18]:I='https://www.screener.in/explore/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[19]:I='https://www.chittorgarh.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[20]:I='https://ipowatch.in/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[21]:I='https://nsepulse.streamlit.app/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[22]:I='https://chartink.com/screeners';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[23]:I='https://chartink.com/scan_dashboard';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[24]:I='https://chartink.com/atlas';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[25]:I='https://www.maheshkaushik.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[26]:I='https://eftiwealth.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[27]:I='https://www.nseindia.com/static/market-data/securities-available-for-trading';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[28]:I='https://www.nseindia.com/companies-listing/corporate-filings-announcements';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[29]:I='https://www.nseindia.com/market-data/52-week-low-equity-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	@DH
	def O3():
		y='0.00%';w='Worst -> Best';v='1 Day';e='RANK';d='📊 BF Grade';b='🔬 BF Score';a='CURRENT PRICE';W='STOCK NAME';A.markdown(c);A.markdown('### 📈 Multi-Horizon Performance Summary Matrix');x,AP=A.columns([4,1])
		with x:f=A.radio(GD,[GE,CW,CX],horizontal=B,help=KV,key='perf_matrix_sizing_mode')
		g=[v,'2 Day','3 Day','5 Day','7 Day','10 Day','12 Day','15 Days','20 Days','25 Days',Gi,'2 Months','3 Months','4 Months','5 Months','6 Months','7 Months','8 Months','9 Months','10 Months','11 Months',Gj,'18 Months','1.5 Years','2 Years','2.5 Years','3 Years',A2];z,A0,A1=A.columns([2,2,3])
		with z:h=A.selectbox('🎯 Base Horizon for Performance Ranking:',g,index=0)
		with A0:A4=A.radio('排序 Sorting Order Type:',['Best -> Worst',w],index=0,horizontal=B)
		with A1:j=A.text_input('🔍 Filter stocks inside this matrix...',placeholder=Jv,key=JU)
		V={}
		for I in g:
			if I==A2:
				if HC:V[I]=HC
				continue
			l=[I.lower(),I.lower().replace(' ',C),I.lower().replace('s',C)]
			if I==v:l.append(D0)
			for X in R:
				if AZ(A in X.lower()for A in l)and AC in X.lower():V[I]=X;break
		if V:
			m=[]
			for(AR,N)in K.iterrows():
				o=G(N.get(n,C)).strip();A5=N.get(A7,C)if A7 else C;A6=f"https://charting.nseindia.com/?symbol={o}-EQ";A8=f'<a href="{A6}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{o}</a>';L={W:A8,a:A5}
				for(I,A9)in V.items():
					p=G(N.get(A9,'0')).replace(AC,C).replace(AB,C).strip()
					try:L[I]=M(p)if p not in[C,A3,AO]else i
					except AY:L[I]=i
				if BQ:
					q=G(N.get(BQ,'0')).replace(AC,C).replace(AB,C).strip()
					try:L[Am]=M(q)if q not in[C,A3,AO]else i
					except AY:L[Am]=i
				if BR:
					r=G(N.get(BR,C)).replace(AC,C).replace(AB,C).strip()
					try:L[BL]=M(r)if r not in[C,A3,AO]else D
					except AY:L[BL]=D
				if BU:
					s=G(N.get(BU,C)).replace(AC,C).replace(AB,C).strip()
					try:L[B2]=M(s)if s not in[C,A3,AO]else D
					except AY:L[B2]=D
				if B5:
					t=G(N.get(B5,C)).replace(AB,C).strip()
					try:L[An]=M(t)if t not in[C,A3,AO]else D
					except AY:L[An]=D
				if B6:
					u=G(N.get(B6,C)).replace(AB,C).strip()
					try:L[Ao]=M(u)if u not in[C,A3,AO]else D
					except AY:L[Ao]=D
				if Ce:L[Bp]=G(N.get(Ce,C)).strip()
				if BS:L[Bq]=G(N.get(BS,C)).strip()
				if DR:L[Br]=G(N.get(DR,C)).strip()
				if DS:L[Bs]=G(N.get(DS,C)).strip()
				if BT:L[Bt]=G(N.get(BT,C)).strip()
				AD={A:B for(A,B)in N.items()if not G(A).startswith(Bo)};AE,AF,_=DK(AD,R);L[b]=AE;L[d]=AF;m.append(L)
			S=H.DataFrame(m)
			if j:S=S[S[W].str.replace(Dv,C,regex=B).str.contains(j,case=J,na=J)]
			AG=h if h in S.columns else S.columns[2];AH=A4==w;S=S.sort_values(by=AG,ascending=AH).reset_index(drop=B);S.insert(0,e,S.index+1);E=S.copy()
			for I in V.keys():
				if I in E.columns:
					if I==DE:E[I]=E[I].apply(lambda x:f"{U(x):,}"if H.notnull(x)else k)
					elif I==A2:E[I]=E[I].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else k)
					else:E[I]=E[I].apply(lambda x:f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)
			if Am in E.columns:E[Am]=E[Am].apply(lambda x:f"{x:.2f}%"if H.notnull(x)else k)
			if BL in E.columns:E[BL]=E[BL].apply(lambda x:f"{x:.2f}"if H.notnull(x)else k)
			if B2 in E.columns:E[B2]=E[B2].apply(lambda x:(f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)if H.notnull(x)else k)
			if An in E.columns:E[An]=E[An].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else k)
			if Ao in E.columns:E[Ao]=E[Ao].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else k)
			O=EX.from_dataframe(E);O.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);O.configure_column(e,width=70,pinned=DA);O.configure_column(W,width=140,pinned=DA,cellRenderer=DW);AI=B3('\n            function(params) {\n                if (params.value === undefined || params.value === null || params.colDef.field === "Volume") return null;\n                let val = parseFloat(String(params.value).replace(/[+%,]/g, \'\'));\n                if (val > 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#e6f4ea\', \'fontWeight\': \'bold\' };\n                if (val < 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#fce8e6\', \'fontWeight\': \'bold\' };\n                return null;\n            }\n            ');AJ=B3(KW);AK=B3("\n            function(params) {\n                let v = String(params.value);\n                if (v.includes('STRONG BUY')) return { 'backgroundColor': '#16e37f44', 'fontWeight': 'bold' };\n                if (v.includes('WATCHLIST')) return { 'backgroundColor': '#f4b40044', 'fontWeight': 'bold' };\n                if (v.includes('CAUTION')) return { 'backgroundColor': '#ff990044' };\n                return { 'backgroundColor': '#ea433544' };\n            }\n            ");AL=B3(KX)
			for F in E.columns:
				if F in(e,):continue
				if f==CW and Q(E)>0:Y=By(E.iloc[0][F]);Z=Q(G(F));P=U(AA(Y,Z)*7+22)
				elif f==CX and Q(E)>1:Y=By(E.iloc[1][F]);Z=Q(G(F));P=U(AA(Y,Z)*7+22)
				else:AM={W:140,a:130,Am:110,b:110,d:160,BL:100,B2:140,An:110,Ao:110,Bp:120,Bq:130,Br:130,Bs:130,Bt:130};P=AM.get(F,130)
				T=AA(70,min(P,90))
				if F==W:O.configure_column(F,width=P,minWidth=T,pinned=DA,cellRenderer=DW)
				elif F==a:O.configure_column(F,width=P,minWidth=T)
				elif F==b:O.configure_column(F,width=P,minWidth=T,cellStyle=AJ)
				elif F==d:O.configure_column(F,width=P,minWidth=T,cellStyle=AK)
				elif F in(Bp,Bq,Br,Bs,Bt):O.configure_column(F,width=P,minWidth=T,cellStyle=AL)
				elif F==A2:O.configure_column(F,width=P,minWidth=T)
				elif F in V or F==B2:O.configure_column(F,width=P,minWidth=T,cellStyle=AI)
				else:O.configure_column(F,width=P,minWidth=T)
			O.configure_grid_options(domLayout=AQ,rowHeight=38,headerHeight=45,enableCellTextSelection=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AN=O.build();EW(E,gridOptions=AN,theme=GF,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=450,width=GG,key='horizon_perf_grid')
	O3()
	@DH
	def O4():
		m='Key Reasons';l='Score (High→Low)';W='Score';A.markdown(c);A.markdown('### 🔬 Bottom Fishing Scanner — Buy from Bottom Candidates');A.caption('Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals');o,AI=A.columns([4,1])
		with o:a=A.radio(GD,[GE,CW,CX],horizontal=B,help=KV,key='bf_scanner_sizing_mode')
		p,q,r=A.columns([2,2,2])
		with p:X=A.slider('Minimum BF Score:',min_value=0,max_value=100,value=55,step=5,key='bf_min_score')
		with q:s=A.radio('Sort by:',[l,'Score (Low→High)'],horizontal=B,key='bf_sort')
		with r:b=A.text_input(Ju,placeholder='e.g. WIPRO',key=JV)
		L=[]
		for(AJ,d)in K.iterrows():
			E={A:B for(A,B)in d.items()if not G(A).startswith(Bo)};e,t,u=DK(E,R)
			if e>=X:
				f=G(d.get(n,C)).strip();v=E.get(A7,C)if A7 else C;g=S((A for A in R if E7 in A.lower()),D);w=E.get(g,C)if g else C;x=f"https://charting.nseindia.com/?symbol={f}-EQ";y=f'<a href="{x}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{f}</a>';P=D
				if BQ:
					h=G(E.get(BQ,C)).replace(AC,C).replace(AB,C).strip()
					try:P=M(h)if h not in[C,A3,AO]else D
					except AY:P=D
				z=G(E.get(BR,C)).strip()if BR else k;A0=G(E.get(BU,C)).strip()if BU else k;A1=G(E.get(B5,C)).strip()if B5 else k;A2=G(E.get(B6,C)).strip()if B6 else k;A4=G(E.get(Ce,C)).strip()if Ce else k;A5=G(E.get(BS,C)).strip()if BS else k;A6=G(E.get(DR,C)).strip()if DR else k;A8=G(E.get(DS,C)).strip()if DS else k;A9=G(E.get(BT,C)).strip()if BT else k;L.append({j:y,W:e,GM:t,AM:v,BL:z,Am:f"{P:.2f}%"if P is not D else k,B2:A0,An:A1,Ao:A2,Bp:A4,Bq:A5,Br:A6,Bs:A8,Bt:A9,GV:G(w)[:30],m:' | '.join(u[:3])})
		if b:L=[A for A in L if b.upper()in re.sub(Dv,C,A[j]).upper()]
		L.sort(key=lambda x:x[W],reverse=s==l)
		if L:
			A.success(f"✅ Found **{Q(L)}** stocks matching your bottom-fishing criteria (score ≥ {X})");I=H.DataFrame(L);N=EX.from_dataframe(I);N.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);AD=B3(KW);AE=B3(KX);AF={j:120,W:90,GM:160,AM:100,Am:110,GV:200,m:400,BL:100,B2:140,An:110,Ao:110,Bp:120,Bq:130,Br:130,Bs:130,Bt:130}
			for F in I.columns:
				if a==CW and Q(I)>0:Y=By(I.iloc[0][F]);Z=Q(G(F));O=U(AA(Y,Z)*7+22)
				elif a==CX and Q(I)>1:Y=By(I.iloc[1][F]);Z=Q(G(F));O=U(AA(Y,Z)*7+22)
				else:O=AF.get(F,120)
				T=DA if F==j else D;V=AA(70,min(O,90))
				if F==W:N.configure_column(F,width=O,minWidth=V,pinned=T,cellStyle=AD)
				elif F==j:N.configure_column(F,width=O,minWidth=V,pinned=T,cellRenderer=DW)
				elif F in(Bp,Bq,Br,Bs,Bt):N.configure_column(F,width=O,minWidth=V,pinned=T,cellStyle=AE)
				else:N.configure_column(F,width=O,minWidth=V,pinned=T)
			N.configure_grid_options(domLayout=AQ,rowHeight=40,headerHeight=45,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AG=N.build();EW(I,gridOptions=AG,theme=GF,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=400,width=GG,key='bf_scanner_grid');i=io.BytesIO()
			with H.ExcelWriter(i,engine=D6)as AH:Gv(I).to_excel(AH,index=J,sheet_name='Bottom Fishing')
			A.download_button('📥 Download BF Scanner Results',data=i.getvalue(),file_name=f"BottomFishing_{H.Timestamp.now().strftime(Bk)}.xlsx",mime=Bl)
		else:A.info(f"No stocks found with BF Score ≥ {X}. Try lowering the minimum score.")
	O4()
	if AJ:
		A.markdown(c);A.markdown('### 🏆 Top 10 & Bottom 10 Performers (Daily badges)');CG=K.copy();CG[AJ]=H.to_numeric(CG[AJ].astype(G).str.replace(BH,C,regex=B),errors=AN);CG=CG.dropna(subset=[AJ]);O5=CG.nlargest(10,AJ);O6=CG.nsmallest(10,AJ);AU,AV=A.columns(2)
		with AU:
			Ir="<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
			for(_,Bf)in O5.iterrows():
				Cq=G(Bf.get(n,C)).strip();AG=Bf[AJ];Cr=Bf.get(A7,C)if A7 else C
				try:Bg=M(G(Cr).replace(AB,C).strip());FY=M(AG);FZ=Bg/(1+FY/100);Fa=Bg-FZ;Cs=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{Fa:,.2f}</span>";Ct=f"₹{Bg:,.2f}"
				except:Ct=f"₹{Cr}";Cs=C
				Fb=f"https://charting.nseindia.com/?symbol={Cq}-EQ";Ir+=f"<a href='{Fb}' target='_blank' style='text-decoration:none;'><div style='background-color:#16e37f; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cq}: +{AG}%</span><span>{Cs}{Ct}</span></div></a>"
			A.markdown(Ir,unsafe_allow_html=B)
		with AV:
			Is="<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
			for(_,Bf)in O6.iterrows():
				Cq=G(Bf.get(n,C)).strip();AG=Bf[AJ];Cr=Bf.get(A7,C)if A7 else C
				try:Bg=M(G(Cr).replace(AB,C).strip());FY=M(AG);FZ=Bg/(1+FY/100);Fa=Bg-FZ;Cs=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{Fa:,.2f}</span>";Ct=f"₹{Bg:,.2f}"
				except:Ct=f"₹{Cr}";Cs=C
				Fb=f"https://charting.nseindia.com/?symbol={Cq}-EQ";Is+=f"<a href='{Fb}' target='_blank' style='text-decoration:none;'><div style='background-color:#f39991; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cq}: {AG}%</span><span>{Cs}{Ct}</span></div></a>"
			A.markdown(Is,unsafe_allow_html=B)
	A.markdown(c);A.markdown('### 📰 Global Market News, Alerts & Corporate Announcements');import urllib.request,urllib.parse,xml.etree.ElementTree as C3,pandas as H
	def Do(pubdate_str):
		try:
			D=H.to_datetime(pubdate_str,utc=B);G=H.Timestamp.now(tz=BM);A=(G-D).total_seconds()
			if A<0:return AH
			if A<60:return f"{U(A)} secs ago"
			if A<3600:E=U(A/60);return f"{E} min{"s"if E!=1 else C} ago"
			if A<86400:F=U(A/3600);return f"{F} hour{"s"if F!=1 else C} ago"
			if A<172800:return f"Yesterday ({D.strftime(EF)})"
			I=U(A/86400);return f"{I} days ago ({D.strftime(EF)})"
		except g:return GN
	@A.cache_data(ttl=600)
	def O7(symbol,limit=10):
		try:
			J=f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")';K=urllib.parse.quote(J);M=f"https://news.google.com/rss/search?q={K}&hl=en-IN&gl=IN&ceid=IN:en";N=urllib.request.Request(M,headers={CY:CZ})
			with urllib.request.urlopen(N)as O:P=O.read()
			Q=C3.fromstring(P);R=[D4,EG,CS,EH,EI,EJ,EK,EL];E=[]
			for A in Q.findall(DD):
				F=A.find(A5).text
				if not AZ(A in F.lower()for A in R):continue
				S=A.find(f).text;I=A.find(Ar).text if A.find(Ar)is not D else C
				try:G=H.to_datetime(I,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				T=H.Timestamp.now(tz=BM);U=(T-G).total_seconds()/86400
				if U<=15.:V=Do(I);E.append({AD:f"🚨 **[ALERT]** {F}",f:S,L:V,AI:G,KY:F})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def O8(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CY:CZ})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[];Q=[D4,EG,CS,EH,EI,EJ,EK,EL,KZ,Ka]
			for A in P.findall(DD):
				G=A.find(A5).text;R=A.find(f).text;I=A.find(Ar).text if A.find(Ar)is not D else C;S=AZ(A in G.lower()for A in Q);T=GO if S else C;U=f"{T}{G}"
				try:F=H.to_datetime(I,utc=B)
				except g:F=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=H.Timestamp.now(tz=BM);W=(V-F).total_seconds()/86400
				if W<=Aq:X=Do(I);E.append({AD:U,f:R,L:X,AI:F})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def O9(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CY:CZ})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[];Q=[D4,EG,CS,EH,EI,EJ,EK,EL,KZ,Ka]
			for A in P.findall(DD):
				F=A.find(A5).text;R=A.find(f).text;G=A.find(Ar).text if A.find(Ar)is not D else C;S=AZ(A in F.lower()for A in Q);T=GO if S else C;U=f"{T}{F}"
				try:I=H.to_datetime(G,utc=B)
				except g:I=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=Do(G);E.append({AD:U,f:R,L:V,AI:I})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OA(symbol,limit=6):
		try:
			I=f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")';J=urllib.parse.quote(I);K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CY:CZ})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[]
			for A in P.findall(DD):
				Q=A.find(A5).text;R=A.find(f).text;F=A.find(Ar).text if A.find(Ar)is not D else C
				try:G=H.to_datetime(F,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				S=Do(F);E.append({AD:f"📢 {Q}",f:R,L:S,AI:G})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	OB={'RELIANCE':'500325','TCS':'532540','HDFCBANK':'500180','INFY':Ke,'ICICIBANK':'532174','HINDUNILVR':'500696','SBIN':'500112','BHARTIARTL':'532454','BAJFINANCE':'500034','KOTAKBANK':'500247','LT':'500510','HCLTECH':'532281','AXISBANK':'532215','ASIANPAINT':'500820','MARUTI':'532500',Kb:Kf,'TITAN':'500114','ULTRACEMCO':'532538','ONGC':'500312','NTPC':'532555','POWERGRID':'532898','WIPRO':'507685','NESTLEIND':'500790','JSWSTEEL':'500228','TATASTEEL':'500470','TATAMOTORS':'500570','TECHM':'532755','GRASIM':'500300','ADANIENT':'512599','ADANIPORTS':'532921','COALINDIA':'533278','DIVISLAB':Kg,'DRREDDY':'500124','EICHERMOT':'505200','BAJAJFINSV':'532978','BAJAJ-AUTO':'532977','CIPLA':'500087','BRITANNIA':'500825','HEROMOTOCO':'500182',Kc:Kh,'HINDALCO':'500440','UPL':'512070','TATACONSUM':'500800','SBILIFE':'540719','HDFCLIFE':'540777','INDUSINDBK':'532187','BPCL':'500547','IOC':'530965','M&M':'500520','PIDILITIND':'500331','SIEMENS':'500550','HAVELLS':'517354','VOLTAS':'500575','AMBUJACEM':'500425','ACC':'500410','SHREECEM':'500387','RAMCOCEM':Ki,Kd:Kj,'JKCEMENT':'532644','STAR':Kk,'TVSMOTOR':'532343','BOSCHLTD':'500530','MUTHOOTFIN':'533398','CHOLAFIN':'500443','BAJAJHLDNG':'500490','TORNTPHARM':Kl,'AUROPHARMA':'524208','LUPIN':'500257','BIOCON':'532523','ALKEM':'539523','IPCALAB':'530827','GLAXO':'500660','ABBOTINDIA':'500488','PFIZER':'500680','SANOFI':'500674','MCDOWELL-N':'532432','ITC':'500875','GODFRYPHLP':'500163','COLPAL':'500830','DABUR':'500096','MARICO':'531642','GODREJCP':'532424','HINDPETRO':'500104','CASTROLIND':'500870','INDIGO':'521737','INTERGLOBE':'539448','SPICEJET':'500285','IRCTC':'542830','CONCOR':'531344','ADANIGREEN':'541450','ADANITRANS':'539254','TATAPOWER':'500400','TORNTPOWER':'532779','CESC':'500084','NHPC':'533098','SJVN':'533206','PFC':'532810','RECLTD':'532955','IRFC':'543257','ZOMATO':'543320','NYKAA':'543384','PAYTM':'543396','POLICYBZR':'543390','DELHIVERY':'543529','CARTRADE':'543202','RVNL':'542649','IRCON':'541956','NBCC':'534309','HUDCO':'540530','MMTC':Km,'MTNL':'500108','BEL':'500049','HAL':'541154','COCHINSHIP':'526235','MAZAGON':'543237','GRSE':'542351','MIDHANI':'541195','BEML':'500048','BHEL':'500103','SAIL':'500113','NMDC':'526371','MOIL':'533286','NATIONALUM':'532234','HINDZINC':'500188','VEDL':'500295','GMRINFRA':'532754','NHAI':'500253','IRB':'532947','ASHOKLEY':'500477','ESCORTS':'500495','FORCE':'517168','SML':'513275','MOTHERSON':'517334','MINDAIND':'532539','ENDURANCE':'540350','BALKRISIND':'502355','APOLLOTYRE':'500877','MRF':'500290','CEATLTD':'500878','JK TYRE':'530007','INOXWIND':'539083','SUZLON':'532667','RPOWER':'500390','JPPOWER':'532627','FEDERALBNK':'500469','IDFCFIRSTB':'539437','BANDHANBNK':'541153','RBLBANK':'540065','DCBBANK':'532772','KTKBANK':Kn,'SOUTHBANK':'532218','CANBK':'532483','BANKBARODA':'532134','UNIONBANK':'532477','INDIANB':'532814','UCOBANK':'532505','CENTRALBK':'532885','MAHABANK':'532525','J&KBANK':Kn,'PNB':'532461','IOB':'532388','BANKINDIA':'532149','DENABANK':'532121','SYNDIBANK':'532276','VIJAYABANK':'532245','ORIENTBANK':'500315','CORPBANK':'532179','ANDHRABANK':'532418','ALLAHABAD':Ko,'ALBK':Ko,'MFSL':'542299','HDFCAMC':'541530','NIPPONLIFE':'543171','UTIAMC':'543238','ABCAPITAL':'540691','ANGELONE':'543235','ICICIGI':'540716','GICRE':'540755','NIACL':'540769','STAR':Kk,'CROMPTON':'539876','ORIENTELEC':'531637','BLUESTAR':'500067','WHIRLPOOL':'500238','VGUARD':'532953','BAJAJEL':'500031','CERA':'532443','HINDWARE':'509820','HSIL':'509675','KAJARIACER':'500233','SOMANYCER':'532622','GRINDWELL':'506076','CARBORUNIV':'513375','ASTRAL':'532830','FINOLEX':'500940','SUPREMEIND':'509930','BERGER':'509480','KANSAINER':'500165','AKZOINDIA':'500710','INDIACEM':'530005','RAMCOIND':Ki,Kd:Kj,'HEIDELBERG':'500292','PRISM':'500338','BIRLACORPN':'500335','ORIENTCEM':'502420','SAGCEM':'502090','STARCEMENT':'540575','JKLAKSHMI':'500380','NUVOCO':'543334','ZYDUSLIFE':'532321','TORNTPHAR':Kl,'NATCOPHAR':'524816','GRANULES':'532482','LAURUS':Kp,'STRIDES':'532531','AJANTPHAR':'532331','CAPLIPOINT':'539266','DIVI':Kg,Kb:Kf,'GLAND':'543245','SEQUENT':'543225','METROPOLIS':'542650','DRLAL':'532259','THYROCARE':'539871','KRSNAA':'543328','VIJAYA':'532542','MAXHEALTH':'543220','KIMS':'543308','ASTER':'540975','FORTIS':'532843','NHOSPIT':'532526',Kc:Kh,'NARAYANA':'539551','YATHARTH':'544120','RAINBOW':'543524','SUVENPHAR':'530239','LAURUSLABS':Kp,'SOLARA':'541540','SHILPAMED':'530879','PERSISTENT':'533179','MINDTREE':'532819','MPHASIS':'526299','HEXAWARE':'532861','NIIT':'500304','KPIT':'542651','LTTS':'540115','COFORGE':'532541','ZENSAR':'504067','RAMSYSTEMS':'532370','MASTEK':'523704','SASKEN':'532663','TATAELXSI':'500408','CYIENT':'532175','SONATSOFTW':'532221','TANLA':'532790','LTIM':'540005','INFY':Ke,'ROUTE':'543228','BSOFT':'526301','NEWGEN':'540900','INTELLECT':'538835','NUCLEUS':'531209','NELCO':'504112','DELTACORP':'532840','WONDERLA':'538268','MAHINDCIE':'532756','STARHLTH':'543412','NAUKRI':'532777','JUSTDIAL':'535648','MATRIMONY':'539846','MAKEMYTRIP':Km,'IXIGO':'544229','RATEGAIN':'543417','TEAMLEASE':'539658','QUESS':'539978','SIS':'540673','SECURKLOUD':'539963','HAPPYFORGE':'543532','KALYANKJIL':'543278','SENCO':'543456','THANGAMAYL':'531509','TRIBHOVAND':'512415','PC JEWELLER':'534809','RAJESHEXPO':'531500'}
	@A.cache_data(ttl=600)
	def OC(bse_code,days_back=90):
		L='SUBCATNAME';A={Gk:[],Gl:[],Gm:[],Gn:[],ET:[]}
		try:
			import datetime as F;G=F.date.today();M=G-F.timedelta(days=days_back);N=M.strftime(Bk);O=G.strftime(Bk);P=f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w?pageno=1&strCat=-1&strPrevDate={N}&strScrip={bse_code}&strSearch=P&strToDate={O}&strType=C&subcategory=-1";Q={CY:CZ,'Referer':'https://www.bseindia.com/','Accept':'application/json'};R=urllib.request.Request(P,headers=Q)
			with urllib.request.urlopen(R,timeout=8)as S:T=EV.loads(S.read())
			for B in(T.get('Table')or[])[:30]:
				U=B.get('HEADLINE',C)or B.get(L,C);I=B.get('NEWS_DT',C)or B.get('DT_TM',C);J=B.get('NEWSID',C);V=f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{J}.pdf"if J else C
				try:K=H.to_datetime(I).strftime(EF)
				except g:K=I[:10]
				E=(B.get(L)or C).lower();D={A5:U,f:V,BJ:K}
				if AZ(A in E for A in['annual report','annual rep']):A[Gl].append(D)
				elif AZ(A in E for A in['credit rat','rating']):A[Gm].append(D)
				elif AZ(A in E for A in['concall','con call','earnings call','analyst']):A[Gn].append(D)
				elif AZ(A in E for A in['investor presentation','presentation',ET]):A[ET].append(D)
				else:A[Gk].append(D)
		except g:pass
		return A
try:
	CH=K[n].dropna().unique()
	if Q(CH)>0:
		OD,OE,OF,OG,OH,OI,OJ=A.tabs(['🚨 Latest Alerts Timeline','🏢 Alerts by Stock','📰 Smart News Engine (1 Day)','📰 Smart News Engine (All News)','📢 Corporate Announcements','📢 DOCUMENTS HUB','📜 Rules']);Cu=[];It=CH[:30]
		with A.spinner('Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)...'):
			for F in It:
				A0=G(F).strip();BC=O7(A0,limit=15)
				for Ax in BC:Ax[Ac]=A0;Cu.append(Ax)
		OK={A[Ac]for A in Cu};Iu={A[Ac]for A in Cu if Ae in A[L]or Af in A[L]or Ag in A[L]or AH in A[L]}
		def OL(sym):
			A=sym
			if A in Iu:B,C,D=Ad,'#003300','#0fbf62'
			elif A in OK:B,C,D='#1a7a45',Cy,'#145e34'
			else:B,C,D='#444',Cy,'#333'
			return f"<span style='background:{B}; color:{C}; padding:2px 9px; border-radius:5px; font-weight:700; font-size:0.82em; border:1px solid {D}; white-space:nowrap;'>⚡ {A}</span>"
		with OD:
			OM,ON,OO=A.columns([2,1,1]);Iv=OM.text_input('🔍 Search Alerts:',placeholder='e.g. ICICIBANK, circuit...',key='global_news_search');Iw=ON.selectbox('⏳ Time Filter:',['All (Up to 15 Days)',Kq,Kr],key='global_news_time');OP=OO.radio('↕️ Sort By Time:',[Ks,'Oldest First'],horizontal=B,key='global_news_sort');Ay=Cu.copy()
			if Iv:Ix=Iv.lower();Ay=[A for A in Ay if Ix in A[Ac].lower()or Ix in A[KY].lower()]
			if Iw==Kr:Ay=[A for A in Ay if Ae in A[L]or Af in A[L]or Ag in A[L]or AH in A[L]]
			elif Iw==Kq:OQ=H.Timestamp.now(tz=BM);Ay=[A for A in Ay if(OQ-A[AI]).total_seconds()/86400<=7.]
			Ay.sort(key=lambda x:x[AI],reverse=OP==Ks);A.markdown(CV,unsafe_allow_html=B)
			if Ay:
				for N in Ay:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;OR=OL(N[Ac]);A.markdown(f"- {OR}&nbsp; <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>",unsafe_allow_html=B)
			else:A.info('No circuit or 52-week alerts match your search or filter criteria.')
		with OE:
			OS=A.columns(2);Fc=0
			for A0 in[G(A).strip()for A in It]:
				Dp=[A for A in Cu if A[Ac]==A0];Dp.sort(key=lambda x:x[AI],reverse=B)
				if Dp:
					with OS[Fc%2]:
						OT='🟢'if A0 in Iu else'🟡'
						with A.expander(f"{OT} {A0} Action Alerts (0 Sec to 15 Days)",expanded=B):
							OU=Dp[:3];Fd=Dp[3:]
							for N in OU:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fd:
								with A.expander(f"🔽 Show {Q(Fd)} more older alerts",expanded=J):
									for N in Fd:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fc+=1
			if Fc==0:A.info('No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.')
		with OF:
			A.markdown('### Latest News & Action Alerts (Past 24 Hours)');OV=A.columns(2);Fe=0
			for Cv in CH[:10]:
				A0=G(Cv).strip();BC=O8(A0,limit=5)
				if BC:
					with OV[Fe%2]:
						with A.expander(f"📰 {A0} News Feed (0 Sec to 1 Day)",expanded=B):
							for N in BC:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fe+=1
			if Fe==0:A.info('No general news found for the currently filtered stocks in the last 24 hours.')
		with OG:
			A.markdown('### Latest News & Action Alerts (All Time)');OW=A.columns(2);Ff=0
			for Cv in CH[:10]:
				A0=G(Cv).strip();BC=O9(A0,limit=6)
				if BC:
					with OW[Ff%2]:
						with A.expander(f"📰 {A0} News Feed (All News)",expanded=B):
							OX=BC[:3];Fg=BC[3:]
							for N in OX:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fg:
								with A.expander(f"🔽 Show {Q(Fg)} more articles",expanded=J):
									for N in Fg:h=Ae in N[L]or Af in N[L]or Ag in N[L]or AH in N[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Ff+=1
			if Ff==0:A.info('No general news found for the currently filtered stocks.')
		with OH:
			A.markdown('### 📢 Official Exchange Filings & Corporate Announcements');A.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>",unsafe_allow_html=B);A.markdown(CV,unsafe_allow_html=B);OY=A.columns(2);Fh=0
			for Cv in CH[:15]:
				A0=G(Cv).strip();Fi=OA(A0,limit=7)
				if Fi:
					with OY[Fh%2]:
						with A.expander(f"📢 {A0} Filings & Announcements",expanded=B):
							OZ=Fi[:3];Fj=Fi[3:]
							for A1 in OZ:h=Ae in A1[L]or Af in A1[L]or Ag in A1[L]or AH in A1[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{A1[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A1[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {A1[L]}</span>",unsafe_allow_html=B)
							if Fj:
								with A.expander(f"🔽 Show {Q(Fj)} more filings",expanded=J):
									for A1 in Fj:h=Ae in A1[L]or Af in A1[L]or Ag in A1[L]or AH in A1[L];s=Ad if h else B1;t=AR if h else AQ;A.markdown(f"- <a href='{A1[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A1[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {A1[L]}</span>",unsafe_allow_html=B)
					Fh+=1
			if Fh==0:A.info('No recent corporate filings or official announcements found for the filtered stocks.')
		with OI:
			A.markdown('### 📄 Documents Hub — Announcements · Annual Reports · Credit Ratings · Concalls · PPT · REC');A.markdown("<span style='font-size:0.88em; color:#888;'>Live BSE India filings (public API, no key needed). Annual Reports & Concalls also link to Screener.in.</span>",unsafe_allow_html=B);A.markdown(CV,unsafe_allow_html=B);Oa,Ob,Oc=A.columns([3,1.2,1.2])
			with Oa:Iy=[G(A).strip()for A in CH[:60]];Iz=A.multiselect('🔍 Stocks to view:',options=Iy,default=Iy[:4],key='doc_hub_stocks_v2')
			with Ob:Od=A.selectbox('📅 Date range:',[Gi,Kt,Ku,Gj],index=1,key='doc_days_v2')
			with Oc:I_=A.selectbox('📋 Rows per section:',[3,5,8,12],index=1,key='doc_limit_v2')
			Oe={Gi:30,Kt:90,Ku:180,Gj:365};Of=Oe[Od]
			if not Iz:A.info('Select at least one stock above to view its documents.')
			else:
				for o in Iz:
					v=OB.get(o.upper(),C)
					with A.expander(f"📁  {o}   {"· BSE "+v if v else"· BSE code not mapped — Screener links shown"}",expanded=B):
						Fk="<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>";Og=[('📢 BSE Announcements',f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",Kv,Kw),('📑 Annual Reports',f"https://www.screener.in/company/{o}/",CU,Kx),('⭐ Credit Ratings',f"https://www.screener.in/company/{o}/",GB,'#f57f17'),('🎙️ Concalls',f"https://www.screener.in/company/{o}/",'#fce4ec',DG),('📊 Investor PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={v}"if v else f"https://www.screener.in/company/{o}/",Ky,Kz),('🏛️ NSE Filings',f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",'#e0f7fa','#00695c'),('📈 Screener',f"https://www.screener.in/company/{o}/",'#fffde7',B0)]
						for(Fl,Fm,Fn,Fo)in Og:Fk+=f"<a href='{Fm}' target='_blank' style='background:{Fn}; color:{Fo}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{Fl}</a>"
						Fk+=Cx;A.markdown(Fk,unsafe_allow_html=B);CI={}
						if v:
							with A.spinner(f"Fetching BSE filings for {o}…"):CI=OC(v,days_back=Of)
						Oh,Oi,Oj,Ok=A.columns([3,2,2,3])
						with Oh:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #5c6bc0; padding-bottom:4px; color:#5c6bc0;'>📢 Announcements</p>",unsafe_allow_html=B);J0=CI.get(Gk,[])
							if J0:
								Ol,Om=A.tabs([GN,'All ↗'])
								with Ol:
									for CJ in J0[:I_]:BD=CJ[A5][:85]+'…'if Q(CJ[A5])>85 else CJ[A5];Bh=f"<a href='{CJ[f]}' target='_blank' style='color:#5c6bc0; text-decoration:none;'>{BD}</a>"if CJ[f]else f"<span>{BD}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid #c5cae9; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{CJ[BJ]}</span></div>",unsafe_allow_html=B)
								with Om:On=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{On}' target='_blank' style='color:#5c6bc0; font-size:0.85em;'>🔗 Open full announcements page →</a>",unsafe_allow_html=B)
							else:Oo=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{Oo}' target='_blank' style='color:#5c6bc0; font-size:0.83em;'>🔗 View on {"BSE"if v else"NSE"} →</a>",unsafe_allow_html=B);A.caption('No announcements in selected date range.')
						with Oi:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #43a047; padding-bottom:4px; color:#43a047;'>📑 Annual Reports</p>",unsafe_allow_html=B);J1=CI.get(Gl,[])
							if J1:
								for Dq in J1[:6]:J2=Dq[BJ][:4]if Dq[BJ]else'Report';Bh=f"<a href='{Dq[f]}' target='_blank' style='color:#43a047; text-decoration:none;'>📄 Annual Report {J2}</a>"if Dq[f]else f"<span>📄 Annual Report {J2}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{Bh}</div>",unsafe_allow_html=B)
							else:
								if v:A.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={v}' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 BSE Annual Reports →</a>",unsafe_allow_html=B)
								A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 View on Screener →</a>",unsafe_allow_html=B);A.caption('Not found in selected range — try 1 Year.')
						with Oj:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #f57f17; padding-bottom:4px; color:#f57f17;'>⭐ Credit Ratings</p>",unsafe_allow_html=B);J3=CI.get(Gm,[])
							if J3:
								for CK in J3[:4]:BD=CK[A5][:70]+'…'if Q(CK[A5])>70 else CK[A5];Bh=f"<a href='{CK[f]}' target='_blank' style='color:#f57f17; text-decoration:none;'>{BD}</a>"if CK[f]else f"<span>{BD}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffe0b2; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{CK[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#f57f17; font-size:0.83em;'>⭐ Ratings on Screener →</a>",unsafe_allow_html=B);A.markdown("<div style='font-size:0.78em; margin-top:8px; color:#888;'><a href='https://www.careratings.com' target='_blank' style='color:#888;'>CARE</a> · <a href='https://www.icra.in' target='_blank' style='color:#888;'>ICRA</a> · <a href='https://www.crisil.com' target='_blank' style='color:#888;'>CRISIL</a> · <a href='https://www.infomerics.com' target='_blank' style='color:#888;'>Infomerics</a></div>",unsafe_allow_html=B);A.caption('Not found via BSE — check links above.')
						with Ok:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #e53935; padding-bottom:4px; color:#e53935;'>🎙️ Concalls &amp; Investor Docs</p>",unsafe_allow_html=B);Op=CI.get(Gn,[]);J4=CI.get(ET,[]);J5=J4+Op
							if J5:
								for Bi in J5[:I_]:Oq=Bi in J4;J6='📊'if Oq else'🎙️';BD=Bi[A5][:70]+'…'if Q(Bi[A5])>70 else Bi[A5];Bh=f"<a href='{Bi[f]}' target='_blank' style='color:#e53935; text-decoration:none;'>{J6} {BD}</a>"if Bi[f]else f"<span>{J6} {BD}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffcdd2; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{Bi[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#e53935; font-size:0.83em;'>🎙️ Concalls on Screener →</a>",unsafe_allow_html=B);A.caption('No concalls/PPT in selected date range.')
							A.markdown(CV,unsafe_allow_html=B);Fp="<div style='display:flex; gap:6px; flex-wrap:wrap;'>";Or=[('📝 Transcript',f"https://www.screener.in/company/{o}/",Kv,Kw),('🤖 AI Summary',f"https://www.screener.in/company/{o}/",CU,Kx),('📊 PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={v}"if v else f"https://www.screener.in/company/{o}/",Ky,Kz),('▶️ REC',f"https://www.youtube.com/results?search_query={o}+concall+earnings",Bm,D7)]
							for(Fl,Fm,Fn,Fo)in Or:Fp+=f"<a href='{Fm}' target='_blank' style='background:{Fn}; color:{Fo}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{Fl}</a>"
							Fp+=Cx;A.markdown(Fp,unsafe_allow_html=B)
		with OJ:A.markdown('### 📜 Trading Rules');A.markdown("<span style='font-size:0.88em; color:#888;'>Edit the <code>TRADING_RULES_LIBRARY</code> constant near the top of the .py file to change anything shown below — same pattern as the AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",unsafe_allow_html=B);A.markdown(CV,unsafe_allow_html=B);A.markdown(L6)
	else:A.info('No stocks currently filtered to check.')
except g as BZ:A.error(f"⚠️ Could not load the News Engine. Error details: {BZ}")
else:A.warning('No data loaded. Check sheet sharing and secrets.')
