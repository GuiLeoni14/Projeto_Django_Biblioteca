from django.shortcuts import render, redirect
from app.forms import livroForm, emprestimoForm
from app.models import livro, emprestimo
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get("search")
    if search:
        data["db"] = livro.objects.filter(nome__icontains=search)
    else:
        data["db"] = livro.objects.all()

        livro_list = livro.objects.all()
        paginator = Paginator(livro_list, 4)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
        # all = livro.objects.all()
        # paginator = Paginator(all, 2)
        # pages = request.GET.get('page')
        # data['db'] = paginator.get_page(pages)
        # data['db'] = livro.objects.all()
    return render(request, "index.html", data)


def form(request):
    data = {}
    data["form"] = livroForm()
    return render(request, "form.html", data)


def create(request):
    form = livroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")


def view(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    return render(request, "view.html", data)


def edit(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    data["form"] = livroForm(instance=data["db"])
    return render(request, "form.html", data)


def update(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    form = livroForm(request.POST or None, instance=data["db"])
    if form.is_valid():
        form.save()
        return redirect("home")


def delete(request, pk):
    db = livro.objects.get(pk=pk)
    db.delete()
    return redirect("home")


def table(request):
    data = {}
    data["db"] = data["db"] = livro.objects.all()  # livroForm()
    return render(request, "table.html", data)


def homeem(request): #nao precisa mais dele
    data = {}
    searchem = request.GET.get("searchem")
    if searchem:
        data["db"] = emprestimo.objects.filter(pessoa__icontains=searchem)
    else:
        data["db"] = emprestimo.objects.all()

        emprestimo_list = livro.objects.all()
        paginator = Paginator(emprestimo_list, 2)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
    return render(request, "emprestimo.html", data)


def list_emprestimo(request):
    data = {}
    #data["db"] = emprestimo.objects.all()
    searchem = request.GET.get("searchem")
    if searchem:
        data["db"] = emprestimo.objects.filter(pessoa__icontains=searchem)
    else:
        data["db"] = emprestimo.objects.all()

        emprestimo_list = emprestimo.objects.all()
        paginator = Paginator(emprestimo_list, 4)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
    return render(request, "emprestimo.html", data)


def createem(request):
    if request.POST:
        option = request.POST["states[]"]
        dataem = request.POST["data"]
        pessoa = request.POST["dest"]
        quantidadeem = request.POST["quant"]
        emprestimo_feito = emprestimo.objects.create(
            nome_id=option, dataem=dataem, pessoa=pessoa, quantidadeem=quantidadeem
        )
        emprestimo_feito.save()
        return redirect("emprestimo")
    data = {}
    data["db"] = livro.objects.all()
    return render(request, "formem.html", data)


def viewem(request, pk):
    data = {}
    data["db"] = get_object_or_404(emprestimo, pk=pk)
    return render(request, "viewem.html", data)


def editem(request, pk):            #puxa o formulário vindo do batão editar do emprestimo.html
    data = {}
    if request.POST:
        data["db"] = emprestimo.objects.get(pk=pk)
        print(data['db'])
    return render(request, "formem.html", data)

def editemp(request, pk):
    data = {}
    data['db'] = livro.objects.all()
    data['pk'] = pk
    data['emprestimo'] = emprestimo.objects.get(id=pk)
    if request.POST:
        registro = emprestimo.objects.get(pk=pk)
        option = request.POST["states[]"]
        dataem = request.POST["data"]
        pessoa = request.POST["dest"]
        quantidadeem = request.POST["quant"]
        registro.nome_id = option
        lista = map(int, request.POST.getlist("states[]"))
        #lista = request.POST.getlist("states[]")
        print(lista)
        registro.dataem = dataem
        registro.pessoa = pessoa
        registro.quantidadeem = quantidadeem
        registro.save()
        return redirect('emprestimo')   #(request, 'emprestimo.html', data)
    return render(request, 'editemp.html', data) #editemp.html


def updateem(request, pk):  #faz o update no banco
    data = {}
    data["db"] = emprestimo.objects.get(pk=pk)
    form = emprestimoForm(request.POST or None, instance=data["db"])
    if form.is_valid():
        form.save()
        return redirect("emprestimo")

def deleteem(request, pk):
    db = emprestimo.objects.get(pk=pk)
    db.delete()
    return redirect("emprestimo")


def tableem(request):
    data = {}
    data["db"] = data["db"] = emprestimo.objects.all()  # livroForm()
    return render(request, "tableem.html", data)
