from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from supabase import create_client

db_url = "https://ttpfqupzerfmplyigjlh.supabase.co"
db_key = "sb_publishable_rQr_fJI27eODJKM0-TOjAQ_kpgSrRBp"

db = create_client(db_url, db_key)

app = FastAPI()

@app.post('/add/contact')
async def add_contact(request:Request):
    data = await request.json() 
    result = db.table('contacts').insert(data).execute()
    return "Success"

@app.get('/contacts')
def get_all_contacts():
    result = db.table('contacts').select('*').execute()
    contacts = result.data
    return contacts

@app.get('/contact')
def get_contact(contact_id):
    result = db.table('contacts').select('*').eq('id', contact_id).execute()
    contacts = result.data
    return contacts

@app.put('/contact/{contact_id}')
async def update_contact(request: Request, contact_id):
    data = await request.json()
    result = db.table('contacts').update(data).eq('id', contact_id).execute()
    return "Updated successfully"

@app.delete('/contact/{contact_id}')
def delete_contacts(contact_id):
    result = db.table('contacts').delete().eq('id', contact_id).execute()
    return "Deleted successfully"