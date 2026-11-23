from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

PRODUTOS_BANCO = [
    {
        'id': 1,
        'nome': 'X-Burger Artesanal',
        'descricao': 'Pão brioche, carne 160g, queijo cheddar derretido e molho especial da casa.',
        'preco': '29,90',
        'imagem': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80'
    },
    {
        'id': 2,
        'nome': 'Pizza Margherita',
        'descricao': 'Massa artesanal fermentada lentamente, molho de tomate fresco, mozarela e manjericão.',
        'preco': '49,90',
        'imagem': 'https://images.unsplash.com/photo-1604382355076-af4b0eb60143?auto=format&fit=crop&w=600&q=80'
    },
    {
        'id': 3,
        'nome': 'Batata Frita com Bacon',
        'descricao': 'Porção generosa de batatas crocantes cobertas com cheddar cremoso e bacon crocante.',
        'preco': '22,00',
        'imagem': 'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=600&q=80'
    }
]

def home(request):
    # Envia a lista de produtos para o index.html
    return render(request, 'core/index.html', {'produtos': PRODUTOS_BANCO})

def detalhe_produto_view(request, pk):
    # Busca o produto pelo ID (pk)
    produto_encontrado = next((p for p in PRODUTOS_BANCO if p['id'] == pk), None)
    
    return render(request, 'core/detalhe_produto.html', {'produto': produto_encontrado})

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        palavra_passe = request.POST.get('password')
        user = authenticate(request, username=usuario, password=palavra_passe)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'erro': 'Usuário ou senha inválidos!'})
    return render(request, 'core/login.html')


@login_required(login_url='/login/')
def cadastrar_produto_view(request):
    """Tela para o admin cadastrar novos produtos"""
    if request.method == 'POST':
        # Aqui você pegará os dados do formulário preenchido pelo admin
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        
        # Como estamos simulando com lista por enquanto, 
        # futuramente isso vai para o banco de dados.
        print(f"Novo produto recebido: {nome} - R$ {preco}")
        
        return redirect('admin_dashboard')
        
    return render(request, 'core/cadastro_produto.html')


@login_required(login_url='/login/')
def acompanhar_pedido_view(request):
    """Tela onde o cliente acompanha a situação do pedido (Pendente, Em preparo, etc.)"""
    
    # Exemplo de dados simulados de um pedido para aparecer na tela do cliente
    pedido_exemplo = {
        'id': 104,
        'status': 'Em preparo',  # Pode ser: 'Pendente', 'Em preparo', 'Saiu para entrega', 'Entregue'
        'itens': ['X-Burger Artesanal', 'Batata Frita com Bacon'],
        'total': '51,90'
    }
    
    return render(request, 'core/acompanhar_pedido.html', {'pedido': pedido_exemplo})

@login_required(login_url='/login/')
def admin_dashboard_view(request):
    return render(request, 'core/admin_dashboard.html')

def cadastro_view(request):
    return render(request, 'core/cadastro.html')

def acompanhar_pedido_view(request):
    # Cenário 1: O usuário NÃO está logado
    if not request.user.is_authenticated:
        status_pedido = 'nao_logado'
        pedido = None
    else:
        # O usuário ESTÁ logado. Vamos buscar se ele tem pedidos.
        # Exemplo buscando no banco de dados pelo usuário atual:
        # pedidos_usuario = Pedido.objects.filter(cliente=request.user)
        
        # Para simular, vamos supor que fazemos a consulta:
        pedidos_usuario = [] # Troque pela sua query real, ex: Pedido.objects.filter(usuario=request.user)
        
        if not pedidos_usuario:
            # Cenário 2: Logado, mas sem pedidos
            status_pedido = 'sem_pedidos'
            pedido = None
        else:
            # Cenário 3: Logado e com pedido ativo
            status_pedido = 'com_pedido'
            pedido = pedidos_usuario.last() # Ou o pedido mais recente

    contexto = {
        'status_pedido': status_pedido,
        'pedido': pedido,
    }
    return render(request, 'core/acompanhar_pedido.html', contexto)