const SERVER_URL = 'http://127.0.0.1:8000/v1/'
const DOCS_URL = SERVER_URL + "contratos/"
const TOKEN_URL = SERVER_URL + "token/"
const USUARIO = "gaibarra"
const PASSWORD = "6Vlgpcr/zaira"
const credenciales = {"username":USUARIO,"password":PASSWORD}

const getToken = async () => {
    const r = await fetch(
        TOKEN_URL, {
        method="POST",
        body=JSON.stringify(credenciales),

        }
    )
}