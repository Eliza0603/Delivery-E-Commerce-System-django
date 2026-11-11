from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
def admin_dashboard_view(request):
    return render(request, 'core/admin_dashboard.html')

def cadastro_view(request):
    return render(request, 'core/cadastro.html')