# Robô de Pregão - Simulador Web

## Como rodar:
1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode o servidor:
   ```bash
   python app.py
   ```

4. Acesse no navegador: http://127.0.0.1:5000

## Para empacotar em .exe:
```bash
pip install pyinstaller
pyinstaller --onefile app.py
```
