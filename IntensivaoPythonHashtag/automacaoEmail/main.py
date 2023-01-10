import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.click(x=503, y=396)
time.sleep(5)
pyautogui.click(x=172, y=28)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(317, 273, clicks=2)
time.sleep(5)
pyautogui.click(398, 274)
time.sleep(5)
pyautogui.click(1160, 189)
time.sleep(5)
pyautogui.click(1001, 626)
time.sleep(10)
pyautogui.click(729, 448)

df = pd.read_excel(r"C:\Users\Dell\Downloads\Vendas - Dez.xlsx")
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()

'''
pyautogui.press('win')
time.sleep(5)
pyautogui.write('chrome')
pyautogui.click(x=503, y=396)
time.sleep(5)
pyautogui.click(x=172, y=28)
'''
pyautogui.hotkey('ctrl', 't')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(76, 196)
time.sleep(10)
pyautogui.write('laisa.fcardoso@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f'''
Prezados, Bom dia!

O faturamento de ontem foi de R$ {faturamento:,.2f}
A quantidade de produtos foi de: R$ {qtde_produtos:,}

Abs

'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

