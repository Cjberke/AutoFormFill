from selenium import webdriver

def init_form(google_form):
    
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    #option.add_argument("--headless")
    #option.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path='/Users/Cjberke/Downloads/chromedriver_win32/chromedriver.exe', options=option)
    browser.get(google_form)

    song_artist = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    className = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoice")
    submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    return(browser, song_artist, className, submitbutton)
