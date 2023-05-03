import time
from termcolor import cprint
import traceback
import os
import platform
import getpass


def path_to_ads_folder():
    # Определение ОС пользователя
    if platform.system() == 'Darwin':
        # Mac operating system
        folder_name = "dolphin_anty"
        username = getpass.getuser()
        path = os.path.join("/Users/", username + "/Library/Application Support/", folder_name)
        if os.path.exists(path):
            return path

    else:
        windows_drive = os.environ["SystemDrive"]
        folder_name = "dolphin_anty"
        username = getpass.getuser()
        path = os.path.join(rf"{windows_drive}/Users/", username + "/AppData/Roaming/", folder_name)
        if os.path.exists(path):
            return path


def runtime_lavamoat_editor(path):
    with open(path, 'r', encoding="utf-8") as read:
        lines = read.readlines()

    # Изменяет переменную scuttleGlobalThis на значение false
    with open(path, 'w', encoding="utf-8") as read:
        for line in lines:
            if line.startswith('    } = {"scuttleGlobalThis":true,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'):
                line = '    } = {"scuttleGlobalThis":false,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'
            read.write(line)


def runtime_lavamoat_editor2(path):
    with open(path, 'r', encoding="utf-8") as read:
        lines = read.readlines()

    # Изменяет переменную scuttleGlobalThis на значение false
    with open(path, 'w', encoding="utf-8") as read:
        for line in lines:
            if line.startswith('    } = {"scuttleGlobalThis":true,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'):
                line = '    } = {"scuttleGlobalThis":false,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'
            read.write(line)


if __name__ == '__main__':

    try:
        path_from_ads_settings = path_to_ads_folder()
        if path_from_ads_settings is None:
            raise FileNotFoundError

        path_to_js = fr'{path_from_ads_settings}/extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/runtime-lavamoat.js'
        runtime_lavamoat_editor(path_to_js)
        cprint(f'Фикс применен/fix applied', 'green')

    except FileNotFoundError:
        cprint(f'Файл не найден. Проверьте путь/наличие файла или обратитесь к разработчику.', 'red')

    except Exception as ex:
        traceback.print_exc()
        time.sleep(.3)
        cprint(f'Unexpected error. Обратитесь к разработчику.', 'red')

# ======================================================================================================================
# Created by Desti
# ======================================================================================================================
