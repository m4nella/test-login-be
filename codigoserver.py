# from http.server import SimpleHTTPRequestHandler
# import socketserver
# import os 
# from urllib.parse import parse_qs, urlparse

# class MyHandler(SimpleHTTPRequestHandler):
#     def list_directory(self, path):
#         try: 
#             with open(os.path.join(path, 'home.html'),'r',encoding='utf-8') as f:
#                 self.send_response(200)
#                 self.send_header('Content-type','text/html; charset=UTF-8')
#                 self.end_headers()
#                 self.wfile.write(f.read().encode('utf-8'))
#                 f.close()
#             return None
#         except FileNotFoundError:
#             pass
#         return super().list_directory(path)
    
#     def do_GET(self):
#         if self.path =='/login':
#             try:
#                 with open(os.path.join(os.getcwd(),'login.html'),'r',encoding='utf-8')as login_file:
#                     content = login_file.read()
#                 self.send_response(200)
#                 self.send_header('Content-type','text/html')
#                 self.end_headers()
#                 self.wfile.write(content.encode('utf-8'))
#             except FileNotFoundError:
#                 self.send_error(404,"File not found")

#         elif self.path == "/login_failed":
#             self.send_response(200)
#             self.send_header('Content-type', 'text/html; charset=utf-8')
#             self.end_headers()
             
#             with open(os.path.join(os.getcwd(), 'login.html'),'r',encoding='utf-8') as login_file:
#                 content = login_file.read()

#             mensagem = "Login e/ou senha incoreta. Tente novamente"
#             content = content.replace('<!-- Mensagem de erro será inserida aqui -->', f'<div class="error_message">{mensagem}</div>')
#             self.wfile.write(content.encode('utf-8'))

#         elif self.path.startswith('/cadastro'):
#             query_params = parse_qs(urlparse(self.path).query)
#             login = query_params.get('login', [''])[0]
#             senha = query_params.get('senha', [''])[0]

#             welcome_message = f"Olá {login}, seja bem vinde, percebemos q vc eh novo por aki"

#             self.send_response(200)
#             self.send_header("Content-type", "text/html; charset=utf-8")
#             self.end_headers()

#             with open(os.path.join(os.getcwd(), 'cadastro.html'), 'r', encoding='utf-8') as cadastro_file:
#                 content = cadastro_file.read()

#             content = content.replace('{login}', login)
#             content = content.replace('{senha}', senha)
#             content = content.replace('{welcome_message}', welcome_message)

#             self.wfile.write(content.encode('utf-8'))

#             return

#         else: 
#             super().do_GET()

#     def usuario_existente(self, login, senha):
#         with open('dados_login.txt', 'r', encoding='utf-8') as file:
#             for line in file:
#                 if line.strip():
#                     stored_login, stored_senha, stored_nome = line.strip().split(';')
#                     if login == stored_login:
#                         print("login informado localizado")
#                         print("senha: " + senha)
#                         print("Senha armazenada: " + senha)
#                         return senha == stored_senha
#         return False
#     def remover_ultima_linha(self, arquivo):
#         print("Vou excluir ultima linha")
#         with open(arquivo, 'r', encoding='utf-8') as file:
#             lines = file.readlines()
#         with open(arquivo, 'w', encoding='utf-8') as file: 
#             file.writelines(lines[:-1])

#     def do_POST(self):
#         if self.path =='/enviar_login':
#             content_lenght = int(self.headers['Content-Length'])
#             body = self.rfile.read(content_lenght).decode('utf-8')
#             form_data = parse_qs(body, keep_blank_values=True)

#             print('Dados do formulário:')
#             print('Email:', form_data.get('email',[''])[0])
#             print('Senha:', form_data.get('senha',[''])[0])

#             login = form_data.get('email',[''])[0]
#             senha = form_data.get('senha',[''])[0]


#         elif self.path.startswith('/confirmar_cadastro'):
#             content_lenght = int(self.headers['Content-Length'])
#             body = self.rfile.read(content_lenght).decode('utf-8')

#             form_data = parse_qs(body, keep_blank_values=True)

#             login = form_data.get('login', [''])[0]
#             senha = form_data.get('senha', [''])[0]
#             nome = form_data.get('nome', [''])[0]

#             print("nome: " + nome)

#             if self.usuario_existente(login, senha):
#                 #  with open(os.path.join(os.getcwd(),'user_existente.html'),'r',encoding='utf-8')as login_file:
#                 #     self.send_response(200)
#                 #     self.send_header('Content-type','text/html')
#                 #     self.end_headers()
#                 #     mensagem = f"Usuáio {login} logado com sucesso!"
#                 #     self.wfile.write(mensagem.encode('utf-8'))
#                 with open('dados_login.txt', 'r', encoding='utf-8') as file:
#                     lines = file.readlines()

#                 with open('dados_login.txt', 'n', encoding='utf-8') as file:
#                     for line in lines:
#                         stored_login, stored_senha, stored_nome = line.strip().split(';')
#                         if login == stored_login and senha == stored_senha:
#                             line = f"{login};{senha};{nome}\n"
#                         file.write(line)

#                 self.send_response(302)
#                 self.send_header("Content-type", "text/html; charset=utf-8")
#                 self.end_headers()
#                 self.wfile.write("Registro Recebido com sucesso rs".encode('utf-8'))

#             else:
                
#                 self.remover_ultima_linha('dados_login.txt')
#                 self.send_response(302)
#                 self.send_header("Content-type", "text/html; charset=utf-8")
#                 self.end_headers()
#                 self.wfile.write("A senha não confere. Retome o procedimento!".encode('utf-8'))
            
#             else: 
#                 if any(line.startswith(f'{login};')for line in open('dados_login.txt','r',encoding='utf-8')):
#                             self.send_response(302)
#                             self.send_header('Location','/login_failed')
#                             self.end_headers()
#                             self.wfile.write(content.encode('utf-8'))
#                             return
#                 else:

#                     with open('dados_login.txt', 'a', encoding='utf-8') as file:
#                             file.write(f"{login};{senha}" + "none" + "\n")

#                     self.send_response(302)
#                     self.send_header('Location', f'/cadastro?login={login}&senha={senha}')
#                     self.end_headers()

#                     return
                    
#                     with open(os.path.join(os.getcwd(),'cadastro.html'),'r',encoding='utf-8')as login_file:
#                         content = login_file.read()
#                     self.send_response(200)
#                     self.send_header('Content-type','text/html;charset=utf-8')
#                     self.end_headers()
#                     self.wfile.write(content.encode('utf-8'))

#                     with open(os.path.join(os.getcwd(),'dtreceb.html'),'r',encoding='utf-8')as login_file:
#                         content = login_file.read()
#                     self.send_response(200)
#                     self.send_header('Content-type','text/html;charset=utf-8')
#                     self.end_headers()
#                     self.wfile.write(content.encode('utf-8'))

#         else: 
#             super(MyHandler,self).do_POST()

    
# endereco_ip = "0.0.0.0"

# porta = 8000

# with socketserver.TCPServer((endereco_ip,porta),MyHandler) as httpd:
#     print(f'Servidor iniciado em {endereco_ip} na porta {porta}')
#     httpd.serve_forever()