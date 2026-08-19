from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()

    automation = pagina.goto("https://practice-automation.com/form-fields/")

    print(pagina.title())

    nome = pagina.get_by_test_id("name-input")
    nome.click()
    nome.fill("Matheus")

    senha = pagina.get_by_role("textbox", name="Password")
    senha.click()
    senha.fill("abc123")

    coffe = pagina.get_by_test_id("drink3")
    coffe.click()

    automacao = pagina.get_by_test_id("automation").select_option("yes")
    cor_favorita = pagina.get_by_test_id("color2").check()
    email = pagina.get_by_test_id("email")
    email.click()
    email.fill("meuemail@email.com")
    mensagem = pagina.get_by_test_id("message")
    mensagem.click()
    mensagem.fill("Automação e muito massa!")

    # submit = pagina.get_by_test_id("submit-btn")
    # submit.click()
    time.sleep(4)
    navegador.close()
