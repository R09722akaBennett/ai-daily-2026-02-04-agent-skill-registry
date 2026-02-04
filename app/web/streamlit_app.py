from __future__ import annotations

import json
import os

import httpx
import streamlit as st

API_URL = os.getenv('UI_API_URL', 'http://127.0.0.1:8000')

st.set_page_config(page_title='Agent Skill Registry', layout='wide')
st.title('Agent Skill Registry')
st.caption('Register tool schemas with versioning, and browse the latest definitions.')

with st.form('create'):
    name = st.text_input('Tool name', value='search_web')
    desc = st.text_area('Description', value='Search the web and return top results')
    schema_text = st.text_area('JSON Schema', value=json.dumps({
        'type': 'object',
        'properties': {'query': {'type': 'string'}},
        'required': ['query']
    }, indent=2))
    submitted = st.form_submit_button('Register')

if submitted:
    schema = json.loads(schema_text)
    with httpx.Client(base_url=API_URL, timeout=10.0) as client:
        r = client.post('/api/tools', json={'name': name, 'description': desc, 'schema': schema})
        st.write(r.status_code)
        st.json(r.json())

st.subheader('Tools (latest versions)')
with httpx.Client(base_url=API_URL, timeout=10.0) as client:
    r = client.get('/api/tools')
    if r.status_code == 200:
        st.json(r.json())
    else:
        st.write(r.status_code)
        st.text(r.text)
