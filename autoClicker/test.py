from pyautogui import alert, confirm, prompt, password, FAILSAFE

# alert(text='hey', title='', button='OK')
# confirm(text='hey', title='doubele hey', buttons=['OK', 'Cancel'])
# i = prompt(text='hey', title='dfg' , default='yo')
p = password(text='df', title='df', default='yi', mask='*')
print(FAILSAFE)

# coll = COLLECT(exe,
#                a.binaries,
#                a.zipfiles,
#                a.datas,
#                strip=False,
#                upx=True,
#                upx_exclude=[],
#                name='AutoClicker')